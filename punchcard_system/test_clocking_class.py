from punchcard import Clocking
# sleep is only for testing and is not needed
from time import sleep

# using total_time instead of total_hours because total_time is easier to test
fake_database = {1: {"name":"hannah", "total_time": 12, "start_time": None, "end_time": None},
                 2: {"name":"aung", "total_time": 14, "start_time": None, "end_time": None},
                 3: {"name":"elsa", "total_time": 10, "start_time": None, "end_time": None},
                 4: {"name":"noah", "total_time": 15, "start_time": None, "end_time": None},
                 }

person_id = 2
person1 = Clocking(person_id, fake_database)
person1.punch_in()
sleep(3)
person1.punch_out()
print(f"{fake_database[person_id]["name"]} has worked a total of: {fake_database[person_id]["total_time"]} seconds")