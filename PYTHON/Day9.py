'''
Sequences --> Strings , Lists[ ], Tuples( ), Sets set( ), Dictionaries{ }
Lists[ ] --> A list is an orderd , Mutable , Indexed and heterogeneous collections
It will be dynamic in size, It also allows duplicates


#Creation of lists
details = [123,'codegnan',22,"PFS",91.12]
print(type(details))
print(len(details))
print(details)

#Nested Lists
batch = ['PFS07',['P','F','S','DA07'],
                'vizag',123,80,['code','gnan']] 
print(batch)
print(len(batch))
print(type(batch))


#Indexing,slicing,striding
batch = ['PFS07',['P','F','S','DA07'],'vizag',123,80,['code','gnan']] 
print(batch[0])
print(batch[-5])
print(batch[1:5]) #observe output
print(batch[:3])
print(batch[1:5:2])
print(batch[-5:-1])
print(batch[-5:-1:4])
print(batch[-1:-5])
print(batch[-4:-2])

#sub Indexing --> Accessing index within the index of a collection(str, list, tuple)
batch = ['PFS07',['P','F','S','DA07'],'vizag',123,80,['code','gnan'],['PSF-VSP-007','DAA-VSP-008']]
print(batch[1])
print(batch[1][3])
print(batch[1][3][2:])
print(batch[2])
print(batch[2][-3:])
print(batch[2][2:])
print(type(batch[2][2:]))
print(batch[5])
print(batch[5][0])
print(batch[5][0][::3])
print(batch[5][0][::2])
print(batch[6])
print(batch[6][0])
print(batch[6][0][0:3])
print(batch[6][0][7:12])
print(batch[6][0][0:3] + batch[6][0][7:12])
print(batch[6][1])
#Lists supports repetition, merging and its also an iterable (iterate through #loops)
print([1,2,3] * 3) #repetition
#print([1,2,3] + 3) #type error
print([1,2,3] + batch) #Merging
b = [1,2,3]
a = b*5
print(len(a))

batch = ['PFS07',['P','F','S','DA07'],'vizag',123,80,['code','gnan'],['PSF-VSP-007','DAA-VSP-008']]
print('PFS07' in batch) #Membership
print('P' in batch) 
print('P' in batch[1]) 


#Lists Methods
data = []
print(data)
#print(dir(data)) #returns list of all available methods
#append(), extend(), insert()
#append(obj) --> Insert object at the end of the list
data.append(2)
print(data)
data.append('abc')
print(data)
#data.append('123','xyz') #type error it will append one obj at a time
data.append([123,'xyz',['python']])
print(data)
print(len(data))
print(type(data))

#Extend --> Insert multiple elements (objects) to the end of the list
data.extend([12,52])
print(data)
print(len(data))
data.extend(['PYTHON','MYSQL','SQL'])
print(data)
data.extend('vizag') #check this it will print individually
print(data)
data.extend([123])
print(data)

#insert(index,object) --> Inserts elements before index
data.insert(5,'codegnan')
print(data)
data.insert(20,'codegnan')
print(data)
data.insert(-5,'codegnan')
print(data)
data.insert(-5,[5,6,7])
print(data)
data.insert(2,[50,60,70])
print(data)
data.insert(4,['A','B','C'])
print(data)

#Lists are mutable
marks = [25,56,24,15,26,34,99,78]
print(marks)
marks[5] = 69
print(marks)
marks[:3] = ['C','V','A','B']
print(marks)
marks[:3] = ['C','V','A','B',1,5,6]
print(marks)
#In the above cases data is being modified in original list
#(Indexing case length remains constant but data is modified,
#whereas in slicing case it may increase,decrease)

#pop(),remove(),clear() --> removes elements from the list
subjects = ['python','aptitude','ss','mysql','flask','frontend']
print(len(subjects))
print(subjects.pop()) #removes and returns last element
#pop --> removes by default last element if index is not mentioned
print(subjects)
print(len(subjects))
print(subjects.pop(2))
print(subjects)
print(len(subjects))
print(subjects.pop(6)) #raise index error

#remove --> It removes specific value from the collection(only first occurence)
subjects = ['python','aptitude','ss','mysql','flask','frontend']
#subjects.remove('ss')
#print(subjects.remove('ss')) #raises error
#print(subjects)
#subjects.remove('sd') #raises value error

#clear() --> removes all elements from the list and returns empty list
print(len(subjects))
subjects.clear()
print(subjects)
print(len(subjects))

#index(),count()
#index(start) --> returns only first occurence index position
marks = [25,56,24,15,26,34,99,78,24]
print(marks.index(24))
print(marks.index(24,4)) #here we are exclusively giving start postn
#print(marks,index(90)) #value error

#count() --> returns the count of occurences
print(marks.count(24))
print(marks.count(246))

#Task : created a nested list with lists and strings perform list methods
# Nested List
data = [[1, 2], [3, 4], [5, 6]]

print(data)

# 1. append()
data.append([7, 8])
print(data)

# 2. insert()
data.insert(1, [10, 20])
print(data)

# 3. extend()
data.extend([[30, 40], [50, 60]])
print(data)

# 4. remove()
data.remove([3, 4])
print(data)

# 5. pop()
removed = data.pop()
print(removed)
print(data)

# 6. reverse()
data.reverse()
print(data)

# 7. count()
print(data.count([1, 2]))

# 8. index()
print(data.index([5, 6]))


# Creating a nested list
data = [
    [10, 20, 30],
    ['Python', 'MySQL', 'SQL'],
    [40, 50, 60],
    'Codegnan',
    'Vizag']
print(data)


# 1. append(object)
# Adds one element at the end of the list.
data.append(['HTML', 'CSS'])
print("After append:")
print(data)


# 2. extend(iterable)
# Adds each element of the iterable to the end of the list.
data.extend([[70, 80], 'Java'])
print("After extend:")
print(data)


# 3. insert(index, object)
# Inserts an element before the specified index.
data.insert(2, ['JavaScript', 'React'])
print("After insert:")
print(data)


# 4. remove(object)
# Removes the first matching element.
data.remove('Vizag')
print("After remove:")
print(data)


# 5. pop()
# Removes and returns the last element.
removed_item = data.pop()
print("Popped item:")
print(removed_item)
print("After pop:")
print(data)


# 6. pop(index)
# Removes and returns the element at the specified index.
removed_item = data.pop(1)
print("Popped item at index 1:")
print(removed_item)
print("After pop(1):")
print(data)


# 7. index(object)
# Returns the index of the first occurrence.
print("Index of 'Codegnan':")
print(data.index('Codegnan'))


# 8. count(object)
# Returns the number of occurrences of an element.
data.append('Codegnan')
print("Count of 'Codegnan':")
print(data.count('Codegnan'))


#copy( ),sort( ),reverse( )

details = [['sanjay','python',50],
                 ['akash','flask',45],
                 ['vinay','aptitude',30]]

print(details)
print(len(details))

#copy() --> creates a shallow copy of the given collection
data = details.copy()
print(data)
print(len(data))

data[0].append('A') #nested lists changes will directly applicable in both lists
data.append('VSP')
print(data)
print(details)
print(len(details))
print(len(data))

data.extend(['PFS','JFS'])
print(data)
print(details)
print(len(details))
print(len(data))

details.extend(['PFS','JFS'])
print(data)
print(details)
print(len(details))
print(len(data))

#In the below case we have created basic lists so original is not effected
subjects = ['Python','Mysql','Aptitude','Softskills']
print(subjects)
data = subjects.copy()
print(data)

data.insert(2,'frontend')
print(data)
print(subjects)
print(len(data))
print(len(subjects))

subjects = ['Python','Mysql','Aptitude','Softskills']
print(subjects)
data = subjects #this is like complete clone of original data
data.insert(2,'frontend')
print(subjects)
print(data)
subjects.remove('Python')
print(subjects)
print(data)


#sort() --> by default sort the list in ascending order or return none

marks = [25,48,10,8,12,22]
print(marks.sort()) #returns none as nothing to be returned
marks.sort()
print(marks)

marks.sort(reverse=True) #it returns in descending order
print(marks)

marks.sort(reverse=False) #it returns in ascending order
print(marks)

marks = [25,48,10,8,12,22]
marks.sort(reverse=True) #it returns in descending order
print(marks)

#marks.append('nikhil')
#print(marks) 
#marks.sort() #raises type error

marks.extend([-21,14,-49])
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True) #it returns in descending order
print(marks)
marks.sort(reverse=False) #it returns in ascending order
print(marks)

#reverse() --> it will return reverse of the list reverse order
marks = [25,48,10,8,12,22]
marks.reverse() #this will make changes in original list
print(marks)
marks.extend(['Polly','saturday',123])
print(marks)
marks.reverse()
print(marks)
print(marks[::-1]) #this will just return the reverse order o/p


#min(),max(),len(),type(),sorted()
marks = [25,48,10,8,12,22]
print(min(marks))
print(max(marks))
b = sorted(marks) #sorted will be function return a new list with elements in ascending order
print(b)
print(marks)
print(len(marks))
print(type(marks))
'''
'''
Tuples --> A list is an orderd , Mutable , Indexed and heterogeneous collections
It will be dynamic in size, It also allows duplicates we use () to store the data

data = ()
print(data)
print(len(data))
print(type(data))

data = 1,2,3,4,
print(data)
print(len(data))
print(type(data))

data = []
data
[]
len(data)
0
data = ['']
data
['']
len(data)
1
data=[' ']
data
[' ']
len(data)
1
data = [0]
data
[0]
len(data)
1

data = ()
data
()
len(data)
0
data = ('')
data
''
len(data)
0
type(data)
<class 'str'>
data = (' ')
data
' '
len(data)
1
data = (',')
len(data)
1
type(data)
<class 'str'>
data = ('',)
data
('',)
len(data)
1
type(data)
<class 'tuple'>

#be specific when we are passing data using ()
#tuples are immutable we cannot modify the elements in it after creation
#data[-2] = 'code' #It is not possible

#Nested tuples (also will have lists in it)
details = ('vizag',8,('PFS','JFS','DA'),['APTITUDE','SOFTSKILLS'])
#print(details)
#print(details[:2])
#print(details[2][1]) #subindexing
#print(details[2][::2])

print(details[-1])
details[-1].extend(['Python','Java'])
print(details)
#we cannot make any changes over tuple directly but we can change on list
print(details[0].upper())
print(details)


#Indexing(),repetition(),merging(),slicing() are possible
temp = (242.5,21,12.5)
print(temp)
b = temp*2
print(b)
print(b + temp)

#Tuple methods --> Index(),count()
data = (1,2,3,1,2,4,1,5,3,6,1,3,2,1)
print(data)
print(data.count(1))
print(data.index(1))
print(data.index(4,1))
print(data.index(6,1))

b = sorted(data) #returns sorted elements in a list 
print(b) 
print(tuple(b))
c = sorted(data,reverse=True) #returns tuple in descending order
print(c)
print(tuple(c))

#del data #it completely eliminates the variable
#print(data) #name error


#sets --> A set is unordered , Unique , Mutable collection, it will never allow duplicates

ids = set()
print(ids)
print(type(ids))

name = {'nikhil','balaga',20,14,'apple'}
print(name)
print(len(name))

#d = {12,3,4[12,3,4],45} #we cannot have lists inside a set 
#print(d)

d = {12,3,4,(12,3,4),45} #we can have tuples in a set 
print(d)
'''

