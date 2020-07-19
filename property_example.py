class Property_example:
    def __init__(self, tem=0):
        self._tem=tem
    @property
    def temp_to_cel(self):
        return (self._tem * 1.8) + 32

    @property
    def temperature(self):
        return self._tem

    @temperature.setter
    def temperature(self, t):
        if t < -273.15:
            raise ValueError('Temp below not allowed')
        self._tem = t


obj = Property_example()
print(obj.temperature)
print(obj.temp_to_cel)

