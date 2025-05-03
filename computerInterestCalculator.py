principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("Enter the principle amount : "))
    if principle <= 0 :
        print("principle cant be less or equals to zero [!]")

while rate <= 0 :
    rate = float(input("Enter the interest rate : "))
    if rate <= 0 :
        print("Interest rate cant be less or equals to zero [!]")

while time <= 0 :
    time = float(input("Enter the time in years : "))
    if time <= 0 :
        print("Interest rate cant be less or equals to zero [!]")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s : ${total:.2f}")