def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

# Example call with uncommon error
print(function_with_uncommon_error(10, 'a')) # TypeError
print(function_with_uncommon_error(10, 0))   # ZeroDivisionError
print(function_with_uncommon_error(10, 2))   # 5.0