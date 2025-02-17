list1 = list(map(int,input("List 1: ").split()))
list2 = list(map(int, input("List 2: ").split()))
uncommon = list1+list2
for i in list1:
    if i in list2:
        uncommon.remove(i)
for j in list2:
    if j in list1:
        uncommon.remove(j)
print(uncommon)