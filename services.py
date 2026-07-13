"""
Service layer for business logic
Handles all core operations for inventory management
"""

from typing import List, Dict, Any, Optional
from models import Product, InventoryDataManager
from config import LOW_STOCK_THRESHOLD


class InventoryService:
    """Service class for inventory operations"""
    
    def __init__(self):
        """Initialize inventory service"""
        self.data_manager = InventoryDataManager()
        self._inventory: List[Product] = []
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory from storage"""
        data = self.data_manager.load()
        self._inventory = [Product.from_dict(item) for item in data]
    
    def save_inventory(self) -> bool:
        """Save inventory to storage"""
        data = [product.to_dict() for product in self._inventory]
        return self.data_manager.save(data)
    
    def backup_inventory(self) -> bool:
        """Create backup of inventory"""
        data = [product.to_dict() for product in self._inventory]
        return self.data_manager.backup(data)
    
    def get_all_products(self) -> List[Product]:
        """Get all products"""
        return self._inventory
    
    def add_product(self, name: str, price: float, stock: int, 
                   supplier: str, category: str = "General") -> bool:
        """
        Add a new product to inventory
        
        Args:
            name: Product name
            price: Product price
            stock: Stock quantity
            supplier: Supplier name
            category: Product category
            
        Returns:
            True if product added successfully, False otherwise
        """
        # Check for duplicates
        if self._product_exists_by_name(name):
            print(f"✗ Product '{name}' already exists!")
            return False
        
        # Validate inputs
        if price < 0 or stock < 0:
            print("✗ Price and stock cannot be negative!")
            return False
        
        # Create new product
        product_id = self._get_next_id()
        product = Product(product_id, name, price, stock, supplier, category)
        self._inventory.append(product)
        
        # Save and return
        if self.save_inventory():
            print(f"✓ Product '{name}' added successfully!")
            return True
        return False
    
    def search_products(self, search_term: str) -> List[Product]:
        """
        Search products by name or ID
        
        Args:
            search_term: Search term (name or ID)
            
        Returns:
            List of matching products
        """
        results = []
        
        # Search by name (case-insensitive)
        results = [p for p in self._inventory 
                  if search_term.lower() in p.name.lower()]
        
        # Search by ID if no results
        if not results:
            try:
                product_id = int(search_term)
                results = [p for p in self._inventory if p.id == product_id]
            except ValueError:
                pass
        
        return results
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """
        Get product by ID
        
        Args:
            product_id: Product ID
            
        Returns:
            Product object or None if not found
        """
        return next((p for p in self._inventory if p.id == product_id), None)
    
    def update_stock(self, product_id: int, quantity: int, action: str) -> bool:
        """
        Update product stock
        
        Args:
            product_id: Product ID
            quantity: Quantity to add/remove
            action: 'add' or 'remove'
            
        Returns:
            True if update successful, False otherwise
        """
        product = self.get_product_by_id(product_id)
        
        if not product:
            print("✗ Product not found!")
            return False
        
        if quantity < 0:
            print("✗ Quantity cannot be negative!")
            return False
        
        if action == 'add':
            product.stock += quantity
            print(f"✓ Added {quantity} units. New stock: {product.stock}")
        elif action == 'remove':
            if quantity > product.stock:
                print(f"✗ Cannot remove {quantity} units. Only {product.stock} available!")
                return False
            product.stock -= quantity
            print(f"✓ Removed {quantity} units. New stock: {product.stock}")
        else:
            print("✗ Invalid action!")
            return False
        
        return self.save_inventory()
    
    def delete_product(self, product_id: int) -> bool:
        """
        Delete a product
        
        Args:
            product_id: Product ID
            
        Returns:
            True if deletion successful, False otherwise
        """
        product = self.get_product_by_id(product_id)
        
        if not product:
            print("✗ Product not found!")
            return False
        
        product_name = product.name
        self._inventory.remove(product)
        
        if self.save_inventory():
            print(f"✓ Product '{product_name}' deleted successfully!")
            return True
        return False
    
    def get_low_stock_products(self, threshold: int = LOW_STOCK_THRESHOLD) -> List[Product]:
        """
        Get products with low stock
        
        Args:
            threshold: Low stock threshold (default from config)
            
        Returns:
            List of products below threshold
        """
        return [p for p in self._inventory if p.stock < threshold]
    
    def get_products_by_category(self) -> Dict[str, int]:
        """
        Get product count by category
        
        Returns:
            Dictionary with category names and product counts
        """
        categories = {}
        for product in self._inventory:
            cat = product.category
            categories[cat] = categories.get(cat, 0) + 1
        return categories
    
    def get_inventory_statistics(self) -> Dict[str, Any]:
        """
        Get inventory statistics
        
        Returns:
            Dictionary with inventory statistics
        """
        total_products = len(self._inventory)
        total_stock = sum(p.stock for p in self._inventory)
        total_value = sum(p.price * p.stock for p in self._inventory)
        
        return {
            "total_products": total_products,
            "total_stock": total_stock,
            "total_value": total_value,
            "categories": self.get_products_by_category(),
            "low_stock_products": self.get_low_stock_products()
        }
    
    # Private helper methods
    def _product_exists_by_name(self, name: str) -> bool:
        """Check if product exists by name"""
        return any(p.name.lower() == name.lower() for p in self._inventory)
    
    def _get_next_id(self) -> int:
        """Get next available product ID"""
        return max([p.id for p in self._inventory], default=0) + 1