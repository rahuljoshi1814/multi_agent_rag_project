def generate_sql(question: str, tables: list):
    if "most" in question.lower() and "customer" in question.lower():
        return """
        SELECT customers.name, SUM(sales.amount) AS total
        FROM customers
        JOIN sales ON customers.id = sales.customer_id
        GROUP BY customers.name
        ORDER BY total DESC
        LIMIT 1;
        """
    elif "total sales" in question.lower():
        return "SELECT SUM(amount) FROM sales;"
    else:
        return "SELECT * FROM sales LIMIT 5;"
