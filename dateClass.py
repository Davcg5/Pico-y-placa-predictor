class Date():
    def __init__(self, date): 
        self.__date= date

    def getDayName(self): 
        
        return self.__date.date().strftime("%A")

