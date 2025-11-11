
---

## 🧩 **Python Collections (List, Tuple, Sets & Dictionaries)**

Python provides four main built-in collection data types used to store multiple items in a single variable:

| Collection Type | Ordered             | Changeable (Mutable) | Allows Duplicates        | Syntax         |
| --------------- | ------------------- | -------------------- | ------------------------ | -------------- |
| **List**        | ✅ Yes               | ✅ Yes                | ✅ Yes                    | `[ ]`          |
| **Tuple**       | ✅ Yes               | ❌ No                 | ✅ Yes                    | `( )`          |
| **Set**         | ❌ No                | ✅ Yes                | ❌ No (Unique items only) | `{ }`          |
| **Dictionary**  | ✅ Yes (Python 3.7+) | ✅ Yes                | ❌ Keys must be unique    | `{key: value}` |

---

## 📝 **1. Lists**

A **list** is an ordered, mutable collection that can store different data types.

### Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.5, True]
```

### Accessing List Elements

```python
print(fruits[0])      # apple
print(fruits[-1])     # cherry (negative index starts from end)
```

### Modifying a List

```python
fruits[1] = "mango"
print(fruits)   # ['apple', 'mango', 'cherry']
```

### Adding and Removing Items

```python
fruits.append("orange")      # Add to end
fruits.insert(1, "grape")    # Add at position
fruits.remove("apple")       # Remove specific item
popped_item = fruits.pop()   # Remove last item
```

### List Operations

```python
print(len(fruits))        # Length of list
print("mango" in fruits)  # Membership test
fruits.sort()             # Sort alphabetically
fruits.reverse()          # Reverse order
```

### List Slicing

```python
print(fruits[1:3])   # Elements from index 1 to 2
```

---

## 🧮 **2. Tuples**

A **tuple** is an ordered and **immutable** collection (cannot be changed after creation).

### Creating Tuples

```python
coordinates = (4, 5)
colors = ("red", "green", "blue")
single_item = ("hello",)   # Must include a comma
```

### Accessing Elements

```python
print(colors[0])   # red
```

### Tuple Unpacking

```python
x, y = coordinates
print(x)  # 4
print(y)  # 5
```

### Why Use Tuples?

* Faster than lists
* Useful for fixed data (e.g., coordinates)
* Can be used as dictionary keys (lists cannot)

---

## 🌿 **3. Sets**

A **set** is an unordered collection with **no duplicate elements**.

### Creating Sets

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)   # {'apple', 'banana', 'cherry'} (duplicates removed)
```

### Adding and Removing Items

```python
fruits.add("orange")
fruits.remove("banana")
fruits.discard("pineapple")  # No error if item doesn’t exist
```

### Set Operations

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union → {1, 2, 3, 4, 5}
print(A & B)   # Intersection → {3}
print(A - B)   # Difference → {1, 2}
print(A ^ B)   # Symmetric Difference → {1, 2, 4, 5}
```

### Checking Membership

```python
print(2 in A)   # True
```

---

## 🗂️ **4. Dictionaries**

A **dictionary** stores data in **key-value pairs**.

### Creating Dictionaries

```python
person = {
    "name": "John",
    "age": 30,
    "country": "Nigeria"
}
```

### Accessing and Modifying Data

```python
print(person["name"])       # John
print(person.get("age"))    # 30

person["age"] = 31          # Modify value
person["email"] = "john@example.com"  # Add new key-value
```

### Removing Items

```python
person.pop("age")
del person["country"]
```

### Dictionary Methods

```python
print(person.keys())     # dict_keys(['name', 'email'])
print(person.values())   # dict_values(['John', 'john@example.com'])
print(person.items())    # dict_items([('name', 'John'), ('email', 'john@example.com')])
```

### Looping Through a Dictionary

```python
for key, value in person.items():
    print(key, ":", value)
```

---

## 🧠 **Summary**

| Feature           | List  | Tuple | Set   | Dictionary     |
| ----------------- | ----- | ----- | ----- | -------------- |
| Ordered           | ✅     | ✅     | ❌     | ✅ (3.7+)       |
| Mutable           | ✅     | ❌     | ✅     | ✅              |
| Indexed Access    | ✅     | ✅     | ❌     | ✅ (by key)     |
| Allows Duplicates | ✅     | ✅     | ❌     | ❌ (keys only)  |
| Syntax            | `[ ]` | `( )` | `{ }` | `{key: value}` |

---

## 💡 Example Use Case

```python
students = [
    {"name": "Adewale", "age": 20, "courses":  ["Math","English"]},
    {"name": "Chika", "age": 22, "courses": ["Biology", "Chemistry"]}
]

for student in students:
    print(f"{student['name']} studies {student['courses']}")
```

**Output:**

```
Adewale studies ['Math', 'English']
Chika studies ['Biology', 'Chemistry']
```

