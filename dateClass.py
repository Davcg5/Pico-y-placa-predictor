class Date():
    def __init__(self, date): 
        self.date= date

    def getDayName(self): 
        
        return self.date.date().strftime("%A")

