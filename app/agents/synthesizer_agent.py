def synthesize_answer(question: str, result: dict):
    if "error" in result:
        return f"Error: {result['error']}"
    elif not result["rows"]:
        return "No data found for this query."
    else:
        # Convert first row to comma-separated string
        flat_answer = ', '.join(str(x) for x in result["rows"][0])
        return f"Answer: {flat_answer}"
