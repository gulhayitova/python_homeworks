#Dear bot, I had to make my code shorter and brief and I tried to explain as concise as I can. Please be soft with me)
numbers = [1,2,6,4,9,2,10,34,2,5,1,9]
#1st task
print("The number 2 in the list:", sum(1 for x in numbers if x==2))
#2nd task
print(sum(numbers))
#3rd and 4th task
print(max(numbers))
print(min(numbers))
print(4 in numbers) #5th
try: #6th
    print(numbers[0])
except IndexError: #in case empty
    print("The list is empty")
try: #7th
    print(numbers[-1])
except IndexError:
    print("The list is empty")
newNum = numbers[0:3] #8 - new shorter list

newnumb = reversed(numbers) #9th

sortedlist = sorted(numbers) #10th - sorting

#removing duplicates - 11th
uniqueList = set(numbers)

element = 17
numbers.insert(0, element) #inserting an element at a specified space - 12

print(numbers.index(17)) #finding an index of an element - 13

print(bool(numbers)) #check whether empty or not, returning boolean - 14

print(sum(1 for i in numbers if i%2==0)) #number of even numbers in list

print(sum(1 for j in numbers if j%2 == 1)) #number of odd numbers - 16

letters = ['a', 'r', 'e', 't','w']
combination = letters.copy()
combination.extend(numbers) #combined two lists into one list - 17

sublist = ['a', 1, 'w']
sublist1 = []
for item in sublist:
    if item in combination: sublist1.append(item) #creating a new list containing only items in bigger list
print(bool(sublist == sublist1)) #checking if all items existing in bigger list are present - 18

numbers[0] = 0 #swapping an element in a list - 19
print(numbers)

print(sorted(numbers)[-2])
print(sorted(numbers)[2]) #printign the second highest and lowest values

evenNum = list(filter(lambda x: x%2 == 0, numbers))
oddNum = list(filter(lambda x: x%2 == 1, numbers)) #filtering odd and even numbers

print(len(numbers))

copied = combination.copy() #makingcopy of an original list

middle = len(numbers)//2
if len(numbers)%2 == 0:
    print(numbers[middle])
else:
    middle = round(middle)
    print(numbers[middle], numbers[middle+1])

sublist = numbers[:5]
print(max(sublist))
print(min(sublist))

del numbers[0] #deleting an element using index

print(bool(sublist == sorted(sublist))) #check if list is sorted - 30

repeatedList = []
n = 3
for i in sublist: #copying every element into new list n number of times
    for j in range(n):
        repeatedList.append(i)
print(repeatedList)

#using evenNum and oddNum created in previous codes to save memory
merged = evenNum.copy() #32 - merge two lists and create a new list and sort it
merged.extend(oddNum)
merged.sort()

#finding indices of an element using enumerate()
indices = []
for i, x in enumerate(numbers): 
    if x == 2:
        indices.append(i)
print(indices)
#OR
print([i for i, x in enumerate(numbers) if x==2])

fruits = ['apple', 'banana', 'pear']
for fruit in fruits:
    fruits[fruits.index(fruit)] = fruit[::-1] #reversing all items in a list

rangeList = []
for i in range(10, 20):
    rangeList.append(i)

posneg = [-1, 3, 7, -5]
print(sum(x for x in posneg if x > 0)) #adding all postitive and negative numbers
print(sum(x for x in posneg if x < 0))

palindrome = ['ada', 'gul', 12321]
palN = 0
for i in palindrome:
    if str(i) == str(i)[::-1]:
        palN+=1 #counting the number of items which are palyndrome
if palN == len(palindrome):
    print("The list is palyndfrome.")
else:
    print("The list is not palyndrome.")

#39 - Create nested list
biglst = [1,2,3,4,5,6,7,8,9]
sublst1 = biglst[:3]
sublst2 = biglst[3:6]
sublst3 = biglst[6:] #made 3 lists containing exact number of tems from the list

#40 - same as 11th question
#uniqueList = set(numbers)