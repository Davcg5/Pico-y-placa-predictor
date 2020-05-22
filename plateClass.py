RESTRICTIONSDICTIONARY={"Monday": ["1", "2"], 
             "Tuesday": ["3", "4"],
             "Wednesday": ["5", "6"],
             "Thursday": ["7", "8"],
             "Friday": ["9", "0"]}

class Plate():

    def __init__(self, plate): 
        self.plate= plate
        self.lastDigit, =self.obtainLastDigit(self.plate)
        

    def getRestrictionDayName(self): 
        for day, digits in RESTRICTIONSDICTIONARY.items(): 
            if self.lastDigit in digits: 
                 return day

    def obtainLastDigit(self, plate): 
        if plate[-1].isnumeric(): 
            lastDigit=plate[-1]
            
        else: 
            lastDigit=plate[-2]
            
        return lastDigit

