import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(type(y))
print(y)
print('#'*60)
d =  {"name": "John", "age": 30,"city": "New York"}
j = json.dumps(d, indent=3, sort_keys=True)
print(type(j))
print(j)
