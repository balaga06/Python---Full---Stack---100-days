'''
while --> Initialized statement,counter...

#banking Scenario --> PIN authentication if more than 3 attempts account locked

pin = '2612'
max_attempts = 3
#You need to have a current attempt
current_attempt = 0
while current_attempt < max_attempts:
    enter_pin = input("Enter the ATM pin : ")
    if enter_pin == pin:
        print("Login Successful")
        print("Withdraw the Money.....")
        break
    else:
        print("Entered ATM pin is incorrect , Try again Carefully")
        current_attempt += 1
else:
    print("Account locked....Try again after 24 hours")

#BMI --> body mass index -->bmi = weight(kgs) / (height**2) meters
#feet --> 1 feet --> 12 inches --> 2.54cm --> 30.48cms
# -->5 feet 6 inches --> 167.78 cms --> 1.67 meters

n = int(input("How many users : "))
for i in range(n):
    weight = float(input("Enter your weight in kgs : "))
    height = float(input("Enter your height in meters : "))
    name = input("enter the name : ")
    bmi = weight / ((height**2))
    #print(round(bmi, 3))
    if weight <= 0 or height <= 0:
        print("enter valid Input")
    else:
        print("Your BMI is:", round(bmi, 2))
        if bmi < 18.5:
            print(f'{name} you are Category: Underweight Your BMI is {round(bmi,3)}')
        elif bmi < 25:
            print(f'{name} you are Category: Normal Weight Your BMI is {round(bmi,3)}')
        elif bmi < 30:
            print(f'{name} you are Category: Overweight Your BMI is {round(bmi,3)}')
        else:
            print(f'{name} you are Category: Obesity Your BMI is {round(bmi,3)}')
            

#Task 1 --> For same above BMI calculator , store the details in details in dictionary

#BMI_result = {'names' : [user 1 , user 2 , user 3],
            #'BMI_values' : [bmi 1 , bmi 2, bmi 3],
                            
BMI_result = {
    'names': [],
    'BMI_values': []
}
n = int(input("How many users : "))
for i in range(n):
    weight = float(input("Enter your weight in kgs : "))
    height = float(input("Enter your height in meters : "))
    name = input("enter the name : ")
    bmi = weight / ((height**2))
    #print(round(bmi, 3))
    if weight <= 0 or height <= 0:
        print("enter valid Input")
    else:
        print("Your BMI is:", round(bmi, 2))
        BMI_result['names'].append(name)
        BMI_result['BMI_values'].append(round(bmi, 3))
        if bmi < 18.5:
            print(f'{name} you are Category: Underweight Your BMI is {round(bmi,3)}')
        elif bmi < 25:
            print(f'{name} you are Category: Normal Weight Your BMI is {round(bmi,3)}')
        elif bmi < 30:
            print(f'{name} you are Category: Overweight Your BMI is {round(bmi,3)}')
        else:
            print(f'{name} you are Category: Obesity Your BMI is {round(bmi,3)}')
            
print("----------------------------------------------------- Final BMI Result -------------------------------------------------------------")
print(BMI_result)

#assert --> It is mainly used in debugging checking during development
#it tests whether a given condition is satisfied or not its
#a mandatory else it will raise an error . It mainly used to catch bugs by ensuring the conditions hold true...

#syntax -- assert <condition>,"Error Message"

x = int(input("Enter the values : "))
#assert x>0
assert x>0, "enter any positive values"
x = x**2
print(f'final result is {x}')
assert x in [24,25,12,10],"checking status"
print(f'Search Found')
'''
