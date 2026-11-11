'''
1. Shopping Cart: Discount at the Right Time
A store needs a bill summary for a shopping cart. Write a Python program to calculate the subtotal, discount and final bill.

prices = list(map(int, input("enter the prices : ").split()))
subtotal = 0
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

2. Password Audit: Count and Decide
A registration form needs a password audit. Count character types and decide whether the password meets the stated rules.

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

if length >= 8 and upper >= 1 and lower >= 1 and digits >= 1 and special >= 1:
    print("Status: STRONG")
else:
    print("Status: WEAK")

3. Watch History: Ignore Skipped Entries
A watch-history list includes the marker SKIP for titles that were not watched. Print a numbered list of watched titles.

history = list(map(str , input("Enter the movies : ").split()))
watched = 0
for title in history:
    if title != "SKIP" and title != "skip":
        watched += 1
        print(f"{watched}. {title}")
print("Total Watched:", watched)

4. Salary Report: Extremes and Threshold
An HR team needs a salary summary and the number of employees earning at least Rs. 60000.

salaries = dict(
    (name, int(salary))
    for name, salary in
    (item.split(':') for item in input("Enter name:salary pairs: ").split())
)

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

5. Cricket Scorecard: Validate Every Ball
A scoring app receives runs for each delivery. Some entries are invalid. Build a summary using only valid entries.

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

6. Email Report: Exact Domain Match
A support team wants a domain report for its contact list. Extract every domain and count addresses belonging to codegnan.com.

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

7. ATM PIN: Stop at the Correct Attempt
An ATM allows at most three PIN attempts. Simulate the attempt process using a for loop.

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

8. Guessing Game: Quit Without Using a Guess
A guessing game uses the secret number 25. The player may enter 0 to quit. Simulate it with a for loop.

used = 0

while True:
    g = int(input("Enter your guess: "))

    if g < 0:
        print("Invalid Guess. Enter a non-negative integer.")
        continue

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

used = 0

while True:
    g = int(input("Enter your guess: "))

    if g < 0:
        print("Invalid Guess. Enter a non-negative integer.")
        continue

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

used = 0

while True:
    g = int(input("Enter your guess: "))

    if g < 0:
        print("Invalid Guess. Enter a non-negative integer.")
        continue

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

9. Food Counter: Bill Until EXIT
A food counter accepts one item name at a time and closes the order when EXIT is entered. Use a for loop to prepare the bill.

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

10. Quiz Game: Score, Lives and Two Stop Conditions
A quiz game starts with 3 lives and a score of 0. A player wins after 3 correct answers in total. Simulate the game using a for loop.

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
