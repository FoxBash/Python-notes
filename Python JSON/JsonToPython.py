import json
x = '{"name":"John", "age":30,"City":"Nairobi"}'
y = json.loads(x)
print(x)
print(y["age"])