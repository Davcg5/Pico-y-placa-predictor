class Date():
    """
    Class of the date entered by user 
    Attributes: 
        date: entered date
    Methods: 
        getDayName
    """
    def __init__(self, date): 
        self.__date= date

    def getDayName(self): 
        """
        Method that retrieves the day name of a date 
        """
        return self.__date.date().strftime("%A")

