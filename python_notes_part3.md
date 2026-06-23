# ★ Interview Questions (20+)

## 🎯 Basic Questions

**Q1. What is Python? What are its key features?**
> Python is a high-level, interpreted, dynamically-typed, general-purpose programming language created by Guido van Rossum in 1991. Key features: simple syntax, platform independent, large standard library, supports OOP and functional programming, extensive community.

**Q2. What is the difference between a Compiler and an Interpreter?**

| Compiler | Interpreter |
|----------|-------------|
| Translates entire code at once | Translates line by line |
| Faster execution | Slower execution |
| Shows all errors after compilation | Stops at first error (easier debugging) |
| Examples: C, C++, Java | Examples: Python, JavaScript |
> Python uses an interpreter, which makes debugging much easier.

**Q3. What is the difference between `=` and `==`?**
```python
x = 5      # Assignment — stores 5 in x
x == 5     # Comparison — checks if x equals 5 (returns True/False)
```

**Q4. What are Python data types?**
> int, float, complex, str, bool, list, tuple, dict, set, frozenset, NoneType

**Q5. What is the difference between a list and a tuple?**

| List | Tuple |
|------|-------|
| Mutable (`[1, 2, 3]`) | Immutable (`(1, 2, 3)`) |
| Slower | Faster |
| 11+ methods | 2 methods |
| More memory | Less memory |

**Q6. What is `None` in Python?**
> `None` represents the absence of a value. It's Python's equivalent of `null`. Functions with no `return` statement return `None`. Type: `NoneType`.

**Q7. What is the difference between `is` and `==`?**
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  → same VALUES
print(a is b)   # False → different OBJECTS in memory
```

**Q8. What are `*args` and `**kwargs`?**
```python
def func(*args):    # Accepts any number of POSITIONAL args (stored as tuple)
    pass

def func(**kwargs): # Accepts any number of KEYWORD args (stored as dict)
    pass
```

---

## 🔥 Intermediate Questions

**Q9. What is a lambda function? When to use it?**
```python
# Lambda = anonymous one-line function
square = lambda x: x ** 2
print(square(5))   # 25

# Use when: simple operations, with map/filter/sorted
nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda x: -x))   # Descending sort
```

**Q10. What is list comprehension? How is it different from a for loop?**
```python
# For loop
squares = []
for i in range(1, 6):
    squares.append(i**2)

# List comprehension (faster, cleaner)
squares = [i**2 for i in range(1, 6)]
# With condition
even_sq = [i**2 for i in range(1, 11) if i % 2 == 0]
```

**Q11. What is a decorator in Python?**
> A decorator is a function that wraps another function to add functionality WITHOUT modifying its code. Uses `@` syntax.
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done!")
        return result
    return wrapper

@logger
def greet(name):
    return f"Hello, {name}!"
```

**Q12. What is a generator? Difference from regular function?**
```python
# Generator uses yield — produces values one at a time
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))   # 1
print(next(g))   # 2
# Memory efficient for large sequences!
```
> **Key difference:** Generator uses `yield` instead of `return` and doesn't execute until iterated.

**Q13. Explain `mutable` vs `immutable` in Python.**

| Mutable (can change) | Immutable (cannot change) |
|---------------------|---------------------------|
| list, dict, set | int, float, str, tuple, bool |
| `my_list[0] = 10` ✅ | `my_str[0] = 'X'` ❌ |

**Q14. What is the difference between `deep copy` and `shallow copy`?**
```python
import copy
original = [[1, 2], [3, 4]]

shallow = original.copy()    # or original[:]
# Nested lists still point to same objects!
shallow[0][0] = 99
print(original[0][0])   # 99 (affected!)

deep = copy.deepcopy(original)
deep[0][0] = 99
print(original[0][0])   # Not affected (true copy)
```

**Q15. What are Python's scope rules (LEGB)?**
> L = Local (inside current function)
> E = Enclosing (outer function)
> G = Global (module level)
> B = Built-in (Python built-ins like `len`, `print`)
> Python searches in LEGB order.

---

## 💼 Advanced Questions

**Q16. Explain the 4 pillars of OOP.**

| Pillar | Meaning | Python |
|--------|---------|--------|
| Encapsulation | Hide data, expose only what's needed | `__private`, getters/setters |
| Inheritance | Child gets parent's properties | `class Child(Parent)` |
| Polymorphism | Same name, different behavior | Method overriding |
| Abstraction | Hide complexity, show essential | Abstract classes (`ABC`) |

**Q17. What is `__init__` in Python? What is `self`?**
> `__init__` is the constructor method — runs automatically when an object is created. `self` is a reference to the current instance of the class, used to access instance attributes and methods.

