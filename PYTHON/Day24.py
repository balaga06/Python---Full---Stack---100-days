'''
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

#Pass by reference --> when mutable objects (List, sets ,dict) are passed into the function,
#changes inside the function the original object...

def update(items):
    """we willl assume items as list"""
    items.append("Laptop")
cart = ["Mobile","watch"]
print(update(cart)) #returns None
print(cart) #original list changes
print(update("saketh")) #raises attribute erro

#Dictionary Usage: --> Updating Profile
def update(profile):
    """usage of Dictionary"""
    profile['Branch'] = "Vizag"
students = {"names" : ['sanjay','Akash']}
pfs_students = {'batches' : [ "PSF_007","DA007"] , 'Subjects' : ["Python","Mysql","Aptitude"]}
update(students)
print(students)
update(pfs_students)
print(pfs_students)


#Pass by value --> Original data will not change , Immutable Objects
#Pass by Object reference --> origina data will change , Mutable objects

#Built - In functions --> functions which are pre defined is inbuilt in python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str(),list(),tuple(),set(),
#dict(),input(),eval(),help()
#print(dir())
#print(dir(__builtins__))#returns list __builtins__ functions and errors
#print(help(print))
#print(help(len))
#abs(),chr(),ord()
print(abs(-34.56)) #returns the absolute value of a numbers
print(chr(176))
print(ord('@')) #returns ascii value
data = [24,45,26,54]
print(any(data)) #any() --> compares bool(x) for any value --> True
print(all(data)) #all() --> need all value to be present
#print(all(None))
print(all([None]))
print(bin(7))

print(help(enumerate))

data = ["akash","Ajay","sanjay"]
c = tuple(enumerate(data)) #by default it creates a counter object
print(c)

d = dict(enumerate(data,1))
print(d)

#zip --> it combine mulitple collections into a single collection
data = ["akash","Ajay","sanjay"]
marks = [25,20,35,52]
f = list(zip(data,marks)) #zip checks for length matching
print(f)
'''






