import sqlite3

table_query = """CREATE TABLE Roster(
Name TEXT, 
Species TEXT,
Age INT
);
"""
values = (
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
)
enter_rank = (
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major','Kira Nerys')
    )
with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster") # creating a new table every run so it doesn't give an error
    cursor.execute(table_query) #1) Adding columns
    cursor.executemany("INSERT INTO Roster Values(?, ?, ?);", values) #2) insert data
    cursor.execute("UPDATE Roster SET Name='Ezri Dax' WHERE Name='Jadzia Dax'") #3) update the name
    # cursor.execute("DELETE FROM Roster WHERE Age>100") #5) remove chars aged over 100; commented not to interfere other parts(optional)
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT") #6) add a new column and update it
    cursor.executemany("UPDATE Roster SET Rank=? WHERE Name=?", enter_rank)
#     cursor.execute("SELECT Name, Age FROM Roster WHERE Species='Bajoran'") #4) retrieve name, age of bajoran species chars query data commented to not interfere(optional)
# for row in cursor.fetchall(): # 4 display data selected
#     print(row)
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC") #7) Sort by age and display
for row in cursor.fetchall(): # 4 display data selected
    print(row)

