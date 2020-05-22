# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:39:28 2020

@author: davcg
"""


import datetime 


dictionary={"Monday": ["1", "2"], 
             "Tuesday": ["3", "4"],
             "Wednesday": ["5", "6"],
             "Thursday": ["7", "8"],
             "Friday": ["9", "0"]}


def searchPlateNumber(lastPlateNumber): 
    for key, values in dictionary.items(): 
        if lastPlateNumber in values: 
           return key

dateString="10-08-2012"
dateString=datetime.datetime.strptime(dateString, '%d-%m-%Y')
dayToCheck=dateString.date().strftime("%A")
print(datetime.datetime.now().strftime("%A"))


plate="PBD-4512"
lastDigit=plate[-1]


time3="1:00"
time2="9:31"
time2=datetime.datetime.strptime(time2, '%H:%M')

timeSM="7:00"
timeFM="9:30"
timeSA="16:00"
timeFA="19:30"

timesList2=[timeSM , timeFM, timeSA, timeFA]

def transformToTime(time): 
    
    return datetime.datetime.strptime(time, '%H:%M')
timesList=[*map(transformToTime, timesList)]


def checkTime(hour):     
    if (timesList[0] <hour < timesList[1]) or (timesList[2]<hour<timesList[3]):
        return True

    
  ###TEST   
plateToTest="PBA7103"
hourToTest="16:00"
dateToTest="19-05-2020"
##Preprocess
dateToTest=datetime.datetime.strptime(dateToTest, '%d-%m-%Y')
dayFromDate=dateToTest.date().strftime("%A")
lastPlateNumber=plateToTest[-1]
hourToTest=datetime.datetime.strptime(hourToTest, '%H:%M')

dayNotToCirculate=searchPlateNumber(lastPlateNumber)

#Check
if dayNotToCirculate==dayFromDate: 
    if (checkTime(hourToTest)): 
        print("No circula")
    else: 
        print("Puede circular")

else: 
    print("Puede circular")

    
    
    