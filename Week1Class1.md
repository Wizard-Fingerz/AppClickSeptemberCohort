# 🐍 Python: Introduction to Python Syntax and Variables

## 1. Introduction to Python

Python is a **high-level, interpreted, object-oriented programming language** known for its **simplicity** and **readability**. It was created by **Guido van Rossum** and first released in 1991.

Key features of Python include:

* Easy-to-read syntax (resembles English)
* Dynamically typed (no need to declare variable types explicitly)
* Interpreted (executed line by line)
* Extensive standard library
* Cross-platform and widely used in web development, data science, AI, automation, and more.

 ---

## 2. Python Syntax Basics

### (a) Case Sensitivity

* Python is **case-sensitive**.

```python
name = "Alice"
Name = "Bob"
print(name)  # Alice
print(Name)  # Bob
```

### (b) Indentation

* **Indentation** is crucial in Python (unlike other languages that use `{}` braces).
* Default is **4 spaces**, but consistency is key.

```python
if True:
    print("This is indented")   # Correct
#   print("This will cause an error")   # Incorrect indentation
```

### (c) Comments

* Comments improve code readability.

```python
# This is a single-line comment

"""
This is a
multi-line comment
"""
```

### (d) Printing Output

* Use the `print()` function.

```python
print("Hello, World!")
```

---

## 3. Python Variables

A **variable** is a name that refers to a value stored in memory.

### (a) Creating Variables

* No need to declare type explicitly; Python infers it.

```python
x = 10        # Integer
name = "John" # String
pi = 3.14     # Float
```

### (b) Variable Naming Rules

* Must begin with a letter or underscore `_`
* Can contain letters, numbers, and underscores
* Cannot be a Python keyword (`if`, `class`, `while`, etc.)
* Case-sensitive

✅ Valid: `age`, `student_name`, `_score1`
❌ Invalid: `1name`, `class`, `my-name`

---

## 4. Data Types in Variables

Python supports multiple **built-in data types**:

| Data Type          | Example                                  |
| ------------------ | ---------------------------------------- |
| **Integer (int)**  | `age = 25`                               |
| **Float (float)**  | `price = 19.99`                          |
| **String (str)**   | `name = "Alice"`                         |
| **Boolean (bool)** | `is_active = True`                       |
| **List**           | `fruits = ["apple", "banana", "cherry"]` |
| **Tuple**          | `coordinates = (10, 20)`                 |
| **Dictionary**     | `student = {"name": "John", "age": 20, "height": "160cm"}`  |
| **Set**            | `unique_nums = {1, 2, 3, 3}`             |

---

## 5. Assigning Values to Variables

### (a) Single Assignment

```python
x = 100
y = "Hello"
```

### (b) Multiple Assignment

```python
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
```

### (c) One Value to Multiple Variables

```python
x = y = z = 50
print(x, y, z)  # 50 50 50
```

---

## 6. Type Checking and Type Casting

### (a) Checking Type

```python
num = 10
print(type(num))  # <class 'int'>
```

### (b) Type Casting (Conversion)

```python
x = int("10")     # Convert string to int
y = float(5)      # Convert int to float
z = str(25)       # Convert int to string
print(x, y, z)    # 10 5.0 '25'
```

---

## 7. Constants in Python

* Python does not have true constants.
* By convention, **uppercase variable names** are treated as constants.

```python
PI = 3.14159
GRAVITY = 9.8
```

---

## 8. Input from Users

* Use `input()` to take user input.
* Input is always received as a **string**, so conversion is needed.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.")
```

---

## 9. Reserved Keywords in Python

* Python has a set of reserved words that cannot be used as variable names. Examples:

`False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield`

---

## 10. Example Code (Putting It All Together)

```python
# Python Syntax and Variables Example

# Variables
name = "Alice"
age = 21
height = 5.6
is_student = True

# Printing
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Type conversion
num_str = "50"
num_int = int(num_str)
print("Converted number:", num_int)

# User input
city = input("Enter your city: ")
print("You live in", city)
```

---

✅ **Summary**

* Python is beginner-friendly with simple syntax.
* Indentation defines blocks of code.
* Variables are dynamically typed (no type declaration needed).
* Supports many data types: `int`, `float`, `str`, `bool`, `list`, etc.
* Input/output is handled using `input()` and `print()`.
* Constants are not enforced, but uppercase naming is convention.

