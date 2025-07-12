#l1=list(int(i) for i in input("enter number :").split(','))
#comparision operator
l1=[2,3,4,5]
l2=[1,2,6,7]
if l1>l2:
    print("lis tone is greater")
else:
    print("list two is greater")
    
#repeatition operator

l3=l1*3
print(l3)

#membership operator
l4=[1,2,3,4,5]
if 3 in l4:
    print("3 is present in list")
else:
    print("3 is not present in list")
    
#identity operator
l5=[1,2,3]          
l6=l5
if l5 is l6:
    print("l5 and l6 are same")     
else:
    print("l5 and l6 are not same")
    
#list of lists

l7=[[1,2,3],[4,5,6],[7,8,9]]

print(l7[0][2])

for e in l7:
    print(e)
    
#list Object

l8=list()
l8.append(30)
l8.append(20)
l8.append(30)
l8.append(40)
print(l8)
print(l8.count(30))
print(l8.index(30))
print(sorted(l8))
print(sorted(l8,reverse=True))

#list Comprehension
l9=[int(e) for e in input("enter number :").split(' ')]
print(l9)

