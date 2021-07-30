class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __str__ (self):
        #return '===this is my_Class(vat x= ' + str(self.x) + ' , var y= ' + self.y + ')'
        return f'===this is my_Class(vat x= {str(self.x)}, var y= {self.y} )'
myObject = MyClass(12345, "Hello")
print("#"*70)
print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())