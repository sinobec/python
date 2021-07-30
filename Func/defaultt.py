def test(ind, sand=None):
    print('==== Inside function, the sandwitch is :',sand,'====')
    if sand is  None:
        sand = ['bread', 'bread']
        sand.insert(1,ind)
    return sand
breakfast = test('veg')
print(breakfast)

lunch = test('egg')
print(lunch)

print()
def workFor(x, y, z='John', age = 30):
    print(x,'and',y,'are working for',z,'.',z,'\'s age is',age)

workFor('Adam','Ben')
workFor('Adam','Ben', 'Lin')