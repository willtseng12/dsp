
import csv

#Q5

# reading in file

lol = []
with open('faculty.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile)
    for faculty in readCSV:
        lol.append(faculty)
        
        
emails = []
for faculty in lol[1:]:
    emails.append(faculty[3].strip())
    
# writing in file

with open('email.csv', 'w') as file:
    for email in emails:
        file.write(email+'\n')