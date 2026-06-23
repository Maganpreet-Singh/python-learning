# 🐍 Python Programming: Complete GODMODE Notes
### *Basic to Advanced — Industry-Ready, Interview-Focused, Project-Ready*

> **Target:** Beginners → Intermediate → Advanced | Placement | GATE | Interviews | Projects

---

## 📑 Table of Contents

| # | Chapter | Topics |
|---|---------|--------|
| 1 | [Introduction to Programming](#chapter-1-introduction-to-programming) | Programming, Compiler vs Interpreter, HLL vs LLL, Python |
| 2 | [Variables & Data Types](#chapter-2-variables--data-types) | Variables, int, float, str, bool, type() |
| 3 | [Operators](#chapter-3-operators) | Arithmetic, Comparison, Logical, Assignment, Bitwise, Identity, Membership |
| 4 | [Conditions (if-else)](#chapter-4-conditions-if-else) | if, if-else, elif, nested, ternary |
| 5 | [Loops](#chapter-5-loops) | while, for, range(), nested, break, continue, pass |
| 6 | [Strings](#chapter-6-strings) | Creation, slicing, 20+ methods, f-strings |
| 7 | [Lists & Tuples](#chapter-7-lists--tuples) | Creation, indexing, slicing, all methods, comparison |
| 8 | [Dictionary](#chapter-8-dictionary) | Key-value pairs, CRUD, 7+ methods |
| 9 | [Sets](#chapter-9-sets) | Set theory, union, intersection, difference |
| 10 | [Functions](#chapter-10-functions) | def, args, kwargs, lambda, decorators, generators |
| 11 | [OOP](#chapter-11-object-oriented-programming-oop) | Classes, objects, 4 pillars, inheritance, polymorphism |
| 12 | [File Handling](#chapter-12-file-handling) | Read, write, append, modes, with statement, os |
| ★ | [Interview Q&A](#-interview-questions-20) | 20+ Q&A across all levels |
| ★ | [Practice Exercises](#-practice-exercises) | 15 exercises (Easy/Medium/Hard) |
| ★ | [Cheat Sheet](#-python-cheat-sheet) | One-page quick revision |
| ★ | [Mini Projects](#-mini-project-ideas) | Beginner → Advanced ideas |

---

# Chapter 1: Introduction to Programming

## 🔰 Introduction

### What is Programming?

Programming is the **process of writing instructions** that a computer can understand and execute.

- These instructions are called **Code**
- The process of removing bugs from code is called **Debugging**
- Computers cannot think on their own — they only follow instructions we give them

> **Real-World Analogy:** Programming is like writing a **recipe for a computer**.
> Just like a robot needs step-by-step cooking instructions (boil water → add ingredients → stir for 10 mins), computers need step-by-step code to perform any task.

**What can you build with programming?**
- Web Applications
- AI/ML Models
- Mobile Apps
- Games
- Automation Scripts
- Data Analysis Pipelines

---

### What is Code?

Code is the set of instructions written in a programming language that tells the computer what to do.

```
Human Instructions → Code → Computer Executes → Output
```

---

## 🔑 Key Concepts

### Compiler vs Interpreter

Computers only understand **Binary (0s and 1s)** — called **Machine Code**.

Humans write code in **High-Level Languages** (Python, Java, C++). To convert human code → machine code, we need either a **Compiler** or an **Interpreter**.

| Feature | Compiler | Interpreter |
|---------|----------|-------------|
| **Translation** | Translates entire code at once | Translates line by line |
| **Speed** | Faster execution | Slightly slower |
| **Error Detection** | Shows all errors after compilation | Stops at first error |
| **Examples** | C, C++, Java | Python, JavaScript, Ruby |
| **Memory** | Needs more memory (full conversion) | Less memory (line by line) |
| **Debugging** | Harder (all errors at once) | Easier (stops at problem line) |

> **Real-World Analogy:**
> Imagine a recipe written in French:
> - **Compiler** = Translates the FULL recipe to English first, then you cook
> - **Interpreter** = Translates and tells you ONE STEP at a time

**Python uses an Interpreter** → This makes Python debugging very easy!

---

### High-Level vs Low-Level Languages

```
Low-Level Languages                High-Level Languages
(Closer to Machine)                (Closer to Human)
─────────────────                  ─────────────────
• Machine Code (0,1)               • Python
• Assembly Language                • Java
                                   • C++
                                   • JavaScript

FAST but DIFFICULT                 EASY but needs TRANSLATION
Direct hardware access             Needs Compiler/Interpreter
```

---

## 🐍 What is Python?

**Python** is a **High-Level, Interpreted, General-Purpose Programming Language** known for its simplicity and readability.

- **Created by:** Guido van Rossum
- **Year:** 1991
- **Philosophy:** "Simple is better than complex"

### Why Python? — Top Features

| # | Feature | Explanation |
|---|---------|-------------|
| 1 | **Simple Syntax** | Reads like plain English — easiest language to learn |
| 2 | **Interpreted** | No compilation needed — run code instantly |
| 3 | **Cross-Platform** | Runs on Windows, Mac, Linux without changes |
| 4 | **Huge Libraries** | NumPy, Pandas, TensorFlow, Flask, Django, etc. |
| 5 | **Large Community** | Millions of developers, tons of support |
| 6 | **OOP + Functional** | Supports both programming paradigms |
| 7 | **Scalable** | Used in small scripts and Google-scale systems |

### Where is Python Used?

```
Python
  ├── 🌐 Web Development       → Django, Flask, FastAPI
  ├── 🤖 AI / Machine Learning → TensorFlow, PyTorch, scikit-learn
  ├── 📊 Data Science          → Pandas, NumPy, Matplotlib
  ├── 🔐 Cybersecurity         → Scripting, network tools
  ├── ⚙️  Automation           → Selenium, PyAutoGUI
  ├── ☁️  DevOps / Cloud        → Ansible, Boto3
  └── 🎮 Game Development      → Pygame
```

### Career Paths & Salaries (India)

| Role | Tools | Starting Salary (LPA) |
|------|-------|----------------------|
| Data Scientist | Pandas, NumPy | ₹10–30 LPA |
| ML Engineer | TensorFlow, PyTorch | ₹12–35 LPA |
| Cybersecurity Specialist | Scripting | ₹8–20 LPA |
| Automation Engineer | Selenium | ₹6–18 LPA |
| Backend Developer | Django, Flask | ₹8–25 LPA |
| DevOps Engineer | Ansible, Docker | ₹10–30 LPA |

---

## 🛠️ Setting Up Python

**Step 1:** Download Python from [python.org](https://python.org)
**Step 2:** Install VS Code from [code.visualstudio.com](https://code.visualstudio.com)
**Step 3:** Install Python Extension in VS Code
**Step 4:** Create a file `hello.py`
**Step 5:** Write and run your first program:

```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

---

## 💬 Comments in Python

```python
# This is a single-line comment

"""
This is a
multi-line comment
(also called docstring)
"""

# Best Practice: Always comment complex logic
x = 5   # This stores the number 5
```

---

## 📝 Summary

- Programming = Writing instructions for computers
- Code = The instructions themselves
- Debugging = Finding and fixing errors (bugs)
- Compiler = Translates all code at once (C, C++)
- Interpreter = Translates line by line (Python)
- Python = Created 1991, simple, powerful, used everywhere
- Python uses Interpreter → easy debugging

---

# Chapter 2: Variables & Data Types

## 🔰 Introduction

### What is a Variable?

A variable is a **named container that stores data** in a computer's memory.

> **Real-World Analogy:** A variable is like a **labeled box**:
> - Box name = Variable name
> - Contents of box = Value stored

```
┌──────────────────────┐
│  Variable: age       │
│  Value: 20           │
└──────────────────────┘
```

### Declaring a Variable in Python

```python
# Syntax: variable_name = value
name = "Sagar"
age = 25
marks = 95.5
is_student = True
```

**Python is Dynamically Typed** — you don't need to declare the type, Python figures it out automatically.

---

## 🔑 Key Concepts

### Variable Naming Rules

| Rule | Example |
|------|---------|
| ✅ Can use letters, digits, underscore | `my_var`, `x1`, `_temp` |
| ✅ Can start with letter or underscore | `name`, `_age` |
| ❌ Cannot start with a digit | ~~`1name`~~ |
| ❌ Cannot use special characters | ~~`my-var`~~, ~~`my var`~~ |
| ❌ Cannot use Python keywords | ~~`if`~~, ~~`for`~~, ~~`class`~~ |
| ✅ Case-sensitive | `Name` ≠ `name` |

**Naming Conventions:**

```python
# Snake Case (Python standard — PEP8)
first_name = "Rahul"
student_marks = 90

# Camel Case (not preferred in Python)
firstName = "Rahul"  # JavaScript style

# Constants (all caps)
PI = 3.14159
MAX_SIZE = 100
```

---

### Data Types in Python

Python has **8 fundamental data types**:

```
Data Types
  ├── Numbers
  │     ├── int   → 1, -5, 100
  │     ├── float → 3.14, -2.5
  │     └── complex → 3+4j
  ├── str    → "Hello", 'Python'
  ├── bool   → True, False
  └── Collections
        ├── list   → [1, 2, 3]
        ├── tuple  → (1, 2, 3)
        ├── dict   → {"name": "Raj"}
        └── set    → {1, 2, 3}
```

---

### int (Integer)

**Definition:** Whole numbers — positive, negative, or zero.

```python
# Syntax
x = 10
y = -5
z = 0
big = 1_000_000   # underscore for readability

# Check type
print(type(x))    # <class 'int'>
print(type(-5))   # <class 'int'>
```

**Operations:**
```python
a = 10
b = 3

print(a + b)   # 13  (Addition)
print(a - b)   # 7   (Subtraction)
print(a * b)   # 30  (Multiplication)
print(a // b)  # 3   (Floor Division)
print(a % b)   # 1   (Modulus/Remainder)
print(a ** b)  # 1000 (Power)
```

---

### float (Floating Point)

**Definition:** Numbers with decimal points.

```python
pi = 3.14159
temperature = -12.5
price = 99.99

print(type(pi))        # <class 'float'>
print(round(pi, 2))    # 3.14
print(int(pi))         # 3 (converts to int, truncates decimal)
```

---

### str (String)

**Definition:** A sequence of characters enclosed in quotes.

```python
name = "Python"           # double quotes
greeting = 'Hello'        # single quotes
message = """Multi
line string"""            # triple quotes

# String operations
print(len(name))          # 6 (length)
print(name.upper())       # PYTHON
print(name[0])            # P (indexing)
print(name + " 3.10")     # Python 3.10 (concatenation)
print(name * 3)           # PythonPythonPython (repetition)
print(f"Hello {name}!")   # Hello Python! (f-string)
```

---

### bool (Boolean)

**Definition:** Stores only two values — `True` or `False`.

```python
is_student = True
is_adult = False

print(type(is_student))   # <class 'bool'>
print(int(True))          # 1
print(int(False))         # 0

# Booleans in conditions
if is_student:
    print("You are a student")
```

---

### Type Conversion (Casting)

Converting one data type to another:

```python
# Implicit (Python does it automatically)
x = 5      # int
y = 2.0    # float
z = x + y  # → 7.0 (int + float = float, auto-conversion)

# Explicit (you force the conversion)
num_str = "100"
num_int = int(num_str)     # "100" → 100
num_float = float(num_str) # "100" → 100.0

age = 25
age_str = str(age)         # 25 → "25"

# Check type
print(type(num_int))       # <class 'int'>
```

---

### input() Function

Takes user input (always returns a **string**):

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # Convert to int
marks = float(input("Enter marks: ")) # Convert to float

print(f"Name: {name}, Age: {age}, Marks: {marks}")
```

---

### Multiple Assignment

```python
# Assign same value
x = y = z = 0

# Assign different values in one line
a, b, c = 1, 2, 3

# Swap variables (Python's elegant way)
a, b = b, a
print(a, b)   # 2 1
```

---

## ❌ Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `NameError: name 'x' is not defined` | Using variable before assigning | Assign value first |
| `TypeError: can only concatenate str` | Mixing str + int | Convert int to str: `str(num)` |
| `ValueError: invalid literal for int()` | `int("hello")` | Only convert numeric strings |
| `SyntaxError: invalid syntax` | Wrong variable name | Follow naming rules |

---

## 💡 Best Practices

- Use **snake_case** for variable names (`my_variable`, not `myVariable`)
- Use **ALL_CAPS** for constants (`MAX_SIZE = 100`)
- Always use **descriptive names** (`student_age` not `sa`)
- Avoid single-letter variables except for loop counters (`i`, `j`, `k`)

---

## 📝 Summary

```
Variable   → Named container to store data
int        → Whole numbers (5, -3, 0)
float      → Decimal numbers (3.14, -2.5)
str        → Text ("Hello", 'World')
bool       → True or False
type()     → Check data type
int()      → Convert to integer
float()    → Convert to float
str()      → Convert to string
input()    → Get user input (always returns str)
```

---

# Chapter 3: Operators

## 🔰 Introduction

**Operators** are symbols that perform mathematical or logical operations on values (**operands**).

> **Real-World Analogy:** Think of a calculator — the buttons (+, -, ×, ÷) are operators. The numbers you enter (5, 10) are operands.

```
10 + 5 = 15
│    │    └── Result
│    └─────── Operator (+)
└──────────── Operand (10 and 5)
```

**Types of Operators in Python:**
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators

---

## 🔑 Key Concepts

### 1. Arithmetic Operators

Used for **mathematical calculations**:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` (removes decimal) |
| `%` | Modulus | `10 % 3` | `1` (remainder) |
| `**` | Exponentiation | `2 ** 10` | `1024` (power) |

```python
x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.3333333333333335
print(x // y)  # 3   ← Floor division (removes decimal)
print(x % y)   # 1   ← Remainder after division
print(x ** y)  # 1000 ← 10 to the power 3

# Important: Modulus finds remainder
# 10 ÷ 3 = 3 remainder 1 → 10 % 3 = 1
```

**Three things to remember:**
- `%` → gives **remainder**
- `//` → removes **decimal part**
- `**` → calculates **power**

---

### 2. Comparison Operators

Used to **compare two values** — always returns `True` or `False`:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

```python
x = 10
y = 5

print(x == y)   # False (10 is not equal to 5)
print(x != y)   # True  (they are not equal)
print(x > y)    # True  (10 > 5)
print(x < y)    # False (10 is not < 5)
print(x >= 10)  # True  (10 >= 10)
print(x <= 5)   # False (10 is not <= 5)
```

---

### 3. Logical Operators

Used to **combine multiple conditions**:

| Operator | Meaning | Returns True when |
|----------|---------|-------------------|
| `and` | Both conditions | ALL conditions are True |
| `or` | At least one | ANY condition is True |
| `not` | Negation | Original is False |

```python
age = 20
is_student = True

# AND — Both must be True
print(age > 18 and is_student)    # True (both True)
print(age > 18 and age > 25)      # False (second is False)

# OR — At least one must be True
print(age > 18 or age > 25)       # True (first is True)
print(age < 18 or age > 25)       # False (both False)

# NOT — Reverses the result
print(not is_student)             # False (reverses True)
print(not (age < 18))             # True (reverses False)
```

**Truth Table for AND:**

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

**Truth Table for OR:**

| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

---

### 4. Assignment Operators

Used to **assign values** to variables:

| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `x = 5` | Assign 5 to x |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

```python
x = 10

x += 5    # x = 10 + 5 = 15
print(x)  # 15

x -= 3    # x = 15 - 3 = 12
print(x)  # 12

x *= 2    # x = 12 * 2 = 24
print(x)  # 24
```

---

### 5. Bitwise Operators

Operate on **binary representations** (used in low-level programming, flags, permissions):

| Operator | Name | Example | Binary |
|----------|------|---------|--------|
| `&` | AND | `5 & 3 = 1` | 101 & 011 = 001 |
| `\|` | OR | `5 \| 3 = 7` | 101 \| 011 = 111 |
| `^` | XOR | `5 ^ 3 = 6` | 101 ^ 011 = 110 |
| `~` | NOT | `~5 = -6` | Flips all bits |
| `<<` | Left Shift | `5 << 1 = 10` | Multiply by 2 |
| `>>` | Right Shift | `5 >> 1 = 2` | Divide by 2 |

---

### 6. Identity Operators

Check if two variables point to the **same memory location** (not just equal value):

| Operator | Meaning |
|----------|---------|
| `is` | Returns True if same object |
| `is not` | Returns True if different objects |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  (same values)
print(a is b)    # False (different objects in memory)
print(a is c)    # True  (c points to same object as a)

# With small integers (Python caches them)
x = 5
y = 5
print(x is y)    # True (Python caches small integers)
```

---

### 7. Membership Operators

Check if a value **exists in a sequence** (list, string, tuple, etc.):

| Operator | Meaning |
|----------|---------|
| `in` | Returns True if found |
| `not in` | Returns True if not found |

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works with strings too
name = "Python"
print("Py" in name)           # True
print("py" in name)           # False (case-sensitive!)
```

---

### Operator Precedence (PEMDAS / BODMAS)

When multiple operators appear, Python follows this order:

```
P → Parentheses ()           ← Highest Priority
E → Exponentiation **
M → Multiplication *
D → Division /  //  %
A → Addition +
S → Subtraction -             ← Lowest Priority
```

**Remember: PEMDAS or BODMAS**

```python
result = 10 + 5 * 2     # 5*2=10 first, then 10+10 = 20 (NOT 30!)
print(result)            # 20

result = (10 + 5) * 2   # Parentheses first: 15*2 = 30
print(result)            # 30

result = 2 ** 3 + 1     # 2**3=8 first, then 8+1 = 9
print(result)            # 9
```

---

## ❌ Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `TypeError: unsupported operand type` | Wrong type operation | Convert types first |
| `ZeroDivisionError: division by zero` | `x / 0` or `x % 0` | Check divisor ≠ 0 |
| Confusing `=` with `==` | `if x = 5` instead of `if x == 5` | Use `==` for comparison |

---

## 📝 Summary

```
+, -, *, /, //, %, ** → Arithmetic (math operations)
==, !=, >, <, >=, <=  → Comparison (returns True/False)
and, or, not          → Logical (combine conditions)
=, +=, -=, *=, /=     → Assignment (store values)
&, |, ^, ~, <<, >>    → Bitwise (binary operations)
is, is not            → Identity (same object?)
in, not in            → Membership (exists in sequence?)

Operator Precedence: () → ** → * / // % → + -
```

---

# Chapter 4: Conditions (if-else)

## 🔰 Introduction

Conditions allow your program to **make decisions** — executing different code blocks based on whether a condition is True or False.

> **Real-World Analogy:**
> - IF it's raining → take umbrella
> - ELSE → wear sunglasses

---

## 🔑 Key Concepts

### Basic if Statement

```python
# Syntax
if condition:
    # code to run if condition is True
    statement

# Example
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")
```

**Important:** Python uses **indentation (4 spaces or 1 tab)** to define code blocks — NO curly braces!

---

### if-else Statement

```python
# Syntax
if condition:
    # runs when condition is True
else:
    # runs when condition is False

# Example
marks = 45

if marks >= 50:
    print("PASS")
else:
    print("FAIL")
```

---

### if-elif-else Statement

Used when there are **multiple conditions** to check:

```python
# Syntax
if condition1:
    # runs when condition1 is True
elif condition2:
    # runs when condition2 is True
elif condition3:
    # runs when condition3 is True
else:
    # runs when none are True

# Example: Grade Calculator
marks = 75

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")   # Your grade is: B
```

---

### Nested if Statements

An `if` inside another `if`:

```python
age = 25
income = 50000

if age >= 18:
    print("Age criteria met")
    if income >= 30000:
        print("Eligible for loan")
    else:
        print("Income too low for loan")
else:
    print("Must be 18+ for loan")
```

---

### Ternary / Conditional Expression

Write `if-else` in **one line**:

```python
# Syntax
value = "result_if_true" if condition else "result_if_false"

# Example
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult

# Finding max of two numbers
a, b = 10, 20
max_val = a if a > b else b
print(max_val)  # 20
```

---

### Practical Examples

**Example 1: Login System**
```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("✅ Login successful!")
elif username == "admin":
    print("❌ Wrong password!")
else:
    print("❌ User not found!")
```

**Example 2: Number Classifier**
```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Also check even/odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Example 3: FizzBuzz (Interview Classic)**
```python
num = int(input("Enter number: "))

if num % 15 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
```

---

## ASCII Diagram: if-else Flow

```
          START
            │
            ▼
      ┌─────────────┐
      │  Condition?  │
      └─────────────┘
           │
     ┌─────┴─────┐
     │           │
   True        False
     │           │
     ▼           ▼
  if block   else block
     │           │
     └─────┬─────┘
           ▼
          END
```

---

## ❌ Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `IndentationError` | Wrong indentation | Use exactly 4 spaces |
| `SyntaxError` | Missing colon (`:`) | Always add `:` after if/else |
| Logic Error | Using `=` instead of `==` | `if x == 5:` not `if x = 5:` |

---

## 📝 Summary

```
if          → Execute if condition is True
else        → Execute if condition is False
elif        → Check another condition
Nested if   → if inside another if
Ternary     → One-line if-else: x if cond else y
```

---

# Chapter 5: Loops

## 🔰 Introduction

Loops allow you to **execute a block of code repeatedly** — saving you from writing the same code again and again.

> **Real-World Analogy:** Imagine you need to send the same message to 100 friends. Instead of sending it 100 times manually, you'd loop through your contact list!

**Two types of loops in Python:**
1. `while` loop — runs based on a condition
2. `for` loop — iterates over a sequence

---

## 🔑 Key Concepts

### while Loop

Runs **as long as the condition is True**:

```python
# Syntax
while condition:
    # code to execute
    # update the variable (IMPORTANT!)

# Example: Print 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1     # ← MUST increment, otherwise infinite loop!

# Output: 1 2 3 4 5
```

**How it works:**
```
1st: i=1, is 1<=5? YES → print(1) → i becomes 2
2nd: i=2, is 2<=5? YES → print(2) → i becomes 3
3rd: i=3, is 3<=5? YES → print(3) → i becomes 4
4th: i=4, is 4<=5? YES → print(4) → i becomes 5
5th: i=5, is 5<=5? YES → print(5) → i becomes 6
6th: i=6, is 6<=5? NO  → Loop stops
```

---

### for Loop

Iterates over a **sequence** (list, string, tuple, range, dict):

```python
# Syntax
for variable in sequence:
    # code to execute

# Example 1: Iterate over list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango

# Example 2: Iterate over string
for char in "Python":
    print(char)

# Output: P y t h o n

# Example 3: Iterate over numbers using range
for i in range(1, 6):
    print(i)

# Output: 1 2 3 4 5
```

---

### range() Function

Generates a **sequence of numbers**:

```python
# Syntax: range(start, stop, step)
# Note: stop is EXCLUSIVE (not included)

range(5)          # 0, 1, 2, 3, 4  (default start=0)
range(1, 6)       # 1, 2, 3, 4, 5
range(1, 11, 2)   # 1, 3, 5, 7, 9  (step of 2)
range(10, 0, -1)  # 10, 9, 8, ... 1 (countdown)

# Convert to list
print(list(range(1, 6)))     # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
print(list(range(10, 0, -2)))# [10, 8, 6, 4, 2]

# Use in for loop
for i in range(1, 101):
    print(i)   # Prints 1 to 100 easily!
```

---

### Nested Loops

A loop inside another loop:

```python
# Outer loop runs 2 times (i = 1, 2)
# Inner loop runs 3 times (j = 3, 4, 5) for each outer iteration

for i in range(1, 3):
    for j in range(3, 6):
        print(f"({i}, {j})")

# Output:
# (1, 3) (1, 4) (1, 5)
# (2, 3) (2, 4) (2, 5)
```

**Practical: Multiplication Table**
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()   # newline after each row
```

**Star Pattern:**
```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

---

### break Statement

**Immediately stops** the loop when a condition is met:

```python
for num in range(1, 10):
    if num == 5:
        break    # Stop loop when num reaches 5
    print(num)

# Output: 1 2 3 4
# (5 is never printed because break fires first)
```

---

### continue Statement

**Skips the current iteration** and moves to the next:

```python
for num in range(1, 6):
    if num == 3:
        continue   # Skip 3, but continue loop
    print(num)

# Output: 1 2 4 5
# (3 is skipped but loop continues)
```

---

### pass Statement

**Does nothing** — placeholder for empty code blocks:

```python
for num in range(1, 6):
    if num == 5:
        pass   # Placeholder — logic to be written later
    print(num)

# Output: 1 2 3 4 5
# (pass does nothing, loop continues normally)
```

**Use case:** When you want to write the structure first and fill logic later.

---

### Infinite Loop

A loop that never stops:

```python
while True:    # Condition always True
    print("Running forever!")
    # Press Ctrl+C to stop!

# Practical use: Menu-driven programs
while True:
    choice = input("Enter choice (1-3, 0 to quit): ")
    if choice == "0":
        break
    elif choice == "1":
        print("Option 1 selected")
    elif choice == "2":
        print("Option 2 selected")
```

---

## 🌍 Practical Examples

**Example 1: Sum of 1 to 100**
```python
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100 = {total}")   # 5050
```

**Example 2: Factorial**
```python
n = int(input("Enter number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
```

**Example 3: Check Prime**
```python
n = int(input("Enter number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")
```

**Example 4: Fibonacci Series**
```python
n = int(input("How many terms? "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Output (n=8): 0 1 1 2 3 5 8 13
```

---

## ASCII Diagram: Loop Flow

```
     WHILE Loop                    FOR Loop
     ──────────                    ────────
       START                        START
         │                            │
    ┌────▼────┐                  Get sequence
    │ Cond?   │                       │
    └────┬────┘              ┌────────▼────────┐
         │                   │  More items?     │
    ┌────┴────┐               └────┬────────┬───┘
    │         │                    │        │
   Yes       No                   Yes      No
    │         │                    │        │
    ▼         ▼                    ▼        ▼
  Code      END           Get next item    END
    │                           │
    └──────────────────────────┘
    (i += 1 / go to condition)
```

---

## ❌ Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| Infinite loop | Forgot to update variable in while | Always update: `i += 1` |
| `range(5, 1)` gives nothing | Step must be negative for countdown | Use `range(5, 1, -1)` |
| Off-by-one error | `range(1, 5)` gives 1-4 not 1-5 | Remember: stop is exclusive |

---

## 📝 Summary

```
while      → Repeat while condition is True
for        → Iterate over a sequence
range()    → Generate number sequence (stop is EXCLUSIVE)
break      → Exit loop immediately
continue   → Skip current iteration
pass       → Placeholder, does nothing
Nested     → Loop inside loop
```

---

# Chapter 6: Strings

## 🔰 Introduction

A **String** is a sequence of characters enclosed in quotes.

> **Real-World Analogy:** A string is like a **train** — each coach (character) has a numbered position (index), and you can access any coach by its number.

```
 P  y  t  h  o  n
 0  1  2  3  4  5   ← Positive Index
-6 -5 -4 -3 -2 -1   ← Negative Index
```

**Key properties:**
- **Ordered** — characters maintain their position
- **Immutable** — you cannot change individual characters after creation
- **Indexed** — each character has a position (starts at 0)

---

## 🔑 Key Concepts

### Creating Strings

```python
# Single quotes
s1 = 'Hello'

# Double quotes
s2 = "World"

# Triple quotes (multi-line)
s3 = """This is
a multi-line
string"""

# f-string (formatted string — Python 3.6+)
name = "Python"
s4 = f"I love {name}!"   # I love Python!
```

---

### String Indexing & Slicing

```python
text = "Python"

# Indexing (single character)
print(text[0])    # P (first character)
print(text[-1])   # n (last character)
print(text[2])    # t

# Slicing: text[start:stop:step]
print(text[0:3])   # Pyt (index 0, 1, 2)
print(text[2:])    # thon (from index 2 to end)
print(text[:4])    # Pyth (from start to index 3)
print(text[::2])   # Pto (every 2nd character)
print(text[::-1])  # nohtyP (reverse!)
```

---

### String Operations

```python
s1 = "Hello"
s2 = "World"

# Concatenation
print(s1 + " " + s2)    # Hello World

# Repetition
print(s1 * 3)            # HelloHelloHello

# Length
print(len(s1))            # 5

# Membership
print("ell" in s1)        # True
print("xyz" in s1)        # False
```

---

### Category 1: Case Conversion Methods

```python
text = "Hello World Python"

print(text.upper())      # HELLO WORLD PYTHON
print(text.lower())      # hello world python
print(text.title())      # Hello World Python (each word capitalized)
print(text.capitalize()) # Hello world python (only first word)
print(text.swapcase())   # hELLO wORLD pYTHON (swap upper↔lower)
```

---

### Category 2: Searching & Replacing Methods

```python
text = "Python is great. Python rocks!"

# find() → returns index of first occurrence (-1 if not found)
print(text.find("Python"))       # 0
print(text.find("Java"))         # -1

# index() → like find() but raises error if not found
print(text.index("great"))       # 10

# count() → counts occurrences
print(text.count("Python"))      # 2

# replace() → replace substring
print(text.replace("Python", "Java"))
# Java is great. Java rocks!

# replace with limit
print(text.replace("Python", "Java", 1))
# Java is great. Python rocks! (only first replaced)
```

---

### Category 3: Splitting & Joining Methods

```python
# split() → splits string into list
sentence = "apple,banana,mango"
fruits = sentence.split(",")
print(fruits)    # ['apple', 'banana', 'mango']

words = "Hello World Python".split()   # split on space by default
print(words)    # ['Hello', 'World', 'Python']

# join() → joins list into string
joined = ", ".join(fruits)
print(joined)   # apple, banana, mango

numbers = "-".join(["1", "2", "3"])
print(numbers)  # 1-2-3
```

---

### Category 4: Checking Methods (return True/False)

```python
text = "Python3"

print(text.startswith("Py"))    # True
print(text.endswith("3"))       # True
print(text.isalpha())           # False (has digit '3')
print("Python".isalpha())       # True (all alphabets)
print("123".isdigit())          # True (all digits)
print(text.isalnum())           # True (alphanumeric)
print("  ".isspace())           # True (all spaces)
print("python".islower())       # True
print("PYTHON".isupper())       # True
```

---

### Category 5: Stripping (Removing whitespace)

```python
text = "   Hello World   "

print(text.strip())    # "Hello World"  (both sides)
print(text.lstrip())   # "Hello World   " (left side)
print(text.rstrip())   # "   Hello World" (right side)
```

---

### f-strings (Formatted Strings)

```python
name = "Rahul"
age = 20
marks = 95.567

# Basic f-string
print(f"Name: {name}, Age: {age}")      # Name: Rahul, Age: 20

# Expressions inside f-strings
print(f"Next year: {age + 1}")          # Next year: 21

# Formatting numbers
print(f"Marks: {marks:.2f}")            # Marks: 95.57 (2 decimal places)
print(f"Marks: {marks:08.2f}")          # Marks: 00095.57 (padded)

# Alignment
print(f"{'Left':<10}|{'Right':>10}")    # Left     |     Right
```

---

## 🌍 Practical Examples

**Example 1: Palindrome Check**
```python
word = input("Enter a word: ").lower().strip()
if word == word[::-1]:
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is NOT a palindrome")
```

**Example 2: Count Vowels**
```python
text = input("Enter text: ").lower()
vowels = "aeiou"
count = sum(1 for char in text if char in vowels)
print(f"Vowel count: {count}")
```

**Example 3: Word Frequency Counter**
```python
sentence = "the quick brown fox jumps over the lazy fox"
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")
```

---

## 📋 String Methods Quick Reference

| Method | Purpose | Example |
|--------|---------|---------|
| `.upper()` | All uppercase | `"hi".upper()` → `"HI"` |
| `.lower()` | All lowercase | `"HI".lower()` → `"hi"` |
| `.title()` | Title Case | `"hello world".title()` → `"Hello World"` |
| `.strip()` | Remove whitespace | `" hi ".strip()` → `"hi"` |
| `.split(x)` | Split by x | `"a,b".split(",")` → `["a","b"]` |
| `.join(lst)` | Join list | `",".join(["a","b"])` → `"a,b"` |
| `.find(x)` | Find index of x | `"hello".find("e")` → `1` |
| `.replace(a,b)` | Replace a with b | `"cat".replace("c","b")` → `"bat"` |
| `.count(x)` | Count occurrences | `"hello".count("l")` → `2` |
| `.startswith(x)` | Starts with x? | `"Python".startswith("Py")` → `True` |
| `.endswith(x)` | Ends with x? | `"Python".endswith("on")` → `True` |
| `.isalpha()` | All letters? | `"abc".isalpha()` → `True` |
| `.isdigit()` | All digits? | `"123".isdigit()` → `True` |
| `.isalnum()` | Letters+digits? | `"abc1".isalnum()` → `True` |
| `len(s)` | Length | `len("Python")` → `6` |

---

## ❌ Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `TypeError: 'str' does not support item assignment` | Strings are immutable | Create new string: `s = s[:2] + "X" + s[3:]` |
| `IndexError: string index out of range` | Accessing invalid index | Check `len(s)` first |
| Case mismatch | `"py" in "Python"` → False | Use `.lower()` before checking |

---

## 📝 Summary

```
Strings    → Immutable, ordered sequence of characters
Indexing   → s[0] = first, s[-1] = last
Slicing    → s[start:stop:step]
Reverse    → s[::-1]
f-strings  → f"Hello {name}!"
.upper()   → ALL CAPS
.lower()   → all lowercase
.split()   → String → List
.join()    → List → String
.strip()   → Remove whitespace
.find()    → Returns index (-1 if not found)
.replace() → Substitute substrings
```

---
