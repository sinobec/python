fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [item for item in fruits if "o" in item]
print(new)

newList=[item if item!='banana' else 'orange' for item in fruits]
print(newList)