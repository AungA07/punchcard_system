from datetime import datetime
# sleep is only for testing and is not needed
from time import sleep

class Clocking:
    # start_time and end_time would be tied to some sort of database
    start_time = None
    end_time = None
    working = False

    def punch_in(self):
        if self.working:
            # no punching in again if you're working
            return
        self.working = True
        self.start_time = datetime.now()
    
    def punch_out(self):
        if not self.working:
            # no punching out if you're not working
            return
        self.working = False
        self.end_time = datetime.now()
        # this value would be shown to the user and then added to the total hours
        time_worked = self.end_time - self.start_time
        # usually would return total seconds
        # can be converted if needed
        print(f"seconds worked: {time_worked.total_seconds()}")


clocking = Clocking()
clocking.punch_in()
# this would be working time
sleep(3)
clocking.punch_out()
