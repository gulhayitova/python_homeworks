password = str(input())
up = 0
if len(password) >= 8:
    for i in password:
        if i.isupper():
            up = 1
    if up: print("Password is strong.")
    else: print("Password must contain an uppercase letter.")
else:
    print("Password is short.")