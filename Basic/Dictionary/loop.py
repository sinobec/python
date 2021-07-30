dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2008
dict['color'] = 'red'
dict.update({"year": 2017})
for i in dict:print(dict[i])

print("#"*30)
for key in dict.keys():print(key)
print("----- values -----")
for value in dict.values(): print(value)
print('---- items -----')
for item in dict.items(): print(item)