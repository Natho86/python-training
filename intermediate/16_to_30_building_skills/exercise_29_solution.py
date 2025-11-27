# Exercise 29: Data Analysis with Lists and Dictionaries - SOLUTION
# Difficulty: Intermediate-
# Concepts: Data structures, List comprehensions, Data aggregation, Statistics

# SOLUTION
from datetime import datetime, timedelta

print("SALES DATA ANALYSIS")
print("=" * 60)

# Sample sales data
sales_data = [
    {'product': 'Laptop', 'quantity': 2, 'price': 999.99, 'date': '2024-01-15'},
    {'product': 'Mouse', 'quantity': 5, 'price': 25.50, 'date': '2024-01-15'},
    {'product': 'Keyboard', 'quantity': 3, 'price': 75.00, 'date': '2024-01-15'},
    {'product': 'Laptop', 'quantity': 1, 'price': 999.99, 'date': '2024-01-16'},
    {'product': 'Mouse', 'quantity': 8, 'price': 25.50, 'date': '2024-01-16'},
    {'product': 'Monitor', 'quantity': 2, 'price': 299.99, 'date': '2024-01-16'},
    {'product': 'Laptop', 'quantity': 3, 'price': 999.99, 'date': '2024-01-17'},
    {'product': 'Keyboard', 'quantity': 4, 'price': 75.00, 'date': '2024-01-17'},
]

print("Sample Sales Data:")
for sale in sales_data[:3]:
    print(f"  {sale}")
print(f"  ... ({len(sales_data)} total records)\n")

# 1. CALCULATE TOTAL REVENUE
print("1. TOTAL REVENUE")
print("-" * 60)

def calculate_total_revenue(sales):
    """Calculate total revenue from all sales."""
    total = sum(sale['quantity'] * sale['price'] for sale in sales)
    return total

total_revenue = calculate_total_revenue(sales_data)
print(f"Total Revenue: ${total_revenue:,.2f}\n")

# 2. FIND BEST-SELLING PRODUCTS
print("2. BEST-SELLING PRODUCTS")
print("-" * 60)

def get_product_quantities(sales):
    """Get total quantity sold for each product."""
    product_totals = {}

    for sale in sales:
        product = sale['product']
        quantity = sale['quantity']
        product_totals[product] = product_totals.get(product, 0) + quantity

    return product_totals

product_quantities = get_product_quantities(sales_data)
print("Units Sold by Product:")
for product, quantity in sorted(product_quantities.items(), key=lambda x: x[1], reverse=True):
    print(f"  {product}: {quantity} units")

# Find best seller
best_seller = max(product_quantities.items(), key=lambda x: x[1])
print(f"\nBest Selling Product: {best_seller[0]} ({best_seller[1]} units)\n")

# 3. CALCULATE AVERAGE SALE AMOUNT
print("3. AVERAGE SALE AMOUNT")
print("-" * 60)

def calculate_average_sale(sales):
    """Calculate average amount per sale transaction."""
    if not sales:
        return 0

    total = sum(sale['quantity'] * sale['price'] for sale in sales)
    return total / len(sales)

avg_sale = calculate_average_sale(sales_data)
print(f"Average Sale Amount: ${avg_sale:,.2f}")
print(f"Total Transactions: {len(sales_data)}\n")

# 4. GROUP SALES BY PRODUCT
print("4. REVENUE BY PRODUCT")
print("-" * 60)

def get_revenue_by_product(sales):
    """Calculate total revenue for each product."""
    product_revenue = {}

    for sale in sales:
        product = sale['product']
        revenue = sale['quantity'] * sale['price']
        product_revenue[product] = product_revenue.get(product, 0) + revenue

    return product_revenue

revenue_by_product = get_revenue_by_product(sales_data)
print("Revenue by Product:")
for product, revenue in sorted(revenue_by_product.items(), key=lambda x: x[1], reverse=True):
    print(f"  {product}: ${revenue:,.2f}")
print()

# 5. GROUP SALES BY DATE
print("5. DAILY SALES SUMMARY")
print("-" * 60)

def get_daily_summary(sales):
    """Get sales summary grouped by date."""
    daily_sales = {}

    for sale in sales:
        date = sale['date']
        revenue = sale['quantity'] * sale['price']

        if date not in daily_sales:
            daily_sales[date] = {
                'revenue': 0,
                'transactions': 0,
                'units': 0
            }

        daily_sales[date]['revenue'] += revenue
        daily_sales[date]['transactions'] += 1
        daily_sales[date]['units'] += sale['quantity']

    return daily_sales

