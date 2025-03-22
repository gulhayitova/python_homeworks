import sqlite3

columns = """CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT)"""
data = (
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Filtgerald', 1925, 'Classic')
)
ratings = (
    (4.8, 'To Kill a Mockingbird'),
    (4.7, '1984'),
    (4.5, 'The Great Gatsby')
)

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Books") # creating a new table every run so it doesn't give an error
    cursor.execute(columns) #1) Adding columns
    cursor.executemany("INSERT INTO Books Values(?, ?, ?, ?);", data) #2) populate the table
    cursor.execute("UPDATE Books SET Year_Published=1950 WHERE Title='1984'") #3) update year published
    cursor.execute("DELETE FROM Books WHERE Year_Published<1950") #5) delete all books published before 1950
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating INT") #6) adding a new column and updating it
    cursor.executemany("UPDATE Books SET Rating=? WHERE Title=?", ratings) 
    #cursor.execute("SELECT Title, Author FROM Books WHERE Genre='Dystopian'") #4) retrieve title and author of books with genre dystopian
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC") #7) retrieve sorting by year in ascending order
for each_row in cursor:
    print(each_row)