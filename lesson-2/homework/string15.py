sent = input().split()
acro = ''
for word in sent:
    acro = acro + word[0]
print(acro.upper())