
import csv
import re

###################
###################
# helper function 1

def degree_formatter(title):
    """
    title: a string representi:ng degree(s) (unformatted)
    return: a string representing degree(s) (formatted)
    """
    degList = title.strip().split(' ') # split into list
    degListIterable = degList[:]
    
    for index, deg in list(enumerate(degListIterable)):
        print(list(enumerate(degListIterable)))
        if re.match(r'(Ph.*|\d)', deg, re.I):
            degList[index] = 'Ph.D'
        elif re.match(r'Sc.*', deg, re.I):
            degList[index] = 'Sc.D'
        elif re.match(r'M.?S.*', deg, re.I):
            degList[index] = 'MS'
    
    print(degList)
    return ' '.join(degList)
        
    
    
# helper function 2

def title_formatter(title):
    """
    title: a string representing title(s) (unformatted)
    return: a string representing title(s) (formatted)
    """
    if re.match(r'Assistant.*Prof.*', title, re.I):
        return 'Assistant Professor'
    elif re.match(r'Associate.*Prof.*', title, re.I):
        return 'Associate Professor'
    elif re.match(r'.*Prof.*', title, re.I):
        return 'Professor'
    else:
        return title

###################
###################
    

# Q6

#reading in file

lol = []
with open('faculty.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile)
    for faculty in readCSV:
        lol.append(faculty)

    
# creating dictionary based off of last names as keys
faculty_dict = {}

for faculty in lol[1:]:
    lastName = faculty[0].split(' ')[-1]
    degree = degree_formatter(faculty[1])
    title = title_formatter(faculty[2])
    email = faculty[3]
    
    if lastName in faculty_dict.keys():
        faculty_dict[lastName].append([degree, title, email])
    else:
        faculty_dict[lastName] = [[degree, title, email]]

# print the first three key value pairs        
for key in list(faculty_dict.keys())[0:3]:
    print(str(key) + ': ' + str(faculty_dict[key]))
    

##################

#Q7

# creating a dictionary with full name (excluding middle name) as keys
faculty_dict2 = {}

for faculty in lol[1:]:
    name = faculty[0].split(' ')
    lastName = name[-1]
    firstName = name[0]
    if len(name) > 2:
        nameFormat = [firstName, name[1], lastName]
    else:
        nameFormat = [firstName, lastName]
    
    degree = degree_formatter(faculty[1])
    title = title_formatter(faculty[2])
    email = faculty[3]

    faculty_dict2[tuple(nameFormat)] = [degree, title, email]

# print the first three key value pairs        
for key in list(faculty_dict2.keys())[0:3]:
    print(str(key) + ': ' + str(faculty_dict2[key]))


####################

#Q8
# print out key value pairs in alphabetical order of last name 
print(faculty_dict2)
