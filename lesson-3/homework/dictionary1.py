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

newDict[10] = {1:2,2:3}
#16 check nested dictionaries
for val in newDict.values():
    if type(val)==dict:
        print("The dictionary has another dictionary value.")
        #17 get a value from it. I got the first value here
        print(list(val.values())[0])
        break

#18 default value for missing keys
from collections import defaultdict
newDict = defaultdict(lambda: "No value for this key")

#19 count unique values
m_values = list(merged.values())
print(len(set(m_values)))

#20 sort by key
print(dict(sorted(merged.items())))

#21 sort by values
print(dict(sorted(merged.items(), key=lambda item: item[1])))

#22 filter by value
m_even = {x:y for x, y in merged.items() if x%2 == 0}

#23 check for common keys
set1 = list(m_even.keys())
set2 = list(merged.keys())
set1, set2 = set(set1), set(set2)
print(set1&set2)

#24 tuple to dict
tuple1 = ((1,"a"),(2,"b"),(3,"c"))
print(dict(tuple1))

#25 get the first pair
tuple1 = dict(tuple1)
print(list(tuple1.items())[0])