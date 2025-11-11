
---

# **📘 Python Notes: Dates, Math Operations, Arrays, and Functions**

---

## 🕒 1. Working with Dates and Time in Python

Python provides a built-in module called **`datetime`** that allows us to work with dates and times — such as displaying the current date, formatting date output, and performing date arithmetic.

---

### **1.1 Importing the datetime Module**

To use date and time functionality, you must first import the `datetime` module.

```python
import datetime
```

---

### **1.2 Getting the Current Date and Time**

```python
import datetime

now = datetime.datetime.now()
print("Current Date and Time:", now)
```

**Output Example:**

```
Current Date and Time: 2025-10-09 13:45:22.123456
```

---

### **1.3 Displaying Only the Date or Time**

```python
today = datetime.date.today()
print("Today's Date:", today)

current_time = datetime.datetime.now().time()
print("Current Time:", current_time)
```

---

### **1.4 Accessing Individual Date/Time Components**

```python
today = datetime.date.today()
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
```

---

### **1.5 Creating Custom Dates**

```python
import datetime

my_birthday = datetime.date(2000, 5, 15)
print("My Birthday:", my_birthday)
```

---

### **1.6 Formatting Dates**

You can format dates using the **`strftime()`** method.

```python
import datetime

now = datetime.datetime.now()
formatted = now.strftime("%A, %d %B %Y")
print("Formatted Date:", formatted)
```

**Common Format Codes:**

| Code | Meaning              | Example  |
| ---- | -------------------- | -------- |
| `%Y` | Year (4 digits)      | 2025     |
| `%m` | Month (2 digits)     | 10       |
| `%B` | Month name           | October  |
| `%d` | Day of the month     | 09       |
| `%A` | Day name             | Thursday |
| `%H` | Hour (24-hour clock) | 14       |
| `%M` | Minute               | 45       |
| `%S` | Second               | 22       |

---

### **1.7 Date Arithmetic**

You can perform calculations with dates using **`timedelta`**.

```python
import datetime

today = datetime.date.today()
future = today + datetime.timedelta(days=10)
past = today - datetime.timedelta(days=5)

print("10 days from now:", future)
print("5 days ago:", past)
```

---

## 🔢 2. Math Operations in Python

Python supports a variety of mathematical operations using basic operators and the **`math`** module for advanced calculations.

---

### **2.1 Basic Arithmetic Operators**

| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | 8      |
| `-`      | Subtraction         | `9 - 4`  | 5      |
| `*`      | Multiplication      | `2 * 6`  | 12     |
| `/`      | Division            | `8 / 2`  | 4.0    |
| `//`     | Floor Division      | `7 // 3` | 2      |
| `%`      | Modulus (remainder) | `10 % 3` | 1      |
| `**`     | Exponentiation      | `2 ** 3` | 8      |

---

### **2.2 Using the `math` Module**

```python
import math

print(math.sqrt(25))      # Square root
print(math.pow(2, 5))     # Power
print(math.pi)            # Value of Pi
print(math.sin(math.pi))  # Trigonometric functions
```

**Other Useful Functions:**

| Function            | Description | Example             | Result   |
| ------------------- | ----------- | ------------------- | -------- |
| `math.ceil(x)`      | Rounds up   | `math.ceil(4.2)`    | 5        |
| `math.floor(x)`     | Rounds down | `math.floor(4.8)`   | 4        |
| `math.factorial(x)` | Factorial   | `math.factorial(5)` | 120      |
| `math.log(x)`       | Natural log | `math.log(10)`      | 2.302... |

---

## 🧮 3. Arrays in Python

Arrays are used to store multiple values in a single variable, just like lists.
However, unlike lists, arrays **store only elements of the same type**.

---

### **3.1 Using the `array` Module**

```python
import array

# Create an integer array
numbers = array.array('i', [1, 2, 3, 4, 5])
print(numbers)
```

**Common Type Codes:**

| Code  | Type  | Description            |
| ----- | ----- | ---------------------- |
| `'i'` | int   | Signed integer         |
| `'f'` | float | Floating point number  |
| `'d'` | float | Double precision float |
| `'u'` | str   | Unicode character      |

---

### **3.2 Accessing and Modifying Array Elements**

```python
import array

nums = array.array('i', [10, 20, 30, 40])

print(nums[0])   # Access first element
nums[1] = 25     # Modify second element
print(nums)
```

---

### **3.3 Adding and Removing Elements**

```python
nums = array.array('i', [1, 2, 3])
nums.append(4)
nums.insert(1, 5)
nums.remove(2)

print(nums)
```

---

### **3.4 Looping Through an Array**

```python
for n in nums:
    print(n)
```

---

## 🧠 4. Functions in Python

Functions are reusable blocks of code that perform a specific task.
They make your code **modular**, **organized**, and **easy to maintain**.

---

### **4.1 Defining a Function**

```python
def greet():
    print("Hello, World!")
```

To **call** a function:

```python
greet()
```

---

### **4.2 Function with Parameters**

```python
def greet_user(name):
    print("Hello,", name)

greet_user("Adewale")
```

---

### **4.3 Function with Return Value**

```python
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
```

---

### **4.4 Default Parameters**

```python
def greet(name="Guest"):
    print("Welcome,", name)

greet()           # Uses default
greet("Tunde")    # Custom value
```

---

### **4.5 Keyword Arguments**

```python
def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=25, name="Bola")
```

---

### **4.6 Variable-Length Arguments**

#### *args (Non-keyword arguments)*

```python
def sum_all(*numbers):
    total = sum(numbers)
    print("Sum:", total)

sum_all(1, 2, 3, 4, 5)
```

#### **kwargs (Keyword arguments)**

```python
def person_info(**info):
    print(info)

person_info(name="Adewale", age=23, city="Ibadan")
```

---

### **4.7 Returning Multiple Values**

```python
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

x, y = calculate(10, 4)
print("Sum:", x, "Difference:", y)
```

---

### **4.8 Lambda Functions (Anonymous Functions)**

Lambda functions are small one-line functions.

```python
square = lambda x: x ** 2
print(square(5))
```

---

### **4.9 Nested Functions**

```python
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()
```

---

## ✅ Summary

| Concept       | Module     | Key Functions/Uses                             |
| ------------- | ---------- | ---------------------------------------------- |
| **Dates**     | `datetime` | `datetime.now()`, `strftime()`, `timedelta()`  |
| **Math**      | `math`     | `sqrt()`, `pow()`, `ceil()`, `pi`              |
| **Array**     | `array`    | `.append()`, `.insert()`, `.remove()`          |
| **Functions** | Built-in   | `def`, `return`, `*args`, `**kwargs`, `lambda` |

---

## 💡 Practice Exercises

1. Display the current date and time in the format `Day-Month-Year Hour:Minute:Second`.
2. Create a function that returns the square and cube of a number.
3. Write a program that adds 10 days to the current date.
4. Create an array of 5 numbers, remove the last one, and print the result.
5. Use `math` functions to find the square root of 144 and round it up.

---
