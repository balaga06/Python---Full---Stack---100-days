'''
usage of for with conditional statements
Normal completion --> Loop us going through the entire sequence naturally.
then else block will run
Interruption --> Jumping statements(break,continue)

#notifications = [0,0,0,0]
#notifications = [1,1,1,1,1]
notifications = [0,1,0,1]
#0 --> Notification read
#1 --> Unread notification
#Notification Checker
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print("Unread Notifications")
else:
        print("All Notifications are caught up")

#searching scenario same above program to be transformed --> if target is found

#break --> terminate the loop or flow of the program
#notifications = [0,0,0,0]
#notifications = [1,1,1,1,1]
notifications = [0,1,0,1]
#0 --> Notification read
#1 --> Unread notification
#Notification Checker
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print("Unread Notifications")
        break
else:
        print("All Notifications are caught up")
#print("All Notifications are caught up"

notifications = [0,1,0,1]
#0 --> Notification read
#1 --> Unread notification
#Notification Checker
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print("Unread Notifications")
        continue
else:
        print("All Notifications are caught up")

#searching in a list
#you want to handle the "item is not found" case

fruits = ['banana','apple','kiwi','cherries']
item = input("which fruit you want : ").lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got desired {item}')
        break
else:
        print(f'could not find {item} in the fruits')

#continue --> will skip the current iteration and proceeds for the remaining iterations
fruits = ['banana','apple','kiwi','cherries']
item = input("which fruit you want : ").lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got desired {item}')
        continue
else:
        print(f'could not find {item} in the fruits')

#observe by modifing usage of break and continue with else blocks
'''
#while --> It is mainly used when we rely on conditions
#it will be completely executed until the condition is satisfies
'''
while<condition>:
    statement(S)....
    ..........
    
while True:
    print("Yes") #it runs an infinite loop we need to key board int
 
#initializer with which we need to initialized statement or count object
i = 0 #initialized statement
while i<=10:
    #print(i)
    i = i+1 #counter
    print(i)

#Get the counter from 10 to 1 using while
i = 10 #initialized statement
while i>=1:
    print(i)
    i = i - 1 #counter decrement
    #print(i)

i = 0
while i<=10:
    print(10 - i)
    i = i + 1
'''
