from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,name):
        self.name = name
    def accountOpening(self):
        print("Account Opening",self.name)
    def accountClosing(self):
        print("Account Closing",self.name)
    @abstractmethod
    def interestCalculater(self):
        '''This method is abstract, so the class cannot be
            instantiated. This method will be overridden in
                       subclasses of Vehicle.'''
        pass
class HDFC(Bank):
    def __init__(self,name):
        super(HDFC,self).__init__(name)#by accessing super we can call the superclass constructor
    def interestCalculater(self):
        '''Override the abstract method of the base class'''
        print('HDFC interest calculation')
class ICICI(Bank):
    def interestCalculater(self):
        print('ICICI interest calculation')
#obj=Bank('bank')# it will give error because we can not create an object of abstarct class
hdfc=HDFC('HDFC')
icici=ICICI('ICICI')#this is an object of the ICICI class.
hdfc.interestCalculater()
hdfc.accountOpening()