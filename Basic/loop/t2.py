g = ['hello', 'hello', 'mello', 'yello', 'hello']
for i in g:
    if i != 'hello': g.remove(i)

print(g)

result = [i for i in g  if i == 'hello']

print(result)






