global file_name
file_name = 'to-do.txt'
global tasks
tasks = []

class Managing:
    import os
    def __init__(self):
        if os.path.exists(file_name):
            with open(file_name, 'w') as file:
                pass
    
    def load():
        with open(file_name, 'r') as file:
            for line in file:
                tasks.append(line)
        
    def add_task(newtask):
        tasks.append('\n' + newtask)

    def view():
        return ''.join(tasks)
        
    def update(updated):
        for line in tasks:
            line1 = line.split(', ')
            updated1 = updated.split(', ')
            if line1[0] == updated1[0]:
                index = tasks.index(line)
                tasks[index] = updated
            else:
                pass
            
    def delete(taskID):
            for line in tasks:
                line1 = line.split(', ')
                count = 0
                if line1[0] == taskID:
                    del tasks[count]
                else:
                    count += 1

    def filter_task(status):
            lines = list()
            for line in tasks:
                line1 = line.split(', ')
                if line1[-1] == status:
                    lines.append(line)
            return ''.join(lines)
        
    def save():
        with open(file_name, 'w') as file:
            for task in tasks:
                if task != tasks[-1]:
                    file.write(f"{task}")
                else:
                    file.write(task)

response = 0 # storing the user's answer as 'int'
print("Welcome to the To-Do Application!")
print("1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task\n5. Filter tasks by status\n6. Save tasks\n7. Load tasks\n8. Exit") # keycode
while True: # endlessly continue until the user wants to stop
    response = input("Enter your choice: ")
    if str(response).isnumeric():
        response = int(response)
    else:
        print("Incorrect input. Try again.")
        continue
    
    match response: # activating different functions according to the user's wish
        case 1:
#             Enter Task ID: 101
# Enter Title: Finish Homework
# Enter Description: Complete math and science homework.
# Enter Due Date (YYYY-MM-DD): 2024-12-31
# Enter Status (Pending/In Progress/Completed): Pending
# Task added successfully!
            task = str()
            task += input("Enter Task ID: ") + ', '
            task += input("Enter Title: ") + ', '
            task += input("Enter Description: ") + ', '
            task += input("Enter Due Date: ") + ', '
            task += input("Enter Status (Pending/In Progress/Completed): ")
            Managing.add_task(task)
            print("Task added successfully!")            
        case 2:
            print(Managing.view())
        case 3:
            task = str()
            task += input("Enter Task ID: ") + ', '
            task += input("Enter Title: ") + ', '
            task += input("Enter Description: ") + ', '
            task += input("Enter Due Date: ") + ', '
            task += input("Enter Status (Pending/In Progress/Completed): ")
            Managing.update(task)
            print("Task updated successfully!")   
        case 4:
            taskid = input("Enter Task ID to delete: ")
            Managing.delete(taskid)
        case 5:
            status = input("Enter status to filter by: ")
            print(Managing.filter_task(status))
        case 6:
            Managing.save()
        case 7:
            Managing.load()
        case 8:
            break
            
        
