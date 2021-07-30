la = ["apple", "banana", "cherry", "orange"]
lb = ["peach", "cherry", "anana"]
la.insert(3,'watermelon')
print('Insert:'+'*'*50)
print(la)
la.append('grape')
print('Append:')
print(la)
la.extend(lb)
print(la)
la.pop()
print(la)
x = la.pop()
print(x)
del la

lb.clear()
print(lb)
print(la)



