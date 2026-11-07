'''
Usage of for with loops
Nested Loops --> Loops inside another loop. They are commonly used in
pattern printing, matrix operations and solving various algorithms problems

syntax:

for in range(outer_loop_range):
    for j in range(inner_loop_range)
        #code...

#Understand with a simple example
for i in range(3): #outer loop runs 3 times
    for j in range(4): #inner loop 2 times for each outer loop
        print(f' i =  {i}, j = {j}')
#for every outerloop innerlopp will be completely executed...
#outerloop --> rows --> innerloop --> columns

for i in range(2): #outer loop runs 3 times
    for j in range(4): #inner loop 2 times for each outer loop
        print(f' i =  {i}, j = {j}')


#Number patterns --> Row based number patterns , column based number patterns
'''
#1 2 3
#1 2 3
#1 2 3
'''
for i in range(1,4): #i - 1,2,3
    for j in range(1,4): #j - 1,2,3
        #print(i,j)
        print(j,end = ' ')
    print()
'''
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4

for i in range(1,5): #i - 1,2,3,4
    for j in range(5): #j - 1,2,3,4
        #print(i,j)
        print(i,end = ' ')
    print()

A A A A A
B B B B B
C C C C C

for i in range(65,68): 
    for j in range(5): 
        #print(i,j)
        print(chr(i),end = ' ')
    print()

for i in range(4): 
    for j in range(65,69): 
        #print(i,j)
        print(chr(j),end = ' ')
    print()
    
1 2 3
4 5 6
7 8 9

num = 1
for i in range(1,4): 
    for j in range(1,4): 
        #print(i,j)
        print(num,end = ' ')
        num += 1
    print()


#Square pattern --> * with n rows and and columns
n = int(input("enter the values  :"))
for i in range(n):
    for j in range(n):
        print('*',end =' ' )
    print()

#change this with different values
n = int(input("enter the values  : "))
for i in range(n):
    for j in range(n+1):
        print('*',end ='  ' )
    print()

#Right angled triangle
*
* *
* * *
* * * *
* * * * *

for i in range(1,6):
    for j in range(i):
        i = '*'
        print(i,end = ' ' )
    print()

        #print(f'value of i is {i} , value of j is {j}' )

#Inverted Triangle
* * * * *
* * * *
* * *
* *
*

n = int(input("enter the value : "))
for i in range(1,n):
    for j in range(n-i):
        i = '*'
        print(i,end = ' ' )
    print()

n = int(input("enter the value : "))
for i in range(n,0,-1):
    for j in range(i):
        i = '*'
        print(i,end = ' ' )
    print()

#Home task -->

1
2 3
4 5 6
7 8 9 10

num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
'''
'''
n = int(input("Enter number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
    '''
'''
A
B C
D E F
G H I J

num = 65

for i in range(1, 5):
    for j in range(i):
        print(chr(num), end=" ")
        num += 1
    print()
'''
'''
n = int(input("Enter number of rows: "))
num = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(num), end=" ")
        num += 1
    print()
    '''
'''
A
A B
A B C
A B C D
A B C D E

for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
'''
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
    '''
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
'''
#star pyramid pattern:

                    *
                *       *
            *       *       *
        *       *       *       *
    *       *       *       *       *

n = int(input("Enter a value : "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        #print(j, end=" ")
        if j <= n-i:
            #print(i,j)
            print("",end = "")
        else:
            print("*",end = " ")
    print()

n = int(input("Enter a value : "))
for i in range(n):
    print("  "*(n-i-1)+" * "*(i+1))
for i in range(n-1):
    print("  " * (i+1) + " * " * (n-i-1))
'''












