'''
operators -- operators help us to perform operations between operands

Arthimetic operators -- + , * , - , / , // (Integer or float division), % (Modulues) , ** (exponential)

Assignment operators -- It helps to assign , update (increment,  decrement) values

# = (assigning) , +=(addition & assign) , -= (subtraction & assign) , *= (Multiple & assign)
# /= , //= , **= , %=


data = 50
print(data)
print(type(data))

stock = data
print(stock)

#Increment the value of stock
stock +=  5 #stock = stock + 5
print(stock)
print(data)

#decrement the value of data by 2 values
data -= 2 #data = data - 5
print(data)


data *= 5
print(data)

data /= 5
print(data)

data //= 5
print(data)

data **= 2
print(data)

data %= 2
print(data)

stock -= data
print(stock)

data = 20
print(data)
stock = data + 5
print(stock)

stock -= data
print(stock)

# Comparision operators (relational operators) --> It performs comparision
#between the operands and results in boolean True?False --> conditions
# == ,  != , < , > ,  <= , >=

name = 'nikhil'
attendance = 80
print(attendance >= 85)
print(attendance != 85)
print(attendance == 85)
print(attendance <= 85)
print(attendance > 85)
print(attendance < 85)
print(attendance == 80)


#Logical operators --> logical and , logical or ,logical not
#values --> and , or  , not
#and --> It needs all conditions to be satisfied (two or more)
#or --> It needs any one condition to be satisfied
#not  --> opposite to existing

max_marks = 80
marks = 75
max_att = 75
att = 70
certificate = marks >= max_marks and att > max_att
print(certificate)

marks += 10
certificate = marks >= max_marks or att > max_att
print(certificate)

marks += 10
certificate = marks >= max_marks or not (att > max_att)
print(certificate)

data = []
print(data)
print(not(data)) #returns true

data = [1,2,3,]
print(data)
print(not(data)) #returns false if data is existing
#Both logical and comparision operators will return result in Boolean


#Membership operators --> in , not in
#check for the existance in sentence (str,list,set,tuple,dict)

names = ['vinay','vijay','balakrishna','raju']
name = 'ajay'

print(name  in names) #return false
print(name not in names) #return true
print('12' in '121')
print('12' not in '121')
print (121 == 121)
#print(12 in 121) #type error as we have taken int type

print('ajay' in 'ajay') #returns true as we are checking type as a string
print(['ajay']  in ['ajay']) #returns false as its a list
print(('ajay')  in ('ajay')) #returns true 
print ('ajay' in ['ajay']) #returns true
print('ajay' in ('ajay',)) #returns true



#Identity operators --> It specifically refers to the object (memorey location)
#id -- > is , is not

a = 15
b = 15
print(a==b)
print(id(a))
print(id(b))
c = a
print(id(c))

print(c is a) #as id of the both a and c are same --> true

a = [1,2,3,4]
b = [1,2,3,4]
print(a==b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with similar values identity
print(a is b)

c = a
print(id(c))
print(c)
print(c is a) #returns true as we are assiging same object

a = [1,2,3,4]
b = [8,7,6,5]
print(a==b)
print(id(a))
print(id(b))
print(a is not b)

a = (1,2,3,4)
b = (1,2,3,4)
print(a==b)
print(id(a))
print(id(b))
print(a is b)

a = [ ]
b = [ ]
print(a==b)
print(id(a))
print(id(b))

c = a
print(id(c))
print(c is a)


a = {1,2,3}
b ={1,2,3}
print(a ==b )
print(id(a))
print(id(b))


#when we check with the inerpreter mode and scripting mode above
#tuple result changes

#Logical , Membership , Identity , Comparision , (relational) --> always result is in boolean


#Bitwise operators --> It performs operators like
# & bitwise and  , | bitwise or  , ^ bitwise xor
#an integer will be converted binary format and performs bitwise operation
#following integer to binary conversion

print(7 & 3)
print(7 | 3)
print(7 ^ 3) #XOR operation it returns 4
#7 to binary -- 0111
#3 to binary -- 0011
#7 ^ 3 -- 0100


#shifting operators(<< , >>)

print(7 << 1)
print(7 >> 1)
'''



