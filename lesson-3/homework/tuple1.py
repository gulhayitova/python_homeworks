#1 - count occurences
tuple1 = (1,2,3,4,5,4,3,2,1,1)
print(tuple1.count(1))

#2 - max element
print(max(tuple1))
#3
print(min(tuple1))

#4 check if element is present
print(bool(7 in tuple1))

#5 first element
if tuple1:
    print(tuple1[0])
else:
    print("The tuple is empty")

#6 last element
if tuple1:
    print(tuple1[-1])
else:
    print("The tuple is empty")

#7 tuple length
print(len(tuple1))

#8 first three elements in a new tuple
tuple2 = tuple1[:3]

#9 concatenate tuples
tuple3 = (2,4,8,10,23456)
tuple4 = list(tuple3)
tuple4.extend(tuple2)
tuple4 = tuple(tuple4)

#10 check if tuple is empty
print(bool(tuple3))

#11 get all indices of an element
print([i for i,x in enumerate(tuple1) if x == 1])

#12 find second largest 13 smallest
tuple1aslist = list(tuple1)
print(sorted(tuple1aslist)[-2])
print(sorted(tuple1aslist)[1])

#14 single element tuple
single = (1,)

#15 make it a list. tuple1aslist already created
#16 check if tuple is sorted
if sorted(tuple1aslist) == list(tuple1): print("Tuple is sorted")
else: print("Tuple is not sorted")

#17/18 max/min of subtuple, tuple2 taken as the subtuple
print(max(tuple2))
print(min(tuple2))

#19 remove element by valule
elem = 1
list1 = list(tuple1)
list1.remove(elem)
tuple1 = tuple(list1)


#20 create a tuple with subtuples, tuple2 and subtuple taken as subtuples
newtuple = list(tuple2)
subtuple = tuple1[3:]
newtuple.extend(subtuple)
newtuple = tuple(newtuple)

#21 repeat elements
num = 3
repetuple = []
for i in tuple1:
    for j in range(num):
        repetuple.append(i)
repetuple = tuple(repetuple)

#22 create range tuple 
ranget = list()
for i in range(4,10):
    ranget.append(i)
ranget = tuple(ranget)

#23 reversetuple
revtup = list(tuple1)
revtup.sort(reverse=True)
revtup = tuple(revtup)

#24 check palindrome
words = ('apple', 'ana')
palin = True
if words:
    for word in words:
        if word != word[::-1]:
            palin = False
            break
    if palin: print("It is palindrome")
    else: print("It is not palindrome")
else:
    print("It's empty")

#25 unique elements
tuple1 = list(tuple1)
tuple1 = tuple(set(tuple1))