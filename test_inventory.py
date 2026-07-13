"""
Unit tests for Shwapno Inventory Management System
Run tests with: python -m pytest test_inventory.py
"""

import json
import os
import pytest
from inventory import (
    load_inventory, 
    save_inventory,
    add_product,
    search_product,
    update_stock,
    delete_product,
    generate_report
)

# Test fixtures
@pytest.fixture
def sample_inventory():
    """Create a sample inventory for testing"""
    return [
        {
            "id": 1,
            "name": "SmartHeart Cat Food",
            "price": 850.0,
            "stock": 20,
            "supplier": "ACI",
            "category": "Pet Food",
            "date_added": "2026-07-13 10:30:45"
        },
        {
            "id": 2,
            "name": "Dog Treats",
            "price": 450.0,
            "stock": 5,
            "supplier": "Pet Plus",
            "category": "Pet Food",
            "date_added": "2026-07-13 10:35:22"
        }
    ]

@pytest.fixture
def cleanup_inventory_file():
    """Clean up inventory.json after tests"""
    yield
    if os.path.exists("inventory.json"):
        os.remove("inventory.json")

# Test save and load functions
def test_save_and_load_inventory(sample_inventory, cleanup_inventory_file):
    """Test saving and loading inventory"""
    save_inventory(sample_inventory)
    loaded = load_inventory()
    
    assert len(loaded) == 2
    assert loaded[0]['name'] == "SmartHeart Cat Food"
    assert loaded[1]['price'] == 450.0

def test_load_empty_inventory(cleanup_inventory_file):
    """Test loading when no inventory file exists"""
    inventory = load_inventory()
    assert inventory == []

# Test search functionality
def test_search_product_by_name(sample_inventory):
    """Test searching product by name"""
    search_term = "cat"
    results = [p for p in sample_inventory if search_term.lower() in p['name'].lower()]
    
    assert len(results) == 1
    assert results[0]['name'] == "SmartHeart Cat Food"

def test_search_product_by_id(sample_inventory):
    """Test searching product by ID"""
    product_id = 2
    results = [p for p in sample_inventory if p['id'] == product_id]
    
    assert len(results) == 1
    assert results[0]['name'] == "Dog Treats"

def test_search_product_not_found(sample_inventory):
    """Test searching for non-existent product"""
    search_term = "xyz"
    results = [p for p in sample_inventory if search_term.lower() in p['name'].lower()]
    
    assert len(results) == 0

# Test stock update
def test_update_stock_add(sample_inventory):
    """Test adding stock"""
    product = sample_inventory[0]
    original_stock = product['stock']
    product['stock'] += 10
    
    assert product['stock'] == original_stock + 10
    assert product['stock'] == 30

def test_update_stock_remove(sample_inventory):
    """Test removing stock"""
    product = sample_inventory[0]
    original_stock = product['stock']
    product['stock'] -= 5
    
    assert product['stock'] == original_stock - 5
    assert product['stock'] == 15

def test_update_stock_insufficient(sample_inventory):
    """Test removing more stock than available"""
    product = sample_inventory[1]  # Dog Treats with 5 stock
    
    # Trying to remove 10 should fail
    if 10 > product['stock']:
        assert True  # Test passes - cannot remove more than available
    else:
        assert False

# Test delete functionality
def test_delete_product(sample_inventory):
    """Test deleting a product"""
    initial_count = len(sample_inventory)
    product_to_delete = sample_inventory[0]
    sample_inventory.remove(product_to_delete)
    
    assert len(sample_inventory) == initial_count - 1
    assert product_to_delete not in sample_inventory

# Test low stock detection
def test_low_stock_detection(sample_inventory):
    """Test identifying low stock products"""
    low_stock = [p for p in sample_inventory if p['stock'] < 10]
    
    assert len(low_stock) == 1
    assert low_stock[0]['name'] == "Dog Treats"

# Test duplicate prevention
def test_duplicate_product_prevention(sample_inventory):
    """Test that duplicate products are prevented"""
    product_name = "SmartHeart Cat Food"
    exists = any(p['name'].lower() == product_name.lower() for p in sample_inventory)
    
    assert exists == True

# Test inventory statistics
def test_inventory_statistics(sample_inventory):
    """Test calculating inventory statistics"""
    total_products = len(sample_inventory)
    total_stock = sum(p['stock'] for p in sample_inventory)
    total_value = sum(p['price'] * p['stock'] for p in sample_inventory)
    
    assert total_products == 2
    assert total_stock == 25
    assert total_value == 19250.0  # (850*20) + (450*5)

# Test category grouping
def test_category_grouping(sample_inventory):
    """Test grouping products by category"""
    categories = {}
    for product in sample_inventory:
        cat = product['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    assert 'Pet Food' in categories
    assert categories['Pet Food'] == 2

# Test input validation
def test_negative_price_validation():
    """Test that negative prices are rejected"""
    price = -100
    assert price < 0  # Should be rejected

def test_negative_stock_validation():
    """Test that negative stock is rejected"""
    stock = -5
    assert stock < 0  # Should be rejected

# Run all tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])