
---

# **📘 Python Notes: User Input & Error Handling (try–except)**

---

## 🧍‍♂️ 1. User Input in Python

When writing programs, we often need to **get information from users** — like their name, age, or any other data.
Python provides the **`input()`** function to collect data from the user.

---

### **1.1 Using the `input()` Function**

The `input()` function **pauses program execution** and waits for the user to type something.
Whatever the user types is returned as a **string**.

```python
name = input("Enter your name: ")
print("Hello", name)
```

**Output:**

```
Enter your name: Adewale
Hello Adewale
```

---

### **1.2 Important: Input Always Returns a String**

Even if you type a number, Python treats it as a **string**.

```python
age = input("Enter your age: ")
print(type(age))
```

**Output:**

```
<class 'str'>
```

---

### **1.3 Converting Input to Numbers**

To perform mathematical operations, you must **convert input to integers or floats**.

```python
age = int(input("Enter your age: "))
print("You are", age, "years old.")
```

or

```python
price = float(input("Enter the price: "))
print("Price with tax:", price * 1.05)
```

---

### **1.4 Example: Adding Two Numbers**

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_ = num1 + num2
print("The sum is:", sum_)
```

---

### **1.5 Example: Taking Multiple Inputs**

You can take multiple inputs in one line using **`split()`**.

```python
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)
```

**Sample Input:**

```
Enter two numbers separated by space: 5 10
```

**Output:**

```
Sum: 15
```

---

### **1.6 Example: Using f-string with Input**

```python
name = input("What is your name? ")
course = input("Which course are you taking? ")

print(f"Welcome {name}! You are enrolled in {course}.")
```

---

## ⚠️ 2. Error Handling in Python

Sometimes, your program may **crash** when users give wrong input or when something unexpected happens (e.g., dividing by zero, opening a missing file, etc.).

Python provides **error handling** using the **`try` and `except`** blocks to **prevent crashes** and handle errors gracefully.

---

### **2.1 The `try` and `except` Structure**

```python
try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    print("You entered:", number)
except:
    # Code that runs if an error occurs
    print("Oops! That was not a valid number.")
```

If the user enters a non-numeric value, instead of crashing, the program prints the message inside `except`.

---

### **2.2 Example: Handling Division by Zero**

```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
```

---

### **2.3 Catching Specific Errors**

You can handle **different types of errors** separately.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("You must enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

### **2.4 Using `else` and `finally` with try–except**

| Block     | Purpose                                          |
| --------- | ------------------------------------------------ |
| `try`     | Contains code that might cause an error          |
| `except`  | Handles the error                                |
| `else`    | Runs if no error occurs                          |
| `finally` | Runs no matter what happens (useful for cleanup) |

Example:

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("Program finished.")
```

**Output Example:**

```
Enter a number: 10
You entered: 10
Program finished.
```

---

### **2.5 Raising Your Own Errors**

You can use the **`raise`** keyword to throw (raise) your own exceptions.

```python
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")
else:
    print("Age recorded:", age)
```

---

### **2.6 Example: Combining Input and Error Handling**

```python
while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid number! Please try again.")
```

✅ This loop keeps asking for input until the user enters a valid number.

---

## 🧠 3. Why Use Error Handling?

Error handling makes programs:

* More **user-friendly**
* More **reliable**
* Easier to **debug**
* Resistant to **crashes**

---

## ✅ 4. Common Python Error Types

| Error Type          | Description                      | Example           |
| ------------------- | -------------------------------- | ----------------- |
| `ValueError`        | Wrong data type                  | `int("abc")`      |
| `ZeroDivisionError` | Division by zero                 | `10 / 0`          |
| `TypeError`         | Operation on incompatible types  | `"5" + 3`         |
| `NameError`         | Undefined variable               | `print(x)`        |
| `IndexError`        | Accessing invalid list index     | `[1, 2, 3][5]`    |
| `KeyError`          | Accessing invalid dictionary key | `my_dict["age"]`  |
| `FileNotFoundError` | Missing file                     | `open("abc.txt")` |

---

## 💻 5. Practical Examples

### Example 1: Safe Calculator

```python
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)
    print("Division:", a / b)
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

### Example 2: Login System with Input Validation

```python
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "" or password == "":
        raise ValueError("Username or password cannot be empty.")

    print(f"Welcome, {username}!")
except ValueError as e:
    print(e)
```

---

### Example 3: File Reading with Error Handling

```python
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found!")
```

---

## 📝 6. Summary

| Concept         | Description                   | Example                           |
| --------------- | ----------------------------- | --------------------------------- |
| `input()`       | Collects user input as string | `name = input("Enter name: ")`    |
| Type Conversion | Converts input to number      | `age = int(input("Enter age: "))` |
| `try`           | Test code for errors          | `try: num = int(input())`         |
| `except`        | Handle the error              | `except ValueError: ...`          |
| `else`          | Runs if no error occurs       | `else: print("Success")`          |
| `finally`       | Runs always                   | `finally: print("Done")`          |

---

## 🧩 7. Practice Exercises

1. Write a program to ask the user for two numbers and divide the first by the second, handling division by zero.
2. Create a program that asks for the user’s age and ensures it’s a positive integer.
3. Ask the user for their name and print it in uppercase.
4. Write a loop that continues asking for a valid number until the user enters one.
5. Build a simple calculator using `try` and `except` to handle invalid inputs.
6. Handle `FileNotFoundError` when trying to open a missing file.
7. Raise a custom error if the user enters a password shorter than 6 characters.

---

