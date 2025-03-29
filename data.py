# Mock in memory database for testing
data = {
    "products": [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200},
        {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 800},
        {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 30},
        {"id": 4, "name": "Jeans", "category": "Clothing", "price": 60},
        {"id": 5, "name": "Headphones", "category": "Electronics", "price": 150},
    ]
}

def get_all_products():
    return data["products"]

def filter_products(category=None, price_less_than=None):
    results = data["products"]
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]
    if price_less_than:
        results = [p for p in results if p["price"] < price_less_than]
    return results
