
def isEqual(a, b):  print('True') if a is b else print('False')
def ifEqual(a, b): print('True') if a == b else print('False')

isEqual(333, 333)
isEqual('good', 'good')
isEqual(('a', 'b'), ('a', 'b'))
isEqual(['a','b'], ['a','b'])
isEqual({'a': 'xxx', 'b': 'yyy'}, {'a': 'xxx', 'b': 'yyy'})

ifEqual(333, 333)
ifEqual('good', 'good')
ifEqual(('a', 'b'), ('a', 'b'))
ifEqual(['a','b'], ['a','b'])
ifEqual({'a': 'xxx', 'b': 'yyy'}, {'a': 'xxx', 'b': 'yyy'})