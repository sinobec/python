def spam(number1, number2):
    return number1 / (number2 - 42)

try:
    spam(101, 42)

except:
    print('Error!')

var = 'djfkg'
class Mycode:
    x = 11
    y = 2
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def func(self):
        return self.x * self.y

aa = Mycode(22, 7)
print(aa.func())