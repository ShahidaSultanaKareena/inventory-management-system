"""
Presentation layer for user interface
Handles all user interactions and display formatting
"""

from typing import List
from models import Product
from config import CURRENCY_SYMBOL


class UIFormatter:
    """Formats and displays data to the user"""
    
    @staticmethod
    def print_menu() -> None:
        """Display main menu"""
        print("\n" + "="*50)
        print("       SHWAPNO INVENTORY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Generate Report")
        print("7. Backup Inventory")
        print("8. Exit")
        print("="*50)
    
    @staticmethod
    def print_products_table(products: List[Product], title: str = None) -> None:
        """
        Display products in a formatted table
        
        Args:
            products: List of products to display
            title: Optional table title
        """
        if not products:
            print("\n✗ No products to display!")
            return
        
        if title:
            print(f"\n{title}")
        
        print("\n" + "="*120)
        print(f"{'ID':<5} {'Product Name':<25} {'Price':<12} {'Stock':<10} {'Supplier':<20} {'Category':<20}")
        print("="*120)
        
        for product in products:
            print(f"{product.id:<5} {product.name:<25} {CURRENCY_SYMBOL}{product.price:<11.2f} "
                  f"{product.stock:<10} {product.supplier:<20} {product.category:<20}")
        
        print("="*120)
    
    @staticmethod
    def print_product_details(product: Product) -> None:
        """
        Display detailed product information
        
        Args:
            product: Product to display details for
        """
        print("\n" + "-"*40)
        print("PRODUCT DETAILS")
        print("-"*40)
        print(f"ID:          {product.id}")
        print(f"Name:        {product.name}")
        print(f"Price:       {CURRENCY_SYMBOL}{product.price:.2f}")
        print(f"Stock:       {product.stock} units")
        print(f"Supplier:    {product.supplier}")
        print(f"Category:    {product.category}")
        print(f"Date Added:  {product.date_added}")
        print("-"*40)
    
    @staticmethod
    def print_report(stats: dict) -> None:
        """
        Display inventory report
        
        Args:
            stats: Dictionary with inventory statistics
        """
        print("\n" + "="*60)
        print("                    INVENTORY REPORT")
        print("="*60)
        
        print(f"\n📊 GENERAL STATISTICS:")
        print(f"   Total Products:        {stats['total_products']}")
        print(f"   Total Units in Stock:  {stats['total_stock']}")
        print(f"   Total Inventory Value: {CURRENCY_SYMBOL}{stats['total_value']:,.2f}")
        
        print(f"\n📦 BY CATEGORY:")
        if stats['categories']:
            for category, count in sorted(stats['categories'].items()):
                print(f"   {category}: {count} products")
        else:
            print("   No categories")
        
        print(f"\n⚠️  LOW STOCK ALERT (< 10 units):")
        if stats['low_stock_products']:
            for product in stats['low_stock_products']:
                print(f"   - {product.name}: {product.stock} units")
        else:
            print("   ✓ All products have sufficient stock!")
        
        print("="*60)
    
    @staticmethod
    def get_menu_choice() -> str:
        """Get user menu choice"""
        return input("\nChoose an option (1-8): ").strip()
    
    @staticmethod
    def get_product_input() -> dict:
        """
        Get product information from user
        
        Returns:
            Dictionary with product data
        """
        print("\n--- ADD NEW PRODUCT ---")
        product_name = input("Product Name: ").strip()
        
        try:
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            supplier = input("Supplier: ").strip()
            category = input("Category (optional, default='General'): ").strip() or "General"
            
            return {
                "name": product_name,
                "price": price,
                "stock": stock,
                "supplier": supplier,
                "category": category
            }
        except ValueError:
            print("✗ Invalid input! Price must be a number and stock must be an integer.")
            return None
    
    @staticmethod
    def get_search_input() -> str:
        """Get search term from user"""
        print("\n--- SEARCH PRODUCT ---")
        return input("Enter Product Name or ID: ").strip()
    
    @staticmethod
    def get_update_stock_input() -> dict:
        """
        Get stock update information from user
        
        Returns:
            Dictionary with update data
        """
        print("\n--- UPDATE STOCK ---")
        
        try:
            product_id = int(input("Enter Product ID: "))
            action = input("Add or Remove stock? (add/remove): ").strip().lower()
            quantity = int(input(f"Quantity to {action}: "))
            
            return {
                "product_id": product_id,
                "action": action,
                "quantity": quantity
            }
        except ValueError:
            print("✗ Invalid input! Please enter valid numbers.")
            return None
    
    @staticmethod
    def get_delete_confirmation(product_name: str) -> bool:
        """
        Get deletion confirmation from user
        
        Args:
            product_name: Name of product to delete
            
        Returns:
            True if user confirms deletion
        """
        confirm = input(f"\nAre you sure you want to delete '{product_name}'? (yes/no): ").strip().lower()
        return confirm == 'yes'


class InventoryUI:
    """Main UI controller"""
    
    def __init__(self, service):
        """
        Initialize UI
        
        Args:
            service: InventoryService instance
        """
        self.service = service
        self.formatter = UIFormatter()
    
    def show_menu(self) -> None:
        """Display and handle main menu"""
        self.formatter.print_menu()
    
    def show_add_product_screen(self) -> None:
        """Handle add product screen"""
        data = self.formatter.get_product_input()
        if data:
            self.service.add_product(
                name=data['name'],
                price=data['price'],
                stock=data['stock'],
                supplier=data['supplier'],
                category=data['category']
            )
    
    def show_products_screen(self) -> None:
        """Handle view products screen"""
        products = self.service.get_all_products()
        self.formatter.print_products_table(products, "--- ALL PRODUCTS ---")
        print(f"\nTotal Products: {len(products)}")
    
    def show_search_screen(self) -> None:
        """Handle search screen"""
        search_term = self.formatter.get_search_input()
        if search_term:
            results = self.service.search_products(search_term)
            if results:
                self.formatter.print_products_table(results, "--- SEARCH RESULTS ---")
            else:
                print(f"✗ No products found matching '{search_term}'!")
    
    def show_update_stock_screen(self) -> None:
        """Handle update stock screen"""
        data = self.formatter.get_update_stock_input()
        if data:
            product = self.service.get_product_by_id(data['product_id'])
            if product:
                print(f"\nCurrent Stock of '{product.name}': {product.stock} units")
                self.service.update_stock(
                    product_id=data['product_id'],
                    quantity=data['quantity'],
                    action=data['action']
                )
            else:
                print("✗ Product not found!")
    
    def show_delete_screen(self) -> None:
        """Handle delete product screen"""
        print("\n--- DELETE PRODUCT ---")
        try:
            product_id = int(input("Enter Product ID to delete: "))
            product = self.service.get_product_by_id(product_id)
            
            if product:
                self.formatter.print_product_details(product)
                if self.formatter.get_delete_confirmation(product.name):
                    self.service.delete_product(product_id)
            else:
                print("✗ Product not found!")
        except ValueError:
            print("✗ Invalid input! Product ID must be a number.")
    
    def show_report_screen(self) -> None:
        """Handle report generation screen"""
        stats = self.service.get_inventory_statistics()
        if stats['total_products'] > 0:
            self.formatter.print_report(stats)
        else:
            print("\n✗ No products in inventory!")
    
    def show_backup_screen(self) -> None:
        """Handle backup screen"""
        print("\n--- BACKUP INVENTORY ---")
        self.service.backup_inventory()
    
    def show_welcome(self) -> None:
        """Show welcome message"""
        print("\n" + "="*50)
        print("Welcome to Shwapno Inventory Management System!")
        print("="*50)