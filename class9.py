
# class Person:
#     def __init__(self, name, age, gender):  # Constructor
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def greet(self):  # Method
#         print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.gender}")

# # Create Object
# p1 = Person("Adewale", 25, 'Male')
# p2 = Person("James", 25, 'Male')
# p3 = Person("Sunday", 25, 'Male')
# p4 = Person("Thomas", 25, 'Male')
# p5 = Person("Adeyinka", 25, 'Female')
# p1.greet()
# p2.greet()
# p3.greet()
# p4.greet()
# p5.greet()



# class Car:
#     wheels = 4  # Class variable (shared)
#     def __init__(self, brand, color):
#         self.brand = brand  # Instance variable
#         self.color = color

# car1 = Car("Toyota", "Red")
# car2 = Car("BMW", "Black")

# print(car1.brand, car1.wheels)
# print(car2.brand, car2.wheels)

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# dog = Dog()
# dog.speak()
# dog.bark()
# animal = Animal()
# animal.speak()


# class BankAccount:
#     def __init__(self, balance, wallet_balnce):
#         self.wallet_balance = wallet_balnce #public
#         self.__balance = balance  # private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount(1000, 2000)
# print(acc.wallet_balance)
# print(acc.get_balance())
# acc.deposit(500)
# # print(acc.get_balance())


# file = open("example.txt", "a")
# print(file.write("\nI am a boy with a bag"))
# file.close()


# with open("example.txt", "r") as file:
#     data = file.read()
#     print(data)



# import os

# if os.path.exists("example.txt"):
#     print("File exists!")
# else:
#     print("File not found!")




import re

text = "I love Python programming"

# Search for word
x = re.search("Python", text)
print(x)  # Match found

# Find all occurrences
print(re.findall("o", text))