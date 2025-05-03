name = input("Enter your name : ")

while name == "" :
    print("You did not enter your name [!]")
    name = input("Enter your name : ")

print(f"Hello {name}")

age = int(input("enter your age : "))

while age < 0 or age == "":
    print("Age cant be lower than 0 [!]")
    age = input("enter your age : ")
else :
    print(f"Hello, my name is {name} and i am {age} years old")