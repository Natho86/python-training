# Exercise 46: Data Analysis Tool - SOLUTION
# Difficulty: Intermediate
# Concepts: File I/O, Data processing, Statistics, Functions, Collections

import csv
from collections import Counter, defaultdict
from datetime import datetime
import json

# SOLUTION

# First, create sample data
def create_sample_data():
    """Create sample CSV file for testing."""
    sample_data = [
        ["date", "product", "category", "quantity", "price"],
        ["2024-01-15", "Laptop", "Electronics", "2", "999.99"],
        ["2024-01-16", "Book", "Books", "5", "15.99"],
        ["2024-01-17", "Phone", "Electronics", "3", "599.99"],
        ["2024-01-18", "Desk", "Furniture", "1", "299.99"],
        ["2024-01-20", "Laptop", "Electronics", "1", "999.99"],
        ["2024-02-01", "Chair", "Furniture", "4", "150.00"],
        ["2024-02-05", "Phone", "Electronics", "2", "599.99"],
        ["2024-02-10", "Book", "Books", "10", "15.99"],
        ["2024-02-15", "Tablet", "Electronics", "3", "399.99"],
        ["2024-03-01", "Desk", "Furniture", "2", "299.99"],
        ["2024-03-05", "Laptop", "Electronics", "4", "999.99"],
        ["2024-03-10", "Book", "Books", "8", "15.99"],
    ]

    with open("sales_data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)

    print("Created sample sales_data.csv")

class SalesAnalyzer:
    """Analyze sales data from CSV file."""

    def __init__(self, filename):
        """
        Initialize analyzer.

        Args:
            filename: Path to CSV file
        """
        self.filename = filename
        self.data = []
        self.load_data()

    def load_data(self):
        """Load data from CSV file."""
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields
                row['quantity'] = int(row['quantity'])
                row['price'] = float(row['price'])
                row['total'] = row['quantity'] * row['price']
                row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
                self.data.append(row)

        print(f"Loaded {len(self.data)} transactions from {self.filename}")

    def total_sales(self):
        """Calculate total sales amount."""
        return sum(item['total'] for item in self.data)

    def average_sale(self):
        """Calculate average sale amount."""
        if not self.data:
            return 0
        return self.total_sales() / len(self.data)

    def sales_by_category(self):
        """Group sales by category."""
        category_sales = defaultdict(float)
        for item in self.data:
            category_sales[item['category']] += item['total']
        return dict(category_sales)

    def top_products(self, n=5):
        """
        Find top N products by revenue.

        Args:
            n: Number of top products to return

        Returns:
            List of (product, revenue) tuples
        """
        product_sales = defaultdict(float)
        for item in self.data:
            product_sales[item['product']] += item['total']

        # Sort by revenue (descending)
        sorted_products = sorted(product_sales.items(),
                                key=lambda x: x[1],
                                reverse=True)
        return sorted_products[:n]

    def sales_by_month(self):
        """Group sales by month."""
        monthly_sales = defaultdict(float)
        for item in self.data:
            month_key = item['date'].strftime('%Y-%m')
            monthly_sales[month_key] += item['total']
        return dict(sorted(monthly_sales.items()))

    def generate_report(self):
        """Generate comprehensive sales report."""
        report = []
        report.append("=" * 60)
        report.append("SALES ANALYSIS REPORT")
        report.append("=" * 60)

        # Overall statistics
        total = self.total_sales()
        avg = self.average_sale()
        report.append(f"\nOVERALL STATISTICS:")
        report.append(f"  Total Sales: ${total:,.2f}")
        report.append(f"  Average Sale: ${avg:,.2f}")
        report.append(f"  Number of Transactions: {len(self.data)}")

        # Top products
        report.append(f"\nTOP 5 PRODUCTS:")
        for i, (product, revenue) in enumerate(self.top_products(5), 1):
            report.append(f"  {i}. {product}: ${revenue:,.2f}")

        # Sales by category
        report.append(f"\nSALES BY CATEGORY:")
        category_sales = self.sales_by_category()
        for category, amount in sorted(category_sales.items(),
                                       key=lambda x: x[1],
                                       reverse=True):
            percentage = (amount / total) * 100
            report.append(f"  {category}: ${amount:,.2f} ({percentage:.1f}%)")

        # Monthly trends
        report.append(f"\nMONTHLY SALES:")
        monthly = self.sales_by_month()
        for month, amount in monthly.items():
            report.append(f"  {month}: ${amount:,.2f}")

        report.append("\n" + "=" * 60)

        return "\n".join(report)

    def save_report(self, output_file="sales_report.txt"):
        """Save report to text file."""
        report = self.generate_report()
        with open(output_file, 'w') as f:
            f.write(report)
        print(f"\nReport saved to {output_file}")

    def export_to_json(self, output_file="sales_summary.json"):
        """Export summary to JSON."""
        summary = {
            'total_sales': self.total_sales(),
            'average_sale': self.average_sale(),
            'transaction_count': len(self.data),
            'top_products': [
                {'product': p, 'revenue': r}
                for p, r in self.top_products(5)
            ],
            'sales_by_category': self.sales_by_category(),
            'monthly_sales': self.sales_by_month()
        }

        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)

        print(f"Summary exported to {output_file}")

