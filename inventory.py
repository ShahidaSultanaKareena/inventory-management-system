import json
import os
from datetime import datetime

# File to store inventory data
INVENTORY_FILE = "inventory.json"

def load_inventory():
    """Load inventory from JSON file"""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_inventory(inventory):
    """Save inventory to JSON file"""
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)
    print("✓ Data saved successfully!")

def display_menu():
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
    print("7. Exit")
    print("="*50)

def add_product(inventory):
    """Add a new product to inventory"""
    print("\n--- ADD NEW PRODUCT ---")
    
    product_name = input("Product Name: ").strip()
    
    # Check if product already exists
    if any(p['name'].lower() == product_name.lower() for p in inventory):
        print("✗ Product already exists!")
        return
    
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        supplier = input("Supplier: ").strip()
        category = input("Category (optional): ").strip() or "General"
        
        if price < 0 or stock < 0:
            print("✗ Price and stock cannot be negative!")
            return
        
        product = {
            "id": len(inventory) + 1,
            "name": product_name,
            "price": price,
            "stock": stock,
            "supplier": supplier,
            "category": category,
            "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        inventory.append(product)
        save_inventory(inventory)
        print(f"✓ Product '{product_name}' added successfully!")
        
    except ValueError:
        print("✗ Invalid input! Price must be a number and stock must be an integer.")

def view_products(inventory):
    """Display all products in inventory"""
    if not inventory:
        print("\n✗ No products in inventory!")
        return
    
    print("\n" + "="*100)
    print(f"{'ID':<5} {'Product Name':<25} {'Price':<10} {'Stock':<10} {'Supplier':<20} {'Category':<15}")
    print("="*100)
    
    for product in inventory:
        print(f"{product['id']:<5} {product['name']:<25} ৳{product['price']:<9.2f} {product['stock']:<10} {product['supplier']:<20} {product['category']:<15}")
    
    print("="*100)
    print(f"Total Products: {len(inventory)}")

def search_product(inventory):
    """Search for a product by name or ID"""
    print("\n--- SEARCH PRODUCT ---")
    search_term = input("Enter Product Name or ID: ").strip()
    
    results = []
    
    # Search by name
    results = [p for p in inventory if search_term.lower() in p['name'].lower()]
    
    # Search by ID if no results
    if not results:
        try:
            product_id = int(search_term)
            results = [p for p in inventory if p['id'] == product_id]
        except ValueError:
            pass
    
    if results:
        print("\n" + "="*100)
        print(f"{'ID':<5} {'Product Name':<25} {'Price':<10} {'Stock':<10} {'Supplier':<20} {'Category':<15}")
        print("="*100)
        for product in results:
            print(f"{product['id']:<5} {product['name']:<25} ৳{product['price']:<9.2f} {product['stock']:<10} {product['supplier']:<20} {product['category']:<15}")
        print("="*100)
    else:
        print(f"✗ No products found matching '{search_term}'!")

def update_stock(inventory):
    """Update stock quantity for a product"""
    print("\n--- UPDATE STOCK ---")
    
    try:
        product_id = int(input("Enter Product ID: "))
        product = next((p for p in inventory if p['id'] == product_id), None)
        
        if not product:
            print("✗ Product not found!")
            return
        
        print(f"\nCurrent Stock of '{product['name']}': {product['stock']} units")
        
        action = input("Add or Remove stock? (add/remove): ").strip().lower()
        
        if action not in ['add', 'remove']:
            print("✗ Invalid action!")
            return
        
        quantity = int(input(f"Quantity to {action}: "))
        
        if quantity < 0:
            print("✗ Quantity cannot be negative!")
            return
        
        if action == 'add':
            product['stock'] += quantity
            print(f"✓ Added {quantity} units. New stock: {product['stock']}")
        else:
            if quantity > product['stock']:
                print(f"✗ Cannot remove {quantity} units. Only {product['stock']} available!")
                return
            product['stock'] -= quantity
            print(f"✓ Removed {quantity} units. New stock: {product['stock']}")
        
        save_inventory(inventory)
        
    except ValueError:
        print("✗ Invalid input! Product ID and quantity must be numbers.")

def delete_product(inventory):
    """Delete a product from inventory"""
    print("\n--- DELETE PRODUCT ---")
    
    try:
        product_id = int(input("Enter Product ID to delete: "))
        product = next((p for p in inventory if p['id'] == product_id), None)
        
        if not product:
            print("✗ Product not found!")
            return
        
        print(f"\nProduct Details:")
        print(f"  Name: {product['name']}")
        print(f"  Price: ৳{product['price']:.2f}")
        print(f"  Stock: {product['stock']}")
        
        confirm = input("\nAre you sure you want to delete this product? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            inventory.remove(product)
            save_inventory(inventory)
            print(f"✓ Product '{product['name']}' deleted successfully!")
        else:
            print("✗ Deletion cancelled!")
    
    except ValueError:
        print("✗ Invalid input! Product ID must be a number.")

def generate_report(inventory):
    """Generate inventory report with statistics"""
    if not inventory:
        print("\n✗ No products in inventory!")
        return
    
    print("\n" + "="*50)
    print("           INVENTORY REPORT")
    print("="*50)
    
    total_products = len(inventory)
    total_stock = sum(p['stock'] for p in inventory)
    total_value = sum(p['price'] * p['stock'] for p in inventory)
    
    low_stock = [p for p in inventory if p['stock'] < 10]
    
    print(f"\nGeneral Statistics:")
    print(f"  Total Products: {total_products}")
    print(f"  Total Units in Stock: {total_stock}")
    print(f"  Total Inventory Value: ৳{total_value:,.2f}")
    
    print(f"\nByCategory:")
    categories = {}
    for product in inventory:
        cat = product['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count} products")
    
    if low_stock:
        print(f"\n⚠ LOW STOCK ALERT (< 10 units):")
        for product in low_stock:
            print(f"  - {product['name']}: {product['stock']} units")
    else:
        print(f"\n✓ All products have sufficient stock!")
    
    print("="*50)

def main():
    """Main application loop"""
    print("\nWelcome to Shwapno Inventory Management System!")
    
    inventory = load_inventory()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            view_products(inventory)
        elif choice == '3':
            search_product(inventory)
        elif choice == '4':
            update_stock(inventory)
        elif choice == '5':
            delete_product(inventory)
        elif choice == '6':
            generate_report(inventory)
        elif choice == '7':
            print("\n✓ Thank you for using Shwapno Inventory Management System!")
            print("Goodbye!\n")
            break
        else:
            print("✗ Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()
