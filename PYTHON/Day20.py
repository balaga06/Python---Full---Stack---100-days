'''
Python --> POP , OOP
POP --> Procedure Oriented Programming --> Functions
Functions -->Reusable Block of statements or Code
#A function is a block of code(statements) which performs a specific task .
It is a reusable code --> Readbility , reusability and easy to maintain...

Type of functions
1.User Defined Function --> def 
2.Built - in - Functions --> Python by default(print , len , min , max , sorted,
str , list , bool , dict...)
3.Anonymous Functions --> Name less functions --> Lamdba (map , filter) reduce
4.Recursive Functions --> Recursion --> Factorial , Fibonacci --> Decorators

Syntax :

def fname(parameters): #Function header
        """Doc string (Description of Function)"""
        statement(s)..... #Body of function
        .............................
        return value(s)
fname(args) #function call

#simple function to understand the reusability
a = 10
b = 20
print(a+b)

def add(a,b):
    """This function returns the sum of the given objects"""
    c = a+b
    #print(c)
    return c
print(add(25,45))
add(14.5,12.2)
print(add('code','gnan'))
print(add([1,2,3],[3,4,5]))
add((1,2,3),(3,4,5))

def add(a,b):
    """sample add function"""
    return f'Result is {a+b}'
c,d = map(int, input("enter the values : ").split())
print(add(c,d))
print(add('code','gnan'))
g,h = 99,-98
e = add(g,h) #Assigning function to a variable
print(e)

#Function are also objects

def greeting():
    """Greeting to the user"""
    return "Hey Guys Welcome to Codegnan"
print(greeting())
print(greeting() * 5)
print(type(greeting)) #returns function
print(type(greeting())) #returns data and sequence types

#A function can have multiple values to return but not multiple return statements

def greeting():
    """Greeting to the user"""
    return "Hey"," Guys"," Welcome to Codegnan"
print(greeting())
print(greeting() * 5)
print(type(greeting)) #returns function
print(type(greeting())) #returns data and sequence types - default tuple
'''



