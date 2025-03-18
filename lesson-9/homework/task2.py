import csv
# 1st task - creating a csv file with the intended structure in the following code
csv_fields = ['Name', 'Subject', 'Grade']

csv_list = [
    ["Alice", "Math", 85],
    ['Bob','Science',78],
    ['Carol','Math',92],
    ['Dave','History',74]
]

with open('grades.csv', 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=',')
    csvwriter.writerow(csv_fields)
    for line in csv_list:
        csvwriter.writerow(line)

# 2nd task - read and store data:
csvlist = list() # for list of dictionaries
with open('grades.csv', 'r') as csvfile:
    csvdict = csv.DictReader(csvfile)
    for row in csvdict:
        csvlist.append(row)

# Calculate the average grade:
grades = list()
for row in csvlist:
    grades.append(int(row['Grade'])) # from str to int
avg_grade = sum(grades)/len(grades) #avg

# Write a new CSV file named average_grades.csv:
avg_grades = list()
for row in csvlist:
    avg_grades.append({row['Subject']:row['Grade']})
subject_data = {}
for everydict in avg_grades:
    for subject, grade in everydict.items():
        if subject in subject_data:
            subject_data[subject][0] += int(grade)
            subject_data[subject][1] += 1
        else:
            subject_data[subject] = [int(grade), 1]

with open("average_grades.csv", 'w', newline='') as new_file:
    first_row = ["Subject", "Average Grade"]
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(first_row)
    for key, value in subject_data.items():
        to_write = [key , str(int(value[0]/value[1]))]
        csv_writer.writerow(to_write)