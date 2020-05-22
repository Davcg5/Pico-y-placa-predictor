import datetime

TIMEINTERVALS={
    "Morning": ["07:00", "09:30"], 
    "Afternoon": ["16:00", "19:30"]
}




class Time(): 
    def __init__(self, time): 
        self.time= time

    def stringToDatetime(self, hourInString):
        return datetime.datetime.strptime(hourInString, '%H:%M')

    def isOnRestriction(self): 
        for key, values in TIMEINTERVALS.items(): 
                
                if (self.stringToDatetime(values[0]) <self.time < self.stringToDatetime(values[1])) :
                    return True
                else: 
                    return False 
   