
---

## 🧱 **A. Object-Oriented Programming (OOP) — 20 Tasks**

### 🔹 **Basic Class and Object**

1. **Create a `Car` class** with attributes `brand` and `model`, and a method to display full car details.
2. **Create a `Student` class** with attributes `name`, `age`, and `grade`. Add a method to print “Pass” or “Fail” based on score.
3. Write a `Book` class with `title`, `author`, and `price`. Add a method that discounts the price by 10%.
4. Create a `Rectangle` class with methods to compute **area** and **perimeter**.
5. Design a `Circle` class that computes **area** and **circumference** using `math.pi`.

---

### 🔹 **Constructors and Instance Methods**

6. Create a `Person` class that initializes with `name` and `birth_year`, and add a method to calculate their **current age**.
7. Create a `BankAccount` class with private attribute `__balance`. Add methods to **deposit**, **withdraw**, and **get_balance**.
8. Write a class `Temperature` that converts **Celsius to Fahrenheit** and vice versa.

---

### 🔹 **Encapsulation & Data Protection**

9. Modify the `BankAccount` class to prevent withdrawing below a minimum balance (₦1000).
10. Create an `Employee` class with a private `__salary` attribute. Add methods to increase salary and view it securely.

---

### 🔹 **Inheritance**

11. Create a base class `Animal` with method `make_sound()`. Inherit it into `Dog`, `Cat`, and `Cow` classes that override the method.
12. Build a `Vehicle` base class and subclasses `Car` and `Bike` that extend it with extra methods.
13. Create a parent class `Shape` and subclasses `Square`, `Triangle`, and `Circle`—each with its own `area()` method.

---

### 🔹 **Polymorphism & Method Overriding**

14. Write a program demonstrating **polymorphism** using `Bird`, `Fish`, and `Dog` classes with the same `move()` method.
15. Implement **method overriding** where `Child` class overrides a `Parent` class method to give a different message.
16. Demonstrate **Duck Typing**: Create two unrelated classes `Laptop` and `Smartphone` that both have a `browse()` method, then call them interchangeably.

---

### 🔹 **Abstraction**

17. Use the `abc` module to define an abstract class `Appliance` with abstract method `power_on()`. Implement it in `Fan` and `Television` subclasses.

---

### 🔹 **Multiple & Multilevel Inheritance**

18. Demonstrate **multiple inheritance** using classes `Father`, `Mother`, and `Child`.
19. Demonstrate **multilevel inheritance** (e.g., `Animal → Mammal → Human`).

---

### 🔹 **Practical OOP Mini Project**

20. Create a small **Student Management System** using OOP:

* `Student` class: name, reg_no, grades
* `Course` class: course title, code, lecturer
* `Result` class: calculates and displays GPA

---

## 📁 **B. File Management — 10 Tasks**

### 🔹 **Basic File Reading & Writing**

21. Create a text file called `notes.txt` and write at least 3 lines into it using Python.
22. Write a Python script to **read all contents** of `notes.txt` and print them.
23. Append a new line `"Learning Python is fun!"` to the same file.
24. Count how many lines, words, and characters are in `notes.txt`.
25. Read a file line by line and **store each line into a list**.

---

### 🔹 **Data Processing**

26. Write a Python program to create a CSV file called `students.csv` and store 5 students' names and scores.
27. Read `students.csv` and print the name of the student with the highest score.
28. Create a text file `numbers.txt` with numbers (one per line). Read it and calculate the **sum and average**.
29. Create a new file `copy.txt` that copies the contents of `notes.txt` into it.
30. Write a program to **check if a file exists** before trying to open it, otherwise print “File not found.”

---

## 🧩 **C. Regular Expressions (Regex) — 10 Tasks**

### 🔹 **Basic Matching**

31. Write a regex to check if a string starts with “Hello”.
32. Extract all **numbers** from the string `"My phone number is 080-1234-5678."`.
33. Validate if a user input is a **valid email address**.
34. Validate if a string contains only **alphabets and spaces**.
35. Find all **capitalized words** in a paragraph.

---

### 🔹 **Advanced Regex**

36. Replace all occurrences of `"Python"` with `"PYTHON"` in a sentence using `re.sub()`.
37. Validate a **Nigerian phone number** pattern (e.g. 0803-123-4567 or +2348031234567).
38. Extract all **dates** from a text in the format `dd/mm/yyyy`.
39. Write a regex to confirm if a password:

* Has at least 8 characters
* Includes uppercase, lowercase, digits, and a special character

40. Write a regex to extract all **email domains** from a list of emails.

---

## 🧠 **Bonus Challenge (Optional, Integrating All Concepts)**

41. Build a small system that:

* Accepts student details via **user input**
* Validates the email and phone number using **regex**
* Stores the data in a **text or CSV file**
* Uses **OOP** to manage student records (add, delete, view)

---

