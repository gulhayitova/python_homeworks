import pandas as pd

titanic = pd.read_excel('titanic.xlsx')
def status(survived):
    return survived[survived['Survived'] == 1]
survived = titanic.pipe(status)

def fill_age(df: pd.DataFrame):
    df['Age'].isnull = df['Age'].mean()
    return df
age_df = titanic.pipe(fill_age)

def fare_age(df: pd.DataFrame, newColumn: str):
    df[newColumn] = df['Fare']/df['Age']
    return df
fare_by_age = titanic.pipe(fare_age, "Fare_Per_age")

flights = pd.read_parquet('part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet')
def big_delay(df: pd.DataFrame):
    df['DepDelay'] = pd.to_numeric(df['DepDelay'], errors='coerce')
    return df[df['DepDelay'] > 30]
delayed = flights.pipe(big_delay)

def delay_hour(df: pd.DataFrame, newcolumn: str):
    df['ArrDelayMinutes'] = pd.to_numeric(df['ArrDelayMinutes'], errors='coerce')
    df['DepDelayMinutes'] = pd.to_numeric(df['DepDelayMinutes'], errors='coerce')
    df['CRSElapsedTime'] = pd.to_numeric(df['CRSElapsedTime'], errors='coerce')
    df[newcolumn] = (df['ArrDelayMinutes'] + df['DepDelayMinutes'])/df['CRSElapsedTime']
    return df
delay_info = flights.pipe(delay_hour, 'Delay_Per_Hour')