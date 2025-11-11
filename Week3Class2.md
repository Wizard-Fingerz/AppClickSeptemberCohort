
---

# **📘 Python Notes: Object-Oriented Programming, File Management & Regular Expressions**

---

## 🧱 **1. Object-Oriented Programming (OOP) in Python**

Object-Oriented Programming (OOP) is a **programming paradigm** that organizes code into **objects** — which bundle together **data (attributes)** and **functions (methods)**.

It helps make programs:

* More **organized**
* Easier to **maintain**
* Easier to **reuse**

---

### **1.1 Core OOP Concepts**

| Concept           | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| **Class**         | A blueprint or template for creating objects                      |
| **Object**        | An instance of a class                                            |
| **Attributes**    | Variables that belong to an object                                |
| **Methods**       | Functions that belong to an object                                |
| **Encapsulation** | Hiding details of how things work internally                      |
| **Inheritance**   | Ability to create a new class from an existing one                |
| **Polymorphism**  | Ability of methods to behave differently based on the object type |

---

### **1.2 Defining a Class and Creating an Object**

```python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create Object
p1 = Person("Adewale", 25)
p1.greet()
```

**Output:**

```
Hello, my name is Adewale and I am 25 years old.
```

---

### **1.3 The `__init__` Method (Constructor)**

* Runs automatically when an object is created.
* Initializes the object’s data (attributes).

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
```

---

### **1.4 Class and Instance Variables**

```python
class Car:
    wheels = 4  # Class variable (shared)
    def __init__(self, brand, color):
        self.brand = brand  # Instance variable
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)
```

---

### **1.5 Inheritance**

Inheritance allows a class to use properties and methods of another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()
```

---

### **1.6 Method Overriding**

Child classes can **override** parent methods.

```python
class Animal:
    def speak(self):
        print("Generic animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat()
cat.speak()
```

---

### **1.7 Encapsulation (Private Attributes)**

Use **`__`** before a variable name to make it private.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
```

---

### **1.8 Polymorphism**

Polymorphism allows objects of different classes to be used interchangeably.

```python
class Bird:
    def sound(self):
        print("Chirp")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Bird(), Dog()]:
    animal.sound()
```

---

### **1.9 OOP Summary Table**

| Concept       | Keyword                              | Example               |
| ------------- | ------------------------------------ | --------------------- |
| Class         | `class`                              | `class Person:`       |
| Object        | Instance                             | `p1 = Person()`       |
| Constructor   | `__init__`                           | Initialize attributes |
| Inheritance   | `class Child(Parent):`               | Code reuse            |
| Polymorphism  | Same method name, different behavior | `speak()`             |
| Encapsulation | Private variables                    | `__balance`           |

---

## 📁 **2. File Management in Python**

Python allows you to **read**, **write**, and **manipulate files** using the built-in `open()` function.

---

### **2.1 Opening Files**

```python
file = open("example.txt", "r")
```

**Modes:**

| Mode  | Meaning                 | Use                    |
| ----- | ----------------------- | ---------------------- |
| `'r'` | Read                    | Default mode           |
| `'w'` | Write (overwrites file) | Create or replace file |
| `'a'` | Append                  | Add to end of file     |
| `'x'` | Create                  | Fails if file exists   |
| `'b'` | Binary                  | Images, etc.           |
| `'t'` | Text                    | Default mode           |

---

### **2.2 Reading from a File**

```python
file = open("data.txt", "r")
print(file.read())
file.close()
```

**Read first 10 characters:**

```python
print(file.read(10))
```

**Read one line:**

```python
print(file.readline())
```

**Read all lines into a list:**

```python
lines = file.readlines()
print(lines)
```

---

### **2.3 Writing to a File**

```python
file = open("newfile.txt", "w")
file.write("Hello, Python File Handling!")
file.close()
```

---

### **2.4 Appending Data**

```python
file = open("newfile.txt", "a")
file.write("\nThis line was appended.")
file.close()
```

---

### **2.5 Using the `with` Statement (Best Practice)**

Automatically closes files even if an error occurs.

```python
with open("newfile.txt", "r") as file:
    data = file.read()
    print(data)
```

---

### **2.6 Checking if a File Exists**

```python
import os