**Q18. What is method overriding? Give an example.**
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):    # Override parent method
        return "Woof!"

class Cat(Animal):
    def speak(self):    # Override parent method
        return "Meow!"

dog = Dog()
print(dog.speak())   # Woof! (not "Some sound")
```

**Q19. What is `super()` in Python?**
> `super()` calls the parent class's method. Used in constructors to call parent `__init__`:
```python
class Child(Parent):
    def __init__(self, name, age, extra):
        super().__init__(name, age)   # Call parent constructor
        self.extra = extra
```

**Q20. What are Python's file modes? What is the `with` statement?**
> File modes: `r` (read), `w` (write — overwrites), `a` (append), `x` (create new), `r+`/`w+`/`a+` (combined).
> `with` statement automatically closes the file even if an error occurs — best practice.
```python
with open("file.txt", "r") as f:
    data = f.read()   # No need to call f.close()!
```

**Q21. What is the difference between `append()` and `extend()` in lists?**
```python
lst = [1, 2, 3]

lst.append([4, 5])      # Adds as single element → [1, 2, 3, [4, 5]]
lst.extend([4, 5])      # Adds each element → [1, 2, 3, 4, 5]
```

**Q22. How do you handle errors/exceptions in Python?**
```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(result)
except ValueError:
    print("Invalid input! Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Success!")     # Runs if no exception
finally:
    print("Always runs!")  # Always executes
```

**Q23. What is the difference between `remove()`, `pop()`, and `del` for lists?**
```python
lst = [10, 20, 30, 40]

lst.remove(20)    # Removes by VALUE (first occurrence)
lst.pop()         # Removes & returns LAST element
lst.pop(0)        # Removes & returns element at INDEX 0
del lst[1]        # Deletes element at index (no return)
del lst[1:3]      # Deletes slice
del lst           # Deletes entire variable!
```

**Q24. What is the GIL (Global Interpreter Lock) in Python?**
> The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This means Python threads cannot truly run in parallel for CPU-bound tasks. Use `multiprocessing` instead for true parallelism.

**Q25. How is Python's `dict` implemented internally?**
> Python dictionaries use **hash tables** internally. Each key is hashed to find its bucket position. This gives O(1) average time complexity for get/set/delete operations.

---

# ★ Practice Exercises

## 🟢 Easy (Basics + Data Types + Operators)

**E1.** Write a program that takes two numbers as input and prints their sum, difference, product, quotient, and remainder.

**E2.** Check if a given number is positive, negative, or zero.

**E3.** Write a program to convert Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32

**E4.** Find the area of a circle given its radius. (Use π = 3.14159)

**E5.** Swap two variables WITHOUT using a third variable.

```python
# Solutions

# E1: Arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum: {a+b}, Diff: {a-b}, Product: {a*b}, Quotient: {a/b:.2f}, Remainder: {a%b}")

# E5: Swap without third variable
x, y = 10, 20
x, y = y, x
print(f"x={x}, y={y}")
```

---

## 🟡 Medium (Loops + Strings + Lists)

**M1.** Print the multiplication table of a given number (1 to 12).

**M2.** Find all prime numbers between 1 and 100 (Sieve of Eratosthenes).

**M3.** Write a function that checks if a string is a palindrome (case-insensitive).

**M4.** Given a list of student names and marks, find the top scorer.

**M5.** Count the frequency of each word in a given sentence.

```python
# Solutions

# M1: Multiplication table
n = int(input("Table of: "))
for i in range(1, 13):
    print(f"{n} × {i} = {n*i}")

# M3: Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("racecar"))    # True
print(is_palindrome("A man a plan a canal Panama"))   # True

# M5: Word frequency
sentence = "the cat sat on the mat the cat"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"{word}: {count}")
```

---

## 🔴 Hard (OOP + File Handling + Advanced)

**H1.** Create a `BankAccount` class with methods for deposit, withdraw, and check balance. Include validation (no negative deposits, no overdraft).

**H2.** Build a simple Student Grade Management System using dictionaries and file handling (save/load from JSON).

**H3.** Implement a **stack** data structure using a class (push, pop, peek, is_empty).

**H4.** Write a decorator called `retry(n)` that retries a function `n` times if it raises an exception.

**H5.** Create a **Contact Book** app using OOP with: add contact, search, update, delete, save to file, and load from file.

```python
# H3: Stack implementation
class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())   # 3
print(s.pop())    # 3
print(s)          # [1, 2]

# H4: Retry decorator
def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
                    if attempt == n - 1:
                        raise
        return wrapper
    return decorator

