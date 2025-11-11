
# 🐍 Python: Data Types and Operations

## 1. Introduction

In Python, **data types** define the kind of values a variable can hold and the possible **operations** that can be performed on them. Python is **dynamically typed**, meaning the type is assigned automatically when a value is stored.

---

## 2. Built-in Data Types in Python

Python has several standard data types, grouped as follows:

### (a) Numeric Types

* **Integer (`int`)** → whole numbers
* **Float (`float`)** → decimal numbers
* **Complex (`complex`)** → numbers with real and imaginary parts

```python
x = 10         # int
y = 3.14       # float
z = 2 + 3j     # complex
```

---

### (b) Sequence Types

* **String (`str`)** → text inside quotes
* **List (`list`)** → ordered, mutable collection
* **Tuple (`tuple`)** → ordered, immutable collection

```python
s = "Hello"              # string
fruits = ["apple", "banana", "cherry"]  # list
point = (3, 5)           # tuple
```

---

### (c) Set Types

* **Set (`set`)** → unordered collection of unique items
* **Frozen Set (`frozenset`)** → immutable version of a set

```python
nums = {1, 2, 3, 3}          # {1, 2, 3}
frozen = frozenset([1, 2, 2, 3])
```

---

### (d) Mapping Type

* **Dictionary (`dict`)** → key-value pairs

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
```

---

### (e) Boolean Type

* **Boolean (`bool`)** → `True` or `False`

```python
is_active = True
has_passed = False
```

---

### (f) None Type

* **None (`NoneType`)** → represents absence of a value

```python
result = None
```

---

## 3. Operations in Python

Operations depend on the data type.

---

### (a) Arithmetic Operations (for `int`, `float`, `complex`)

| Operator | Description         | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `5 + 3 → 8`   |
| `-`      | Subtraction         | `10 - 4 → 6`  |
| `*`      | Multiplication      | `6 * 2 → 12`  |
| `/`      | Division (float)    | `7 / 2 → 3.5` |
| `//`     | Floor Division      | `7 // 2 → 3`  |
| `%`      | Modulus (remainder) | `7 % 2 → 1`   |
| `**`     | Exponentiation      | `2 ** 3 → 8`  |

```python
a, b = 10, 3
print(a + b)   # 13
print(a / b)   # 3.333...
print(a // b)  # 3
```

---

### (b) Comparison Operations

Used to compare values. Returns a **Boolean** (`True` or `False`).

| Operator | Meaning               | Example         |
| -------- | --------------------- | --------------- |
| `==`     | Equal                 | `5 == 5 → True` |
| `!=`     | Not equal             | `5 != 3 → True` |
| `>`      | Greater than          | `7 > 4 → True`  |
| `<`      | Less than             | `2 < 5 → True`  |
| `>=`     | Greater than or equal | `6 >= 6 → True` |
| `<=`     | Less than or equal    | `3 <= 5 → True` |

```python
x, y = 10, 20
print(x == y)  # False
print(x < y)   # True
```

---

### (c) Logical Operations

Used with `bool` values.

| Operator | Meaning                      | Example                  |
| -------- | ---------------------------- | ------------------------ |
| `and`    | True if both are true        | `True and False → False` |
| `or`     | True if at least one is true | `True or False → True`   |
| `not`    | Negates the boolean value    | `not True → False`       |

```python
x = 5
print(x > 2 and x < 10)   # True
print(x < 2 or x > 10)    # False
print(not(x > 2))         # False
```

---

### (d) Assignment Operations

Assign values with operators.

| Operator | Example   | Equivalent   |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | Assign 5     |
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 2`  | `x = x - 2`  |
| `*=`     | `x *= 4`  | `x = x * 4`  |
| `/=`     | `x /= 2`  | `x = x / 2`  |
| `%=`     | `x %= 3`  | `x = x % 3`  |
| `**=`    | `x **= 2` | `x = x ** 2` |

```python
x = 10
x += 5
print(x)  # 15
```

---

### (e) String Operations

```python
s1 = "Hello"
s2 = "World"

# Concatenation
print(s1 + " " + s2)   # Hello World

# Repetition
print(s1 * 3)          # HelloHelloHello

# Indexing
print(s1[0])           # H

# Slicing
print(s1[1:4])         # ell

# Length
print(len(s1))         # 5

# Membership
print("H" in s1)       # True
print("x" not in s1)   # True
```

---

### (f) List Operations

```python
numbers = [1, 2, 3, 4]

# Indexing
print(numbers[0])     # 1

# Slicing
print(numbers[1:3])   # [2, 3]

# Append
numbers.append(5)
print(numbers)
# Remove
numbers.remove(2)

# Length
print(len(numbers))   # 4
```

---

### (g) Dictionary Operations

```python
student = {"name": "Alice", "age": 20}

# Access by key
print(student["name"])      # Alice

# Add new key
student["grade"] = "A"

# Keys and values
print(student.keys())       # dict_keys(['name', 'age', 'grade'])
print(student.values())     # dict_values(['Alice', 20, 'A'])
```

---

### (h) Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric difference → {1, 2, 4, 5}
```

---

## 4. Type Conversion (Casting)

* **Implicit conversion**: Python automatically converts types when safe.

```python
x = 5      # int
y = 2.5    # float
z = x + y  # float
print(z)   # 7.5
```

* **Explicit conversion**: Using functions `int()`, `float()`, `str()`, `list()`, etc.

```python
a = int("10")    # String → Integer
b = float(5)     # Int → Float
c = str(100)     # Int → String
```

---

## 5. Example Program

```python
# Data Types and Operations Example

x, y = 15, 4

print("Arithmetic Operations")
print(x + y, x - y, x * y, x / y, x % y, x ** y)

print("\nComparison Operations")
print(x > y, x == y, x != y)

print("\nLogical Operations")
print(x > 10 and y < 10)
print(not(x < y))

print("\nString Operations")
name = "Python"
print(name[0], name[1:4], name * 2)

print("\nList Operations")
nums = [1, 2, 3]
nums.append(4)
print(nums)

print("\nDictionary Operations")
student = {"name": "John", "age": 21}
student["grade"] = "B"
print(student)

print("\nSet Operations")
a, b = {1, 2, 3}, {3, 4, 5}
print(a | b, a & b)
```

---

✅ **Summary**

* Python supports **numeric, sequence, set, mapping, boolean, and None** data types.
* Operations include **arithmetic, comparison, logical, assignment, string, list, dict, and set operations**.
* **Type conversion** can be implicit (automatic) or explicit (manual).

