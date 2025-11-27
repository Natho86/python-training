"""
Inventory Management System - Intermediate Python Project
==========================================================
A text-based inventory system for managing products with stock tracking and reporting.

Features:
- Add, update, delete products
- Track stock quantities
- Low stock alerts
- Search and filter products
- Generate reports
- JSON data persistence
- Product categories

Concepts: OOP, JSON, file I/O, dictionaries, list comprehensions, error handling, data validation
"""

import json
import os
from datetime import datetime
from collections import defaultdict


class Product:
    """Represents a product in the inventory."""

    def __init__(self, name, sku, category, quantity, price, min_stock=5, product_id=None):
        """Initialize a product."""
        self.id = product_id if product_id else datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.name = name
        self.sku = sku.upper()
        self.category = category
        self.quantity = int(quantity)
        self.price = float(price)
        self.min_stock = int(min_stock)
        self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def is_low_stock(self):
        """Check if product is low on stock."""
        return self.quantity <= self.min_stock

    def is_out_of_stock(self):
        """Check if product is out of stock."""
        return self.quantity == 0

    def total_value(self):
        """Calculate total value of this product in inventory."""
        return self.quantity * self.price

    def to_dict(self):
        """Convert product to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'sku': self.sku,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price,
            'min_stock': self.min_stock,
            'last_updated': self.last_updated
        }

    def __str__(self):
        """String representation."""
        status = ""
        if self.is_out_of_stock():
            status = " [OUT OF STOCK]"
        elif self.is_low_stock():
            status = " [LOW STOCK]"

        return f"{self.sku:<10} | {self.name:<25} | {self.category:<15} | Qty: {self.quantity:4} | ${self.price:7.2f}{status}"


class InventorySystem:
    """Main inventory management system."""

    CATEGORIES = ['Electronics', 'Clothing', 'Food', 'Books', 'Toys', 'Sports', 'Home', 'Other']

    def __init__(self, filename='inventory.json'):
        """Initialize the inventory system."""
        self.filename = filename
        self.products = []
        self.load_data()

    def load_data(self):
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.products = [
                        Product(
                            p['name'], p['sku'], p['category'],
                            p['quantity'], p['price'],
                            p.get('min_stock', 5),
                            p['id']
                        ) for p in data
                    ]
                print(f"✓ Loaded {len(self.products)} products")
            else:
                print("No existing inventory file. Starting fresh!")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.products = []

    def save_data(self):
        """Save inventory to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump([p.to_dict() for p in self.products], f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def find_by_sku(self, sku):
        """Find product by SKU."""
        for product in self.products:
            if product.sku == sku.upper():
                return product
        return None

    def sku_exists(self, sku):
        """Check if SKU already exists."""
        return self.find_by_sku(sku) is not None

    def add_product(self):
        """Add a new product."""
        print("\n=== Add New Product ===")

        name = input("Product name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        sku = input("SKU code: ").strip().upper()
        if not sku:
            print("SKU cannot be empty!")
            return

        if self.sku_exists(sku):
            print(f"SKU '{sku}' already exists!")
            return

        # Show categories
        print("\nCategories:")
        for i, cat in enumerate(self.CATEGORIES, 1):
            print(f"{i}. {cat}")

        try:
            cat_choice = int(input("Select category (1-8): "))
            if 1 <= cat_choice <= len(self.CATEGORIES):
                category = self.CATEGORIES[cat_choice - 1]
            else:
                print("Invalid category!")
                return
        except ValueError:
            print("Invalid input!")
            return

        try:
            quantity = int(input("Initial quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                return
        except ValueError:
            print("Invalid quantity!")
            return

        try:
            price = float(input("Price per unit: $"))
            if price < 0:
                print("Price cannot be negative!")
                return
        except ValueError:
            print("Invalid price!")
            return

        try:
            min_stock = int(input("Minimum stock level (default 5): ") or "5")
        except ValueError:
            min_stock = 5

        product = Product(name, sku, category, quantity, price, min_stock)
        self.products.append(product)
        self.save_data()
        print(f"\n✓ Product added successfully! (SKU: {product.sku})")

    def view_all_products(self):
        """View all products."""
        if not self.products:
            print("\nNo products in inventory!")
            return

        print(f"\n=== All Products ({len(self.products)} total) ===")
        print("-" * 100)
        print(f"{'SKU':<10} | {'Name':<25} | {'Category':<15} | {'Quantity':>8} | {'Price':>9}")
        print("-" * 100)

        total_value = 0
        for product in sorted(self.products, key=lambda x: x.name):
            print(product)
            total_value += product.total_value()

        print("-" * 100)
        print(f"Total Inventory Value: ${total_value:,.2f}")

    def search_products(self):
        """Search for products."""
        print("\n=== Search Products ===")
        query = input("Enter search term (name or SKU): ").strip().lower()

        if not query:
            return

        results = [
            p for p in self.products
            if query in p.name.lower() or query in p.sku.lower()
        ]

        if not results:
            print("No products found!")
            return

        print(f"\nFound {len(results)} product(s):")
        print("-" * 100)
        for product in results:
            print(product)

    def update_stock(self):
        """Update product stock quantity."""
        print("\n=== Update Stock ===")

        sku = input("Enter product SKU: ").strip().upper()
        product = self.find_by_sku(sku)

        if not product:
            print(f"Product with SKU '{sku}' not found!")
            return

        print(f"\nProduct: {product.name}")
        print(f"Current quantity: {product.quantity}")

        print("\n1. Add stock")
        print("2. Remove stock")
        print("3. Set exact quantity")

        choice = input("Choose option (1-3): ").strip()

        try:
            if choice == '1':
                amount = int(input("Amount to add: "))
                if amount < 0:
                    print("Amount must be positive!")
                    return
                product.quantity += amount
                print(f"✓ Added {amount} units. New quantity: {product.quantity}")

            elif choice == '2':
                amount = int(input("Amount to remove: "))
                if amount < 0:
                    print("Amount must be positive!")
                    return
                if amount > product.quantity:
                    print(f"Cannot remove {amount} units. Only {product.quantity} in stock!")
                    return
                product.quantity -= amount
                print(f"✓ Removed {amount} units. New quantity: {product.quantity}")

            elif choice == '3':
                new_qty = int(input("New quantity: "))
                if new_qty < 0:
                    print("Quantity cannot be negative!")
                    return
                old_qty = product.quantity
                product.quantity = new_qty
                print(f"✓ Updated quantity from {old_qty} to {new_qty}")

            else:
                print("Invalid choice!")
                return

            product.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_data()

            if product.is_low_stock():
                print(f"⚠️  Warning: {product.name} is now at or below minimum stock level!")

        except ValueError:
            print("Invalid input!")

    def update_product(self):
        """Update product details."""
        print("\n=== Update Product ===")

        sku = input("Enter product SKU: ").strip().upper()
        product = self.find_by_sku(sku)

        if not product:
            print(f"Product with SKU '{sku}' not found!")
            return

        print(f"\nUpdating: {product.name}")
        print("(Press Enter to keep current value)")

        name = input(f"Name [{product.name}]: ").strip()
        if name:
            product.name = name

        price_input = input(f"Price [{product.price}]: ").strip()
        if price_input:
            try:
                price = float(price_input)
                if price >= 0:
                    product.price = price
            except ValueError:
                print("Invalid price, keeping original")

        min_stock_input = input(f"Minimum stock level [{product.min_stock}]: ").strip()
        if min_stock_input:
            try:
                min_stock = int(min_stock_input)
                if min_stock >= 0:
                    product.min_stock = min_stock
            except ValueError:
                print("Invalid value, keeping original")

        product.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_data()
        print("✓ Product updated!")

    def delete_product(self):
        """Delete a product."""
        print("\n=== Delete Product ===")

        sku = input("Enter product SKU: ").strip().upper()

        for i, product in enumerate(self.products):
            if product.sku == sku:
                print(f"\nDeleting: {product}")
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm == 'yes':
                    self.products.pop(i)
                    self.save_data()
                    print("✓ Product deleted!")
                return

        print(f"Product with SKU '{sku}' not found!")

    def low_stock_report(self):
        """Show products with low or no stock."""
        low_stock = [p for p in self.products if p.is_low_stock()]
        out_of_stock = [p for p in self.products if p.is_out_of_stock()]

        if not low_stock and not out_of_stock:
            print("\n✓ All products have adequate stock levels!")
            return

        if out_of_stock:
            print("\n=== OUT OF STOCK ===")
            print("-" * 100)
            for product in sorted(out_of_stock, key=lambda x: x.name):
                print(product)

        if low_stock:
            print("\n=== LOW STOCK ===")
            print("-" * 100)
            for product in sorted(low_stock, key=lambda x: x.quantity):
                if not product.is_out_of_stock():  # Don't show out-of-stock again
                    print(product)

    def category_report(self):
        """Show inventory grouped by category."""
        if not self.products:
            print("\nNo products in inventory!")
            return

        print("\n=== Inventory by Category ===")

        categorized = defaultdict(list)
        for product in self.products:
            categorized[product.category].append(product)

        total_value = 0
        for category in sorted(categorized.keys()):
            products = categorized[category]
            category_qty = sum(p.quantity for p in products)
            category_value = sum(p.total_value() for p in products)
            total_value += category_value

            print(f"\n{category} ({len(products)} products, {category_qty} units, ${category_value:,.2f}):")
            for product in sorted(products, key=lambda x: x.name):
                print(f"  {product}")

        print(f"\nTotal Inventory Value: ${total_value:,.2f}")

    def inventory_summary(self):
        """Show inventory statistics."""
        if not self.products:
            print("\nNo products in inventory!")
            return

        print("\n=== Inventory Summary ===")

        total_products = len(self.products)
        total_items = sum(p.quantity for p in self.products)
        total_value = sum(p.total_value() for p in self.products)
        low_stock_count = len([p for p in self.products if p.is_low_stock()])
        out_of_stock_count = len([p for p in self.products if p.is_out_of_stock()])

        print(f"Total Product Types: {total_products}")
        print(f"Total Items in Stock: {total_items}")
        print(f"Total Inventory Value: ${total_value:,.2f}")
        print(f"Average Value per Product: ${total_value / total_products:,.2f}")

        if out_of_stock_count > 0:
            print(f"\n⚠️  Out of Stock: {out_of_stock_count} products")
        if low_stock_count > 0:
            print(f"⚠️  Low Stock: {low_stock_count} products")

        # Most valuable products
        print("\nTop 5 Most Valuable (by total value):")
        top_value = sorted(self.products, key=lambda x: x.total_value(), reverse=True)[:5]
        for i, product in enumerate(top_value, 1):
            print(f"  {i}. {product.name}: ${product.total_value():,.2f}")

    def run(self):
        """Run the main application loop."""
        print("\n" + "="*60)
        print("         INVENTORY MANAGEMENT SYSTEM")
        print("="*60)

        while True:
            print("\n=== Main Menu ===")
            print("1. Add Product")
            print("2. View All Products")
            print("3. Search Products")
            print("4. Update Stock")
            print("5. Update Product Details")
            print("6. Delete Product")
            print("7. Low Stock Report")
            print("8. Category Report")
            print("9. Inventory Summary")
            print("10. Exit")

            choice = input("\nEnter choice (1-10): ").strip()

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.view_all_products()
            elif choice == '3':
                self.search_products()
            elif choice == '4':
                self.update_stock()
            elif choice == '5':
                self.update_product()
            elif choice == '6':
                self.delete_product()
            elif choice == '7':
                self.low_stock_report()
            elif choice == '8':
                self.category_report()
            elif choice == '9':
                self.inventory_summary()
            elif choice == '10':
                print("\nThank you for using Inventory System!")
                break
            else:
                print("\nInvalid choice! Please enter 1-10.")


if __name__ == "__main__":
    system = InventorySystem()
    system.run()
