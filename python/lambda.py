#print sum of natural number using lambda function

sum=lambda a,b:a+b

print(sum(10,20))  # Output: 30

sum1=(lambda a,b,c:a+b+c)(10,20,30)

print(sum1)  # Output: 60

f=lambda n:n if n<=1 else n+f(n-1)
print(f(5))  # Output: 15 (5 + 4 + 3 + 2 + 1)