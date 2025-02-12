#1 get value
dict1 = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e'
}
key = 6
try:
    print(dict1[key])
except KeyError:
    print("Doesn't exist")

#2 check key
print(bool(key in dict1.keys()))

#3 n of keys
print(len(dict1))

#4 get keys
print(dict1.keys())

#5 get all values
print(dict1.values())

#6 merge dicts
dict2 = {5:'e', 6:'f', 7:'g',8:'h'}
merged = dict1|dict2
print(merged)

#7 remove key
if key in merged.keys():
    del merged[key]
    print(merged)
else:
    print("The key doesn't exist.")

#8 clear
dict2.clear()

#9 check if empty
print(bool(merged))

#10 key value pair
key = 2
print({key: merged[key]})

#11 update
merged[key] = 'B'

#12 count occureces
same_keys = 0
for i in merged.values():
    if i == merged[key]:
        same_keys +=1
print(same_keys)

#13 Invert 
merged1 = dict()
for i,x in merged.items():
    merged1[x] = i
print(merged1)
# OR
print({o: x  for x,o in merged.items() })

#14 find key iwth value
print(list(merged.keys())[list(merged.values()).index('h')])

#15 create a dict from 2 lists
keys = list(dict1.keys())
values = list(dict1.values())
print(keys,values)
newDict = dict()
for i in range(len(keys)):
    newDict.update({keys[i]:values[i]})
print(newDict)








