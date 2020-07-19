x=7958347983759387598345983579*5
print(x)
#find factorial using recursive
def factorial(no):
    if no==1:
        return 1
    else:return no*factorial(no-1)

    # while no==1:
    #     return no*factorial(no-1)

def factorialNormal(no):
    fact=1
    if no==0:
        return (fact)
    elif no==1:return(fact)
    else:
        for i in range(1,no+1):
            fact=fact*i
        return(fact)

print(factorial(25))
print(factorialNormal(5))