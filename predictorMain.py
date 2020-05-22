from dateClass import Date
from plateClass import Plate
from timeClass import Time 
import datetime
from constantsClass import Constants
from colorama import Back,  Fore, init, Style
init()


if __name__=="__main__": 
    print(Fore.BLUE+"Welcome, insert plate, time and date to consult if you are under restriction to circulate\n"+Style.RESET_ALL)
    """
    Receiving plate, input and date of user's vehicle
    For all of them, checking whether the info is in the right format
    """
    while True:   
        plateInput=input("Please, insert the plate number of your vehicle: ").upper()
        if not Constants.PLATEPATTERN.match(plateInput):
            print("Sorry, the correct format is: AAA111 or AAA1111")
            continue
        else: 
            plate=Plate(plateInput)
            break

    while True:   
        dateInput=input("Please, insert the date (dd-mm-yyyy) you want to consult: ")
        try: 
            dateInput=datetime.datetime.strptime(dateInput, '%d-%m-%Y')
        
        except ValueError: 
            
            print("Sorry, the correct format is:dd-mm-yyyy")
            continue
            
        else: 
            date=Date(dateInput)
            break
        
    while True:   
        timeInput=input("Please, insert the time (H:M, 24h format) you want to consult: ")
        try: 
            timeInput=datetime.datetime.strptime(timeInput, '%H:%M')
            
        except ValueError:
            print("Sorry, the correct format is:H:M, 24h format")
            continue
        else: 
            time=Time(timeInput)
            break
        
    """
    Algorithm that determines if vehicle can be on the street or not 

    Checks time first, if time is not under restriction the vehicle is free 
    to go otherwise if the day of restriction of the plate is the same as 
    the day of the date entered by user the vehicle can't be on the street,
    otherwise the car is free to go 
    """

    if (time.isOnRestriction()): 
        if(plate.getRestrictionDayName()==date.getDayName()):
            print(Fore.RED+f"Sorry, you can't take your vehicle out")
        else: (
            print(Fore.GREEN+f"You are free to take your vehicle out")
        )    
    else: 
        print(Fore.GREEN+"You are free to take your vehicle out")
        




