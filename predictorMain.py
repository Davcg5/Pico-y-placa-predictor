from dateClass import Date
from plateClass import Plate
from timeClass import Time 


if __name__=="__main__": 
    
    date=input("Insert date: ")
    date=Date(date) 
    plate=input("Insert plate number: ")
    plate=Plate(plate)
    time=input("Insert time: ")
    time=Time(time)


    if (time.isOnRestriction()): 
        if(plate.getRestrictionDay()==date.getDay()):
            print("You can´t go")
        else: (
            print("You can go ")
        )    
    else: 
        print("You can go ")
        




    #print(dayOfRestriction)

    #time=input("Insert time")


   # print (dayNotToCirculate)


