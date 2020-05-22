from constantsClass import Constants


class Plate():

    def __init__(self, plate): 
        self.__plate= plate
        self.__lastDigit, =self.__obtainLastDigit(self.__plate)
        

    def getRestrictionDayName(self): 
        for day, digits in Constants.RESTRICTIONSDICTIONARY.items(): 
            if self.__lastDigit in digits: 
                 return day

    def __obtainLastDigit(self, plate): 
        if plate[-1].isnumeric(): 
            lastDigit=plate[-1]
            
        else: 
            lastDigit=plate[-2]
            
        return lastDigit

