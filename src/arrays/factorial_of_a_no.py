def fact(n):
     f = 1
     while (n > 1):
          f *= n
          n -= 1
     return f

a = input("enter the number whose factorial you want  :")
a = int(a)
l = fact(a)
print("factorial of a number ",l)