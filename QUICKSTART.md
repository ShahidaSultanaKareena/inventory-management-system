# Shwapno Inventory Management System - Quick Start Guide

## Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/ShahidaSultanaKareena/inventory-management-system.git
cd inventory-management-system
```

### Step 2: Install Python (if not already installed)
- Download from: https://www.python.org/downloads/
- Version required: Python 3.6 or higher

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python inventory.py
```

---

## Basic Operations

### 1️⃣ Adding a Product
```
Choose: 1
Product Name: SmartHeart Cat Food
Price: 850
Stock Quantity: 20
Supplier: ACI
Category (optional): Pet Food
✓ Product 'SmartHeart Cat Food' added successfully!
```

### 2️⃣ Viewing All Products
```
Choose: 2
```
Shows a formatted table of all products with ID, Name, Price, Stock, Supplier, and Category.

### 3️⃣ Searching for a Product
```
Choose: 3
Enter Product Name or ID: SmartHeart
```
Returns matching products by name or product ID.

### 4️⃣ Updating Stock
```
Choose: 4
Enter Product ID: 1
Current Stock of 'SmartHeart Cat Food': 20 units
Add or Remove stock? (add/remove): add
Quantity to add: 10
✓ Added 10 units. New stock: 30
```

### 5️⃣ Deleting a Product
```
Choose: 5
Enter Product ID to delete: 1
Product Details:
  Name: SmartHeart Cat Food
  Price: ৳850.00
  Stock: 20
Are you sure you want to delete this product? (yes/no): yes
✓ Product 'SmartHeart Cat Food' deleted successfully!
```

### 6️⃣ Generating a Report
```
Choose: 6
```
Shows:
- Total number of products
- Total units in stock
- Total inventory value (in Bengali Taka)
- Products by category
- Low stock alerts (< 10 units)

---

## File Structure

```
inventory-management-system/
├── inventory.py          # Main application
├── config.py            # Configuration settings
├── test_inventory.py    # Unit tests
├── requirements.txt     # Python dependencies
├── README.md           # Full documentation
├── QUICKSTART.md       # This file
└── inventory.json      # Data file (auto-created)
```

---

## Data Storage

All inventory data is saved in `inventory.json` automatically. The file is created after you add the first product.

Example structure:
```json
[
  {
    "id": 1,
    "name": "SmartHeart Cat Food",
    "price": 850.0,
    "stock": 20,
    "supplier": "ACI",
    "category": "Pet Food",
    "date_added": "2026-07-13 10:30:45"
  }
]
```

---

## Running Tests

If you installed pytest, run tests to verify everything works:
```bash
python -m pytest test_inventory.py -v
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run: `pip install -r requirements.txt` |
| `permission denied` | Run: `chmod +x inventory.py` (Mac/Linux) |
| Can't find inventory.json | It will be created automatically on first product add |
| Invalid input errors | Make sure to enter numbers for price and stock |

---

## Tips & Tricks

✅ Use descriptive product names for easier searching
✅ Organize products by category for better reporting
✅ Check the report regularly to monitor low stock items
✅ Backup your `inventory.json` file regularly
✅ Use consistent supplier names for data accuracy

---

## Keyboard Shortcuts

While in menu selection, you can:
- Press `Ctrl+C` to exit the application immediately
- Press `Ctrl+Z` then `Enter` on Windows to exit
- Use `Ctrl+D` on Mac/Linux to exit

---

## Next Steps

1. ✅ Add your first product
2. ✅ Practice searching and updating stock
3. ✅ Generate your first report
4. ✅ Explore all features

---

**Need help?** Check the README.md for detailed documentation!
