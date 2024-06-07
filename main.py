# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.
def verifyDate():
    validDate = True
    MIN_YEAR = 0
    MIN_MONTH = 1
    MAX_MONTH = 12
    MIN_DAY = 1
    MAX_DAY = 31


    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))

# Get the year, then the month, then the day
# housekeeping()

# Check to be sure date is valid
    if int(month) in {4, 6, 9, 11} and int(day) >= MAX_DAY:# invalid day   
        validDate = False
    elif int(year) <= MIN_YEAR: # invalid year
        validDate = False
    elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
        validDate = False
    elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
        validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
    if validDate == True:
    # Output statement    
        print(str(month)+"/"+str(day)+"/"+str(year)+" is a valid date")
        return str(month)+"/"+str(day)+"/"+str(year)+" is a valid date"
    else:
    # Output statement
        print(str(month)+"/"+str(day)+"/"+str(year)+" is an invalid date")
        return str(month)+"/"+str(day)+"/"+str(year)+" is an invalid date"
    
if __name__ == "__main__":
    verifyDate()