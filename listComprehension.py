# doubles = []
# for x in range (1,11):
#     doubles.append(x * 2)
#
# print(doubles)

doubles = [x*2 for x in range (1,11)]
print(doubles)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
