

def division(numerator, denominator):
    assert denominator != 0, "cannot divide by zero denominator must be non-zero"
    return numerator / denominator

def division(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return numerator / denominator