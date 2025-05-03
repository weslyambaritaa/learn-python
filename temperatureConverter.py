temp = float(input("Enter the temperature : "))
unit = input("Celcius or Fahrenheit or Réaumur ( C or F or R ) : ")
unit2 = input("Convert to ? ( C or F or R ) : ")

if unit == "C" and unit2 == "F" :
    temp = (9 * temp) / 5 + 32
    print(f"The temperature in Fahrenheit is {temp}")
elif unit == "C" and unit2 == "R" :
    temp = temp * 4 / 5
    print(f"The temperature in Reaumur is {temp}")
elif unit == "F" and unit2 == "C" :
    temp = (temp - 32) * 5 / 9
    print(f"The temperature in Celcius is {temp}")
elif unit == "F" and unit2 == "R" :
    temp = (temp - 32) * 4 / 9
    print(f"The temperature in Reaumur is {temp}")
elif unit == "R" and unit2 == "C":
    temp = temp * 5 / 4
    print(f"The temperature in Celcius is {temp}")
elif unit == "R" and unit2 == "F":
    temp = (temp * 9 / 4) + 32
    print(f"The temperature in Reaumur is {temp}")
elif unit == unit2 :
    print("You convert to the same unit [!]")
else :
    print("Invalid unit [!]")
