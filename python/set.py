#HOW TO CREATE SET OBJECT
s1={1,5,6,7,8}
s2={}#not a set it is a empty dict
s3=set()
s4=set([1,2,3,4,5])
#print(type(s4))
#s5=set(10,20,30) error
#s5=set(10)#error
s6=set("trapti")
#print(s6)


#Q. write program to remove duplicate [10,20,10,30,40,30,20,10]
l1=[10,20,10,30,40,30,20,10]
l2=list(set(l1))
#print(l2)

#concatination And repeatition operator
#we can not perfrom thi operation on set


#comparision operator

s7={30,29,47,20,10}
s8={48,37,59,27,10}
#print(s7>s8)

s7.add(100)
#s7.add(100,200)#error But
s7.add((300,400))
#print(s7)

