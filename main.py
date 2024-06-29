import json
x="put the relative path of the pinecode file to be read"
f=open(x)
data=json.load(f)
print(data["source"])
