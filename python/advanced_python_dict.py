
import csv

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
        if 'PhD' in deg.replace('.','') or deg.isdigit(): 
            # make uniform all Ph.D degrees. One typo '0' case
            degList[index] = 'Ph.D'
        elif 'ScD' in deg.replace('.',''):
            degList[index] = 'Sc.D'
        elif 'MS' in deg.replace('.',''):
            degList[index] = 'MS'
    
    return ' '.join(degList)
        
    
    
# helper function 2

def title_formatter(title):
    """
    title: a string representing title(s) (unformatted)
    return: a string representing title(s) (formatted)
    """
    if 'Assistant' in title:
        return 'Assistant Professor'
    elif 'Associate' in title:
        return 'Associate Professor'
    elif 'Professor' in title:
        return 'Professor'
    else:
        return title

###################
###################
    

# Q6

# reading in file

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
    

###################

#Q7

# creating a dictionary with full name (excluding middle name) as keys
faculty_dict2 = {}

for faculty in lol[1:]:
    lastName = faculty[0].split(' ')[-1]
    firstName = faculty[0].split(' ')[0]
    degree = degree_formatter(faculty[1])
    title = title_formatter(faculty[2])
    email = faculty[3]
    
    faculty_dict2[(firstName, lastName)] = [degree, title, email]

# print the first three key value pairs        
for key in list(faculty_dict2.keys())[0:3]:
    print(str(key) + ': ' + str(faculty_dict2[key]))


###################

#Q8
# print out key value pairs in alphabetical order of last name 
print(faculty_dict2)

 