#Task : Create a Nested Tuple with Lists inside it and make all methods of lists in the tuples

# Nested Tuple with Lists

student = (
    'Nikhil',
    25,
    ('Python', 'MySQL', 'Java'),
    ['HTML', 'CSS', 'JavaScript']
)

print(student)

# Accessing the list inside tuple
print(student[-1])

# append() --> Adds one element at the end
student[-1].append('React')
print(student)

# extend() --> Adds multiple elements at the end
student[-1].extend(['Flask', 'Django'])
print(student)

# insert() --> Inserts an element at a particular index
student[-1].insert(1, 'Bootstrap')
print(student)

# remove() --> Removes the specified element
student[-1].remove('CSS')
print(student)

# pop() --> Removes and returns an element
x = student[-1].pop()
print(x)
print(student)

# index() --> Returns the index of the first occurrence
print(student[-1].index('JavaScript'))

# count() --> Returns the number of occurrences
student[-1].append('Python')
student[-1].append('Python')
print(student[-1])
print(student[-1].count('Python'))

# sort() --> Sorts the list
student[-1].sort()
print(student)

# reverse() --> Reverses the list
student[-1].reverse()
print(student)

# copy() --> Creates a copy of the list
new_list = student[-1].copy()
print(new_list)

# clear() --> Removes all elements from the list
new_list.clear()
print(new_list)

