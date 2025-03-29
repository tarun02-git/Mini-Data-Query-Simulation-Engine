def translate_query(query):
    query = query.lower()

    if "electronics" in query:
        category = "Electronics"
    elif "clothing" in query:
        category = "Clothing"
    else:
        category = None

    if "less than" in query:
        try:
            price = int(query.split("less than")[-1].strip())
        except ValueError:
            price = None
    else:
        price = None

    return category, price

def process_query(category, price):
    from data import filter_products
    return filter_products(category=category, price_less_than=price)

def validate_query(query):
    query = query.lower()
    if "electronics" in query or "clothing" in query or "less than" in query:
        return True
    return False

def convert_to_pseudo_sql(query):
    category, price = translate_query(query)
    sql = "SELECT * FROM products"
    conditions = []
    if category:
        conditions.append(f"category = '{category}'")
    if price:
        conditions.append(f"price < {price}")
    if conditions:
        sql += " WHERE " + " AND ".join(conditions)
    return sql
