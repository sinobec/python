list = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 21 },
{ "name" : "Nikhil" , "age" : 19 }]

s = sorted(list, key = lambda i: i['age'] )
print(s)