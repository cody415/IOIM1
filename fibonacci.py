# Fibonacci Series up to n terms

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Take input from user
n_terms = int(input("Enter the number of terms: "))

if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series up to", n_terms, "terms:")
    print(fibonacci(n_terms))
