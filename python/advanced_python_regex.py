
import csv

#Q1
# trying to figure out how many different degrees there are
# reading in file

lol = []
with open('faculty.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile)
    for faculty in readCSV:
        lol.append(faculty)

# extracting the different degrees
degrees = []
for faculty in lol[1:]:# first line is header
    degCleaned = faculty[1].replace('.','') # remove all dots
    degCleaned = degCleaned.strip() # remove leading and ending spaces
    degCleaned = degCleaned.split(' ') # put all of one person's degrees in a list
    degrees.extend(degCleaned)

uniqueDegrees = set(degrees)
print(uniqueDegrees)
uniqueDegrees.remove('0') 
#'0' is a typo. The corresponding individual has at least a PhD since he's prof.
print(uniqueDegrees) # revised list
numOfDegrees = len(uniqueDegrees)
print(numOfDegrees)



###################


#Q2
# trying to figure out how many different titles there are and respective frequencies

titles = {}
for faculty in lol[1:]:
    if 'Assistant' in faculty[2]:
        if 'Assistant Professor' in titles.keys():
            titles['Assistant Professor'] += 1
        else:
            titles['Assistant Professor'] = 1
    
    elif 'Associate' in faculty[2]:
        if 'Associate Professor' in titles.keys():
            titles['Associate Professor'] += 1
        else:
            titles['Associate Professor'] = 1
    
    elif 'Professor' in faculty[2]:
        if 'Professor' in titles.keys():
            titles['Professor'] += 1
        else:
            titles['Professor'] = 1
    
    else:
        if titles[faculty[2]] in titles.keys():
            titles[faculty[2]] += 1
        else:
            titles[faculty[2]] = 1
        
    
print(titles.keys())
print((titles.values()))
  

###################
 

#Q3
# trying to print out the list of email addresses

emails = []
for faculty in lol[1:]:
    emails.append(faculty[3].strip())
    
print(emails)
print(len(emails))

###################
 

#Q4
# trying to print out the list of unique email address domains

domains = []
for faculty in lol[1:]:
    atIndex = faculty[3].index('@')
    domain = faculty[3][atIndex + 1:].strip() # domain starts from after '@'
    domains.append(domain)
    
uniqueDomains = set(domains)
print(uniqueDomains)
print(len(uniqueDomains))