@retry(3)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"
```

---

# ★ Python Cheat Sheet

## One-Page Quick Revision

```python
# ═══════════════════════════════════════════════════
# PYTHON COMPLETE CHEAT SHEET
# ═══════════════════════════════════════════════════

# ── DATA TYPES ──────────────────────────────────────
x = 10          # int
y = 3.14        # float
s = "Hello"     # str
b = True        # bool
lst = [1,2,3]   # list (mutable, ordered)
tup = (1,2,3)   # tuple (immutable, ordered)
d = {"k":"v"}   # dict (key-value)
st = {1,2,3}    # set (unique, unordered)
n = None        # NoneType

# ── OPERATORS ────────────────────────────────────────
# Arithmetic:  +  -  *  /  //  %  **
# Comparison:  ==  !=  >  <  >=  <=
# Logical:     and  or  not
# Assignment:  =  +=  -=  *=  /=  //=  %=  **=
# Identity:    is  is not
# Membership:  in  not in

# ── CONDITIONS ───────────────────────────────────────
if x > 5:           elif x == 5:        else:
    print("Big")        print("Five")       print("Small")
    
result = "Yes" if x > 5 else "No"   # Ternary

# ── LOOPS ────────────────────────────────────────────
for i in range(1, 6):    while i <= 5:
    print(i)                 print(i)
                             i += 1
                             
break    # exit loop
continue # skip iteration
pass     # placeholder

# ── STRINGS ──────────────────────────────────────────
s = "Python"
s.upper()  s.lower()  s.title()  s.strip()
s.split()  ",".join(lst)
s.find("x")  s.replace("old","new")
s.startswith("Py")  s.endswith("on")
s[0]  s[-1]  s[1:4]  s[::-1]
f"Hello {name}!"   # f-string

# ── LISTS ────────────────────────────────────────────
lst.append(x)      lst.insert(i,x)    lst.extend(lst2)
lst.remove(x)      lst.pop()          lst.pop(i)
lst.sort()         lst.reverse()      lst.copy()
lst.index(x)       lst.count(x)       lst.clear()
[x**2 for x in lst if x>0]  # List comprehension

# ── TUPLES ───────────────────────────────────────────
t = (1,2,3)  t[0]  t.count(x)  t.index(x)  len(t)
a,b,c = t    # Unpacking

# ── DICTIONARIES ─────────────────────────────────────
d = {"k": "v"}
d["k"]              d.get("k", default)
d["new_k"] = "v"    del d["k"]
d.keys()            d.values()          d.items()
d.update(d2)        d.pop("k")          d.copy()
{k:v for k,v in d.items() if v>0}   # Dict comprehension

# ── SETS ─────────────────────────────────────────────
s.add(x)    s.remove(x)    s.discard(x)
A | B  # Union       A & B  # Intersection
A - B  # Difference  A ^ B  # Symmetric diff

# ── FUNCTIONS ────────────────────────────────────────
def name(params, *args, key=val, **kwargs):
    """Docstring"""
    return value

lambda x,y: x+y              # Anonymous function
map(func, lst)                # Apply func to all
filter(func, lst)             # Keep where func=True
sorted(lst, key=lambda x:-x)  # Custom sort

# ── OOP ──────────────────────────────────────────────
class MyClass(Parent):
    class_attr = "shared"
    
    def __init__(self, x):
        self.x = x           # Instance attribute
        self._protected = 1  # Protected (convention)
        self.__private = 2   # Private (name mangled)
    
    def method(self):        # Instance method
        return self.x
    
    @classmethod             # Class method
    def class_method(cls): pass
    
    @staticmethod            # Static method
    def static_method(): pass

obj = MyClass(5)
obj.method()
super().__init__()   # Call parent constructor

# ── FILE HANDLING ────────────────────────────────────
with open("f.txt", "r") as f:     # r w a x r+ w+ a+
    content = f.read()             # Read all
    line = f.readline()            # Read one line
    lines = f.readlines()          # Read all → list
    f.write("text")                # Write
    f.writelines(["a\n","b\n"])    # Write list

import os
os.path.exists("f.txt")   os.remove("f.txt")
os.path.join(dir, fname)  os.listdir(".")

# ── ERROR HANDLING ───────────────────────────────────
try:
    risky_code()
except ValueError as e:
    print(f"Error: {e}")
except (TypeError, KeyError):
    pass
else:
    print("No error!")
finally:
    print("Always runs")

