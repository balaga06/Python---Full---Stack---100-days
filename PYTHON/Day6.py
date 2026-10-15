'''
TOKENS,DATATYPES (NUMERIC,BOOLEAN,NONETYPE,SEQUNCES (STR,LISTS,TUPLES,SETS,FROZENSETS,MAPPING OBJECTS
(DICTS)) TYPECASTING
OPERATORS
INPUT FORMATTING /OUTPUT FORMATTING

#input Formatting --->input()

#Usage of input()
#we can pass any type of objects as input -->result is in only string
name=input("enter name:")
print(name)
print(type(name))

#Integer input --->INT() ---> if you  mismatch value ---> it raise valueerror
age=int(input("Enter age:"))
print(age)
print(type(age))

#Float input ---->Float() ---->we can pass either integer/decimal value -->float
marks=float(input("enter the marks:"))
print(marks)
print(type(marks))


#GROUP of strings (Multiple values as strings)
#space seperated valuesn---> we need to give one space after each object
#returns list
names=input().split()#no need of promt(competative coding platforms)
names =input("enter the names:").split() 
print(names)
print(type(names))

#comma seperated values
subjects =input("enter the subjects:").split(',')
print(subjects)
print(type(subjects))

 #multiple values (more than one ) strings
name,batch=input("enter the details:").split()
print(name)
print(batch)
print(type(name))

#multiple integer values

order_id,cost=map(int,input().split())
print(order_id,cost)

marks_p,marks_a,marks_e=map(float,input().split())
print(marks_p,marks_a,marks_e)

#Group of Integers,float values
stu_marks=list(map(int,input("enter the marks:").split('*')))
print(stu_marks)

discounts=list(map(float,input("enter the discounts:").split('*')))
print(discounts)

#accept the cost of selling the product from user and also the orginal coast
#of the products and determine the profit /loss amount for user
original_cost=float(input("enter the cost:"))
selling_cost=float(input("enter the s_cost:"))
profit=selling_cost - original_cost
print(profit)

#Set of integers --->replaces int with float
ids =set(map(int,input("ids:").split(',')))
print(ids)
print(type(ids))

#Passing list() as input using eval()

list_data=eval(input("enter the values:"))
print(list_data)
print(type(list_data))
print(len(list_data))
tuple_data=eval(input("enter the values:"))
print(tuple_data)
print(type(tuple_data))
print(len(tuple_data))
set_data=eval(input("enter the values:"))
print(set_data)
print(type(set_data))
print(len(set_data))

#passing dict data using eval
stu_ids=eval(input("enter ids:"))
print(stu_ids)
# so using eval() u can pass any type of data

#output formating --->print() 
a,b,c=map(str,input("enter the names:").split())
print(a,b,c)

#now we will use sep --->sep is a keyword
print(a,b,c,sep="-----")

#End is specifically telling how u wanna end the statements

print(a,b,c,sep=":",end='\t') #here end = tab space character
print('balu','kumar',ends="") #here end =space character
print(34,4.4)

 #1)Using commas in print() ---> we separate by commas
name ="codegnan";branch="vizag";batch='pfs-vsp-007'
print(name,"is in",branch)
print(batch,"from",branch,"branch")

#2) Using%(modulus) formatting -->old style c programming
#% d---->integers,%f ---->float,%s --->strings

age = 23
price=45.256
place="vizag"
print("age =%d | price =%f |place =%s"%(age,price,place))
print("price is %.f"%price)#in this case complete decimal part is wiped 
print("price is %.2f "%price)#rounding off to two decimals


#3) Usage of String formatting --> str.format()

name = "Codegnan";branch = "Vizag";age = 8
print("{} is in {} and its of {} years in Edtech Industry".format(name,branch,age))

a,b = 2,45
print("{0},{1}".format(a,b))
print("value of a is {} and value of b is {}".format(a,b))

#f.string notation --> Python 3.9+ versions
print(f'{name} is in {branch}')
#make sure to denote the variables only in curly braces
print(f'Value of a is {a} and b is in {b}')
print(f'"codegnan is in {branch} and of {age} years in training"')
'''
























