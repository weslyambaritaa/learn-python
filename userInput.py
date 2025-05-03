#input() = a function that prompts the user to enter data and returns the entered data as a string
name = input("What is yout name? = ")
age = input("How old are you? = ")
food = input(("What is your favourite food? = "))
favaorite_num = int(input("What is your favoritw number? = "))

favaorite_num += 1

print(f"Hello, my name is {name} and i am {age} years old and i like to eat {food} and my favorite number is {favaorite_num}")

#claculating the wide of the triangle
alas = int(input("masukkan ukuran alas : "))
tinggi = int(input("masukkan ukuran tinggi : "))
luas = 0.5 * (alas * tinggi)
print(luas)