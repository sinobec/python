# instead of 10000 times concatenations string addition, first converting str into list,
#then only execute once string concatenation.
oldstr = 'a' # the final str would be 'aaa......aaa'
templist = list(oldstr)
for i in range(10):
    templist.append('a')

result = ''.join(templist)
print(result)