# Create sample data and run analysis
create_sample_data()

print("\n" + "=" * 60)
print("Running Sales Analysis")
print("=" * 60 + "\n")

# Create analyzer
analyzer = SalesAnalyzer("sales_data.csv")

# Display report
print(analyzer.generate_report())

# Save report
analyzer.save_report()

# Export to JSON
analyzer.export_to_json()

"""
EXPLANATION:
1. csv.DictReader reads CSV files into dictionaries (column names as keys)
2. defaultdict(float) creates a dictionary that defaults to 0.0 for new keys
3. We convert strings to appropriate types (int, float, datetime)
4. Data is stored in a list of dictionaries for easy processing
5. Each analysis method processes the data differently
6. Report generation combines all analyses into formatted text
7. JSON export provides machine-readable output

Key Concepts:
- CSV processing for structured data
- Data aggregation and grouping
- Statistical calculations
- Report generation
- Multiple export formats
- Class-based organization for related functionality
"""

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

class AdvancedSalesAnalyzer(SalesAnalyzer):
    """Enhanced analyzer with visualization and filtering."""

    def create_bar_chart(self, data_dict, title, max_width=40):
        """
        Create ASCII bar chart.

        Args:
            data_dict: Dictionary of label: value pairs
            title: Chart title
            max_width: Maximum bar width in characters
        """
        if not data_dict:
            return

        print(f"\n{title}")
        print("=" * 60)

        # Find max value for scaling
        max_value = max(data_dict.values())

        # Sort by value descending
        sorted_data = sorted(data_dict.items(),
                           key=lambda x: x[1],
                           reverse=True)

        for label, value in sorted_data:
            # Calculate bar length
            bar_length = int((value / max_value) * max_width)
            bar = "█" * bar_length

            # Format with label, bar, and value
            print(f"{label:15} {bar} ${value:,.2f}")

    def filter_by_date_range(self, start_date, end_date):
        """
        Filter data by date range.

        Args:
            start_date: Start date string (YYYY-MM-DD)
            end_date: End date string (YYYY-MM-DD)

        Returns:
            List of filtered records
        """
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')

        filtered = [item for item in self.data
                   if start <= item['date'] <= end]

        print(f"\nFiltered {len(filtered)} transactions between {start_date} and {end_date}")
        return filtered

    def sales_by_product_quantity(self):
        """Calculate quantity sold per product."""
        product_qty = defaultdict(int)
        for item in self.data:
            product_qty[item['product']] += item['quantity']
        return dict(product_qty)

    def generate_visual_report(self):
        """Generate report with ASCII visualizations."""
        print("\n" + "=" * 60)
        print("VISUAL SALES ANALYSIS")
        print("=" * 60)

        # Category sales chart
        self.create_bar_chart(
            self.sales_by_category(),
            "SALES BY CATEGORY"
        )

        # Top products chart
        top_products_dict = dict(self.top_products(5))
        self.create_bar_chart(
            top_products_dict,
            "TOP 5 PRODUCTS BY REVENUE"
        )

        # Monthly sales chart
        self.create_bar_chart(
            self.sales_by_month(),
            "MONTHLY SALES TREND"
        )

        # Product quantity chart
        self.create_bar_chart(
            self.sales_by_product_quantity(),
            "UNITS SOLD BY PRODUCT"
        )

# Test advanced analyzer
print("\nTesting Advanced Analyzer:")
advanced = AdvancedSalesAnalyzer("sales_data.csv")

# Generate visual report
advanced.generate_visual_report()

# Test date filtering
print("\n" + "=" * 60)
filtered_data = advanced.filter_by_date_range("2024-02-01", "2024-02-28")
print(f"Total sales in February: ${sum(item['total'] for item in filtered_data):,.2f}")

# Additional statistics
print("\n--- ADDITIONAL STATISTICS ---")

def calculate_statistics(values):
    """Calculate mean, median, min, max."""
    if not values:
        return {}

    sorted_values = sorted(values)
    n = len(values)

    return {
        'mean': sum(values) / n,
        'median': sorted_values[n // 2] if n % 2 else
                 (sorted_values[n//2-1] + sorted_values[n//2]) / 2,
        'min': min(values),
        'max': max(values),
        'count': n
    }

# Transaction value statistics
transaction_values = [item['total'] for item in analyzer.data]
stats = calculate_statistics(transaction_values)

print("\nTransaction Value Statistics:")
print(f"  Mean: ${stats['mean']:.2f}")
print(f"  Median: ${stats['median']:.2f}")
print(f"  Min: ${stats['min']:.2f}")
print(f"  Max: ${stats['max']:.2f}")
print(f"  Count: {stats['count']}")
