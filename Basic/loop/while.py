list = ["peach", "cherry", "anana", "orange", "grape"]
j = 0
i = 0
while i < len(list):
    if i == 3:break
    print(list[i])
    i += 1
print("."*30)
while j < len(list):
    if j == 2:
        j += 1
        continue
    print(list[j])
    j += 1
else:print("!!finished!!")