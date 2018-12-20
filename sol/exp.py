def factorial(x):
    return x * factorial(x - 1) if x > 0 else 1 if x == 0 else None 

def exp(x, tol=1e-8):
    n = 1
    approx = 1
    while abs(x ** n / factorial(n)) >= tol:
        approx += x ** n / factorial(n)
        n += 1
    return approx
