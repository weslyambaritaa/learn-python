# Python weight converter

weight = float(input("Enter your weight : "))
unit = input("Kilograms or pounds? ( K or L ) : ")

if unit == "K" or unit == "k" :
    weight *= 2.205
    unit = "Lbs."
elif unit == "L" or unit == "l" :
    weight /= 2.205
    unit = "Kgs."
else :
    print("The unit is not valid [!]")

print(f"Your weight is {weight} {unit}")