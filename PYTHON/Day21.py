'''
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

Positional Arguements --> count of arguements to be matched
Default Arguements --> we can make arguements as default
Keyword Arguements --> order / keyword name to be matched
Variable length Arguements --> (*args) we can pass any number of positional arguements
Keyword Variable length Arguements --> (**kwargs) we can pass any number of keyword arguements

#Positional Arguements --> count of arguements to be matched
def data(a,b,c):
    """Function to perform arthimetic operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(12,3,1))
#print(data(24,4)) #type error as count is mismatched
#print(data(1,32,4,5)) #type error as count is mismatched it takes only 3 arguements
d,e,f = map(int, input().split())
result = data(d,e,f)
print(f'Result is { result } ')
#it matches count of parameters in functions match with arguements in call function

#Default arguements --> we can make arguements as default
def data(a,b,c=6): #Non default arguements always follows default arguements
    """Function to perform arthimetic operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(12,3,2))
#print(data(12)) #here we need not mention other args as they are default
print(data(36,4)) #here one default arguement taken
#d = int(input())
#print(data(d)) #mandatory count to be matches
#print(data(a=24,4,3))

#Keyword Arguements --> order / keyword name to be matched
#grocery purchase
#def grocery(item,price):
def grocery(item,price=40):
#def grocery(item="Chock",price): #not at all possible
    """usage of keyword arguements"""
    print(f'Item is {item}')
    print(f'value of item is  {price}')
grocery("Pizza") #it takes default
grocery("Milk",35)
#grocery(50,"Bread") in this case order differs result changes 
grocery(price = 50, item = "Bread") #then we use keyword
#grocery(prices = 50, item = "jam") #type error keyword arguement mismatch

#Variable length Arguements --> (*args) we can pass any number of positional arguements
#we can capture any number of positional arguements , we use (*args), capture excess positional arguements and
#it will pack them into tuple...

def sample(*a):
    """usage of arbitary arguements"""
    print(a)
    print(type(a))
sample()
sample(1,2,3)
sample("saketh","code","gnan")

#In above case we use '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c = 2,4,5,6,65,12,-12
print(a)
print(b) #In this case all values are stored into list
print(c)
#a,*b,*c = 2,4,5,6,65,12,-12 #mutiple starred expressions not allowed 
#print(a)
#print(b) #In this case all values are stored into list
#print(c)
a,*b,c = (2,4,5),6,65,12,-12
print(a)
print(b) #In this case all values are stored into list
print(c)

#Find the sum of values

def add(*a):
    """Usage of Variable length arguements"""
    #print(a)
    #print(type(a))
    result = 0
    res = ""
    for value in a:
        #if type(value) in (int,float): #we use membership operator
        if type(value) == int or type(value) == float: #comparision and logical or 
            result += value
            #print(result)
        elif type(value) == str:
            res += value
            #print(res)
    #print(result)
    return result, res
#add()
#add(4,2,1,6)
#add(2,4,5,6,65,12,-12)
#print(add(2,4,5,6,10.45,"codegnan","vsp",65,12,-12))
num_sum, string_result = add(2,4,5,6,10.45,"codegnan","vsp",65,12,-12)
print(num_sum)
print(string_result)

#what if we accept group of values
d = list(map(int,input().split()))
print(d)
print(add(*d)) #we need to use * to unpack the values from the tuple

#we will use above usage of variable length arguements for ordering pizza

def order_pizza(size,*toppings):
    """Usage of *args"""
    print(f'size of pizza is {size} ')
    print(f'toppings : {toppings} ')
    for topping in toppings:
        print(f'topping added : {topping}')
order_pizza("Large","onions","paneer","capsicum","olives","mushroom")

#Keyword Variable length Arguements --> (**kwargs) we can pass any number of keyword arguements
#Data is stored in dictionary , we use **kwargs
def sample(**a):
    """Usage of **kwargs"""
    print(a)
    print(type(a))
#sample()
sample(name = "nikhil",batch = "pfs-vsp-007" , place = "vizag" , branch = "cse" ,rollno = 7)

def order_pizza(size,*toppings,**details):
    """Usage of *args"""
    print(f'size of pizza is {size} ')
    print(f'toppings : {toppings} ')
    for topping in toppings:
        print(f'topping added : {topping}')
    for key,value in details.items():
        print(f'Data is {key} , result is {value}')
order_pizza("Large","onions","paneer","capsicum","olives","mushroom",name = 'Nikhil' , bill = 200, delivery = False
                        , tip = 50)
'''














