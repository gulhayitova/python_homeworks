#1
#two_r = float(input("Number: "))
#print(round(two_r, 2))

#2
# a, b, c = map(int, input("Enter three integer separated by space: ").split())
# print("The greatest number is ", max(a, b ,c))
# print("The smallest number is ", min(a, b, c))

#3
# km = float(input("The distance in kilometers: "))
# print("The distance in meters is", format(km*1000,'g'),
#       "and", format(km*100000,'g'), 'in meters.')

#4
# a, b = input("Input two numbers separated with space: ").split()
# a, b = int(a), int(b)
# print("The integer division:", a//b,"\nThe remainder:", a%b)

#5
# celsius = float(input("The temperature in Celsius: "))
# faren = celsius*9/5 +32
# print("The temperature in Farenheits is", round(faren, 1))

#6
# num = input("Number: ")
# print(num[-1])

#7
# number = int(input("The integer: "))
# if number%2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#String questions
#1
# name = input("Your name: ")
# year = int(input("Your year of birth: "))
# print(name + ", you are", 2025-year,"years old.")

#2
# txt = "LMaasleitbtui"
# tlt = list(txt)
# car1 = [tlt[1], tlt[2], tlt[5], tlt[7], tlt[9], tlt[11]]
# car2 = [tlt[8], tlt[6], tlt[4], tlt[5], tlt[2]]
# print(''.join(car1), ''.join(car2))

#3
# word = input("The string: ")
# print("The length of the string is", len(word))
# print(word.lower())
# print(word.upper())

#4
# string = input("Enter: ")
# if string == string[::-1]:
#     print("It is palyndrome.")
# else:
#     print("It is not palyndrome.")

#5
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# gstring = input("Strign: ")
# v = 0
# for i in gstring:
#     if i in vowels: v+=1
# print("The number of vowels:", v,"\nThe number of consonants:", len(gstring)-v)

#6
# str1 = input("First word: ")
# str2 = input("Second word: ")
# if (str1 in str2) or (str2 in str1):
#     print("Yes")
# else: print('No')

#7
sent = input("Input sentence: ")
rep = input("Replace: ")
sub = input("With: ")
sent = sent.replace(rep, sub)
print (sent)

