'''
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
