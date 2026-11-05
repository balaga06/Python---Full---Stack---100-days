'''
#1. Best seller tag display
product_sales = int(input("enter product sales:"))
if product_sales > 0:
    if product_sales > 1000:
        print("Best Seller")
    else:
        print("No Output")
else:
    print("Product sales cannot be negative")
'''
'''
#2. Zepto applies additional delivery charges true or false
rain = bool(input("Enter current weather True or False:"))
print(type(rain)) #bool
if rain == True:
    print("Extra Rain Charges Applied")
else:
    print("No Output")

rain = input("Enter current weather True or False: ")
print(type(rain)) #str
if rain == "True":
    print("Extra Rain Charges Applied")
if rain == "False":
    print("No Output")

#3. Delivery Charge Calculation...
bill = int(input("enter the food Bill : "))
if bill > 99:
            print(f'Final Bill Amount = {bill}')
            print("Free delivery")
else:
    print(f'Final Bill Amount = {bill + 30}')

#4. Weekend Planner Based on Budget
Trip_Budget =  int(input("Enter the Trip Budget : "))
if Trip_Budget > 10000:
    print("Plan : Trip")
elif Trip_Budget > 5000:
    print("Plan : Resort Stay")
elif Trip_Budget > 3000:
    print("Plan : Movie and Dinner")
elif Trip_Budget > 1000:
    print("Plan : Cafe and Shopping")
elif Trip_Budget > 500:
    print("Plan : Street Food and Park Visit")
else:
    print("Plan : Stay Home")
'''

#Repetition Statements(Loops) ---> Loops helps us in automating repetitive
#Takse --> For , While
#Usage of For: --> It is used Mainly to iterate within in Lists,strings
#ranges..
'''
Syntax :
for <temp> in Collection/range:
        statement(s)...
        ...............
        ...............

#marks = [25,20,21,19,10,12]
#marks can be dynamic
marks = list(map(int, input("enter the marks : ").split()))
total = 0
for i in marks:
    print (i) #it traverse within the loop
    #calculate the total marks
    total = i + total
    print(total)
print(f'total marks are : {total}')
print(f'avg marks are : {total/len(marks)}')

subject = input("enter the subject")
for i in subject:
    print(i)


details = {'ids' : [12,13,14,15],
                   'marks' : (90,91,94,95)}
for data in details: #indexed through keys
    print(data)
    print(details[data]) #it returns values

for data in details.values():
    print(data)
for key,value in details.items():
    print(key,value)

details = {'ids' : [12,13,14,15],
                   'marks' : (90,91,94,95)}
print(details['ids'][1])

#range(stop) --> takes any default minimum value as 0
for i in range(5):
    print(f'value of i is{i}')
    print(f'square of i is{i**2}')

#range(start,stop) --> you can mention start and stop index postns(values)
#start is included , end is excluded
for i in range(1,11):
    print(i,i**2)
    print('--')

#range(start,stop,step)
for i in range(1,21,1):
    print(i,i**2)
for i in range(1,21,2):
    print(i,i**2)

for i in range(0,21,2):
    print(i)
for i in range(10,0,-1):
    print(i)

#for ord we use string and chr we use range
for i in range(65,91):
    print(chr(i),end = " ")
for i in range(90,64,-1):
    print(chr(i),end = " ")
'''
'''
names = ['Akash','Koushik','Vijay','Sanjay','Lokesh']
for name in names:
    print(name,end = ' ') #this returns horizontal order
for i in range(len(names)):
    print(names[i]) #names[0]--Akash,names[1]--Koushik,names[2]--Vijay,names[3]--Sanjay
    
#ask input from the user and get the sum of the number as per input
'''
'''
Test - 1
4
10

Test - 2
6
21

Test - 3
-5
No output

n = int(input("enter the number : "))
sum = 0
if n >= 0:
    for i in range(n+1):
        sum += i
    print(sum)
else:
    print("No Output")

#usecase : Checking daily workout app usage
work_log = [1,1,1,0,1,1,0]
#1 means workout done
#2 means workout missing
#find the longest workout streak
current_streak = 0
longest_streak = 0
for i in (work_log):
    #print(i)
    if i == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
                longest_streak = current_streak
    else:
        current_streak = 0
print(f'longest streak - {longest_streak} ')
'''

