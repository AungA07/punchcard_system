from datetime import datetime

class Clocking:
    """Using database as a test. the database argument would be replaced with however we access the actual database"""
    working = False

    def __init__(self, id:int, database:dict) -> None:
        # id could also be the name or whatever would be used to identify the person
        self.id = database[id]

    def punch_in(self):
        if self.working:
            # no punching in again if you're working
            return
        self.working = True
        self.id["start_time"] = datetime.now()
    
    def punch_out(self):
        if not self.working:
            # no punching out if you're not working
            return
        self.working = False
        self.id["end_time"] = datetime.now()

        # this value would be shown to the user
        time_worked = self.id["end_time"] - self.id["start_time"]
        # add to running total
        self.id["total_time"] += time_worked.total_seconds()
        print(f"seconds worked: {time_worked.total_seconds()}")
