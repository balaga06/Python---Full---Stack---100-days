'''
Functions are turned as First Class Objects...

Anonynous Functions: An Anonymous Function is a nameless function, we lambda keyword to use it..
They are generally used for sort simple,Operations can be written in a single line. They are also termed as
Lambda Functions...They are generally used with filter(),map() and reduce()

syntax : Lambda argument(s) : expression

#Create a function to get the area of rectangle

def rectangle(l,b):
    """Area of rectangle"""
    return l*b
print(rectangle(7,5))

area = lambda l,b : l*b
print(f'Area of rectangle is {area(7,5)}')


#Square of a number --> Normal functions --> lambda function
def square(number):
    """Square of a number"""
    return number ** 2
number = int(input())
print(f'Square of a {number} is {square(6)}')


number = int(input())
square = lambda number : number ** 2
print(f'square of a {number} is {square(number)}')

#Find the Maximum of two numbers

def max(a,b):
    """Find the Maximum of two numbers"""
    return a if a>b else b
print(max(13,17))

a, b = map(int, input().split())
max = lambda a,b : a if a>b else b
print(max(a,b))

#No parameter in Lambda
greet = lambda : "Welcome to Codegnan"
print(greet())


#Filter() used to select elements from an iterable based on a condition
#only the elements that satisfy the condition are returned

#filter(function,iterable)

num = [1,2,3,4,5,6,4,5,6,7,8,9,10,11,12,13]
def even(number):
    even_list = [ ]
    for i in number:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
print(even(num))

number = [1,2,3,4,5,6,4,5,6,7,8,9,10,11,12,13]
result = list(filter(lambda num:num%2==0,number))
print(result)

odd_result = list(filter(lambda num:num%2!=0,number))
print(odd_result)


prices = list(map(int,input().split()))
result = dict(filter(lambda price:price>700,prices))
print(result)


#map() applies transformation to every element in a collection
#map(function,*iterables)
scores = [15,20,19,23]
result = list(map(lambda new_score:new_score+1,scores))
print(result)

d = list(map(int,input().split())) #list of integers 
print(d)

#add GST --> 18%
prices = [1000,5000,4500]
final_price = list(map(lambda price:price + (price*0.18),prices))
print(final_price)


#calculate length of objects in a collection
subject = ['python','sql','aptitude','softskills']
result = list(map(lambda word:len(word),subject))
print(result)
result = list(map(lambda word:word.upper(),subject))
print(result)
'''

