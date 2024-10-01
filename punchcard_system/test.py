import sqlite3
import datetime

path = r"C:\Users\aung512x01\Desktop\Aung Programs\Punchcard_System\test_database\cosmetology_records.db"

connection = sqlite3.connect(path)
cursor = connection.cursor()

now = datetime.datetime.now()
cursor.execute(f"UPDATE students SET working = 1 WHERE id = 1")
connection.commit()

working = cursor.execute(f"SELECT working FROM students WHERE id = 1")



print((working.fetchone())[0])

