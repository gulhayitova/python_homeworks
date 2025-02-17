def is_prime(n):
    isd = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: isd = 1
    if isd == 0 and n != 1: return True
    else: return False
num = int(input("Number: "))
print(is_prime(num))