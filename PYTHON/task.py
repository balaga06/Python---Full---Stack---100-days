# ---------- WELCOME TO GAMING WORLD ----------

# 1. FACTORIAL USING RECURSION
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 2. SUM OF NATURAL NUMBERS USING RECURSION
def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n + natural_sum(n - 1)


# 3. BMI CALCULATION
def bmi_calculation():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive!")
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
            print("Category: Obesity")


# 4. FIBONACCI SERIES
def fibonacci():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Enter a positive number!")
    else:
        a = 0
        b = 1
        print("Fibonacci Series:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()


# 5. ATM USECASE
# ---------- ATM USECASE ----------
def atm():
    balance = 10000
    correct_pin = 1234
    attempts = 3

    while attempts > 0:
        pin = int(input("Enter your ATM PIN: "))

        if pin == correct_pin:
            print("PIN verified successfully!")
            break
        else:
            attempts -= 1
            print("Incorrect PIN!")

            if attempts > 0:
                print(f"You have {attempts} attempts remaining.")
            else:
                print("Your ATM card is blocked for 24 hours.")
                print("Please try again after some time.")
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
                print("Enter a valid deposit amount!")
            else:
                balance += amount
                print("Deposit Successful!")
                print(f"Updated Balance: ₹{balance}")

        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Enter a valid withdrawal amount!")
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Withdrawal Successful!")
                print(f"Remaining Balance: ₹{balance}")

        elif choice == '4':
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid ATM choice! Enter 1 - 4.")

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
        n = int(input("Enter a number: "))
        if n < 0:
            print("Negative numbers are not accepted!")
        else:
            print("Factorial:", factorial(n))
    elif choice == '2':
        n = int(input("Enter a number: "))
        if n < 0:
            print("Negative numbers are not accepted!")
        else:
            print("Sum of Natural Numbers:", natural_sum(n))
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
