from constantsClass import Constants


class Plate():

    """
    Class of the plate entered by user 
    Attributes: 
        plate: plate entered by user 
        lastDigit: last digit of the plate entered by user 
    Methods: 
    getRestrictionDayName
    __obtainLastDigit
    """
    def __init__(self, plate): 
        self.__plate= plate
        self.__lastDigit, =self.__obtainLastDigit(self.__plate)
        

    def getRestrictionDayName(self): 
        """
        Method that retrieves the day of restriction for a plate
        checking the last digit in the restrictions dictionary of 
        the Constants class 
        """
        for day, digits in Constants.RESTRICTIONSDICTIONARY.items(): 
            if self.__lastDigit in digits: 
                 return day

    def __obtainLastDigit(self, plate): 
        """
        Method that obtains the last digit of a plate 
        regardless of the type of vehicle (car or motorbike) 
        """
        if plate[-1].isnumeric(): 
            lastDigit=plate[-1]
            
        else: 
            lastDigit=plate[-2]
            
        return lastDigit

