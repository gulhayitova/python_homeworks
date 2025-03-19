import json

# 'tasks.json' file created as instructed
with open("tasks.json", 'r') as file:
    data = json.load(file)

# changing the keys
newdata = list()
def change_keys(diction, keymap):
    return {keymap.get(k, k):v for k, v in diction.items()}
key_map = {
    'id':"ID",
    'task':"Task Name",
    'completed':'Completed Status',
    'priority':'Priority'
}
for every in data:
    newdata.append(change_keys(every, key_map))

# modifying the tasks. Made a comment to not interfere the actual data.
# newdata[1]['Completed Status'] = True

# Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
with open("tasks.json", 'w') as file:
    json.dump(newdata, file, indent = 2)

# data should be loaded here. We don't because we already have the same data in newdata variable stored
print("The number of tasks:", len(newdata))
completed = 0
priority = {'sum': 0, 'count': 0}
for task in newdata:
    # to count the number of completed tasks
    if task["Completed Status"] == True:
        completed += 1
    # to calculate the average priority
    priority['sum'] += task['Priority']
    priority['count'] += 1

print("The number of completed tasks:", completed)
print("The number of tasks yet to be done:", len(newdata) - completed)
print("The average priority per task:", priority['sum']/priority['count'])

# 3. Convert from JSON to a CSV file
import csv
keys = newdata[0].keys()
with open("tasks.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(keys)
    for task in newdata:
        csvwriter.writerow(task.values())