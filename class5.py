# fruits = ['apple', 'mango', 'banana', 'orange', ]

# # popped_item = fruits.pop()
# # print(popped_item)

# print(len(fruits))        # Length of list
# print("mango" in fruits)  # Membership test
# fruits.sort()             # Sort alphabetically
# print(fruits)
# fruits.reverse()          # Reverse order
# print(fruits)

# print(fruits[1:3])   # Elements from index 1 to 2


# fruits = {"apple", "banana", "cherry", "apple"}

# fruits.add("orange")
# print(fruits) 

# # fruits.remove("pineapple")
# # print(fruits) 

# fruits.discard("pineapple") 

# print(fruits) 

# person = {
#     'name': 'Shogo',
#     'school': "Saint Agnes",
#     'height': 160.98,
#     'age': 20
# }

# for key, value in person.items():
#     print(key, "-", value)


students = [
    {"name": "Adewale", "age": 20, "coursse":  ["Math","English"]},
    {"name": "Chika", "age": 22, "courses": ["Biology", "Chemistry"]}
]

for student in students:
    print(f"{student['name']} studies {student['courses']}") 