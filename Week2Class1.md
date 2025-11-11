
---

# 🐍 Python: Conditions and Conditional Statements

## 1. Introduction

In programming, **conditions** allow you to make **decisions** based on certain situations.
They enable your program to **execute different blocks of code** depending on whether a condition is **True** or **False**.

Python uses **conditional statements** (also known as *control flow statements*) to handle decision-making.

---

## 2. Boolean Expressions

A **Boolean expression** is an expression that evaluates to either **`True`** or **`False`**.

Examples:

```python
5 > 3        # True
10 == 5      # False
"cat" != "dog"  # True
```

Boolean expressions are formed using **comparison operators**.

---

## 3. Comparison Operators

| Operator | Meaning                  | Example    | Result |
| -------- | ------------------------ | ---------- | ------ |
| `==`     | Equal to                 | `5 == 5`   | True   |
| `!=`     | Not equal to             | `5 != 3`   | True   |
| `>`      | Greater than             | `10 > 2`   | True   |
| `<`      | Less than                | `4 < 8`    | True   |
| `>=`     | Greater than or equal to | `10 >= 10` | True   |
| `<=`     | Less than or equal to    | `7 <= 9`   | True   |

---

## 4. Logical Operators

Used to combine multiple conditions.

| Operator | Meaning                      | Example                | Result |
| -------- | ---------------------------- | ---------------------- | ------ |
| `and`    | True if both are True        | `(5 > 3) and (10 > 8)` | True   |
| `or`     | True if at least one is True | `(5 > 10) or (10 > 8)` | True   |
| `not`    | Reverses True/False          | `not(5 > 3)`           | False  |

Example:

```python
age = 18
country = "Nigeria"
if age >= 18 and country == "Nigeria":
    print("You are eligible to vote.")
```

---

## 5. The `if` Statement

The `if` statement checks a condition and executes a block of code **only if** the condition is `True`.

### Syntax:

```python
if condition:
    # code to execute if condition is true
```

### Example:

```python
age = 20
if age >= 18:
    print("You are an adult.")
```

Output:

```
You are an adult.
```

---

## 6. The `if...else` Statement

Use `else` when you want to run one block if the condition is true and another block if it is false.

### Syntax:

```python
if condition:
    # code if true
else:
    # code if false
```

### Example:

```python
age = int(input('Enter age:'))
if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")
```

Output:

```
You are too young to vote.
```

---

## 7. The `if...elif...else` Statement

Use `elif` (short for *else if*) when you have **multiple conditions** to check.

### Syntax:

```python
if condition1:
    # code block 1
elif condition2:
    # code block 2
else:
    # code block 3
```

### Example:

```python
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

Output:

```
Good
```

---

## 8. Nested `if` Statements

An `if` statement can be placed inside another `if` block — this is called a **nested condition**.

### Example:

```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are too young to vote.")
```

Output:\```
You are eligible to vote.
```

---

## 9. The `pass` Statement

If you want to create a conditional block but don’t want it to do anything yet, use `pass`.
It prevents syntax errors in empty blocks.

```python
x = 10
if x > 5:
    pass  # do nothing for now
```

---

## 10. The `in` and `not in` Operators (Membership Tests)

These operators are used to check if a value exists within a sequence (like a list, tuple, or string).

| Operator | Meaning                | Example              | Result |
| -------- | ---------------------- | -------------------- | ------ |
| `in`     | True if item is found  | `"a" in "apple"`     | True   |
| `not in` | True if item not found | `"z" not in "apple"` | True   |

Example:

```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list.")
```

---

## 11. Conditional Expressions (Ternary Operator)

A **short form** of `if-else` for simple decisions.

### Syntax:

```python
value_if_true if condition else value_if_false
```

### Example:

```python
age = 18
message = "Adult" if age >= 18 else "Minor"
print(message)
```

Output:

```
Adult
```

---

## 12. Combining Conditions

You can combine multiple conditions using `and`, `or`, and `not`.

```python
temperature = 30
raining = False

if temperature > 25 and not raining:
    print("It’s a good day for swimming!")
else:
    print("Stay indoors.")
```

Output:

```
It’s a good day for swimming!
```

---

## 13. Example Program

```python
# Example: Grading System

score = int(input("Enter your score: "))

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")
```

Sample Output:

```
Enter your score: 65
Your grade is B
```

---

## 14. Common Mistakes to Avoid

❌ **Using assignment (=) instead of comparison (==):**

```python
if x = 5:   # ❌ Wrong
```

✅ Correct:

```python
if x == 5:
```

❌ **Forgetting indentation:**

```python
if x > 0:
print("Positive")   # ❌ Wrong indentation
```

✅ Correct:

```python
if x > 0:
    print("Positive")
```

---

## 15. Real-Life Example

```python
# Check eligibility for scholarship
gpa = float(input("Enter your GPA: "))
income = int(input("Enter your annual income: "))

if gpa >= 3.5 and income < 50000:
    print("You are eligible for the scholarship.")
elif gpa >= 3.5 and income >= 50000:
    print("You qualify but need to apply for partial support.")
else:
    print("You are not eligible.")
```

---

✅ **Summary Table**

| Statement          | Description                                   |
| ------------------ | --------------------------------------------- |
| `if`               | Executes code when condition is true          |
| `else`             | Executes code when condition is false         |
| `elif`             | Checks additional conditions                  |
| `nested if`        | Places one condition inside another           |
| `and`, `or`, `not` | Combine or invert conditions                  |
| `in`, `not in`     | Check membership in lists, tuples, or strings |
| `pass`             | Placeholder for future code                   |
| `Ternary`          | Short single-line conditional                 |

---
