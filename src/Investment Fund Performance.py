from datetime import date

def getstartvalue():
    
    # Gets the initial value of an investment
    
    startvalue = int(input("Enter the starting value of the investment: "))
    return startvalue

def getendvalue():
    
    # Gets the end value of an investment

    endvalue = int(input("Enter the end value of the investment: "))
    return endvalue

def getstartdate():
    
    # Gets the start date of the investment period
    
    date_entry = input('Enter the start date in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    startdate = datetime.date(day, month, year)
    return startdate

def getenddate():
    
     # Gets the end date of the investment period
    
    date_entry = input('Enter the end date in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    enddate = datetime.date(day, month, year)
    return enddate

def getyearfrac():
    
    # Calculates the fraction of the year represented by the number of whole days between the start and end dates
    
    startdate=getstartdate()
    enddate=getenddate()
    num = (360 * (enddate.year - startdate.year) + (30*(enddate.month - startdate.month) + (enddate.day - startdate.day)))
    yearfrac = num / 360
    return yearfrac

def calc():
    
    # Calculates the investment performance and provides an output to the user
    
    startvalue=getstartvalue()
    endvalue=getendvalue()
    yearfrac=getyearfrac()
    
    ifp=((endvalue/startvalue)**(1/(yearfrac))-1)*100
    
    print(f"Your investment has grown by a compound annual growth rate of {ifp}%")
    
calc()
