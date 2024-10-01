from datetime import datetime
import sqlite3
# testing purposes
from time import sleep

class Clocking:
    def __init__(self, person_id:int, database_path:str) -> None:
        self.id = person_id
        self.path = database_path

        # connecting to the database
        connection = self.connect()
        cursor = connection.cursor()

        # get working status from database
        working = cursor.execute(f"SELECT working FROM students WHERE id = {self.id}")
        self.working = (working.fetchone())[0]

    def connect(self):
        connection = sqlite3.Connection(self.path)
        return connection

    def punch_in(self):
        if self.working == 1:
            # no punching in again if you're working
            return

        # start connection and get cursor
        connection = self.connect()
        cursor = connection.cursor()

        # change working status in db
        cursor.execute(f"UPDATE students SET working = 1 WHERE id = {self.id}")
        start_time = datetime.now()

        # add/update start time in database
        cursor.execute(f"UPDATE students SET start_time = '{start_time}' WHERE id = {self.id}")

        # saving all the changes to database
        connection.commit()
        cursor.close()

    def punch_out(self):
        if self.working == 0:
            return

        # start connection and get cursor
        connection = self.connect()
        cursor = connection.cursor()

        # update working status
        cursor.execute(f"UPDATE students SET working = 0 WHERE id = {self.id}")

        # update end time
        end_time = datetime.now()
        #self.cursor.execute(f"UPDATE students SET end_time = '{end_time}' WHERE id = {self.id}")

        # retrieving start_time
        cursor.execute(f"SELECT start_time FROM students WHERE id = {self.id}")
        start_time = (cursor.fetchone())[0]

        # convert str to datetime object
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")

        # calculate time worked
        time_worked = end_time - start_time
        time_worked = int(time_worked.total_seconds())

        # retrieving total_time
        cursor.execute(f"SELECT total_time_in_seconds FROM students WHERE id = {self.id}")
        total_time = (cursor.fetchone())[0]

        # add to running total
        total_time += time_worked
        cursor.execute(f"UPDATE students SET total_time_in_seconds = {total_time} WHERE id = {self.id}")
        connection.commit()
        cursor.close()


path = r"C:\Users\aung512x01\Desktop\Aung Programs\Punchcard_System\test_database\cosmetology_records.db"
person_id = 2

conn = sqlite3.connect(path)
cursor = conn.cursor()

clocking = Clocking(person_id, path)

clocking.punch_in()

# change total_hours to total_time_in_seconds
cursor.execute(f"SELECT total_time_in_seconds FROM students WHERE id = {person_id}")
print(cursor.fetchone()[0])

sleep(3)

clocking.punch_out()

cursor.execute(f"SELECT total_time_in_seconds FROM students WHERE id = {person_id}")
print(cursor.fetchone()[0])
