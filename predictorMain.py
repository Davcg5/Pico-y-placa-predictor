from dateClass import Date
from plateClass import Plate
from timeClass import Time 
import datetime
import re
from colorama import Back,  Fore, init, Style
init()

PLATEPATTERN = re.compile("^[A-Z]{3}[0-9]{3,4}|^[A-Z]{2}[0-9]{3}[A-Z]{1}")

if __name__=="__main__": 
    print(Fore.BLUE+"Welcome, insert plate, time and date to consult if you are under restriction to circulate\n"+Style.RESET_ALL)

    while True:   
        plateInput=input("Please, insert the plate number of your vehicle: ").upper()
        if not PLATEPATTERN.match(plateInput):
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
        


    if (time.isOnRestriction()): 
        if(plate.getRestrictionDayName()==date.getDayName()):
            print(Fore.RED+f"Sorry, you can't take your vehicle out")
        else: (
            print(Fore.GREEN+f"You are free to take your vehicle out")
        )    
    else: 
        print(Fore.GREEN+"You are free to take your vehicle out")
        




