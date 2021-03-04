def leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return "That is a leap year"
            else:
                return "That is not a leap year"
        else:
            return "That is a leap year"
    else:
        return "That is not a leap year"


