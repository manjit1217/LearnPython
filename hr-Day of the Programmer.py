def leapyear(year):
    if year < 1917 and year >= 1700:
        if(year%4==0):
            return True
        else:return False
    else: return ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0

def dayOfProgrammer(year):
    global sumofdaytillSept
    dayofprogram=256
    if(leapyear(year)):
        sumofdaytillSept =244
    else:
        sumofdaytillSept=243

    date=dayofprogram-sumofdaytillSept
    if year == 1918:
        date=date+13
    return (str(date)+'.09.'+str(year))


print(leapyear(1918))
print(dayOfProgrammer(1918))
