'''
Dictionaries -->A Dictionary is a Mutable collection,data is indexed
using keys,keys must be unique.Dictionaries Methods
'''
details = {'ids':['CGVI0242','CGVI0249',
                  'CGVI0224','CGVI0240'],
           'names':['Nikitha','Deepthi',
                    'Vinay','Tej'],
           'batch':'PFS-VSP-007',
           'place':('Vizag','Vjwda','Hyd','Bnglre'),
           'subjects':{'Python','Aptitude','Softskills'}}
#print(len(details))
#Membership
'''print('ids' in details)
print('Vinay' in details['names']) #we are accessing via keys
print('Python' in details['subjects'])

#print(details*2) #TypeError
#print(details + details) #TypeError'''

#Dictionary is a Mutable collection
details['marks'] = [25,20,18,20]
#print(details)
#print(len(details))
#in above way we can insert new data into the dictionary

#Methods on Dictionaries:

#print(dir(details))
print(details.keys()) #returns Dictionary Keys
#print(details.values()) #returns Dictionary values
#print(details.items())  #returns Key value pairs from the dictionary

#print(details['id']) #KeyError -->as the key is not present

#print(details.get('ids'))

#print(details.get('id')) #as the key is not present it returns None

#Inserting multiple keys into the dictionary
data = {'email_ids':['nkt@gmail.com','dpt@icloud.com',
                     'vny@yahoo.com','tej@gmail.com'],
        'linkedin_ids':['nkt_123','dpt_234',
                        'vinay345','tej13']}
details.update(data)
#print(details.keys())

#Delete data from the dictionary
#pop(key) -->removes specified data from the dict
'''
print(details.pop('marks'))
print(details.keys())
print(details.popitem()) #removes and returns key value pair from last
print(details.clear())
print(details)

#del details[['marks','ids']] #not possible
del details['marks'],details['ids'] #to delete multiple pairs ata time
print(details.keys())
'''
#print(details.keys())

#setdefault() -->inserts key  into the dictionary if its not present

details.setdefault('status')
#print(details.keys())
#print(details)
details['status'] = ['Placed','Active','OnHold']

#print(details.setdefault('ids')) #aswe already have ids in dictionayry
#its just prints the values
print(details.keys())

#fromkeys() -->create a new dictionary from an iterable
'''
duration = [35,30,65,30]
data = dict.fromkeys(duration)
#data = dict.fromkeys(duration,['Flask','SQL','FastAPI']) #we get 3 keys only as 30 is present
#2 times
print(data)
data[35] = 'Python'
data[30] = 'MYSQL'
print(data)

name = dict.fromkeys('Codegnan')
print(name)
'''
#Nested Dictionaries -->A dictionary inside another dictionary

Students = {'s1':{'Name':'Sai',
                   'ID':'CGVI0240',
                   'batch':'PFS-VSP-007'},
             's2':{'Name':'Raj',
                    'ID':'CGVI0245',
                    'batch':'PFS-VSP-008'}}
'''print(Students)
print(len(Students))
print(Students.keys())
print(type(Students['s1'])) #returns dictionary
print(Students['s1'].keys())

print(Students['s1']['ID'])

#For student s1 update subjects,marks (two new keys to be created)
#Students['s1'].update({'subjects':['Python','Java'],'marks':[95,86]})
#print(Students['s1'])

Students['s1']['subjects'] = ['Python','Aptitude','SS']
Students['s1']['marks'] = [20,20,25]
print(Students['s1'])

#Task: Create your Student Profile with fields as ID number
#Email id,Mobile Number,Parent Whatsappnumber,subjects,
#batch no,daily exam marks,weekly exam marks,batch rank,
#githuburl,linkedinid

Make sure you apply methods also to it(Lists/Sets)

#FrozenSets --> Frozensets are Unordered,it also an Immutable
#collection

data = frozenset()
#print(data)
#print(type(data))
data = frozenset(['Saketh',32,'Codegnan','Vizag'])
print(data)
print(type(data))
print(len(data))
print(data.union(data)) #within itself but no change
print(data.union({'Python','Aptitude'})) #we are passing a set to it
del data   #we can completely remove the collection
#print(data)
'''
# Student Profile

