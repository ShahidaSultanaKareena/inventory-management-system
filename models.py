"""
Data management module for Inventory Management System
Handles all file I/O operations and data persistence
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any
from config import INVENTORY_FILE


class InventoryDataManager:
    """Manages inventory data persistence and loading"""
    
    @staticmethod
    def load() -> List[Dict[str, Any]]:
        """
        Load inventory from JSON file
        
        Returns:
            List of product dictionaries, or empty list if file doesn't exist
        """
        if os.path.exists(INVENTORY_FILE):
            try:
                with open(INVENTORY_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except (json.JSONDecodeError, IOError) as e:
                print(f"✗ Error loading inventory: {e}")
                return []
        return []
    
    @staticmethod
    def save(inventory: List[Dict[str, Any]]) -> bool:
        """
        Save inventory to JSON file
        
        Args:
            inventory: List of product dictionaries to save
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            with open(INVENTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(inventory, f, indent=4, ensure_ascii=False)
            print("✓ Data saved successfully!")
            return True
        except IOError as e:
            print(f"✗ Error saving inventory: {e}")
            return False
    
    @staticmethod
    def backup(inventory: List[Dict[str, Any]]) -> bool:
        """
        Create a backup of the current inventory
        
        Args:
            inventory: List of product dictionaries to backup
            
        Returns:
            True if backup successful, False otherwise
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"inventory_backup_{timestamp}.json"
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(inventory, f, indent=4, ensure_ascii=False)
            print(f"✓ Backup created: {backup_file}")
            return True
        except IOError as e:
            print(f"✗ Error creating backup: {e}")
            return False


class Product:
    """Product model class"""
    
    def __init__(self, product_id: int, name: str, price: float, stock: int, 
                 supplier: str, category: str = "General", date_added: str = None):
        """
        Initialize a product
        
        Args:
            product_id: Unique product identifier
            name: Product name
            price: Product price
            stock: Stock quantity
            supplier: Supplier name
            category: Product category (default: "General")
            date_added: Date product was added (auto-generated if None)
        """
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier = supplier
        self.category = category
        self.date_added = date_added or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert product to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "supplier": self.supplier,
            "category": self.category,
            "date_added": self.date_added
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Product':
        """Create product from dictionary"""
        return Product(
            product_id=data['id'],
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            supplier=data['supplier'],
            category=data.get('category', 'General'),
            date_added=data.get('date_added')
        )
    
    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"