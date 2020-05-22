from dateClass import Date
from plateClass import Plate
from timeClass import Time 
import datetime
import re
PLATEPATTERN = re.compile("^[A-Z]{3}[0-9]{3,4}|^[A-Z]{2}[0-9]{3}[A-Z]{1}")

if __name__=="__main__": 
 while True:   
    plateInput=input("Insert plate number: ").upper()
    if not PLATEPATTERN.match(plateInput):
        print("Sorry, the correct format is: AAA111 or AAA1111")
        continue
    else: 
        plate=Plate(plateInput)
        break

 while True:   
    dateInput=input("Insert date: ")
    try: 
        dateInput=datetime.datetime.strptime(dateInput, '%d-%m-%Y')
       
    except ValueError: 
        
        print("Sorry, the correct format is:dd-mm-YY")
        continue
        
    else: 
        date=Date(dateInput)
        break
     
while True:   
    timeInput=input("Insert time: ")
    try: 
        timeInput=datetime.datetime.strptime(timeInput, '%H:%M')
        
    except ValueError:
        print("Sorry, the correct format is:H:M")
        continue
    else: 
        time=Time(timeInput)
        break
     



if (time.isOnRestriction()): 
    if(plate.getRestrictionDay()==date.getDay()):
        print("You can´t go")
    else: (
        print("You can go ")
    )    
else: 
    print("You can go ")
    




