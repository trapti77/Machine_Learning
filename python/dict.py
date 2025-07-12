#Create Dict
d1={}
d2=dict()
d3={100:"abc",200:"def"}
d4=dict(r="abc",p="def")
#print(type(d4))

#Accessing 
#print(d3[100])
#for k in d3:
 #   print(k," ",d3[k])
    

#METHODS
'''
for k,d in d3.items():
    print(k,d)

for k in d3.keys():
    print(k,end=" ")

print()
    
for v in d3.values():
    print(v,end=" ")

'''
# built In metod len(), max(),min(),sorted()
#comparision operator-- but in this >,<,>=,<= not support only !=,== support

#methods d1.pop(200) , d1.popitem(), d1,clear()

#comprehension

d4={a:a**2 for a in range(1,5)}

print(d4)
