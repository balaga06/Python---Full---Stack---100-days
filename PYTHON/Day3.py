'''
Datatypes --> It will tell us how to define the data
Numeric Datatypes - Integer , Float , Complex
Boolen type - True / False
None type -  None
Sequence types - Strings , Lists , Sets , frozensets , Mappings(dictionaries)

#Numeric datatypes --> Integer --> Quantities, ID, ORDER ID, STOCK , AGE, SALARY -- INT
age = 32
print(age)
print(type(age))
stock = 35
print(type(stock))
batch_rank = 1
print(type(batch_rank))

#Float values --> Salaries, price, percentage calculations , temp .....
salary = 40555.25
print(salary)
print(type(salary))

#Complex numbers --> It is a combination of real and imaginary values -- scientific calculations , signal processing
#i5 = 10
#data = 3+i5
#print(data)

data = 3+5j
print(data)
print(type(data))

#Boolen --> True / False --> Validations
access = True
print(access)
print(type(access))
result = False
print(result)
print(type(result))


#Nonetype --> None
#None -- 0 , False , ' ' , [ ] , ( ) , { } , set() -- None cases in Python
branch_rank = None
print(branch_rank)
print(type(branch_rank))


#TypeConversion -- Converting one datatype to another datatype using built in functions
#Explicit Conversion

#integer --  float , complex , boolean

rank = 5
print(type(rank))
b = float(rank)
print(b)
print(type(b))
c  = complex(rank)
print(c)
print(type(c))
d = bool(rank)#bool of anything is true or bool of nothing is false
print(d)
print(type(d))
d = 0
e = bool(d)
print(e)
print(type(e))
#Space is also a character
#bool([''])#empty string inside a list
print(bool(['']))

#float -- int , complex, boolean
salary = 10.25
print(type(salary))
a = int(salary)
print(a)
print(type(a))
b = complex(salary)
print(b)
print(type(b))
c = bool(salary)
print(c)
print(type(c))

#complex --  int , float , boolean
signal = 3+5j
print(type(signal))
a = float(signal)
print(a)
print(type(a))
signal = 3+5j
print(type(signal))
a = float(signal)
print(a)
print(type(a))
#raise type error for int or float conversion from complex

signal = 3+5j
print(type(signal))
a = bool(signal)
print(a)
print(type(a))
#only in boolean it will work

#boolean -- float , int , complex
access  = True
print(type(access))
a = int(access)
print(a)
print(type(a))
b = float(access)
print(b)
print(type(b))
c = complex(access)
print(c)
print(type(c))

access  = True
print(int(access))
print(float(access))
print(complex(access))
print(bool(access))

a = int(float(bool(5)))
print(a)
b = bool(float(int(35)))#check for outer one
print(b)

c = True + 35 + 3.5 + (6+5j) # True becomes 1
print(c)
d = False + 35 + 3.5 + (6+5j) # False becomes 0 
print(d)


#Sequence types - Strings , Lists , Sets , frozensets , Mappings(dictionaries)
#strings --> Quotations --> Single , double , triple Quotes
place = 'Balaga Nikhil'
print(type(place))
name = "codegnan"
print(type(name))
#Strings are Immutable , Ordered , Indexed , collection
#length -- len(obj) --> returns the number of items in a collection
print(len(name))
print(len(place))
print(len('Qwerty'))
#Space is also a character
a = " "
print(len(a))


#Type Casting -- String conversion into int,float,bool,complex

course = ' python'
#print(int(course)) #ValueError
#print(float(course)) #ValueError
#print(complex(course)) #ValueError
print(bool(course))


#int -- str
a = 45
b = str(a)
print(b)
print(type(b))
#float --  str
a = 45.25
b = str(a)
print(b)
print(type(b))
#bool -- str
a = True
b = str(a)
print(b)
print(type(b))
a = False
b = str(a)
print(b)
print(type(b))
#complex -- str
a = 4+5j
b = str(a)
print(b)
print(type(b))
'''