# ── COMMON BUILT-INS ─────────────────────────────────
len(x)    type(x)   range(n)   enumerate(lst)
zip(a,b)  sorted()  reversed() min() max() sum()
int() float() str() list() tuple() dict() set()
print()   input()   abs()      round()
```

---

# ★ Mini Project Ideas

## 🟢 Beginner Projects

**1. Simple Calculator**
- Take two numbers and an operation (+, -, *, /)
- Display the result
- *Concepts:* Variables, input(), if-elif, functions, basic operators

**2. Number Guessing Game**
- Computer picks random number (1-100)
- User guesses until correct
- Show "Too high" / "Too low" hints
- *Concepts:* random module, while loop, conditions, counter

**3. Student Grade Calculator**
- Input marks for 5 subjects
- Calculate average and assign grade (A/B/C/D/F)
- *Concepts:* Lists, loops, functions, conditions

**4. Simple ATM Simulator**
- Check balance, deposit, withdraw
- PIN authentication
- *Concepts:* Functions, conditions, while loop, variables

**5. Word Counter**
- Count words, characters, vowels, consonants in a text
- *Concepts:* Strings, loops, counting

---

## 🟡 Intermediate Projects

**6. Contact Book (with File Saving)**
- Add, search, update, delete contacts
- Save to and load from file (JSON)
- *Concepts:* Dictionary, lists, file handling, OOP

**7. To-Do List App**
- Add tasks, mark complete, delete, view all
- Persist data between sessions
- *Concepts:* Lists, file handling, while loop, OOP

**8. Caesar Cipher Encoder/Decoder**
- Encrypt and decrypt text with shift key
- *Concepts:* Strings, loops, ASCII, chr()/ord()

**9. Simple Quiz App**
- 10 MCQ questions
- Show score and percentage at end
- *Concepts:* Lists, dictionaries, loops, conditions, functions

**10. Basic Web Scraper** (using `requests` + `beautifulsoup4`)
- Scrape top 10 headlines from a news site
- *Concepts:* Libraries, loops, strings, file writing

---

## 🔴 Advanced Projects

**11. Library Management System**
- Add/remove books, search by title/author
- Track borrowed books with member info
- Save all data to files
- *Concepts:* Full OOP (classes, inheritance), file handling, JSON

**12. Student Report Card System**
- Multiple students, multiple subjects
- Generate grade report (text file or CSV)
- *Concepts:* OOP, dictionaries, file handling, sorting

**13. Mini Banking System**
- Multiple accounts, transfer between accounts
- Transaction history
- *Concepts:* OOP (Account class, Bank class), inheritance, file handling

**14. Data Analysis Pipeline**
- Read CSV file of student data
- Calculate statistics (mean, median, mode, std dev)
- Generate summary report
- *Concepts:* File handling, lists, mathematical operations, string formatting

**15. Simple Text Editor (CLI)**
- Open file, edit text, search and replace, save
- Undo last change
- *Concepts:* File handling, strings, OOP, Stack data structure

---

# ★ Revision Notes (Exam Focus)

## 📚 Exam-Critical Definitions

| Term | Definition |
|------|------------|
| **Compilation** | Converting entire source code to machine code at once |
| **Interpretation** | Converting and executing source code line by line |
| **Variable** | Named memory location that stores a value |
| **Data Type** | Category of data (int, float, str, bool, list, etc.) |
| **Immutable** | Cannot be changed after creation (str, tuple, int, float) |
| **Mutable** | Can be changed after creation (list, dict, set) |
| **Function** | Reusable block of code that performs a specific task |
| **Parameter** | Variable in function definition |
| **Argument** | Actual value passed when calling a function |
| **Class** | Blueprint for creating objects |
| **Object** | Instance of a class |
| **Constructor** | `__init__` method — called automatically on object creation |
| **Inheritance** | Child class gets properties of parent class |
| **Polymorphism** | Same method name, different behavior in different classes |
| **Encapsulation** | Hiding internal data, exposing only necessary parts |
| **Decorator** | Function that wraps another to add functionality |
| **Generator** | Function using `yield` — returns one value at a time |
| **Lambda** | Anonymous single-expression function |

---

## 🔑 Key Rules to Remember

**Indexing:**
- Positive: starts at `0` (left to right)
- Negative: starts at `-1` (right to left)
- Slicing: `[start:stop:step]` — **stop is EXCLUSIVE**

**range():**
- `range(n)` → 0 to n-1
- `range(start, stop)` → start to stop-1
- `range(start, stop, step)` → with step interval

**String Immutability:**
- `s[0] = 'X'` → TypeError! Use `s = 'X' + s[1:]`

**List vs Tuple:**
- List: `[1,2,3]` — mutable, use for dynamic data
- Tuple: `(1,2,3)` — immutable, use for fixed data

**Dictionary keys:**
- Must be **hashable** (immutable) → str, int, tuple ✅
- Lists as keys → TypeError ❌

**Set:**
- No duplicates
- No indexing (`set[0]` → TypeError)
- Empty set: `set()` NOT `{}` (that's an empty dict)

**OOP - self:**
- Always first parameter of instance methods
- Refers to the current object
- Python passes it automatically

**File Handling:**
- `'w'` mode OVERWRITES — be careful!
- Always use `with` statement
- `'a'` is safer for adding data

---

## 📊 Data Structure Comparison Table

| Feature | List | Tuple | Dict | Set |
|---------|------|-------|------|-----|
| Syntax | `[1,2]` | `(1,2)` | `{"k":v}` | `{1,2}` |
| Ordered | ✅ | ✅ | ✅ (3.7+) | ❌ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | Keys: ❌ | ❌ |
| Indexed | ✅ | ✅ | Keys only | ❌ |
| Use case | Dynamic sequence | Fixed record | Key-value store | Unique collection |

---

## ⚡ Quick Formulas

```
String reversal:    s[::-1]
Check palindrome:   s == s[::-1]
List max/min:       max(lst), min(lst)
Sum of list:        sum(lst)
Unique elements:    list(set(lst))
Flatten list:       [x for sub in lst for x in sub]
Sort by key:        sorted(lst, key=lambda x: x[1])
Count chars:        Counter("string")  # from collections
Remove whitespace:  s.strip()
Check empty:        if not lst:  or  if len(lst) == 0:
Swap:               a, b = b, a
Power:              2 ** 10  # 1024
Modulus:            n % 2 == 0  # even check
Floor division:     10 // 3    # 3 (removes decimal)
```

---

## 🧭 Next Topics to Learn

After mastering this course, learn these in order:

```
Python Basics (THIS COURSE)
        ↓
