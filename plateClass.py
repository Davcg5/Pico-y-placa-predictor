RESTRICTIONSDICTIONARY={"Monday": ["1", "2"], 
             "Tuesday": ["3", "4"],
             "Wednesday": ["5", "6"],
             "Thursday": ["7", "8"],
             "Friday": ["9", "0"]}

class Plate():

    def __init__(self, plate): 
        self.plate= plate
        self.lastDigit=self.plate[-1]
        
    def getRestrictionDay(self): 
        for key, values in RESTRICTIONSDICTIONARY.items(): 
            if self.lastDigit in values: 
                 return key

       

