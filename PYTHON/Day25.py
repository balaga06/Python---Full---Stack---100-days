'''
# Built-in Functions --> Functions which are already available in Python.
# Examples: abs(), any(), all(), bin(), bool(), etc.
# dir(builtins) --> Used to display the names of built-in functions and objects.
# Other built-in functions: enumerate(), zip(), etc.
'''
details = ['Codegnan', 'Saketh', 'PFS-VSP-007']
'''
#Method 1: Using for loop with index()
for i in details:
    print(details.index(i), ':', i)
#Method 2: Using for loop with range()
for i in range(len(details)):
    print(i, ':', details[i])

for i,j in enumerate(details,1):

#enumerate() will create a counter object for an iterable
#zip() will combine multiple iterable into a single iterable

data = ['ajay','sai','sanjay']
marks = (20,24,25)
place = ["vizag","vjy","hyd"] 
details = dict(zip(data,marks)) #if we take one more iterable it raises value error
print(details)
    print(f'{i} : {j}')

#eval() --> you can take any input --> dict
salaries = eval(input("enter the salaries : "))
print(salaries)
print(type(salaries))

print(int(4.56))
print(round(4.56)) #round it will round off to next decimals/nearest value
print(round(4.567,2))
'''
#Function is termed as First class object
#Recursive Functions  --> A Function Calling itself , where it make the smaller problem is broken into mutliple times....
#Depends on two cases --> base case (it indicates when to stop recursion)
                                        #--> Recursive case(it makes the problem to be repeated)
#suitable for tree structures , graph traversal....
'''
Syntax :
def function():
     if base_condition:
         return
    function( ) #we write our recursive
function()

#factorial approch using recursion
def factorial(n):
    """Recursive Usage"""
    if n==0 or n==1:
        return 1
    elif n < 0:
        return "No -ve values accepted only +ve values"
    else:
        return  n*factorial(n-1)
n = int(input("Enter a values : "))
print(factorial(n))

#sum of Natural numbers using recursive topic
def add(n):
    """Recursive Usage"""
    if n < 0:
        return "Negative values are not accepted"
    elif n == 0:
        return 0
    else:
        return n + add(n - 1)
n = int(input("Enter a value: "))
print("Sum of Natural Numbers:", add(n))

Task: Build a simple choice chooser:
----------welcome to gaming world------------------------
1 - recursion logic factorial
2 - sum of natural numbers(recursion)
3 - BMI calculation
4 - Fibonacci series
5 - ATM usecase
any other number - only enter 1 - 5
Q - quit
'''



