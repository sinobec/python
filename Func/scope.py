def func(para):
    temp = 5
    global var 
    var = 'my variable'
    var = 'random'
    return lambda x : x + para
res = func(' !!')
print(res('Welcome'))
print(var)