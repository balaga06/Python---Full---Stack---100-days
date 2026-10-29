'''
Sets --> A set is an Unordered , Unindexed collection , Allow unique values , Heterogeneous collection
Mutable collection

#A set can contain only tuples in it but not lists,sets..
we use set() or data inside { } brances

#Every Built - in data type is a built - in functions
#subjects = { } By default it will be empty dictonary
subjects = set()
print(type(subjects))
print(len(subjects))
data = ('Python','Aptitude','SQL','SS')
subjects = set(data)
print(subjects)
print(type(subjects))
print(len(subjects))

#ids = {123,124,125,126,["poll",123]} #type error

#set properties --> Membership, #concatenation is not possible
print(123 in {124,125,123})
ids = {124,125,123}
new_ids = {126,121,122}
#total = ids + new_ids #it raises type error because it was unordered and unindexed collection
#print(total)

#set is mutable collection --> Methods : Insertion, deletion along with mathematical set operations
#add() --> Inserts single element to the set (unique values)
marks = {45,25,35,20,21}
print(type(marks))
print(len(marks))
marks.add(25)
print(marks)
print(len(marks))
marks.add((21,23,31))
print(marks)
print(len(marks))

d_marks = [1,2,3,4,5,6]
marks.update(d_marks) #updates the set within itself or can take other sequence
print(marks)
print(len(marks))

d_marks = (1,2,3,4,5,6,7,8)
marks.update(d_marks) #updates the set within itself or can take other sequence
print(marks)
print(len(marks))

d_marks = {1,2,3,4,5,6,7,9,10}
marks.update(d_marks) #updates the set within itself or can take other sequence
print(marks)
print(len(marks))

marks.update("codegnana") #updates the set within itself or can take other sequence
print(marks)
print(len(marks))

#remove(),discard(),pop()
marks = {45,25,35,20,21}
print(marks.remove(45))
print(marks)
#marks.remove(4)
#print(marks)
#print(marks.remove(4)) #remove will remove the object if existing else raise key error

#discard() --> removes an element from the set if existing if not it overrides the error
print(marks.discard(45))
print(marks.discard(1234))

marks.discard(21)
print(marks)

#pop() will removes and returns an arbitary element from the set
print(marks.pop())
print(marks)
print(marks.pop())
print(marks.pop())
#print(marks.pop()) #it returns keyerror as set has become empty

#clear() will removes all elements and returns an empty set 
marks = {45,25,35,20,21}
print(marks)
print(marks.clear())
print(marks)


#Mathematical operations --> Union(), intersection(), difference().....
a1 = {12,34,23,45}
a2 = {3,45,23,12}
a3 = a1.union(a2)
print(a3)
print(len(a3))
a4 = a1 | a2
print(a4)
a5 = a1.intersection(a2) #returns the common elements in both sets and
print(a5)
print(len(a5))
a6 = a2 & a1
print(a6)
a7 = a1.difference(a2) #removes common elements from both sets and returns #elements from first
print(a7)
a8 = a2.difference(a1)
print(a8)
a8 = a1 - a2 #- is set difference operation
print(a8)
a9 = a1.symmetric_difference(a2) #removes common elements from both sets returns all remaining elements from both sets
print(a9)
a10 = a1 ^ a2
print(a10)

#intersection_update() --> perfroms intersection and update the first set
a1 = {12,34,23,45}
a2 = {3,45,23,12}
a3 = a1.intersection_update(a2)
print(a3)
print(a1)
a4 = a2.intersection_update(a1)
print(a2)
#difference_update(),symmetric_difference_update()
a5 = a2.difference_update(a1)
print(a5)
print(a2)
print(a1)
a6 = a1.symmetric_difference_update(a2)
print(a6)
print(a2)
print(a1)

a1 = {12,34,23,45}
a2 = {3,45,23,12}
print(a1,a2)
a1.add(3)
print(a1,a2)

print(a1.issubset(a2))
print(a2.issubset(a1))
print(a1.issuperset(a2))
print(a2.issuperset(a1))
print(a2.isdisjoint(a1)) #returns True only when both sets have Null intersection


#Dictionaries --> A dictionary is a collection of key , value pairs , we use {k:v} as syntax , keys must be
#unique, Mutable , ordered, Indexed through keys can be strings , numbers(int , float)

data = {1:"BALU",
            2:'RAVI',
            3:'HARI'}
print(data)
print(len(data))
print(type(data))
print(data[2])
print(type(data[2]))

details = {'ids' : ['CGVI0242','CGVI0249',
                         'CGVI0224','CGVI0240'],
                'names' : ['nikitha','deepthi',
                         'vinay','tej'],
                'batch' : 'PFS-VSP-007',
                'place' : ('vizag','vijayawada','hyd','banglore'),
                'subjects' : {'python','aptitude','softskills'}}
print(details)
print(len(details))
print(details.keys())
print(details['ids'])
print(type(details['ids']))
details['ids'].append("CGVI0245")
print(details['ids'])
details['ids'].insert(1,"CGVI0247")
print(details['ids'])
print(details['ids'][:3])
print(details['ids'][::2])

#Taks :
#1) Insert raju at the end also sanju and nihanth at the end in names
#2)update subjects with SQL,Flask,FastAPI
#3)remove banglore and vizag from place #tuple is immutable we 
#4)convert batch number to lower case

details['names'].extend(['raju', 'sanju', 'nihanth'])
print(details['names'])

sub = ('SQL','Flask','FastAPI')
details['subjects'].update(sub) 
print(details['subjects'])

#3)remove banglore and vizag from place
#tuple is immutable we cannot add or remove elements place is tuple

details['batch'] = details['batch'].lower()
print(details['batch'])

['nikitha', 'deepthi', 'vinay', 'tej', 'raju', 'sanju', 'nihanth']
{'aptitude', 'Flask', 'FastAPI', 'python', 'SQL', 'softskills'}
pfs-vsp-007
'''




