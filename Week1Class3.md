
# 🐍 Python: Numbers and Strings

## 1. Introduction

In Python, **numbers** and **strings** are among the most commonly used data types.
They represent numeric values (for calculations) and text (for words or sentences).

---

## 2. Numbers in Python

Python supports three main **numeric types**:

| Type      | Description                                    | Example        |
| --------- | ---------------------------------------------- | -------------- |
| `int`     | Integer — whole numbers (positive or negative) | `x = 10`       |
| `float`   | Floating-point numbers (decimals)              | `pi = 3.14159` |
| `complex` | Complex numbers (real + imaginary parts)       | `z = 2 + 3j`   |

---

### (a) Integer (`int`)

* Used to store **whole numbers** (no decimal point).

```python
age = 25
print(type(age))  # <class 'int'>
```

---

### (b) Float (`float`)

* Used to store **numbers with decimal points**.

```python
price = 19.99
print(type(price))  # <class 'float'>
```

---

### (c) Complex (`complex`)

* Used in scientific and mathematical computations.
* Written as `a + bj`, where `j` is the imaginary unit.

```python
num = 2 + 3j
print(num.real)  # 2.0
print(num.imag)  # 3.0
```

---

## 3. Number Operations

You can perform various **arithmetic operations** on numbers:

| Operator | Meaning             | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `10 - 4` | `6`    |
| `*`      | Multiplication      | `6 * 2`  | `12`   |
| `/`      | Division (float)    | `7 / 2`  | `3.5`  |
| `//`     | Floor Division      | `7 // 2` | `3`    |
| `%`      | Modulus (remainder) | `7 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |

```python
a, b = 10, 3
print(a + b)   # 13
print(a ** b)  # 1000
print(a // b)  # 3
```

---

### (a) Mathematical Functions

Python’s built-in `math` module provides additional functions for numbers.

```python
import math

print(math.sqrt(16))     # 4.0
print(math.pow(2, 3))    # 8.0
print(math.ceil(4.3))    # 5
print(math.floor(4.7))   # 4
print(round(3.567, 2))   # 3.57
```

---

### (b) Type Conversion

You can convert numbers between different types using:

* `int()`, `float()`, `complex()`

```python
x = 5.7
print(int(x))     # 5
print(float(5))   # 5.0
print(complex(5)) # (5+0j)
```

---

### (c) Random Numbers

Use the `random` module to generate random numbers.

```python
import random

print(random.randint(1, 10))     # Random integer between 1 and 10
print(random.random())           # Random float between 0 and 1
print(random.choice([1, 2, 3]))  # Randomly pick from a list
```

---

## 4. Strings in Python

A **string** is a sequence of characters enclosed in **single (' ')**, **double (" ")**, or **triple quotes (''' ''' or """ """)**.

```python
name = "Python"
greeting = 'Hello'
text = """This is 
a multi-line 
string."""
```

---

### (a) String Indexing and Slicing

| Operation             | Example      | Result     |
| --------------------- | ------------ | ---------- |
| Indexing (first char) | `word[0]`    | `'P'`      |
| Last character        | `word[-1]`   | `'n'`      |
| Slice a range         | `word[1:4]`  | `'yth'`    |
| Skip characters       | `word[::2]`  | `'Pto'`    |
| Reverse string        | `word[::-1]` | `'nohtyP'` |

```python
word = "Python"
print(word[0])      # P
print(word[1:4])    # yth
print(word[::-1])   # nohtyP
```

---

### (b) String Concatenation and Repetition

```python
first = "Hello"
second = "World"

# Concatenation
print(first + " " + second)  # Hello World

# Repetition
print(first * 3)             # HelloHelloHello
```

---

### (c) String Methods

Python provides many built-in **methods** to manipulate strings:

| Method           | Description                     | Example                         |
| ---------------- | ------------------------------- | ------------------------------- |
| `.lower()`       | Converts to lowercase           | `"HELLO".lower()` → `'hello'`   |
| `.upper()`       | Converts to uppercase           | `"hi".upper()` → `'HI'`         |
| `.title()`       | Capitalizes each word           | `"hello world".title()`         |
| `.strip()`       | Removes leading/trailing spaces | `"  hello ".strip()`            |
| `.replace(a, b)` | Replace substring               | `"apple".replace("a", "A")`     |
| `.split()`       | Splits string into a list       | `"a,b,c".split(",")`            |
| `.join()`        | Joins list into a string        | `" ".join(['I', 'am', 'here'])` |
| `.find()`        | Finds index of substring        | `"hello".find('e')`             |
| `.count()`       | Counts occurrences              | `"banana".count('a')`           |

```python
text = "  Python Programming  "
print(text.strip())           # "Python Programming"
print(text.upper())           # "  PYTHON PROGRAMMING  "
print(text.replace("Python", "Java"))  # "  Java Programming  "
```

---

### (d) String Formatting

#### Using f-Strings (Recommended)

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

#### Using `format()`

```python
print("My name is {} and I am {} years old.".format("Alice", 25))
```

#### Using Percent (%) Formatting

```python
print("My name is %s and I am %d years old." % ("Alice", 25))
```

---

### (e) Escape Characters

| Code | Description  | Example                |
| ---- | ------------ | ---------------------- |
| `\n` | New line     | `"Hello\nWorld"`       |
| `\t` | Tab          | `"Name:\tJohn"`        |
| `\\` | Backslash    | `"C:\\path\\to\\file"` |
| `\'` | Single quote | `'It\'s fine'`         |
| `\"` | Double quote | `"She said \"Hi\""`    |

```python
print("Hello\nWorld")
print("It\'s a good day!")
```

---

### (f) Checking String Membership

```python
msg = "Python is fun"
print("Python" in msg)   # True
print("Java" not in msg) # True
```

---

## 5. Example Code

```python
# Numbers and Strings Example

# Numbers
a, b = 10, 3
print("Sum:", a + b)
print("Division:", a / b)
print("Power:", a ** b)

# Math functions
import math
print("Square root of 16:", math.sqrt(16))

# Strings
greet = "Hello"
lang = "Python"
message = f"{greet}, welcome to {lang} programming!"
print(message)

# String operations
print(lang[0:3])       # Pyt
print(lang.upper())    # PYTHON
print(lang[::-1])      # nohtyP
```

---

✅ **Summary**

| Concept                   | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| **Numbers**               | Includes `int`, `float`, and `complex` types                |
| **Arithmetic Operations** | `+`, `-`, `*`, `/`, `//`, `%`, `**`                         |
| **Math Functions**        | `sqrt()`, `pow()`, `ceil()`, `floor()`, `round()`           |
| **Strings**               | Sequences of characters enclosed in quotes                  |
| **String Operations**     | Indexing, slicing, concatenation, repetition                |
| **String Methods**        | `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()` |
| **Formatting**            | f-strings, `.format()`, or `%` formatting                   |

---

