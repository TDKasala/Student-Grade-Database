
import sqlite3

# Connect to the SQLite database and getting a cursor object

db = sqlite3.connect('python_programming.db')
cursor = db.cursor()


cursor.execute('''
    CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT,
                                grade INTEGER)
''')
db.commit()

cursor = db.cursor()

name1= 'Carl Davis'
grade1 = 61

name2 = 'Dennis Fredrickson'
grade2 = 88

name3 = 'Jane Richards'
grade3 = 78

name4 = 'Peyton Sawyer'
grade4 = 45

name5 = 'Lucas Brooke'
grade5 = 99

# Insert student 1
cursor.execute('''INSERT INTO students(name, grade)
                  VALUES(?,?)''', (name1, grade1))
print('First user inserted')

# Insert student 2
cursor.execute('''INSERT INTO students(name, grade)
                  VALUES(?,?)''', (name2, grade2))
print('Second user inserted')

# Insert student 3
cursor.execute('''INSERT INTO students(name, grade)
                  VALUES(?,?)''', (name3, grade3))
print('Third user inserted')

# Insert student 4
cursor.execute('''INSERT INTO students(name, grade)
                  VALUES(?,?)''', (name4, grade4))
print('Fourth user inserted')

# Insert student 5
cursor.execute('''INSERT INTO students(name, grade)
                  VALUES(?,?)''', (name5, grade5))
print('Fith user inserted')

db.commit()

# Retrieving data

id = 1
cursor.execute('''SELECT name, grade FROM students WHERE id=?''', (id,))
student = cursor.fetchall()
print(student)

id = 2
cursor.execute('''SELECT name, grade FROM students WHERE id=?''', (id,))
student = cursor.fetchall()
print(student)

# Changing data

grade = 65
id = 1
cursor.execute('''UPDATE students SET grade = ? WHERE id = ?''', (grade, id))
print('Student data updated!')


 #Deleting a row
id = 1
cursor.execute('''DELETE FROM students WHERE id = ? ''', (id,))
print('Student %d deleted' %id)

#Changing grades
id = 2
new_grade = 80
cursor.execute('''UPDATE students SET grade = ? WHERE id = ?''', (new_grade, id))
print('Student data changed!')

db.commit()
db.close()
print('Connection to database closed')
