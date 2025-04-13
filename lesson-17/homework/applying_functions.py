import pandas as pd

def age_class(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

passengers = pd.read_excel('titanic.xlsx')
passengers['AgeGroup'] = passengers['Age'].apply(age_class)

employees = pd.read_csv('employee.csv')
def normalize(salary):
    return (salary - salary.min())/(salary.max() - salary.min())
normal = employees.groupby('DEPARTMENT')['BASE_SALARY'].apply(normalize)


def duration(time):
    if time < 60:
        return 'Short'
    elif time > 60 and time < 120:
        return 'Medium'
    else:
        return 'Long'
    
movies = pd.read_csv('movie.csv')
durations = movies['duration'].apply(duration)