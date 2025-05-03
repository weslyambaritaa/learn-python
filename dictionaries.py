 #dictionary = a collection of {key:value} pairs
 #             ordered and a=changeable. No duplicates

capitals = {"USA" : "Washingtion D.C.",
            "India" : "New Dehli",
            "China" : "Bejing",
            "Russia" : "Moscow"}

# print(dir(capitals))

print(capitals.get("USA"))
# print(capitals.get("Japan"))
#
# if capitals.get("Japan") :
#     print("That capital exist")
# else :
#     print(("That capital doesn't exist"))

# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA" : "Detroit"})
# capitals.pop(("China"))
# capitals.popitem() # for popping the last item in the dictionary
# capitals.clear() # removing all the item in the dictionary

# keys = capitals.keys()
#
# for key in capitals.keys() :
#     print(key)

# values = capitals.values()
# for key in capitals.values():
#     print(key)

# items = capitals.items()
# for key, value in capitals.items() :
#     print(f"{key} : {value}")