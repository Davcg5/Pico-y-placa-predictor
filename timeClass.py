import datetime
from constantsClass import Constants
class Time(): 
    def __init__(self, time): 
        self.__time= time
    def __convertToTime(self, hourInString):
        return datetime.datetime.strptime(hourInString, '%H:%M')

    def isOnRestriction(self): 
        #
        restriction=False
        for time in Constants.TIMEINTERVALS.values(): 
                if (self.__convertToTime(time[0]) <self.__time < self.__convertToTime(time[1])) :
                    restriction= True
                    break
                else: 
                    restriction= False 
                    continue
        return restriction