Exception Handling (try/except/finally)
        ↓
Regular Expressions (re module)
        ↓
Modules & Packages (import, pip)
        ↓
NumPy & Pandas (Data Science)
        ↓
Matplotlib / Seaborn (Data Visualization)
        ↓
Scikit-learn (Machine Learning)
        ↓
TensorFlow / PyTorch (Deep Learning)
        ↓
Flask / FastAPI (Web Development)
        ↓
SQL + Databases (SQLite, PostgreSQL)
        ↓
Git & GitHub (Version Control)
        ↓
Docker (Containerization)
        ↓
Cloud (AWS / GCP / Azure)
```

**For AI/ML Track (Maganpreet's SHOGUN 2029 Path):**
```
Python Basics → NumPy → Pandas → Matplotlib
     ↓
Scikit-learn (Classical ML)
     ↓
Deep Learning (PyTorch / TensorFlow)
     ↓
Computer Vision (OpenCV, YOLOv8)
     ↓
NLP / Transformers (HuggingFace)
     ↓
Multimodal AI (CLIP, LLaVA)
     ↓
Research & Publication
```

---

## 📝 Final Summary

```
PROGRAMMING FUNDAMENTALS
  Programming  = Writing instructions for computers
  Compiler     = All at once translation (C, C++)
  Interpreter  = Line by line translation (Python)
  Python       = Created 1991, Guido van Rossum

PYTHON BASICS
  Variables    = Named memory containers
  Data Types   = int, float, str, bool, list, tuple, dict, set
  Operators    = Arithmetic, Comparison, Logical, Assignment

CONTROL FLOW
  if/elif/else = Decision making
  while loop   = Condition-based repetition
  for loop     = Sequence-based iteration
  break        = Exit loop
  continue     = Skip iteration

DATA STRUCTURES
  List    = Mutable, ordered, allows duplicates [1,2,3]
  Tuple   = Immutable, ordered, allows duplicates (1,2,3)
  Dict    = Mutable, key-value pairs {"k":"v"}
  Set     = Mutable, unique, unordered {1,2,3}

FUNCTIONS
  def      = Define function
  return   = Return value
  *args    = Variable positional args
  **kwargs = Variable keyword args
  lambda   = One-line anonymous function

OOP
  class    = Blueprint
  object   = Instance of class
  __init__ = Constructor
  self     = Reference to current object
  4 Pillars: Encapsulation, Inheritance, Polymorphism, Abstraction

FILE HANDLING
  open()   = Open file
  r/w/a/x  = Read/Write/Append/Create
  with     = Auto-close context manager
  json     = Read/write JSON data
```

---

*📚 Notes Generated via GODMODE System | Python Course by Sagar (CodingWise Academy)*
*🎯 Designed for: MEXT/UTokyo/SHOGUN 2029 preparation | AI/ML track*
