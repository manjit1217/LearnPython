inputTime = "07:05:45PM"

hour=""
if inputTime.__contains__("PM") and inputTime[:2]!="12":
    x=inputTime
    hour=inputTime[:2]
    hour24=int(hour)+12
    y=inputTime.replace(str(hour),str(hour24))
    print(y[:-2])

elif inputTime.__contains__("AM") and inputTime[:2]=="12":
    zerotime= inputTime.replace(inputTime[:2],"00")
    print(zerotime[:-2])
else:
    print(inputTime[:-2])





