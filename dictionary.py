# dictionary are used to store data values in key value pair
myDictionary={
    "name":"Anisha",
    "age":18,
    "Roll":57,
    "percentage":99.99
}
print(myDictionary)
# ordered
# duplicates are not allowed
print(len(myDictionary))
a=myDictionary.get("name")
print(a)
b=myDictionary.keys()
print(b)
c=myDictionary.values()
print(c)
# myDictionary["age"]=22
# print(myDictionary)
# myDictionary.update({"age":22})
# print(myDictionary)
# myDictionary.pop("Roll")
# print(myDictionary)
print("keys are:",b)
print("values are:",c)
myDictionary={
    "class":{
        "student":{
            "name": "abc",
            "marks":{
                "python": 90,
                "web":95
            }
        }
    }
}
print(myDictionary["class"]["student"]["marks"]["web"])










