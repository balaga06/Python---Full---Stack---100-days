'''
String methods --> case conversions, replacing , finding , white trailing spaces, testing methods, alignment methods...

#Case conversions --> Upper(), lower(), title(), capitalize(), swapcase()

data = 'COdegnan'
print(type(data))
print(dir(data)) #dir() returns availabe methods/functions

#upper() --> converts object into uppercase
print(data.upper())
e = data.upper()
print(e)

#lower() --> converts object into lowercase
print(e.lower())
print(data.lower())

#capitalize() --> Capitalize the first letter of the word
print('codegnan vizag'.capitalize())

#title() --> it will capitalize every letter of the word
print('it will capitalize every letter of the word'.title())

#swapcase() --> uses for when your input is lower it will return in upper vise versa
print('CODEGNAN vizag'.swapcase())

#testing methods --> which give the result as boolen (true/false)
#isupper(), islower(), isalnum(), isdigit(), isalpha(), startswith(), endswith().....

print('codegnan vizag'.isupper()) #returns false
print('codegnan vizag'.islower()) #returns true
print('CODEGNAN vizag'.isupper()) #returns false
print('CODEGNAN vizag'.islower()) #returns false
print('CODEGNAN VIZAG'.isupper()) #returns true

print('nikki06'.isalpha()) #returns true only when we have all alphabets
print('nikki'.isalpha()) 
print('nikki06'.isalnum()) #returns true only when we have alphabets and numbers together
print('nikki'.isalnum())
print('2022'.isalnum())
print('nikki06'.isdigit()) #returns true only when input contains only numbers
print('06'.isdigit())

print('Python'.istitle()) #returns true
print('Python aptitude'.istitle()) #returns false

print('Python'.startswith('P')) #returns true
print('Python'.startswith('p')) #returns false
print('Python aptitude'.startswith('a'))

data = 'Python aptitude'
print(data[7:].startswith('a')) #returns true
print(data.startswith('a',7)) #returns true
print(data.endswith('e')) #returns true
print(data[:6].endswith('n')) #returns true
print(data.endswith('n',0,6)) #returns true
print(data.endswith('n',6)) #returns false


print('77.45'.isalnum())
print('77.45'.isdigit())
print('77.45'.isnumeric()) #fractions,roman numericals
print('VIII'.isnumeric()) #roman numericals but we need to encode the data and get it


#Finding and searching methods --> find(), index(), count()

data = 'codegnan is in vizag'
print(data.find('a')) #returns only the first occurence
print(data.find('a',8)) #here we will check for the next occurences
print(data.find('u')) #returns -1 if the given object is not exist
print(data.find('a',20))#returns -1 if accurence is not find 
print(data.rfind('a')) #rfind() will return the last occurence
print(data.index('i')) #returns first occurence
print(data.rindex('i')) #returns last occurence
#if given object is not present it raises an value error
#print(data.index('t')) #raises value error

print('qwerty'.index('werty')) #as substring is starting with 'w'
#print('qwerty'.index('s')) #raises value error
print('qwerty'.rindex('y'))

#count() will return total number of occurences
print('codegnan'.count('n')) #returns 2
print('codegnan'.count('s')) #returns o as 's' is not present

#split(), join(), strip(), lstrip(), rstrip(), zfill()
#split --> returns the list of substrings from the string using separator
a = 'will return total number of occurences'
print(a.split()) #by default space is treated
b = 'will,return,total,number,of.occurences'
print(b.split())
c = b.split(',')
print(c)

#join --> concatenates every object with given iterables
print('code'.join('gnan'))
print('#'.join('gnan'))
print(','.join('gnan'))
print(' '.join('gnan'))
print('1000'.join('gnan'))


#white spaces & trimming methods --> strip(), lstrip(), rstrip()
a = ' nikhil '
print(len(a))
print(a.strip())
print(len(a.strip()))
print(a.lstrip())
print(len(a.lstrip()))
print(a.rstrip())
print(len(a.rstrip()))

#alignment methods --> zfill() (make sure to pass the width > len(obj))

print('python'.zfill(10))
print('python'.zfill(1))
print('python'.center(10,'%'))
print('python'.ljust(10,'%')) #returns the left justified string fill character 
print('python'.rjust(10,'%')) #returns the right justified string fill character
'''










