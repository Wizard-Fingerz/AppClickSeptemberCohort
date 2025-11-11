
---

# 🔁 **Loops in Python**

## 🧠 **Introduction**

In programming, **loops** are used to **repeat a block of code** multiple times until a specific condition is met.

Python provides two main types of loops:

1. **`for` loop** — used to iterate over a sequence (like a list, tuple, string, or range).
2. **`while` loop** — used to execute code as long as a condition is `True`.

---

## 🌀 **1. The `for` Loop**

The `for` loop is used to **iterate over a sequence** (list, tuple, dictionary, set, or string).

### 🧩 **Syntax**

```python
for variable in sequence:
    # code block
```

### 📘 **Example**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
cherry
```

---

### 🔢 **Using `range()` with `for` Loop**

The `range()` function generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

**Output:**

```
0
1
2
3
4
```

👉 `range(5)` means from `0` to `4`.
You can also specify **start**, **stop**, and **step**:

```python
for i in range(2, 10, 2):
    print(i)
```

**Output:**

```
2
4
6
8
```

---

### 🧮 **Looping Through Strings**

```python
for letter in "Python":
    print(letter)
```

**Output:**

```
P
y
t
h
o
n
```

---

### 🧩 **Looping Through Dictionaries**

```python
student = {"name": "Adewale", "age": 20, "course": "Math"}

for key, value in student.items():
    print(key, ":", value)
```

**Output:**

```
name : Adewale
age : 20
course : Math
```

---

## 🔁 **2. The `while` Loop**

The `while` loop runs as long as a given **condition is True**.

### 🧩 **Syntax**

```python
while condition:
    # code block
```

### 📘 **Example**

```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```

**Output:**

```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

⚠️ **Be careful!**
If the condition never becomes `False`, the loop runs **forever** (infinite loop).

---

## 🚦 **Loop Control Statements**

Python provides **three** control statements to modify loop behavior:

| Statement      | Description                                             |
| -------------- | ------------------------------------------------------- |
| **`break`**    | Terminates the loop immediately                         |
| **`continue`** | Skips the current iteration and continues with the next |
| **`pass`**     | Does nothing (placeholder for future code)              |

---

### 🛑 **1. `break` Statement**

Used to exit a loop prematurely.

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

**Output:**

```
0
1
2
3
4
```

---

### ⏭️ **2. `continue` Statement**

Skips the current iteration and goes to the next one.

```python
for num in range(6):
    if num == 3:
        continue
    print(num)
```

**Output:**

```
0
1
2
4
5
```

---

### 💬 **3. `pass` Statement**

Used as a placeholder when a statement is required but no action is needed.

```python
for i in range(5):
    pass  # do nothing yet
```

---

## ⚙️ **Nested Loops**

A loop inside another loop.

### Example:

```python
for i in range(1, 4):          # Outer loop
    for j in range(1, 4):      # Inner loop
        print(f"({i}, {j})")
```

**Output:**

```
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
```

---

## 💡 **Loop with `else` Clause**

Python allows an `else` block with loops — it runs **only if the loop completes normally** (not broken by `break`).

### Example with `for`:

```python
for num in range(5):
    print(num)
else:
    print("Loop completed!")
```

**Output:**

```
0
1
2
3
4
Loop completed!
```

### Example with `while`:

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop ended!")
```

---

## 🧠 **Common Use Cases for Loops**

* Iterating through lists or dictionaries
* Performing repetitive calculations
* Searching or filtering data
* Automating repetitive tasks
* Reading files line by line

---

## ⚡ **Summary Table**

| Loop Type  | When to Use                                              | Example                    |
| ---------- | -------------------------------------------------------- | -------------------------- |
| `for`      | When iterating over a known sequence (e.g., list, range) | `for i in range(5):`       |
| `while`    | When repeating until a condition becomes False           | `while x < 10:`            |
| `break`    | Exit loop early                                          | Stop on condition          |
| `continue` | Skip iteration                                           | Skip even numbers          |
| `pass`     | Placeholder                                              | Empty loop or future logic |

---

## 🧩 **Example Program**

```python
# Sum of even numbers from 1 to 10
total = 0
for num in range(1, 11):
    if num % 2 == 0:
        total += num
print("Sum of even numbers:", total)
```

**Output:**

```
Sum of even numbers: 30
```

---
