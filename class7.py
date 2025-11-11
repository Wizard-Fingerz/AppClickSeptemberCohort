from calendar import month
import datetime

# print(datetime.datetime.now().time())

# today = datetime.date.today()
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)



# my_birthday = datetime.date(2000, 5, 15)
# print("My Birthday:", my_birthday)


# now = datetime.datetime.now()
# formatted = now.strftime("%A, %d %B %Y")
# print("Formatted Date:", formatted)


# today = datetime.date.today()
# future = today + datetime.timedelta(days=10)
# past = today - datetime.timedelta(days=5)

# print("10 days from now:", future)
# print("5 days ago:", past)


# import array

# # Create an integer array
# numbers = array.array('f', [1, 2, 3, 4, 5])
# print(numbers)
# print(numbers[0])
# numbers.append(4)
# numbers.insert(1, 5)
# print(numbers)
# numbers.remove(2)
# print(numbers)

# for num in numbers:
#     print(num)


# def greet(name, age, height):
#     print(f'Hello, {name}. You are {age} years old, and your height is {height}')


# greet(name= 'Segun', height = 120.34, age = 20)


# def add(a, b = 2):
#     return a + b

# x = add(2, 44)

# print(x)



# def sum_all(*numbers):
#     total = sum(numbers)
#     print("Sum:", total)

# sum_all(1, 2, 3, 4, 5)


# def person_info(**info):
#     print(info)

# person_info(name="Adewale", age=23, city="Ibadan")



def calculate(a, b):
    sum_ = a + b
    diff = a - b
    mult = a * b
    return sum_, diff, mult

x, y, z = calculate(10, 4)
print("Sum:", x, "Difference:", y, "Mult:", z)


calculate = lambda a, b: a * b
print(calculate(5, 4))