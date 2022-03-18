# Investment Fund Performance

import datetime

def data():

    startvalue = input("Enter the starting value of the investment: ")
    endvalue = input("Enter the ending value of the investment: ")
    
    date_entry = input('Enter the start date in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(day, month, year)

    date_entry = input('Enter the end date in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    date2 = datetime.date(day, month, year)


    date1 = datetime.date(d1year, d1month, d1day)

    date2 = datetime.date(d2year, d2month, d2day)

data()

def yearfrac(date1, date2):

    num = (360 * (date2.year - date1.year) + (30*(date2.month - date1.month) + (date2.day - date1.day)))
    return num / 360

yearfrac(date1, date2)

def ifp():

    ifp = (endvalue/startvalue)**(1/yearfrac(date1, date2))

    print("The investment fund's performance is: ", ifp)

ifp()

