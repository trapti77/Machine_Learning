#CREATE Tuple
t1=(10,30,30,40,50)
#print(type(t1))
t2=(10)#error
t5=(10,)
#print(type(t2))
l1=[2,3,5]
t3=l1,3,4,5,
#print(type(t3))

#accessing element
#print(t1[0])
#print(t1[5])#out of range
i=0
'''
while i<len(t3):
    print(t3[i],end=" ")
    i+=1

print()
print(sum(t1))
print(max(t1))
print(min(t1))'''

#concatination and repeatition and comparision  operator
'''
print(t1+t3)
print(t1*3)
print(t1>t2)
'''
#Tuple object method
'''
print(t1.index(40))
print(t1.count(30))
'''
#slicing Operator
'''
print(t1[::-1])
print(t1[0:5:1])
print(t1[0:8:2])
print(t1[0:8:3])
'''
#user input of tuple

#t1=tuple(int(e) for e in range(0,int(input())))
#OR
t1=tuple([int(e) for e in input().split(',')])
print(t1)
t3=tuple()
t4=tuple([1,2,3,4,5])
t5=tuple(range(5))

