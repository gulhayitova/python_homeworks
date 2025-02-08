string = input("String: ")
for i in ['a','e','i','o','u','y']:
    string = string.replace(i,'')
print(string)