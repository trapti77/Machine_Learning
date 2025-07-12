def fact(n): #formal argument
    if n<=1:return 1
    return n*fact(n-1)

print(fact(5))  # Output: 120  actual argument


def fact2(n=1): #default argument
    if n <= 1:  return 1
    return n * fact2(n - 1)     

print(fact2()) 

#postional vs keyword arguments
def add(a, b):  # formal arguments
    return a + b
print(add(3, 3))  # positional arguments
print(add(a=7, b=2))  # keyword arguments
print(add(b=4, a=5))  # keyword arguments in different order
print(add(1, b=2))  # mix of positional and keyword arguments
#print(add(b=3,4))  #Error: positional argument after keyword argument


