'''
Reduce() -- It reduces an iterable into a single value....
It repeatedly applies a function to combine elements

we can use it from function tools

import functools
from functools import reduce
#Sum of numbers from a iterable
numbers = [1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)
print(result)

#Largest from a collection
import functools
from functools import reduce
data = list(map(int,input().split()))
print(data)
result = reduce(lambda a,b:a if a > b else b ,data)
print(result)

#Return the longest word in the strings
import functools
from functools import reduce
words = ['python','developer','sql','programming']
longest = reduce(lambda a,b :  a if len(a) > len(b) else b , words)
print(longest)
#Map is for Transformation
#filter is for selection
#reduce is for aggregation

#List Comprehensions --> In Python it is a precise way to create
#Lists
#Syntax -- [expresssion for item in iterable]
#iterable == list,set,dict or range

li = []
for i in range(10):
    #print(i)
    li.append(i)
print(li)

li = [i for i in range(10)]
print(li)

squares = [i**2 for i in range(1,11)]
print(squares)

even = [int(i%2==0) for i in range(1,11)]
print(even)

even = [i for i in range(1,11) if i%2==0]
print(even)

scores = [25,48,55,45,62]
f_scores = [i+10 for i in scores]
print(f_scores)
m_scores = list(map(lambda i:i+10,scores))
print(m_scores)

names = ['saketh','codegnan','vizag']
result = [i.upper() for i in names]
print(result)
result = list(map(lambda i:i.upper(),names))
print(result)

#List comprehension with if-else usage
#[true_value if condition else false_value for item in iterable]
data = [12,4,5,6,8,9]
result = ["even" if i%2==0 else "odd" for i in data]
print(result)
result = [i**2 if i%2==0 else i**3 for i in data]
print(result)
'''




