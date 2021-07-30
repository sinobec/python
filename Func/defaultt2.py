def test(ind, sand=None):
    print('==== Inside function, the sandwitch is :',sand,'====')
    if sand is None: 
        sand = ['bread', 'bread']
        sand.insert(1,ind)
    return sand

breakfast = test('veg')
print(breakfast)

lunch = test('egg')
print(lunch)