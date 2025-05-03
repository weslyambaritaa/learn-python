# students = {"Wesly", "Joey", "firman"}
#
# student = input("Enter a name of a student ")
#
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not found")

# grades = {"Sandy" : "A",
#           "Squidwar" : "B",
#           "Spongebob" : "C",
#           "Patrick" : "D"}
#
# student = input("Enter the name of a student: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "weslyambarita4@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
