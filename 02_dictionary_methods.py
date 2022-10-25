myDict = {
"Fast" :"in a quick mannner",
"anisha":"a girl",
"Marks": [1,2,5],
"anotherdict":{'Anisha': 'my freind'},
1:2
}

#dictionary methods
print(list(myDict.keys()))#print the keys of the dictionary
print(myDict.values())
print(myDict.items())#print the (key,value) for all contents of the dictionary
print(myDict)
updateDict= {
"shruti":"roommate",
"sonu" : "brother",
"sakshi": "freind"
}
myDict.update(updateDict)# update the dictionary by adding key-value pair from updateDict
print(myDict)
print(myDict.get("sonu"))
print(myDict.get("sonu2"))#returns none as sonu2 is not present in the dictionary
#print(myDict("sonu2"))#throws an error as sonu2 is not present in the dictionary