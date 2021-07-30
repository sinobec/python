import re
txt = 'your interview preparations Enhance your Data Structures concepts'
result = re.search('y', txt)
print('$'*50)

print(result.span())
print('$'*50)
split = re.split(' ',txt)
print(split)
sub = re.sub(' ','_',txt)
print(type(sub))

