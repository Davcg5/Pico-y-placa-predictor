import datetime

TIMEINTERVALS={
    "Morning": ["07:00", "09:30"], 
    "Afternoon": ["16:00", "19:30"]
}

class Time(): 
    def __init__(self, time): 
        self.time= time
    def convertToTime(self, hourInString):
        return datetime.datetime.strptime(hourInString, '%H:%M')

    def isOnRestriction(self): 
        #
        restriction=False
        for time in TIMEINTERVALS.values(): 
                if (self.convertToTime(time[0]) <self.time < self.convertToTime(time[1])) :
                    restriction= True
                    break
                else: 
                    restriction= False 
                    continue
        return restriction