# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you ti pass multiple keyword-arguments
#           * unpacking operator
#           1. positional 2. defaults 3. keyword 4. ARBITARY

# def add(*args):
#     total = 0
#     for arg in args:
#         total += args
#     return total
#
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
#
# # print(add(1, 2, 3))
# display_name("Dr.", "Wesly", "Fery", "Wanda", "Ambarita")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
#
#
# print_address(street="Bahkota atas",
#               city="Siantar",
#               state="Sumut",
#               zip="4231")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(f"{value}", end=" ")
    print(f"{kwargs.get('street')}")

shipping_label("Dr.", "Wesly", "Fery", "Wanda", "Ambarita",
               street="Bahkota atas",
               city="Siantar",
                state="Sumut",
                zip="4231"
               )

