class Girl:
    def __init__(self, age, weight, birth):
        self.age = age
        self.weight = weight
        self.birth = birth
    
    def isAdult(self):
        print('Adult') if self.age >= 18 else print('Not adult')
    def shape(self):
        print('buxom') if self.weight >= 52 else print('slim')


amy = Girl(29, 54, 'Jan')
print('[Amy]')
print(amy.age)
amy.isAdult()
amy.shape()

diana = Girl(17, 48, 'Nov')
print('[Diana]')
diana.isAdult()
diana.shape()