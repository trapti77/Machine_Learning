
x=int(input("Enter the number of rows: "))
# pattern 1
'''       t
        t t t
      t t t t t       
    t t t t t t t     
  t t t t t t t t t  '''
'''for i in range(x,0,-1):
    for j in range(0,x):
        if j<i:
            print(" ",end=' ')
        else :
            print("t",end=' ')
    for k in range(x+1,0,-1):
        if k<=i:
            print(" ",end=' ')
        else :
            print("t",end=' ')
    print()'''
    
# pattern 2
'''t t t t t 
     t t t t 
       t t t 
         t t 
           t '''
'''for i in range(0,x):
    for j in range(0,x):
        if j<i:
            print(" ",end=' ')
        else :
            print("t",end=' ')
    print()
    '''
# pattern 3
''' t t t t 
    t t t   
    t t     
    t    '''
'''for i in range(x,0,-1):
    for j in range(i,0,-1):
        if j<i:
            print("t",end=' ')
        else :
            print(" ",end=' ')
    print()
'''
# pattern 4
'''* * * * * * * * * 
    * * * * * * *   
      * * * * *     
       * * *       
         *'''
'''for i in range(0,x):
    for j in range(0,x):
        if j<i:
            print(" ",end=' ')
        else :
            print("*",end=' ')
    for j in range(x-1,0,-1):
        if i>=j:
            print(" ",end=' ')
        else :
            print("*",end=' ')
    print()
'''
#pattern 5

    
   