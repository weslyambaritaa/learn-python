def happy_birthday(name, age) :
    print(f"Happy birthday to {name}")
    print(f"You are getting older with {age} years old")
    print()

# happy_birthday("Bro", 19)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due to: {due_date}")

# display_invoice("Wesly", 50, "29/01")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def devide(x, y):
    z = x / y
    return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(devide( 1,2))

def create_name (first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("wesly", "Ambarita")

print(full_name)

