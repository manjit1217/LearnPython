
singleDigit=['one','two','three','four','five','six','seven','eight','nine']
doubleDigit=['ten','twenty','thirty','fourty','fifty','sixty','seventy']
def printNoinWords(number):
    if(len(str(number))==2):
        first=int(number[:1])
        second=int(number[1:2])
        print(doubleDigit[first-1])
        print(singleDigit[second-1])


printNoinWords("65")
x="85"
print(int(x[:1]))