class Person:
    def __init__(self, age, birth):
        self.age = age
        self.birth = birth
    def isAdult(self):
        print('Adult') if self.age >= 18 else print('Teen')
    def astro(self):
        if self.birth == "Jan": print('摩羯座')
        if self.birth == "Nov": print("天蝎座")

class Girl(Person):
    def __init__(self,age, birth, weight):
        super().__init__(age, birth)
        self.weight = weight
    def shape(self):
        print('buxom') if self.weight >= 52 else print('slim')
print('[Amy]')
amy = Girl(17, "Jan", 51)
amy.isAdult()
amy.shape()
amy.astro()

print('[Diana]')
diana = Girl(29, 'Nov', 54)
diana.isAdult()
diana.astro()
diana.shape()

        

