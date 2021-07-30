fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [item for item in fruits if "o" in item]
print(new)

newList=[item if item!='banana' else 'orange' for item in fruits]
print(newList)
#####
print('*'*80)
five = [num for num in range(1,101) if num % 7 == 0]
print(five)
