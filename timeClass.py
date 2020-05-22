import datetime
from constantsClass import Constants
class Time(): 
    """
    Class of the time entered by user 
    Attributes: 
        time:entered time
    Methods: 
        __convertToTime
        isOnRestriction
    """
    def __init__(self, time): 
        self.__time= time
    def __convertToTime(self, hourInString):
        """
        Method that transforms a string into a valid hour
        """
        return datetime.datetime.strptime(hourInString, '%H:%M')

    def isOnRestriction(self): 
        """
        Method that iterates the intervals of time and determines if the 
        time entered by the user is between a restriction interval or not 
        """
        restriction=False
        for time in Constants.TIMEINTERVALS.values(): 
                if (self.__convertToTime(time[0]) <self.__time < self.__convertToTime(time[1])) :
                    restriction= True
                    break
                else: 
                    restriction= False 
                    continue
        return restriction