# Shwapno Inventory Management System

A command-line inventory management application designed for retail operations. This system helps manage products, track stock levels, and generate inventory reports efficiently.

## 📋 Features

- **Add Product** - Add new products with details (name, price, stock, supplier, category)
- **View Products** - Display all products in a formatted table
- **Search Product** - Search products by name or ID
- **Update Stock** - Increase or decrease stock quantities
- **Delete Product** - Remove products with confirmation
- **Generate Report** - View inventory statistics, category breakdown, and low stock alerts
- **Data Persistence** - Automatic JSON-based data storage
- **Input Validation** - Prevents invalid data entry
- **Low Stock Alerts** - Identifies products with stock below 10 units

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/ShahidaSultanaKareena/inventory-management-system.git
cd inventory-management-system
```

2. Ensure Python 3.6+ is installed:
```bash
python --version
```

3. Run the application:
```bash
python inventory.py
```

## 🚀 Usage

### Main Menu
```
==================================================
       SHWAPNO INVENTORY MANAGEMENT SYSTEM
==================================================
1. Add Product
2. View All Products
3. Search Product
4. Update Stock
5. Delete Product
6. Generate Report
7. Exit
==================================================
```

### Example: Adding a Product
```
Choose an option (1-7): 1

--- ADD NEW PRODUCT ---
Product Name: SmartHeart Cat Food
Price: 850
Stock Quantity: 20
Supplier: ACI
Category (optional): Pet Food
✓ Product 'SmartHeart Cat Food' added successfully!
```

### Example: Updating Stock
```
Choose an option (1-7): 4

--- UPDATE STOCK ---
Enter Product ID: 1

Current Stock of 'SmartHeart Cat Food': 20 units
Add or Remove stock? (add/remove): add
Quantity to add: 15
✓ Added 15 units. New stock: 35
✓ Data saved successfully!
```

### Example: Generating Report
```
Choose an option (1-7): 6

==================================================
           INVENTORY REPORT
==================================================

General Statistics:
  Total Products: 5
  Total Units in Stock: 125
  Total Inventory Value: ৳45,500.00

ByCategory:
  Pet Food: 2 products
  General: 3 products

⚠ LOW STOCK ALERT (< 10 units):
  - Dog Treats: 5 units

✓ All other products have sufficient stock!
==================================================
```

## 📁 File Structure

```
inventory-management-system/
├── inventory.py          # Main application file
├── config.py             # Configuration settings
├── test_inventory.py     # Unit tests
├── inventory.json        # Data storage (auto-created)
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── QUICKSTART.md        # Quick start guide
```

## 💾 Data Storage

All inventory data is stored in `inventory.json` with the following structure:
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

## 🎯 Key Functions

| Function | Purpose |
|----------|----------|
| `load_inventory()` | Load products from JSON file |
| `save_inventory()` | Save products to JSON file |
| `add_product()` | Add new product to inventory |
| `view_products()` | Display all products in table format |
| `search_product()` | Search by name or product ID |
| `update_stock()` | Increase/decrease product stock |
| `delete_product()` | Remove product with confirmation |
| `generate_report()` | Generate comprehensive inventory report |

## ✨ Special Features

- **Duplicate Prevention** - Cannot add products with same name
- **Input Validation** - Prevents negative prices/stock and invalid entries
- **Confirmation Dialogs** - Confirms deletion before removing products
- **Formatted Output** - Professional table layouts with proper alignment
- **Low Stock Warnings** - Automatic alerts for products below 10 units
- **Category Organization** - Track products by category
- **Total Inventory Value** - Calculates total worth of all products

## 🔍 Search Capabilities

- **Search by Product Name** - Partial name matching (case-insensitive)
- **Search by Product ID** - Exact ID matching

## ⚠️ Error Handling

The system includes comprehensive error handling for:
- Invalid menu choices
- Non-numeric input for prices and quantities
- Negative values
- Duplicate product names
- Insufficient stock when removing
- Missing product IDs

## 🐛 Troubleshooting

**Issue:** `ModuleNotFoundError`
- **Solution:** Ensure all required modules are installed: `pip install -r requirements.txt`

**Issue:** `inventory.json` not found
- **Solution:** This is normal on first run. The file will be created automatically when you add the first product.

**Issue:** Permission denied when running
- **Solution:** Make the file executable: `chmod +x inventory.py` (Linux/Mac)

## 📝 License

This project is open source and available for educational and commercial use.


## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📞 Support

For issues or questions, please create an issue in the GitHub repository.

---

