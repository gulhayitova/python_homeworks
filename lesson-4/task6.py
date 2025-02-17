n = int(input("Input a number: "))
div = []
for i in range(2, n+1):
    isd  = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            isd = 1
    if isd == 0: div.append(i)
print(div)