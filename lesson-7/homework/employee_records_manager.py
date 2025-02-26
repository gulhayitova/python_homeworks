# ovqatga qaynadimi?
# class for individual employees
import os

class Employee():
    def __init__(self, employee_id, name, position, salary):
        self.e_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def to_string(self):
        return f"{self.e_id}, {self.name}, {self.position}, {self.salary}"
    
    @staticmethod
    def from_string(employee):
        details = employee.split(', ')
        return Employee(details[0], details[1], details[2], details[3])
    
global file_name 
file_name = "employees.txt"
# class for managing the employees
class EmployeeManager():
    import os

    def __init__(self):
        if os.path.exists(file_name):
            with open(file_name, 'w') as file:
                pass


    def add_employee(employee):
        with open(file_name, 'a') as file:
            file.write('\n' + employee.to_string()) # txt is added new details

    def view():
        with open(file_name, 'r') as file:
            emps = list()
            for line in file:
                emps.append(Employee.from_string(line))
            return emps
        
    def search(emp_id):
        with open(file_name, 'r') as file:
            for line in file:
                line0 = line.split(', ')
                if line0[0] == str(emp_id):
                    return line
            return None
        
    def modify(emp_id, new_txt):
        with open(file_name, 'r') as file:
            lines = list()
            for line in file:
                lines.append(line)
        with open(file_name, 'w') as file:
            new_list = new_txt.split(', ')
            for line in lines:
                lineList = line.split(', ')
                if lineList[0] == new_list[0]:
                    file.write(new_txt)
                else:
                    file.write(line)

    def delete_info(emp_id):
        with open(file_name, 'r') as file:
            lines = list()
            for line in file:
                lines.append(line)
        with open(file_name, 'w') as file:
            for line in lines:
                lineList = line.split(', ')
                if lineList[0] == emp_id:
                    pass
                else:
                    file.write(line)


response = 0 # storing the user's answer as 'int'
print("1 - Adding a new data\n2 - View all data\n3 - Search\n4 - Overwrite the data\n5 - Delete a data\n6 - Exit\n") # keycode
while True: # endlessly continue until the user wants to stop
    response = input("The key code: ")
    if str(response).isnumeric():
        response = int(response)
    else:
        print("Incorrect input. Try again.")
        continue
    
    match response: # activating different functions according to the user's wish
        case 1:
            employee_id = input("Enter ID: ")
            e_name = input("Enter Name: ")
            e_job = input("Enter Position: ")
            e_salary = input("Enter Salary: ")
            EmployeeManager.add_employee(Employee(employee_id, e_name, e_job, e_salary))
            print("Employee added successfully!")

        case 2:
            print("Employee records: \n")
            for i in EmployeeManager.view():
                print(f"{i.e_id}, {i.name}, {i.position}, {i.salary}")
        case 3:
            searchID = input("Enter Employee ID to search: ")
            EmployeeManager.search(searchID)
        case 4:
            employee_id = input("Enter ID: ")
            e_name = input("Enter Name:")
            e_job = input("Enter Position: ")
            e_salary = input("Enter Salary: ")
            EmployeeManager.modify(employee_id, f"{employee_id}, {e_name}, {e_job}, {e_salary}\n")
        case 5:
            deleteID = input("Enter Employee ID to delete: ")
            EmployeeManager.delete_info(deleteID)
        case 6:
            break
        case _:
            print(end = '')

