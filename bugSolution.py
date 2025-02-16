def function_with_uncommon_error(x, y):
    try:
        if not isinstance(y, (int, float)):
            raise TypeError("Divisor must be a number")
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"TypeError: {e}"

# Example call with uncommon error
print(function_with_uncommon_error(10, 'a')) # TypeError
print(function_with_uncommon_error(10, 0))   # Division by zero
print(function_with_uncommon_error(10, 2))   # 5.0