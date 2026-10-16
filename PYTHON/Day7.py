'''
sequences --> Strings, Lists, Tuples, Sets, Frozensets, Dicts
Strings --> A string is group of characters, It is immutable, ordered , Indexed Collection.
we can denote it in single , double or triple quotes....

data = '' #empty string 
print(type(data))
print(len(data))

data = [''] #only list and set getting length 1 when we write the input value like this...
print(type(data))
print(len(data))

#Operations --> concatenation,Repetition, Indexed,slicing
#concatenation --> Combining multiple strings
sub1 = 'python'
sub2 = 'Mysql'
print(sub1+sub2)
#output should be python,Mysql
#python <-> mysql
print(f'{sub1},{sub2}')
print(sub1+' <-> '+sub2)
print(f'{sub1} <-> {sub2}')


#Repetition --> String can be repeated any number of items with a valid int
print('*')
print('*' * 10)
name = 'nikhil';place = 'vizag'
print(f'{name * 10}')
print(f'------>{name} is in ------->{place}')


#Membership --> in, not in
print('jay' in 'ajay')
print('Jay' in 'ajay') #return false
print('Jay' not in 'ajay')

#Indexing --> Accessing each position{index} in an object
#it starts at 0 and ends at len(obj) - 1
name = 'placement'
print(len(name))
#traversing  the elements --> positive indexing
print(name[4]) #output will be e
#print(name[9]) #index error
#Negative Indexing --> Start from back it is denoted as -1 to len(obj)
print(name[-1])
print(name[-4]) 
print(name[-0]) #it will return 'p'


#slicing --> group of characters --->[start : end] start is included , end is excluded (len(obj) - 1)
s = 'codegnan'
print(s[:])
print(s[0:])
print(s[1:])
print(s[4:8])
print(s[:6])
print(s[1:6]) #In this case it will return 'odegn' 
print(s[4:21]) #In this case it will return 'gnan' because start with 4 included upto 21 it will excluded...
print(s[2:5])
print(s[5:])
print(s[21:]) #it returns empty string 
print(s[3:21]) #returns till end of string
print(s[5:1]) #returns empty string as positive slicing lower index to higher index

#name[2] = 'nikki' #Strings are immutable


s = "Nikhil"
print(s[-1:]) #returns only last character
print(s[-4:-1]) #'khi
print(s[-1:-1]) #it returns empty string
print(s[:-4]) #it returns 'Ni'
print(s[-1:-6]) #it returns empty string
print(s[: : -1]) #reverse string

print(s[1:-1])
print(s[-1:2])
#Task --> create a string and explore above possibilites

#Striding --> [start : end : step] --> Now we can specifically desired characters in an interval
a = 'placement'
print(a[::1])
print(a[::2])
print(a[::3])
#print(a[::0]) #value error
print(a[1:4:2])
print(a[1:5:1])


c = 'visakhapatnam'
print(c[:4])
print(c[7:])
print(c[-6:])
print(c[1:7:2])

print(c[4:9])
print(c[-9:-4])


#what if we give -1 in interval
print(c[::-1]) #this is helps return in reverse order
print(c[::-2])
print(c[-1:-5:-1])
print(c[1:9:-1]) #it returns empty string
print(c[-9:-1:2]) #it will not empty it will process step and start and end 'kaan'
 #you can explore all cases in striding

#Built in functions --> type(), len(), min(), max(), ord(), chr() ,sorted()

password = 'admin'
print(len(password))
print(type(password))
print(min(password))
print(ord('a'))
print(ord("A"))
print(ord('!'))
print(ord('#'))
print(ord('@'))
print(ord('$'))
print(ord('%'))
print(sorted(password))
'''












