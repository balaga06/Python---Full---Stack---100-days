'''
Tokens --> Keywords, Variables, Literals, Operators, Punctuators, Identifiers
keywords are reserve words
'''
"""
#variables --> variables are named memory location that stores the data/
#it also acts as placeholder.It also has some rules,It cannot start with
#a number , or a special  character and no spaces in between

name = "codegnan"
age = 5
place = "vizag"
print(place)
print(name)
print(age)
#print

email_id = "nikhil@codegnan" #snakecase convention we use underscores(multiple words)
print(email_id)

branch_1 = "vizag"#we can use number anywhere but not at the start
print(branch_1)

true = 45 #as True is a keyword we cannot use as variable
print(true)
"
#Comments --> It will make users understand what it is conveying
#Single Line comment --> #
#MultiL Line comment --> we can use triple quotes '''(Doc string)

#Multiassignment of variables #Make sure to pass same number of values
#name,email,mobile,gender = "codegnan","codegnan@vizag",1236547891,"Male"
#print (name,email,mobile,gender)
#Python by default follows Implicit type

#So you can prefer single line or multiple lines for assigning variables
name = "codegnan"; age = 23; place = "vizag"
print(name,age,place)

#Deletion --> Del
del age,name #permanent deletion
print(name)

#Swapping of variables
a,b = 15,25
a,b = b,a #values of a will become b
print(a)
print(b)
c = a
print(c)

#Literals --> these are constants such as numbers (int, float, complex)
#"hello" , "bad"
age = 24
print(age)

price = 11023.33
print(price)

Match = "cricket"
print(Match)

print(type(price)) #it returns the type of object
#type() is very very important
print(type(Match)) #it returns the type of object


#Identifiers --> Name given to variables, functions, classes, objects, Modules

#Punctuators --> [ ] --> Lists, ( ) --> Tuples, { } --> Dictionaries, Sets

#Operators --> There are different type of operators --> Operations
#+, - , * ,  ** , / (arthimetic Operators), //, %

a = 5
b = 3
print(a/b) # / --> Float Division (answer is always in float values)
print(a//b) # //  --> Flooring Division (Integer division) returns Quotient
print(a%b) #Modules --> returns remainder
#Raju purchased shoes with price 1000, discount  15%, now how much raju has to pay
shoe = 1000
discount = 0.15
final_price = shoe - (shoe * discount)
print(final_price)

#Vijay went to hotel for dinner his bill is 2500 , GST applicable is 5%
#hotel manager has given him 5% discount, how much vijay has to pay?

bill = 2500
GST = 0.05
discount = 0.05

discount_amount = bill * discount
bill_after_discount = bill - discount_amount

gst_amount = bill_after_discount * GST
final_amount = bill_after_discount + gst_amount

print("Discount:", discount_amount)
print("After Discount:", bill_after_discount)
print("GST:", gst_amount)
print("Final Amount:", final_amount)

"""








