'''
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

#usage of variable length and keyword variable length arguements

def scores(*marks,branch="codegnan",**names):
    """Scores scenario with variable and keyword variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'total marks are : {total} ')
    for name , value in names.items():
    #for name in names.values():
    #for name in names.keys():
        print(f'Name : {name}')
        print(f'value : {value}')
        print(f'branch : {branch}')
scores(25,20,15,18,16,name="Nikhil",place="vizag",batch="PFS_VSP_007")

#Positional arguements always follows keyword arguements
#Non default always follows default args
'''

#Scope -->  Determines where a variable can be accessed within a program
#A variable is only accessible within the region where it is defined.....
'''
Type of scope : Local , global , global keyword , non local

#Local scope : variable defined and accessible only inside the function...

def fname():
    """usage of local variable"""
    name = "codegnan"
    return f'{name} is in vizag'
print(fname())
#print(name) #it raises name error As local variable name is inside the function
name = "nikhil"
print(name)
print(fname())

#Global Variable --> A variable declared outside all functions is called global variable
#it can be accessed from anywhere in the program
#local variable gets higher priority
name = "Codegnan"
def uname():
    """usage of global variable"""
    name = "nikhil"
    return f'{name} is in vizag,vijayawada and hyderabad'
print(uname())
print(name)

#Global Keyword  --> Used when we want to modify a global variable
#inside the functions
count = 15
def update():
    """usage of global keyword"""
    global count
    count = count + 10 #unbound localError 
    return f'updated count is {count}'
print(update())
print(f'new count is {count}')
values = [1,3,45]
values.insert(1,count)
print(values)


#Non local scope --> Used in nested functions allows modifications of variables from the outer function

def outer():
    """usage of outer function"""
    count = 10
    def inner():
        nonlocal count
        count = count+15
        return f'result from inner function is {count}'
    print(inner())
    return f'result from outer function is {count}'
print(outer())


#LEGB RULE --> LOCAL , ENCLOSING -- GLOBAL -- BUILT - IN 

len = 45
a = ["codegnan","Python"]
print(len(a)) #Here we have used built in functions as identifier it fails


#Functions are termed as first class objects
#Pass by value and pass by object references

#Pass by value --> Immutable objects
#int,float,bool,str,tuple,complex,frozenset
#when immutable objects are passed to function , changes inside the function
#do not effect the original value
#original value remains unchanged
def update(number):
    """pass by value usage"""
    #number = 15
    return number * 3
    #print("Inside function:",number)
number = 20
print(update(number))
print(update(25))
'''
'''
