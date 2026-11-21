'''
#1. Shopping Cart: Discount at the Right Time
#A store needs a bill summary for a shopping cart. Write a Python program to calculate the subtotal, discount and final bill.

prices = list(map(int, input("Enter the prices: ").split()))
subtotal = 0
if any(price < 0 for price in prices):
    print("Enter only positive values")
else:
    for i in prices:
        subtotal += i
    if subtotal >= 2000:
        discount = subtotal * 0.10
    else:
        discount = 0
    final_bill = subtotal - discount
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Bill: {final_bill:.2f}")

#2. Password Audit: Count and Decide
#A registration form needs a password audit. Count character types and decide whether the password meets the stated rules.

password = input("Enter your password: ")

upper = 0
lower = 0
digits = 0
special = 0
length = 0
for ch in password:
    length += 1
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif '0' <= ch <= '9':
        digits += 1
    else:
        special += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Special:", special)
if length >= 8 and upper >0 and lower >0 and digits >0 and special >0:
    print("Status: STRONG")
else:
    print("Status: WEAK")

#3. Watch History: Ignore Skipped Entries
#A watch-history list includes the marker SKIP for titles that were not watched. Print a numbered list of watched titles.

history = list(map(str , input("Enter the movies : ").split()))
watched = 0
for title in history:
    if title != "SKIP" and title != "skip":
        watched += 1
        print(f"{watched}. {title}")
print("Total Watched:", watched)
prices = list(map(int, input("Enter the prices: ").split()))
subtotal = 0
if any(price < 0 for price in prices):
    print("Enter only positive values")
else:
    for i in prices:
        subtotal += i
    if subtotal >= 2000:
        discount = subtotal * 0.10
    else:
        discount = 0
    final_bill = subtotal - discount
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Bill: {final_bill:.2f}")
#4. Salary Report: Extremes and Threshold
#An HR team needs a salary summary and the number of employees earning at least Rs. 60000.

salaries = dict(
    (name, int(salary))
    for name, salary in
    (item.split(':') for item in input("Enter name:salary pairs: ").split()))
if salaries == {}:
    print("No salary records")
else:
    total = 0
    count = 0
    above = 0
    highest = 0
    lowest = 0
    first = True
    for name in salaries:
        s = salaries[name]
        total += s
        count += 1
        if s >= 60000:
            above += 1
        if first:
            highest = s
            lowest = s
            first = False
        else:
            if s > highest:
                highest = s
            if s < lowest:
                lowest = s
    average = total / count
    print("Highest:", highest)
    print("Lowest:", lowest)
    print(f"Average: {average:.2f}")
    print("At Least 60000:", above)

#5. Cricket Scorecard: Validate Every Ball
#A scoring app receives runs for each delivery. Some entries are invalid. Build a summary using only valid entries.

runs = list(map(int, input("enter the runs : ").split()))
total_runs = 0
boundaries = 0
dots = 0
invalid = 0
for r in runs:
    if r == 0 or r == 1 or r == 2 or r == 3 or r == 4 or r == 6:
        total_runs += r
        if r == 4 or r == 6:
            boundaries += 1
        if r == 0:
            dots += 1
    else:
        invalid += 1
print("Total Runs:", total_runs)
print("Boundaries:", boundaries)
print("Dot Balls:", dots)
print("Invalid Entries:", invalid)

#6. Email Report: Exact Domain Match
#A support team wants a domain report for its contact list. Extract every domain and count addresses belonging to codegnan.com.

emails = input("Enter email addresses: ").split()
codegnan = 0
for email in emails:
    domain = ""
    after_at = False
    for ch in email:
        if after_at:
            domain += ch
        elif ch == '@':
            after_at = True
    print(domain)
    if domain == "codegnan.com":
        codegnan += 1
print("Codegnan Emails:", codegnan)

#7. ATM PIN: Stop at the Correct Attempt
#An ATM allows at most three PIN attempts. Simulate the attempt process using a for loop.

used = 0
granted = False
for i in range(3):
    pin = input("Enter your 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN! Enter exactly 4 digits.")
        continue
    used += 1
    if pin == "1234":
        granted = True
        break
if granted:
    print("Access Granted")
else:
    print("Card Blocked")
print("Attempts Used:", used)

#8. Guessing Game: Quit Without Using a Guess
#A guessing game uses the secret number 25. The player may enter 0 to quit. Simulate it with a for loop.

guesses = list(map(int, input("Enter your guesses: ").split()))
used = 0
for g in guesses:
    if g == 0:
        print("Game Cancelled")
        break
    used += 1
    if g < 25:
        print("Too Low")
    elif g > 25:
        print("Too High")
    else:
        print("Correct Guess")
        break
print("Guesses Used:", used)


#9. Food Counter: Bill Until EXIT
#A food counter accepts one item name at a time and closes the order when EXIT is entered. Use a for loop to prepare the bill.

orders = input("Enter your orders: ").split()
items = 0
bill = 0
invalid = 0
for item in orders:
    item = item.title()
    if item == "EXIT":
        break
    elif item == "Burger":
        items += 1
        bill += 80
    elif item == "Pizza":
        items += 1
        bill += 150
    elif item == "Fries":
        items += 1
        bill += 60
    else:
        invalid += 1
print("Items Ordered:", items)
print("Total Bill:", bill)
print("Invalid Orders:", invalid)

#10. Quiz Game: Score, Lives and Two Stop Conditions
#A quiz game starts with 3 lives and a score of 0. A player wins after 3 correct answers in total. Simulate the game using a for loop.

answers = input("Enter your answers: ").split()
score = 0
lives = 3
used = 0
result = ""
for ans in answers:
    ans = ans.title()
    used += 1
    if ans == "Python":
        score += 10
    else:
        lives -= 1
    if score == 30:
        result = "You Win"
        break
    if lives == 0:
        result = "Game Over"
        break
print(result)
print("Score:", score)
print("Lives Remaining:", lives)
print("Answers Used:", used)

'''
Task: Build a simple choice chooser:
----------welcome to gaming world------------------------
1 - recursion logic factorial
2 - sum of natural numbers(recursion)
3 - BMI calculation
4 - Fibonacci series
5 - ATM usecase
any other number - only enter 1 - 5
Q - quit

 # ---------- GAMING WORLD ----------

