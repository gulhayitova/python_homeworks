def invest(amount, rate, years):
    for i in range(int(years)):
        amount += amount*rate
        print(f"Year {i+1}: {amount:.2f}")
    return None
amount = float(input("Enter the amount: "))
rate = float(input("Rate: "))
year = float(input("Enter the number of years: "))
invest(amount, rate, year)