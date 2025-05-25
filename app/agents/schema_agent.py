def extract_schema_info(question: str):
    keywords = {
        "customers": ["customer", "name", "email"],
        "sales": ["sales", "amount", "purchase", "bought"],
        "employees": ["employee", "staff", "hire"],
        "products": ["product", "category", "price"],
        "projects": ["project", "deadline", "end"]
    }

    relevant_tables = []
    for table, words in keywords.items():
        if any(word in question.lower() for word in words):
            relevant_tables.append(table)

    return relevant_tables
