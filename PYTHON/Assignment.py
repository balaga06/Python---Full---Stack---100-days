'''
1. if Statement Programs
Q1. Best Seller Tag Display
sales = int(input("Enter product sales: "))
	if sales > 1000:    
		print("Best Seller")



Q2. Instagram Verification Status
eligible = input("Eligible Account (True/False): ")
subscription = input("Meta Verified Subscription (True/False): ")
	if eligible == "True" and subscription == "True":    
		print("Verified Badge Granted")



Q3. Zepto Rain Delivery Charges
rain = input("Is it raining? (True/False): ")
	if rain == "True":    
		print("Extra Rain Charges Applied")




2. if-else Statement Programs
Q1. Username and Password Login
username = input("Enter Username: ")
password = input("Enter Password: ")
	if username == "admin" and password == "admin123":
		print("Login Successful")
	else:    
		print("Invalid Credentials")



Q2. Product Search
products = ["Laptop", "Mobile", "Watch"]
search = input("Enter Product to Search: ")
	if search in products:
		print("Product Found")
	else:    
		print("Product Not Found")



Q3. Delivery Charge Calculation
order = int(input("Enter Order Amount: "))
	if order > 99:    
	bill = orderelse:    
	bill = order + 30
	print("Final Bill Amount:", bill)




3. if-elif-else Statement Programs
Q1. Weekend Planner Based on Budget
budget = int(input("Enter Your Budget: "))
if budget > 10000:
	print("Plan: Trip")
elif budget > 5000:    
	print("Plan: Resort Stay")
elif budget > 3000:
	print("Plan: Movie and Dinner")
elif budget > 1000:
	print("Plan: Cafe and Shopping")
elif budget > 500:
	print("Plan: Street Food and Park Visit")
else:
	print("Plan: Stay Home")



Q2. Greeting Based on Time
hour = int(input("Enter Current Hour: "))
if hour >= 5 and hour <= 11:
	print("Good Morning")
elif hour >= 12 and hour <= 16:
	print("Good Afternoon")
elif hour >= 17 and hour <= 20:
	print("Good Evening")
else:   
	print("Good Night")



Q3. Hostinger Hosting Plan
budget = int(input("Enter Your Budget: "))
if budget > 10000:
	print("Cloud Hosting")
elif budget > 5000:
	print("Business Hosting")
elif budget > 2000:
	print("Premium Hosting")
else:
	print("Single Hosting")




4. Nested if Statement Programs
Q1. Instagram Story Visibility
follows = input("Follows Account (True/False): ")
if follows == "True":
close_friend = input("Close Friend (True/False): ")
	if close_friend == "True":
		print("Story Visible")
	else:
		print("Not in Close Friends List")
else:
	print("Follow the Account First")



Q2. BGMI Tournament Entry
registered = input("Registered (True/False): ")
if registered == "True":
fee_paid = input("Fee Paid (True/False): ")
	if fee_paid == "True":
		print("Tournament Entry Confirmed")
	else:
		print("Entry Fee Pending")
else:
	print("Registration Required")



Q3. Google Drive File Access
link = input("Link Active (True/False): ")
if link == "True":
permission = input("Permission Granted (True/False): ")
	if permission == "True":
		print("File Opened Successfully")
	else:
		print("Access Denied")
else:
	print("Invalid File Link")
'''