'''Tuples --> A list is an orderd , Mutable , Indexed and heterogeneous collections
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
'''