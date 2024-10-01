from datetime import datetime
import sqlite3

path = r'C:\Users\aung512x01\Desktop\Aung Programs\Punchcard_System\test_database\cosmetology_records.db'
class Clocking:
    connection = sqlite3.connect(path)

    def __init__(self, person_id:int):
        self.id = person_id
        self.working = self.connection.execute(f"SELECT working FROM students WHERE id == {self.id}")

    def punch_in(self):
        if self.working is 1:
            # no punching in if you're already working
            return
        self.working.execute(f'UPDATE students ')