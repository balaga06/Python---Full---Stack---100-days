'''
Datatypes --> It will tell us how to define the data
Numeric Datatypes - Integer , Float , Complex
Boolen type - True / False
None type -  None
Sequence types - Strings , Lists[ ] , Tuples ( ), Sets ( ) , frozensets , Mappings (dictionaries) { }

#Lists --> A list is an ordered , mutable , indexed and heterogeneous collection
#we use [ ] to represent lists
#student details , Order details , stock entries.....
details =  [1, 'Nikki', 'PSF7' ,'VIZAG',45.50]
print(details)
print(len(details))
print(type(details))

stu_id = ['CGVI0232','CGVI0233','CGVI0234']
print(stu_id[0])
print(stu_id[1])
print(stu_id[2])
#List is mutable we can change in anywhere
stu_id[0] = 'codegnan' #here we are indexing
print(stu_id[0])


#Tuples --> tuples are also Immutable, Ordered , Indexed and heterogeneous
#collections , we use ( ) parenthesis
#dimensions , coordinates

place = ('hyd','vizag','sklm')
print(place)
print(len(place))
print(type(place))
print(place[0])
print(place[1])
place[0] = 'chennai' #It is immutable we cannot change
print(place)
details =  (1, 'Nikki', 'PSF7' ,'VIZAG',45.50)
print(details)
print(type(details))

dimensions = 10,20,30 # By default it becomes tuple
print(dimensions)
print(type(dimensions))


#Sets --> A set Unique collection which will not allow duplicates(removes duplicates)
#A set is a unordered collection, Unindexed but it is a mutable collection
ids = set()#empty set
print(ids)
ids = set([123,124,125,123])
print(ids)
ids = set({123,124,125,123})
print(ids)
ids = set((123,124,125,123))
print(ids)
course = {2,3,4,2,3}
print(course)
print(type(course))
print(course[0])
courses = {'PF','DS','JAVA'}
print(courses)
s = {'hello', 10, 20.5, (1, 2)}
print(s)


#Dictionaries -->  A dictonary (mapping object) is a collection of key value pairs
##dict -- {k : v}, we access only by keys ( indexed by keys )
# Dictionary is also mutable collection
#Keys must be unique in a dictionary (keys can be int , float , str)
details = {'branch' : 'vizag',
               'batch' : ['PFS-VSP007','PFS-VSP008','PFS-VSP009'],
               'COURSE' : 'PFS',
               'COUNT' : (19, 20, 21)}
print(details)
print(type(details))
print(len(details))
print(details['branch'])
print(details['COUNT'])
print(details['batch']) #we can access by giving only keys


#every build-in  datatypes is built-in functions
#int,float,complex,bool,str,None
#Lists --> tuples, sets, dictionaries,str
marks = [23, 33 ,45]
a = tuple(marks)
print(a)
print(type(a))
print(len(a))
b = set(marks)
print(b)
print(type(b))
print(len(b))
c =  str(marks) #it marks every symbol as a character
print(c)
print(type(c))
print(len(c))

#from tuple -- list,set,str,dict
marks = (34,56,75)
a = list(marks)
print(a)
print(type(a))
print(len(a))
b = set(marks)
print(b)
print(type(b))
print(len(b))
c = str(marks) #it marks every symbol as a character
print(c)
print(type(c))
print(len(c))

#set -- list,tuple,str,dict
marks = {23, 33 ,45}
a = tuple(marks)
print(a)
print(type(a))
print(len(a))
b = list(marks)
print(b)
print(type(b))
print(len(b))
c =  str(marks) #it marks every symbol as a character
print(c)
print(type(c))
print(len(c))

#dict <-- lists,tuples,sets,str
marks = [23,45,34]
#a = dict(marks) #it is not possible like this
#print(a)
b = dict.fromkeys(marks) #we need to use from keys( ), whatever elements we have in data like list,tuple,set,str
#taken will become keys and values will be None
print(b)

marks = (23,45,34)
#a = dict(marks) #it is not possible like this
#print(a)
b = dict.fromkeys(marks)
print(b)

marks = {23,45,34}
#a = dict(marks) #it is not possible like this
#print(a)
b = dict.fromkeys(marks)
print(b)

data = '{"name": "Nikki", "age": 19, "course": "PFS"}'
#a = dict(marks) #it is not possible like this
#print(a)
b = dict.fromkeys(data) #every character as a index make count....
print(b)

#dict -- lists,tuples,sets,str
ids = {1 : 22, 2 : 43}
print(ids)
a = list(ids) #it will only fetch keys
print(a)
print(len(a))
b = tuple(ids)
print(b)
print(len(b))
c = set(ids)
print(c)
print(len(c))
d = str(ids) #every symbol/object will be character
print(d)
print(len(d))


#frozenset datatype -->  It is an immutable set , unordered , unindexed
#we can use typecasting to list,tuple,set,dict
a = frozenset({1,2,3,4,2,4})
print(a)
b = list(a)
c = tuple(a)
d = set(a)
f  = str(a)
print(b,c,d,f)
print(type(a))

#from string to list,tuple,set,dict
d = 'nikhil'
e = list(d)
f = tuple(d)
g = set(d)
h = dict.fromkeys(d)
print(e,f,g,h)

#operators --> Arthimetic operators, assignment operators, comparision
#logical , membership , identity  bitwise operators

#arthimetic ---> +,-,*,/(float division), // (floor division) quotient , %Modulues(remainder), ** (exponential)

a = 3
b = 2
print(a*b)
print(a**b)
print(a//b)
print(a/b)
print(a%b)
'''

