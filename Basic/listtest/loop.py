list = ["apple", "banana", "cherry", "orange", "peach", "cherry", "anana"]
#for i in range(len(list)):
#    print(list[i])
#or
iterator = iter(list)
print('Iterator :')
print(iterator)
print('#'*10)
list2 = [item.title() for item in list]
print(' ----- List 2:')
print(list2)
print('#'*10)
[print(fruit) for fruit in list]
print('#'*10)
i = 0
while i < len(list):
    print(list[i])
    i = i+1

print('#'*10) 
toBeAdded = ['first ol', 'second ol']
htmlCnt = "<ul>\n" 

for i in range(len(toBeAdded)):
    htmlCnt=htmlCnt+'<li>'+toBeAdded[i]+'</li>\n'

htmlCnt = htmlCnt + "</ul>"
print(htmlCnt)