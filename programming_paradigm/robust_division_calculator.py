# robust_division_calculator.py
class RobustDivision:
    def __init__ (self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        result = 0
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