# Original list is not affected by clear()
print(student)

# Nested Tuple with Lists

employee = (
    'Rahul',
    101,
    ('Python', 'SQL', 'Flask'),
    ['HTML', 'CSS', 'JavaScript', 'React', 'MySQL']
)

# Printing complete tuple
print(employee)

# Indexing
print(employee[0])
print(employee[1])

# Negative indexing
print(employee[-1])

# Sub-indexing
print(employee[2][1])
print(employee[2][-1])

# Slicing
print(employee[-1][1:4])
print(employee[-1][::2])

# LIST METHODS INSIDE TUPLE

# append() --> Adds one element at the end
employee[-1].append('MongoDB')
print(employee)


# extend() --> Adds multiple elements
employee[-1].extend(['Django', 'Node.js', 'Express'])
print(employee)


# insert() --> Adds an element at a particular index
employee[-1].insert(2, 'Bootstrap')
print(employee)


# remove() --> Removes a specified element
employee[-1].remove('CSS')
print(employee)


# pop() --> Removes the last element
x = employee[-1].pop()
print('Removed element:', x)
print(employee)


# pop(index) --> Removes element from a particular index
x = employee[-1].pop(3)
print('Removed element:', x)
print(employee)


# index() --> Returns the index of first occurrence
employee[-1].append('React')
print(employee[-1].index('React'))


