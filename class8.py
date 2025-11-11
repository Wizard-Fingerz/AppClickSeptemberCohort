
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_ = num1 + num2
# print("The sum is:", sum_)



# x, y = input("Enter two numbers separated by comma: ").split(',')
# x = int(x)
# y = int(y)
# print("Sum:", x + y)

# number = int(input("Enter a number: "))
# print("You entered:", number)

# try:
#     # Code that might cause an error
#     number = int(input("Enter a number: "))
#     print("You entered:", number)
# except:
#     # Code that runs if an error occurs
#     print("Oops! That was not a valid number.")


# a = int(input("Enter numerator: "))
# b = int(input("Enter denominator: "))
# result = a / b
# print("Result:", result)

# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")



# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("You must enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("Program finished.")