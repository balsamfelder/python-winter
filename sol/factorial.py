def factorial(x):
    return x * factorial(x - 1) if x > 0 else 1 if x == 0 else None 
