clothes = ['skirt', 'red sock', 'white sock', 'gray sock', 'gray sock', 'white sock', 'black sock', 'pant']
result = clothes.copy()
tmp = list(dict.fromkeys(clothes))
tobeadded = []
print('Temp is:',tmp)
for product in tmp:
    clothes.remove(product)

for item in result:
    if not item in clothes:
        tobeadded.append(item)

result.extend(tobeadded)
print(result)


 

