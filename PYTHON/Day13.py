'''
#conditional statements --> statements rely on the condition

sytax if :

if <condition>:
        statements(S).....

if True:
    print("welcome to codegnan")
    print("This is PFS_VSP_007")

if False:
    print("welcome to codegnan")
    print("This is PFS_VSP_007")

data = False
if data:
    print("welcome to codegnan")
    print("This is PFS_VSP_007")

data = True
if data:
    print("welcome to codegnan")
    print("This is PFS_VSP_007")
print("Guys are good but they will come late")

data = False
if data:
    print("welcome to codegnan")
    print("This is PFS_VSP_007")
print("Guys are good but they will come late")

#mark = 25
mark = int(input("Enter a value"))
marks = [12,16,25,14]
if mark in marks:
        print("Marks successfully fetched")
        print(f'marks are {mark}')
print(f'Its done for a day')

age = int(input("enter a age"))
min_age = 18
if age > min_age :
        print(f'eligible to vote')
print(f'Not eligible to vote')

stock = int(input("enter a value"))
total_stock = 100
if stock > 0 and stock < total_stock:
        print(f'You can order the item')
        print(f'Item selected and placed into cart')
        print(f'Item ordered')

#Usage of else:

if <condition>:
    statement(s).....
else:
    statement(s).....
'''
'''
stock = int(input("enter a value"))
total_stock = 100
if stock > 0 and stock < total_stock:
        print(f'You can order the item')
        print(f'Item selected and placed into cart')
        print(f'Item ordered')
else:
        print(f'Invalid entry')

algorithm:
accept the input from the user
if check whether enter age should not be negative 
    if make the eligibility case as age greater than or equals to 18:
        eligibility granted
    else age is not matching eligibility:
        inform number of years to wait
else entered age is negative 

#code
age = int(input("enter a age = "))
min_age = 18
if age > 0 and age < 100:
        if age >= min_age :
                print(f'eligible to vote')
        else:
                print(f'Not eligible to vote')
                print(f'you need to wait to get voting in {min_age - age} years')
else:
    print(f'enter valid age')

#if - elif - else --> we wanted to map multiple conditions

if condition1:
    statement(s)....
    ............
elif condition2:
    statement(s)......
    ..............
elif condition3:
    statement(s)......
    .............
else:
    statement(s)....
    ..........


age = int(input("enter a age = "))
min_age = 18
if age < 0 or age > 100:
    print(f'enter valid age')
elif age >= min_age :
    print(f'eligible to vote')
else:
    print(f'Not eligible to vote')
    print(f'you need to wait to get voting in {min_age - age} years')

#Task --> Placement Eligibility Tracker/System
print("--------------------------------PLACEMENT ELIGIBITY CHECKER---------------------------------")
name = input("enter the name of the student")
attendance = float(input("enter the attendance of the student"))
daily_exam = float(input("enter the daily exam score average"))
weekly_exam = float(input("enter the weekly exam score average"))
mock_interview = float(input("enter mock interview score "))
projects = int(input("enter number of projects"))
project_score = float(input("enter project score"))

avg_score = (daily_exam + weekly_exam + mock_interview + project_score)/4
print("student name = " , name )
print(avg_score)
if (attendance < 0 or attendance > 100 or
    daily_exam < 0 or daily_exam > 100 or
    weekly_exam < 0 or weekly_exam > 100 or
    mock_interview < 0 or mock_interview > 100 or
    projects < 0 or
    project_score < 0 or project_score > 100):
    
    print("Invalid input! Please enter valid values.")
elif attendance >= 75 and avg_score >= 75 and projects >= 2:
    print(f'Result : Student is placement ready he falls in hotlist')
elif attendance >= 60 and avg_score >= 60 and projects > 1:
    print(f'Result : Students need to push more preparation - Improvement stage'
          )
else:
    print(f'Result : Student is in foundation stage - Need Practice session')
'''







