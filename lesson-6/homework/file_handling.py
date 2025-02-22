def add_employee():
    op = open('employees.txt', 'a') #the file opened
    employee = list()
    employee.append(input("Please enter the employee id: ")) #asking the user to input the details and saving in a list
    employee.append(input("Enter their name: "))
    employee.append(input("The position: "))
    employee.append(input("Now enter their salary: "))
    employee = ', '.join(employee) + '.\n' #employee saved as str containing all items in the list and separated by a space
    op.write(employee) # txt is added new details
    op.close() # file closed

def view_all():
    with open('employees.txt', 'r') as op: #opening the file 
        for x in op.readlines(): #printing every line
            print(x, end = '')

def search_out():
    emp_id = input("The employee's ID: ")
    with open('employees.txt', 'r') as op: # reading the file
        for x in op:
            if emp_id in x.split()[0]: # checking the id of every line in op to match the one being searched
                print("\nEmployee is found.\n" + x, end = '')
                return # ending the process so the final message isn't shown
    print("\nEmployee not found.")

def overwrite(): # modifying the file
    emp_id = input("The ID of the employee to modify their information: ") 
    new_data = int(input("Which information do you want to change?\n1 - Name\n2 - Position\n3 - Salary\n")) # key code to understand what information needs to be changed
    emp_new = input("Enter the employee's information here: ")
    lines = list() # list to save the content in the file
    with open('employees.txt', 'r') as op:
        for x in range(2):
            lines.append(op.readline()) # adding every line in file
    with open('employees.txt', 'w') as op:
        ispresent = False # boolean value to check if the line is the one to be changed or not
        for line in lines:
            line = line.split(', ')
            if emp_id == line[0]: # if id matches
                match new_data: # modifying single info of the employee
                    case 1: # name
                        line[1] = emp_new
                    case 2: # position
                        line[2] = emp_new
                    case 3: # salary
                        line[3] = emp_new
                line = ', '.join(line) # making the line 'str' object again
                op.write(line + '\n') # modified
                ispresent = True # letting the user know it was found and modified
            else: 
                line = ', '.join(line) # 'list' -> 'str' object
                op.write(line + '\n') # if it's not the id we're looking at, we'll directly write it back
        if ispresent: print("Found and modified.")
        else:
            print("The ID not found.")

def del_data():
    del_id = input("The ID of the employee to be deleted from the server: ")
    with open('employees.txt', 'r') as op:
        lines = op.readlines() # copying the data to modify the file
    with open('employees.txt', 'w') as op:
        for line in lines: 
            if line.split(', ')[0] == del_id: # checking the id
                pass # not copying the info back to delete it
            else:
                op.write(line + '\n') # copying it back

response = 0 # storing the user's answer as 'int'
print("1 - Adding a new data\n2 - View all data\n3 - Search\n4 - Overwrite the data\n5 - Delete a data\n6 - Exit\n") # keycode
while response != 'exit': # endlessly continue until the user wants to stop
    response = input("The key code: ")
    if str(response).isnumeric():
        response = int(response)
    else:
        print("Incorrect input. Try again.")
        continue
    
    match response: # activating different functions according to the user's wish
        case 1:
            add_employee()
        case 2:
            view_all()
        case 3:
            search_out()
        case 4:
            overwrite()
        case 5:
            del_data()
        case 6:
            response = 'exit' # modifying the 'response' to stop the program
        case _:
            print(end = '')
