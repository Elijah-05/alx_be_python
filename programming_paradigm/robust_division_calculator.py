
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        deno = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        try:
            result = float(numerator) / float(denominator)
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {result}"