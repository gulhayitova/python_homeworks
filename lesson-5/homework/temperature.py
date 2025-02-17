def convert_cel_to_far(deg):
    deg = deg*9/5 + 32
    return deg
def convert_far_to_cel(deg):
    deg = (deg - 32)*5/9
    return deg
far = float(input("Enter a temperature in degrees F: "))
print(far, f"degrees F = {convert_far_to_cel(far):.2f} degrees C.")
cel = float(input("Enter a temperature in degrees C: "))
print(cel, f'degrees C = {convert_cel_to_far(cel):.2f} degrees F.')