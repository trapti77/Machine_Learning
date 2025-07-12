'''s5=str(123)
print(s5)
s6=str(333.45)
print(s6)

s1="hello world"
print(s1[2])

for s in s1:
    print(s,end='')
    
print(s1*3)  #repeatition operator
print(s5+s6)# concatenation operator

#comparision operator
s1="hello"
s2="world"
print(s1>s2)
'''
#STR METHODS
'''
s="trapti patel"
print(s.index('a'))
print(s.count('t'))
print(s.split(' '))
print(" ".join(["abc","sd"]))
print(s.endswith('patel'))
print(s.startswith('trapti'))
print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())
print(s.replace('t','k'))
print(s.replace('trapti','krati'))
s4="sum of {} and {} is= {}"
print(s4.format(10,20,10+20))
print(s.isdigit())
print(s.capitalize())
print(s4.partition('and'))
'''

#slicing operator

s2="trapti patel"
print(s2[0:25:2])
print(s2[::-1])
print(s2[0:10:1])