# count() --> Counts occurrences
employee[-1].append('Python')
employee[-1].append('Python')

print(employee[-1])
print(employee[-1].count('Python'))


# sort() --> Sorts the list in ascending order
employee[-1].sort()
print(employee)


# reverse() --> Reverses the list
employee[-1].reverse()
print(employee)


# copy() --> Creates a separate copy
skills_copy = employee[-1].copy()

print('Original List:', employee[-1])
print('Copied List:', skills_copy)


# Modify copied list
skills_copy.append('C++')

print('Original List:', employee[-1])
print('Copied List:', skills_copy)


# clear() --> Removes all elements from copied list
skills_copy.clear()

print('After clear:', skills_copy)

# Original list is not affected
print('Original:', employee)

# TUPLE OPERATIONS

# Indexing
print(employee[0])

# Slicing
print(employee[:2])
print(employee[2:])

# Nested tuple slicing
print(employee[2][::2])


# Repetition
data = ('Python', 'SQL')
print(data * 3)


# Merging / Concatenation
languages1 = ('Python', 'Java')
languages2 = ('C++', 'JavaScript')

languages3 = languages1 + languages2

print(languages3)


# This will give an error:
# employee[0] = 'Suresh'

# But the list inside the tuple can be modified:
employee[-1].append('TypeScript')

print(employee)
