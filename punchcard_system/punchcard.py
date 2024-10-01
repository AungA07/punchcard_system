from datetime import datetime
import sqlite3
# testing purposes
from time import sleep

path = r"C:\programing\anthis_code\2024-2025\punchcard_system\test_database\cosmetology_records.db"
class Clocking:
    connection = sqlite3.Connection(path)

    def __init__(self, id:int) -> None:
        self.id = id
        self.working = self.connection.execute(f"SELECT working FROM students WHERE id = {self.id}")

    def punch_in(self):
        if self.working == 1:
            # no punching in again if you're working (1 means true)
            return
        # change working status in db
        self.connection.execute(f"UPDATE students SET working = 1 WHERE id = {self.id}")
        start_time = str(datetime.now())
        # add/update start time in database
        self.connection.execute(f"UPDATE students SET start_time = '{start_time}' WHERE id = {self.id}")

    def punch_out(self):
        if self.working == 0:
            return
        self.connection.execute(f"UPDATE students SET working = 0 WHERE id = {self.id}")
        end_time = str(datetime.now())
        self.connection.execute(f"UPDATE students SET end_time = '{end_time}' WHERE id = {self.id}")
        time_worked = self.connection.execute() # get end_time value -> convert back to datetime obj and then subtract start_time (also change to datetime)
        total_time = self.connection.execute() # get total time value
        total_time += time_worked
        self.connection.execute() # update total time

time = str(datetime.now())
print(time)
# converts string back into datetime object
time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
sleep(3)
time_now = datetime.now()
print(time_now)
time_difference = time_now - time
print(time_difference.total_seconds())