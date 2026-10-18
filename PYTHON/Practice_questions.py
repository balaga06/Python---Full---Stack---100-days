#Section 1: Basic String Manipulation
#1. Student Name Formatter
#A college registration system receives student names in inconsistent formats. Normalize the name so
#that each word begins with a capital letter.

name = "sAkEtH kAlLePu"
print(name.title()) #Saketh Kallepu
name = input("Enter student name: ")
result = " ".join(word.capitalize() for word in name.split())
print(result)
#Enter student name: saKETH kALLePu
#Saketh Kallepu


#2. Customer Email Cleanup
#An online shopping application receives an email address with accidental spaces and uppercase
#letters. Clean it before storing it.

email = " Saketh.KALLEPU@GMAIL.COM "
print(email.lstrip().lower()) #saketh.kallepu@gmail.com 
email = " Saketh.KALLEPU@GMAIL.COM "
print(email.strip().casefold()) #saketh.kallepu@gmail.com 

#3. Product Code Replacement
#A company has changed its product prefix from OLD to NEW. Update the product code.

product_code = "OLD-101-OLD-202"
product_code = product_code.replace("OLD", "NEW")
print(product_code) #NEW-101-NEW-202
product_code = "OLD-101-OLD-202"
print(product_code.replace("OLD", "NEW", 2)) #NEW-101-NEW-202

#4. Username Generator
#A website creates usernames by combining a student's first name and graduation year, separated by
#an underscore. Convert the first name to lowercase.

first_name = "SAKETH"
year = 2027
username = first_name.lower() + "_" + str(year)
print(username) #saketh_2027
first_name = "SAKETH"
year = 2027
print(f"{first_name.lower()}_{year}") #saketh_2027

#5. Sentence Character Count
#A content-writing application needs the total number of characters in a sentence, including spaces.

sentence = "Python makes coding easy"
print(len(sentence)) #24

#Section 2: Indexing and Slicing
#6. Employee ID Extraction
#An employee ID starts with EMP followed by a six-digit number. Extract the numeric portion

employee_id = "EMP582741"
print(employee_id[3:]) #582741
employee_id = "EMP582741"
print(employee_id[-6:]) #582741

#7. Mask a Bank Account Number
#A banking application displays only the last four digits of an account number. Replace the preceding
#digits with eight asterisks.

account_number = "123456789012"
print(account_number[-4:].rjust(12, '*')) #********9012
print("*" * 8 + account_number[-4:]) #********9012
print('*' * (len(account_number) - 4) + account_number[-4:]) #********9012
print(f"{'*' * 8}{account_number[-4:]}") #********9012

#8. Alternating Character Extraction
#Extract every second character from the string, starting with the first character.

text = "CODEGNANPYTHON"
print(text[::2]) #CDGAPTO
print(text[0:13:2]) #CDGAPTO

#9. Reverse a Product Serial Number
#Reverse a serial number for a device-testing format.

serial_number = "PYTHON123"
print(serial_number[::-1]) #321NOHTYP
print("".join(reversed(serial_number))) #321NOHTYP

#10. Extract a File Extension
#A document system needs the final three characters of a filename as its extension.

filename = "student_report.pdf"
print(filename[-3:]) #pdf
print(filename.split(".")[-1]) #pdf
print(filename.rsplit(".", 1)[1]) #pdf

#Section 3: Searching, Splitting, and Joining
#11. Search for a Course Name
#Count the occurrences of the word Python in a course description, ignoring case.

description = "Python is easy. I love PYTHON. Learn python today."
print(description.title().count('Python')) #3
print(description.casefold().count("python")) #3

#12. Convert a Sentence into Words
#Separate a sentence into individual words.

sentence = "Learn Python Full Stack Development"
print(sentence.split()) #['Learn', 'Python', 'Full', 'Stack', 'Development']

#13. Generate a Formatted Address
#Combine the house number, street, city, and state into one address separated by commas.

house = "12-4"
street = "MG Road"
city = "Vijayawada"
state = "Andhra Pradesh"
print(f"{house}, {street}, {city}, {state}") #12-4, MG Road, Vijayawada, Andhra Pradesh
print(house, street, city, state, sep=', ') #12-4, MG Road, Vijayawada, Andhra Pradesh
print(house + ", " + street + ", " + city + ", " + state) #12-4, MG Road, Vijayawada, Andhra Pradesh
print(", ".join([house, street, city, state])) #12-4, MG Road, Vijayawada, Andhra Pradesh

#14. Count Words in a Message
#Calculate the number of words in a message without using loops

message = "Your application has been successfully submitted"
print(len(message.split())) #6
print(message.count(" ") + 1) #6

#15. Validate a Coupon Code
#Display the result of checking whether a coupon code contains only alphabetic characters.

coupon_code = "CODEGNAN"
print(coupon_code.isalpha()) #True
coupon_code = "CODEGNAN123" 
print(coupon_code.isalpha()) #False
print(coupon_code.isalnum()) #True