if os.path.exists("newfile.txt"):
    print("File exists!")
else:
    print("File not found!")
```

---

### **2.7 Deleting a File**

```python
import os
os.remove("newfile.txt")
```

---

### **2.8 Example: Counting Words in a File**

```python
with open("data.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Number of words:", len(words))
```

---

## 🔍 **3. Regular Expressions (Regex) in Python**

Regular Expressions (**regex**) are patterns used to **search**, **match**, or **replace** text.

Python provides the **`re`** module for regex operations.

---

### **3.1 Importing the `re` Module**

```python
import re
```

---

### **3.2 Common Regex Functions**

| Function       | Description                                 |
| -------------- | ------------------------------------------- |
| `re.search()`  | Searches for a pattern anywhere in a string |
| `re.match()`   | Checks if pattern matches at the beginning  |
| `re.findall()` | Returns all matches in a list               |
| `re.split()`   | Splits string by pattern                    |
| `re.sub()`     | Replaces pattern with new text              |

---

### **3.3 Basic Examples**

```python
import re

text = "I love Python programming"

# Search for word
x = re.search("Python", text)
print(x)  # Match found

# Find all occurrences
print(re.findall("o", text))
```

---

### **3.4 Using Special Characters**

| Symbol | Meaning               | Example          | Matches              |      |                |
| ------ | --------------------- | ---------------- | -------------------- | ---- | -------------- |
| `.`    | Any character         | `p.thon`         | “python”             |      |                |
| `^`    | Start of string       | `^Hello`         | “Hello world”        |      |                |
| `$`    | End of string         | `world$`         | “Hello world”        |      |                |
| `*`    | 0 or more repetitions | `ab*`            | “a”, “abbb”          |      |                |
| `+`    | 1 or more repetitions | `ab+`            | “ab”, “abb”          |      |                |
| `?`    | Optional character    | `ab?`            | “a”, “ab”            |      |                |
| `{n}`  | Exactly n times       | `a{3}`           | “aaa”                |      |                |
| `[ ]`  | Set of characters     | `[A-Z]`          | Any uppercase letter |      |                |
| `      | `                     | OR               | `cat                 | dog` | “cat” or “dog” |
| `\d`   | Digit                 | `\d+`            | “123”                |      |                |
| `\w`   | Word character        | `[a-zA-Z0-9_]`   |                      |      |                |
| `\s`   | Whitespace            | space, tab, etc. |                      |      |                |

---

### **3.5 Example: Validate an Email Address**

```python
import re

email = input("Enter your email: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email!")
else:
    print("Invalid email!")
```

---

### **3.6 Example: Find All Phone Numbers**

```python
import re

text = "Call 08012345678 or 09123456789"
phones = re.findall(r"\d{11}", text)
print("Phone Numbers:", phones)
```

---

### **3.7 Example: Replace Text**

```python
import re

text = "I hate bugs"
result = re.sub("hate", "love", text)
print(result)
```

**Output:**

```
I love bugs
```

---

## 🧠 **4. Summary Table**

| Concept                | Module         | Key Functions / Syntax                   |
| ---------------------- | -------------- | ---------------------------------------- |
| **OOP**                | Built-in       | `class`, `__init__`, `self`, inheritance |
| **File Management**    | `open()`, `os` | `read()`, `write()`, `remove()`          |
| **Regular Expression** | `re`           | `search()`, `findall()`, `sub()`         |

---

## 💻 **5. Practice Exercises**

### 🧱 OOP

1. Create a class `Student` with attributes name and score, and a method to display the grade.
2. Create a `BankAccount` class with deposit and withdraw methods, ensuring balance can’t go below zero.
3. Implement inheritance using classes `Person` → `Teacher` → `MathTeacher`.

### 📁 File Management

4. Write a program to create a text file and write your name and age in it.
5. Read the content of the file and count how many words are in it.
6. Write a program that appends the current date to a log file each time it runs.

### 🔍 Regular Expressions

7. Write a regex to validate Nigerian phone numbers.
8. Find all words that start with a capital letter in a sentence.
9. Replace all digits in a string with the symbol `#`.
10. Extract all email addresses from a block of text.

---

