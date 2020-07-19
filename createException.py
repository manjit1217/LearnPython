#Write your code here

class NegativeError(Exception):
    pass

class Calculator:
    def power(self,n,p):
        self.n=n
        self.p=p
        try:
            if(self.n<0 or self.p<0):
                raise NegativeError
            else:
                return self.n**self.p
        except NegativeError:
            return('n and p should be non-negative')




obj=Calculator()
print(obj.power(1,2))