import datetime
from datetime import date

def getstartvalue():

    startvalue = int(input("Enter the starting value of the investment: "))
    return startvalue

def getendvalue():

    endvalue = int(input("Enter the end value of the investment: "))
    return endvalue

def getstartdate():
    
    date_entry = input('Enter the start date in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    startdate = datetime.date(day, month, year)
    return startdate

def getenddate():
    
    date_entry = input('Enter the end date in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    enddate = datetime.date(day, month, year)
    return enddate

def date_factor():
    
    startdate=getstartdate()
    enddate=getenddate()
    num = (360 * (enddate.year - startdate.year) + (30*(enddate.month - startdate.month) + (enddate.day - startdate.day)))
    yearfrac = num / 360
    return yearfrac

def calc():
    
    startvalue=getstartvalue()
    endvalue=getendvalue()
    yearf=date_factor()
    
    ifp=((endvalue/startvalue)**(1/(yearf))-1)*100
    
    print(f"Your investment has grown by a compound annual growth rate of {ifp}%")
    
calc()
