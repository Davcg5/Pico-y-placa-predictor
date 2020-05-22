import re
class Constants: 
    """
    Class where the constants are stored 
    """
    PLATEPATTERN = re.compile("^[A-Z]{3}[0-9]{3,4}|^[A-Z]{2}[0-9]{3}[A-Z]{1}")

    TIMEINTERVALS={
        "Morning": ["07:00", "09:30"], 
        "Afternoon": ["16:00", "19:30"]
    }
    RESTRICTIONSDICTIONARY={"Monday": ["1", "2"], 
             "Tuesday": ["3", "4"],
             "Wednesday": ["5", "6"],
             "Thursday": ["7", "8"],
             "Friday": ["9", "0"]}