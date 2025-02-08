vowels = ['a', 'e', 'i', 'o', 'u', 'y']
gstring = input("Strign: ")
v = 0
for i in gstring:
    if i in vowels: v+=1
print("The number of vowels:", v,"\nThe number of consonants:", len(gstring)-v)

