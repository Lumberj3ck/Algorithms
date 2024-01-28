class M:
    def __init__(self, temp) -> None:
        self.temperature = temp

    def get_temperature(self):
        print('doing some work in the background')
        return self.temp

    def set_temperature(self, value):
        print('we are setting given value')
        self.temp = value

    temperature = property(fget=get_temperature, fset=set_temperature, doc='I"m documentation')


ex = M(12)
# getter function
print(ex.temperature)
# getter function
ex.temperature = 123
# setter function
print(ex.temperature)
# how to call doc string 
# property just wraps when someone calls this methods on given attribute 
print(M.temperature.__doc__)
