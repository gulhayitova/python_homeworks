#1 create a union of sets with unique elements in both lists
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set3 = set1.copy()
set3 = set1|set2 #union sign

#2 inersection of sets
set4 = set1&set2 

#3 difference of sets
difset = set1.copy()
difset.difference_update(set2)

#4 check subset
bigset = {1,2,3,4,5,6,7,8}
smallset = {3,4}
print(bool(smallset <= bigset))

#5element in set
elem = 6
print(bool(elem in bigset))

#6 set length
print(len(bigset))

#7 convert list to set
liset = [1,42,46,2,1,4,4,3,0]
liset = set(liset)

#8 remove element
element = 42
try:
    liset.remove(element)
except KeyError:
    print("The element does not exist in the set")

#9 clear set
liset.clear()

#10 check if empty
print(bool(liset))

#11 create a list with elements which are not the intersection
uncommon = set1^set2
print(uncommon)

# 12 add element
# element = 4 from 8th task
if element not in bigset:
    bigset.add(element)
else:
    print("Already exists.")

#13 pop an element
print(bigset.pop())

#14/15 maximum/minimum
print(max(bigset))
print(min(bigset))

#16/17 create a new set with even/odd numbers
even = set(x for x in bigset if x%2 == 0)
odd = set(y for y in bigset if y%2 == 1)

#18 create a set of range
rangingset = set()
for i in range(20,31):
    rangingset.add(i)

#19 merge two lists, removing duplicates
list1 = ['a','b','c']
list2 = ['a', 'c','d']
merged = set(list1+list2)
print(merged)

#20 no common items
endset = {'w','y','z'}
inter = merged & endset
print(bool(not inter))

#21 remove duplicates from list
list3 = list1 + list2
#22 from here
list3 = set(list3)
list3 = list(list3)

#22 count unique el. beginning just like 21, so continue from 21

print(len(list3))

import random
#23 random elements
randomset = set()
for i in range(10):
    randomset.add(random.randint(1, 100))
print(randomset)