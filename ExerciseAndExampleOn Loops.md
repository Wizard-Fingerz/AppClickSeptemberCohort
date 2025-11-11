
---

# 🧩 **Python Loop Practice Exercises**

---

## 🧠 **Exercise 1: Print Numbers from 1 to 10**

### ✅ Task

Use a `for` loop to print numbers from **1 to 10**.

### 💡 Solution

```python
for i in range(1, 11):
    print(i)
```

---

## 🧠 **Exercise 2: Print Even Numbers between 1 and 20**

### ✅ Task

Use a `for` loop to print all **even numbers** between 1 and 20.

### 💡 Solution

```python
for i in range(2, 21, 2):
    print(i)
```

*or using an if-condition:*

```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

---

## 🧠 **Exercise 3: Sum of First 10 Natural Numbers**

### ✅ Task

Find and print the **sum** of the first 10 natural numbers.

### 💡 Solution

```python
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)
```

**Output:** `Sum: 55`

---

## 🧠 **Exercise 4: Print Multiplication Table**

### ✅ Task

Print the **multiplication table** of any number entered by the user.

### 💡 Solution

```python
num = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")
```

---

## 🧠 **Exercise 5: Reverse Counting**

### ✅ Task

Print numbers from **10 down to 1** using a loop.

### 💡 Solution

```python
for i in range(10, 0, -1):
    print(i)
```

---

## 🧠 **Exercise 6: Count Digits in a Number**

### ✅ Task

Use a `while` loop to count how many digits are in a number.

### 💡 Solution

```python
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits:", count)
```

---

## 🧠 **Exercise 7: Sum of Even Numbers Using While Loop**

### ✅ Task

Find the sum of even numbers between 1 and 50 using a `while` loop.

### 💡 Solution

```python
num = 1
total = 0

while num <= 50:
    if num % 2 == 0:
        total += num
    num += 1

print("Sum of even numbers:", total)
```

---

## 🧠 **Exercise 8: Find Factorial of a Number**

### ✅ Task

Use a `for` loop to calculate the **factorial** of a given number.

### 💡 Solution

```python
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
```

---

## 🧠 **Exercise 9: Print a Pattern (Pyramid)**

### ✅ Task

Print a simple pyramid pattern using a nested loop.

### 💡 Solution

```python
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```

**Output:**

```
*
**
***
****
*****
```

---

## 🧠 **Exercise 10: Loop with Break and Continue**

### ✅ Task

Print numbers from 1 to 10, but:

* **Skip** number `5` using `continue`
* **Stop** completely at number `8` using `break`

### 💡 Solution

```python
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
```

**Output:**

```
1
2
3
4
6
7
```

---

## ⭐ **Bonus Challenge: Palindrome Checker**

### ✅ Task

Check if a given number is a palindrome (reads the same backward).

### 💡 Solution

```python
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome number!")
else:
    print("Not a palindrome.")
```

---

## 🏁 **Summary Table of Key Concepts**

| Concept                | Loop Type          | Example                      |
| ---------------------- | ------------------ | ---------------------------- |
| Count up               | `for`              | `for i in range(1, 11):`     |
| Count down             | `for`              | `for i in range(10, 0, -1):` |
| Conditional skip       | `continue`         | `if i == 5: continue`        |
| Early stop             | `break`            | `if i == 8: break`           |
| Repeat until condition | `while`            | `while x < 10:`              |
| Nested loop            | `for` inside `for` | Printing patterns            |

---