def factorial(n):
    if n < 0:
        return "Negative numbers are not accepted"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_program():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Negative numbers are not accepted")
        else:
            print("Factorial:", factorial(n))
    except ValueError:
        print("Please enter a valid integer!")


# ---------- SUM OF NATURAL NUMBERS (RECURSION) ----------

def natural_sum(n):
    if n < 0:
        return "Negative numbers are not accepted"
    elif n == 0:
        return 0
    else:
        return n + natural_sum(n - 1)


def sum_program():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Negative numbers are not accepted")
        else:
            print("Sum of Natural Numbers:", natural_sum(n))
    except ValueError:
        print("Please enter a valid integer!")


# ---------- BMI CALCULATION ----------

def bmi_calculation():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values!")
        else:
            bmi = weight / (height ** 2)
            print(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("Category: Underweight")
            elif bmi < 25:
                print("Category: Normal Weight")
            elif bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")

    except ValueError:
        print("Please enter valid numeric values!")


# ---------- FIBONACCI SERIES ----------

def fibonacci():
    try:
        n = int(input("Enter the number of terms: "))

        if n <= 0:
            print("Please enter a positive number!")
        else:
            a = 0
            b = 1

            print("Fibonacci Series:")

            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b

            print()

    except ValueError:
        print("Please enter a valid integer!")


# ---------- ATM USECASE ----------

def atm():
    balance = 10000
    correct_pin = 1234

    try:
        pin = int(input("Enter your ATM PIN: "))

        if pin != correct_pin:
            print("Incorrect PIN!")
            return

        print("Welcome to ATM!")

        while True:
            print("1 - Check Balance")
            print("2 - Deposit Money")
            print("3 - Withdraw Money")
            print("4 - Exit ATM")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                print(f"Available Balance: ₹{balance}")

            elif choice == '2':
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    print("Deposit amount must be greater than zero!")
                else:
                    balance += amount
                    print("Deposit Successful!")
                    print(f"Updated Balance: ₹{balance}")

            elif choice == '3':
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Withdrawal amount must be greater than zero!")
                elif amount > balance:
                    print("Insufficient Balance!")
                else:
                    balance -= amount
                    print("Withdrawal Successful!")
                    print(f"Updated Balance: ₹{balance}")

            elif choice == '4':
                print("Thank you for using ATM!")
                break

            else:
                print("Invalid choice! Enter 1 - 4.")

    except ValueError:
        print("Please enter valid numeric values!")


# ---------- MAIN MENU ----------

print("---------- WELCOME TO GAMING WORLD ----------")

while True:

    print("1 - Recursion Logic Factorial")
    print("2 - Sum of Natural Numbers (Recursion)")
    print("3 - BMI Calculation")
    print("4 - Fibonacci Series")
    print("5 - ATM Usecase")
    print("Q - Quit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        factorial_program()

    elif choice == '2':
        sum_program()

    elif choice == '3':
        bmi_calculation()

    elif choice == '4':
        fibonacci()

    elif choice == '5':
        atm()

    elif choice.lower() == 'q':
        print("Thank you for visiting Gaming World! Have fun!")
        break

    else:
        print("Invalid choice! Only enter 1 - 5 or Q.")
'''