student = {
    'id_number': 'PFS-VSP-007-101',
    'email': 'nikhil@gmail.com',
    'mobile_number': '9876543210',
    'parent_whatsapp_number': '9123456780',

    # List
    'subjects': ['Python', 'MySQL', 'HTML', 'CSS', 'JavaScript'],

    'batch_no': 'PFS-VSP-007',

    # List of daily exam marks
    'daily_exam_marks': [8, 7, 9, 6, 10],

    # List of weekly exam marks
    'weekly_exam_marks': [78, 85, 82, 91],

    'batch_rank': 5,

    'github_url': 'github.com/nikhil',
    'linkedin_id': 'linkedin.com/in/nikhil',

    # Set
    'skills': {'Python', 'MySQL', 'HTML'}
}

print(student)


# SUBJECTS - LIST METHODS
print(student['subjects'])

# append() --> Add one subject
student['subjects'].append('React')
print(student['subjects'])

# extend() --> Add multiple subjects
student['subjects'].extend(['Flask', 'Git'])
print(student['subjects'])

# insert() --> Insert at a particular position
student['subjects'].insert(1, 'SQL')
print(student['subjects'])

# remove() --> Remove a subject
student['subjects'].remove('CSS')
print(student['subjects'])

# pop() --> Remove last subject
removed_subject = student['subjects'].pop()
print('Removed subject:', removed_subject)
print(student['subjects'])

# index() --> Find position of subject
print(student['subjects'].index('Python'))

# count() --> Count occurrences
student['subjects'].append('Python')
print(student['subjects'].count('Python'))

# sort() --> Sort subjects
student['subjects'].sort()
print(student['subjects'])

# reverse() --> Reverse subjects
student['subjects'].reverse()
print(student['subjects'])

# DAILY EXAM MARKS - LIST METHODS

print(student['daily_exam_marks'])

# Add a new mark
student['daily_exam_marks'].append(9)

# Add multiple marks
student['daily_exam_marks'].extend([8, 10])

print(student['daily_exam_marks'])

# Insert mark
student['daily_exam_marks'].insert(2, 10)
print(student['daily_exam_marks'])

# Count 10 marks
print('Number of 10 marks:',
      student['daily_exam_marks'].count(10))

# Find position
print('Position of 9:',
      student['daily_exam_marks'].index(9))

# Sort marks
student['daily_exam_marks'].sort()
print(student['daily_exam_marks'])

# Reverse marks
student['daily_exam_marks'].reverse()
print(student['daily_exam_marks'])


# WEEKLY EXAM MARKS

print(student['weekly_exam_marks'])

student['weekly_exam_marks'].append(88)
student['weekly_exam_marks'].extend([76, 95])

print(student['weekly_exam_marks'])

# Highest mark
print('Highest weekly mark:',
      max(student['weekly_exam_marks']))

# Lowest mark
print('Lowest weekly mark:',
      min(student['weekly_exam_marks']))

# Total marks
print('Total weekly marks:',
      sum(student['weekly_exam_marks']))

# Number of exams
print('Number of exams:',
      len(student['weekly_exam_marks']))


# SET METHODS - SKILLS

print(student['skills'])

# add() --> Add one element
student['skills'].add('JavaScript')
print(student['skills'])

# update() --> Add multiple elements
student['skills'].update(['React', 'Flask', 'Git'])
print(student['skills'])

# discard() --> Remove element
student['skills'].discard('HTML')
print(student['skills'])

# add duplicate
student['skills'].add('Python')
print(student['skills'])
# Duplicate will not be added

# SET OPERATIONS

python_skills = {'Python', 'Django', 'Flask', 'Git'}

student_skills = student['skills']

# Union
print('All Skills:',
      student_skills | python_skills)

# Intersection
print('Common Skills:',
      student_skills & python_skills)

# Difference
print('Student-only Skills:',
      student_skills - python_skills)

# LIST COPY

marks_copy = student['daily_exam_marks'].copy()

marks_copy.append(100)

print('Original marks:',
      student['daily_exam_marks'])

print('Copied marks:',
      marks_copy)


# CLEAR A COPY

temp_subjects = student['subjects'].copy()

temp_subjects.clear()

print('Cleared copy:', temp_subjects)
print('Original subjects:', student['subjects'])


#FINAL STUDENT PROFILE
print(student)

for key, value in student.items():
    print(key, ':', value)
