import datetime 
RESTRICTIONSDICTIONARY={"Monday": ["1", "2"], 
             "Tuesday": ["3", "4"],
             "Wednesday": ["5", "6"],
             "Thursday": ["7", "8"],
             "Friday": ["9", "0"]}

class Date():

    def __init__(self, date): 
        self.date= date


    def getDay(self): 
        
        return self.date.date().strftime("%A")

