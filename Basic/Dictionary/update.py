dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2008
dict['color'] = 'red'
dict.update({"year": 2017})
for i in dict:
    print(i)


print(dict.keys())