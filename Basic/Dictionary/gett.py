dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(dict.get('model'))

print(dict.values())
print(dict.keys())

print('#'*60)

pets= {'cat': 3}
print('I have',pets.get('cat',0),'cats, you have',pets.get('dog', 'star'), 'dogs')