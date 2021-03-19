def factorial(n):
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

    # Driver Code


num = 5;
print("Factorial of", num, "is",
      factorial(num))
