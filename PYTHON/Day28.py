'''
data = [[i * j for i in range(1, 11)] for j in range(1, 11)]
for row in data:
    print(*row)

#Nested Comprehension with if condition
#Syntax: [expression for i in iterable 1 for j in iterable 2 if condition]
#Possible Pairs without matching values

data=[(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(data)

f=[i*j for i in range(1,4) for j in range(1,4) if i!=j]
print(f)
print(*f)
'''

#Nested Comprehenion with if-else condition
#Syntax : [true_value if condition else false_value for i in iterable1 for j in iterable2 if condition ]
'''
week_1 = [15,20,25,29,28,30]
week_2 = [24,25,28,29,21,22]
result = ["pass" if x<y else "fail" for x in week_1 for y in week_2]
result = ["Improved" if x<y else "Lagged" for x in week_1 for y in week_2]
print(result)
'''
#Generators
week_1 = [15,20,25,29,28,30]
week_2 = [24,25,28,29,21,22]

result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
print(result)

#GENERATOR  --->IT is a Special Function,Which produces one value at a time
#we use yield Keyword
'''
def fname():
    """Doc string"""
    return value(s)
fname()

def fname():
    """DOC string"""
    yield value1
    yield value2
    yield value3
fname()
'''
'''
def func():
    """Normal Function"""
    return[1,2,3,4,5]
    #return "Saketh" # A function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)

def func():
    """Generator Function"""
    yield 1
    yield 2
    yield 3
#print(func())
b = func()
print(next(b))
print(next(b))
print(next(b))
#print(next(b)) it raises stop Iteration as value are already fetched

def display():
    """Subjects Covered"""
    yield ["Python",45,'paperbased Exams']
    yield "Aptitude"
    yield"Softskills"
    yield"Frontend"
    yield"FastApi"
print(display())
g=display()
print(f"subjects alloted is {next(g)}")
print(f"subjects alloted is {next(g)}")
print(f"subjects alloted is {next(g)}")
print(f"subjects alloted is {next(g)}")

week_1 = [15,20,25,29,28,30]
week_2 = [24,25,28,29,21,22]
result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result) #it returns a generator
g = result
print(next(g))
print(next(g))
print(next(g)) #next function will fetch the value from the generator
print(*result)
'''
#exception handling --It is the machanism in python
#Runtime Errors or Exceptions
#Exception is an event that occurs during the execution of a program
#which disrupts its normal flow...

#TypeError,ValueError,IndexError,AttributeError,KeyError,ZeroDivisionError.

#We will be using try,Except and finally
'''
Syntax:
try: #You write code which may cause an error
       #Code that raises an expection
except ExceptionType: #it handles the error if it occurs
        #Code to handle the Exception
'''

#Basic Exception Handling
a,b=5,0
try:
    result =a/b
    print(result)
except Exception as e:
    print(e)


























