daily_summary = get_daily_summary(sales_data)
print("Daily Sales:")
for date in sorted(daily_summary.keys()):
    summary = daily_summary[date]
    print(f"  {date}:")
    print(f"    Revenue: ${summary['revenue']:,.2f}")
    print(f"    Transactions: {summary['transactions']}")
    print(f"    Units: {summary['units']}")
print()

# 6. COMPREHENSIVE SALES REPORT
print("6. COMPREHENSIVE REPORT")
print("-" * 60)

def generate_sales_report(sales):
    """Generate a comprehensive sales report."""
    if not sales:
        return "No sales data available"

    # Calculate various metrics
    total_revenue = calculate_total_revenue(sales)
    avg_sale = calculate_average_sale(sales)
    product_quantities = get_product_quantities(sales)
    revenue_by_product = get_revenue_by_product(sales)

    # Build report
    report = []
    report.append("=" * 60)
    report.append("SALES ANALYSIS REPORT")
    report.append("=" * 60)
    report.append("")

    # Overview
    report.append("OVERVIEW")
    report.append("-" * 60)
    report.append(f"Total Revenue: ${total_revenue:,.2f}")
    report.append(f"Total Transactions: {len(sales)}")
    report.append(f"Average Transaction: ${avg_sale:,.2f}")
    report.append(f"Total Units Sold: {sum(product_quantities.values())}")
    report.append("")

    # Top products
    report.append("TOP PRODUCTS BY REVENUE")
    report.append("-" * 60)
    top_products = sorted(revenue_by_product.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (product, revenue) in enumerate(top_products, 1):
        units = product_quantities[product]
        report.append(f"{i}. {product}: ${revenue:,.2f} ({units} units)")
    report.append("")

    report.append("=" * 60)

    return "\n".join(report)

print(generate_sales_report(sales_data))

"""
EXPLANATION:
1. Sales data stored as list of dictionaries for flexibility
2. List comprehensions and generator expressions for calculations
3. sum() with generator: sum(expr for item in list)
4. Dictionaries used to aggregate data by category
5. .get(key, default) safely adds to dictionary values
6. sorted() with key parameter for custom sorting
7. max() with key parameter finds maximum by custom criteria

Key Concepts:
- List of dictionaries is common data structure for records
- Generator expressions are memory-efficient for calculations
- Dictionary aggregation pattern: dict[key] = dict.get(key, 0) + value
- Lambda functions for custom sorting and filtering
- Breaking complex analysis into smaller functions
"""

# Extension solution: Advanced analysis
print("\n--- EXTENSION SOLUTION: ADVANCED ANALYSIS ---")

def filter_sales_by_date_range(sales, start_date, end_date):
    """Filter sales within a date range."""
    filtered = [
        sale for sale in sales
        if start_date <= sale['date'] <= end_date
    ]
    return filtered

# Filter sales for specific date range
jan_15_16_sales = filter_sales_by_date_range(sales_data, '2024-01-15', '2024-01-16')
print(f"\nSales from Jan 15-16: {len(jan_15_16_sales)} transactions")
print(f"Revenue: ${calculate_total_revenue(jan_15_16_sales):,.2f}")

# Top N products
def get_top_products(sales, n=3, by='revenue'):
    """Get top N products by revenue or quantity."""
    if by == 'revenue':
        product_data = get_revenue_by_product(sales)
    else:  # by quantity
        product_data = get_product_quantities(sales)

    top = sorted(product_data.items(), key=lambda x: x[1], reverse=True)[:n]
    return top

print(f"\nTop 3 Products by Revenue:")
for product, revenue in get_top_products(sales_data, n=3, by='revenue'):
    print(f"  {product}: ${revenue:,.2f}")

print(f"\nTop 3 Products by Quantity:")
for product, quantity in get_top_products(sales_data, n=3, by='quantity'):
    print(f"  {product}: {quantity} units")

# Product performance analysis
def analyze_product_performance(sales):
    """Analyze performance metrics for each product."""
    products = {}

    for sale in sales:
        product = sale['product']
        if product not in products:
            products[product] = {
                'total_revenue': 0,
                'total_quantity': 0,
                'transaction_count': 0,
                'prices': []
            }

        revenue = sale['quantity'] * sale['price']
        products[product]['total_revenue'] += revenue
        products[product]['total_quantity'] += sale['quantity']
        products[product]['transaction_count'] += 1
        products[product]['prices'].append(sale['price'])

    # Calculate additional metrics
    for product, data in products.items():
        data['avg_price'] = sum(data['prices']) / len(data['prices'])
        data['avg_quantity_per_transaction'] = data['total_quantity'] / data['transaction_count']

    return products

print("\n--- PRODUCT PERFORMANCE ANALYSIS ---")
performance = analyze_product_performance(sales_data)

print(f"\n{'Product':<15} {'Revenue':>12} {'Units':>8} {'Avg Price':>12} {'Transactions':>15}")
print("-" * 70)
for product in sorted(performance.keys()):
    data = performance[product]
    print(f"{product:<15} ${data['total_revenue']:>10,.2f} {data['total_quantity']:>8} "
          f"${data['avg_price']:>10,.2f} {data['transaction_count']:>15}")

# Comparative analysis
def compare_periods(sales, date_separator):
    """Compare sales before and after a specific date."""
    before = [s for s in sales if s['date'] < date_separator]
    after = [s for s in sales if s['date'] >= date_separator]

    before_revenue = calculate_total_revenue(before)
    after_revenue = calculate_total_revenue(after)

    return {
        'before': {
            'transactions': len(before),
            'revenue': before_revenue,
            'avg_sale': calculate_average_sale(before) if before else 0
        },
        'after': {
            'transactions': len(after),
            'revenue': after_revenue,
            'avg_sale': calculate_average_sale(after) if after else 0
        }
    }

print("\n--- PERIOD COMPARISON ---")
comparison = compare_periods(sales_data, '2024-01-16')

print(f"\nBefore Jan 16:")
print(f"  Transactions: {comparison['before']['transactions']}")
print(f"  Revenue: ${comparison['before']['revenue']:,.2f}")
print(f"  Average Sale: ${comparison['before']['avg_sale']:,.2f}")

print(f"\nFrom Jan 16 onwards:")
print(f"  Transactions: {comparison['after']['transactions']}")
print(f"  Revenue: ${comparison['after']['revenue']:,.2f}")
print(f"  Average Sale: ${comparison['after']['avg_sale']:,.2f}")

# Calculate growth
if comparison['before']['revenue'] > 0:
    growth = ((comparison['after']['revenue'] - comparison['before']['revenue'])
              / comparison['before']['revenue'] * 100)
    print(f"\nRevenue Growth: {growth:+.1f}%")

# Sales with profit margin
print("\n--- PROFIT ANALYSIS ---")

# Add cost data to sales
sales_with_costs = [
    {'product': 'Laptop', 'quantity': 2, 'price': 999.99, 'cost': 700.00, 'date': '2024-01-15'},
    {'product': 'Mouse', 'quantity': 5, 'price': 25.50, 'cost': 12.00, 'date': '2024-01-15'},
    {'product': 'Keyboard', 'quantity': 3, 'price': 75.00, 'cost': 40.00, 'date': '2024-01-15'},
]

def calculate_profit_margin(sales):
    """Calculate profit margin for sales with cost data."""
    results = []

    for sale in sales:
        revenue = sale['quantity'] * sale['price']
        cost = sale['quantity'] * sale['cost']
        profit = revenue - cost
        margin = (profit / revenue * 100) if revenue > 0 else 0

        results.append({
            'product': sale['product'],
            'revenue': revenue,
            'cost': cost,
            'profit': profit,
            'margin': margin
        })

    return results

profit_analysis = calculate_profit_margin(sales_with_costs)

print(f"\n{'Product':<15} {'Revenue':>12} {'Cost':>12} {'Profit':>12} {'Margin':>10}")
print("-" * 65)
for item in profit_analysis:
    print(f"{item['product']:<15} ${item['revenue']:>10,.2f} ${item['cost']:>10,.2f} "
          f"${item['profit']:>10,.2f} {item['margin']:>9.1f}%")

# Summary statistics
print("\n--- SUMMARY STATISTICS ---")

def get_statistics(values):
    """Calculate statistics for a list of values."""
    if not values:
        return None

    sorted_values = sorted(values)
    n = len(values)

    stats = {
        'count': n,
        'sum': sum(values),
        'mean': sum(values) / n,
        'min': min(values),
        'max': max(values),
        'range': max(values) - min(values),
    }

    # Median
    if n % 2 == 0:
        stats['median'] = (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
    else:
        stats['median'] = sorted_values[n//2]

    return stats

# Get all sale amounts
sale_amounts = [sale['quantity'] * sale['price'] for sale in sales_data]
stats = get_statistics(sale_amounts)

print("\nSale Amount Statistics:")
print(f"  Count: {stats['count']}")
print(f"  Total: ${stats['sum']:,.2f}")
print(f"  Mean: ${stats['mean']:,.2f}")
print(f"  Median: ${stats['median']:,.2f}")
print(f"  Min: ${stats['min']:,.2f}")
print(f"  Max: ${stats['max']:,.2f}")
print(f"  Range: ${stats['range']:,.2f}")

print("\n" + "=" * 60)
print("Analysis complete!")
print("=" * 60)
