# Chapter 7: Lists & Tuples

## 🔰 Introduction

### Why Lists?

**Problem:** If you need to store 100 student names, you'd need 100 separate variables! Lists solve this by storing **multiple values in a single variable**.

> **Real-World Analogy:**
> - **List** = Shopping bag — can hold multiple items, you can add/remove items
> - **Tuple** = Sealed delivery package — items are fixed, you can't change them

---

## 🔑 Key Concepts — Lists

### Creating a List

```python
# Method 1: Square brackets (most common)
fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]   # Different types allowed!

# Method 2: list() constructor
nums = list((1, 2, 3))         # from tuple
chars = list("Python")          # from string → ['P','y','t','h','o','n']

# Empty list
empty = []
empty2 = list()

# Nested list (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### List Properties

| Property | Meaning |
|----------|---------|
| **Ordered** | Elements maintain their insertion order |
| **Mutable** | You can add, remove, change elements |
| **Dynamic** | Size grows and shrinks as needed |
| **Heterogeneous** | Can store different data types |

---

### Accessing List Elements

```python
fruits = ["apple", "banana", "mango", "grape", "orange"]
#           0         1         2        3         4
#          -5        -4        -3       -2        -1

# Positive indexing
print(fruits[0])    # apple (first)
print(fruits[2])    # mango
print(fruits[-1])   # orange (last)
print(fruits[-2])   # grape

# Slicing
print(fruits[1:4])   # ['banana', 'mango', 'grape']
print(fruits[:3])    # ['apple', 'banana', 'mango']
print(fruits[2:])    # ['mango', 'grape', 'orange']
print(fruits[::2])   # ['apple', 'mango', 'orange'] (every 2nd)
print(fruits[::-1])  # Reversed list!
```

---

### Updating List Elements

```python
fruits = ["apple", "banana", "mango"]

# Update single element
fruits[1] = "kiwi"
print(fruits)   # ['apple', 'kiwi', 'mango']

# Update multiple via slice
fruits[0:2] = ["pear", "plum"]
print(fruits)   # ['pear', 'plum', 'mango']
```

---

### List Methods (Complete Guide)

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6]

# ─── ADDING ───────────────────────────────────────────
my_list.append(7)          # Add to END → [3,1,4,1,5,9,2,6,7]
my_list.insert(0, 10)      # Insert at index 0 → [10,3,1,4,1,5,9,2,6,7]
my_list.extend([8, 8])     # Add multiple at end → [..., 8, 8]

# ─── REMOVING ─────────────────────────────────────────
my_list.remove(1)          # Remove FIRST occurrence of 1
my_list.pop()              # Remove & return LAST element
my_list.pop(0)             # Remove & return element at index 0
del my_list[0]             # Delete element at index 0
my_list.clear()            # Remove ALL elements → []

# ─── SEARCHING ────────────────────────────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums.index(5))       # 4 (index of value 5)
print(nums.count(1))       # 2 (count of value 1)
print(1 in nums)           # True
print(7 in nums)           # False

# ─── ORDERING ─────────────────────────────────────────
nums.sort()                # Sort in-place ascending
nums.sort(reverse=True)    # Sort in-place descending
nums.reverse()             # Reverse in-place
sorted_nums = sorted(nums) # Returns new sorted list (original unchanged)

# ─── COPYING ──────────────────────────────────────────
copy1 = nums.copy()        # Shallow copy
copy2 = nums[:]            # Also shallow copy
import copy
deep = copy.deepcopy(nums) # Deep copy (for nested lists)
```

---

### Useful List Operations

```python
numbers = [5, 2, 8, 1, 9, 3]

print(len(numbers))    # 6  (length)
print(min(numbers))    # 1  (minimum)
print(max(numbers))    # 9  (maximum)
print(sum(numbers))    # 28 (sum)

# List unpacking
a, b, c = [1, 2, 3]
print(a, b, c)   # 1 2 3

first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]
```

---

### List Comprehension

A **powerful shorthand** for creating lists from loops:

```python
# Syntax: [expression for item in iterable if condition]

# Normal way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# List comprehension (one line!)
squares = [i ** 2 for i in range(1, 6)]
print(squares)    # [1, 4, 9, 16, 25]

# With condition
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)      # [2, 4, 6, 8, 10]

# Nested comprehension (flattening matrix)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)       # [1, 2, 3, 4, 5, 6]
```

---

## 🔑 Key Concepts — Tuples

### What is a Tuple?

A **Tuple** is like a list but **immutable** — once created, you cannot change it.

```python
# Creating tuples (parentheses)
point = (3, 4)
rgb = (255, 128, 0)
mixed = (1, "hello", 3.14)

# Single element tuple (NOTE: comma is required!)
single = (5,)       # ✅ This is a tuple
not_tuple = (5)     # ❌ This is just the integer 5!

# From list
my_tuple = tuple([1, 2, 3])

# Access (same as list)
print(point[0])     # 3
print(point[-1])    # 4
print(point[0:2])   # (3, 4)
```

### Tuple Methods

Tuples only have 2 methods (since they're immutable):

```python
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))   # 3 (count occurrences)
print(t.index(4))   # 4 (index of first occurrence)
print(len(t))       # 6
print(min(t))       # 1
print(max(t))       # 4
print(sum(t))       # 14
```

### Tuple Unpacking

```python
# Basic unpacking
x, y = (10, 20)
print(x, y)   # 10 20

# Swapping with tuple
a, b = 1, 2
a, b = b, a   # Python uses tuple behind the scenes!

# Function returning multiple values
def get_dimensions():
    return 1920, 1080   # Returns tuple

width, height = get_dimensions()
print(width, height)   # 1920 1080

# Named tuple (advanced)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)   # 3 4
```

---

## 📊 List vs Tuple Comparison

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Methods | 11+ methods | 2 methods |
| Speed | Slower | Faster |
| Memory | More | Less |
| Use case | Dynamic data | Fixed data, coordinates, DB records |

> **When to use what?**
> - Use **List** for data that will change (shopping cart, student list)
> - Use **Tuple** for data that should NOT change (RGB colors, GPS coordinates, days of week)

---

## 🌍 Practical Examples

```python
# 1. Finding unique elements (convert list to set)
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(sorted(unique))   # [1, 2, 3, 4]

# 2. 2D Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Access element at row 1, col 2
print(matrix[1][2])   # 6

# 3. Zip two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))
print(combined)   # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Sort by score
sorted_by_score = sorted(combined, key=lambda x: x[1], reverse=True)
print(sorted_by_score)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

---

## 📝 Summary

```
LIST
  []           → Create list
  append()     → Add to end
  insert(i,x)  → Add at index i
  extend()     → Add multiple
  remove(x)    → Remove first x
  pop()        → Remove & return last (or pop(i) for index i)
  sort()       → Sort in-place
  reverse()    → Reverse in-place
  index(x)     → Find index of x
  count(x)     → Count occurrences
  len()        → Length

TUPLE
  ()           → Create tuple
  (x,)         → Single element tuple (comma required!)
  count()      → Count occurrences
  index()      → Find index
  Immutable    → Cannot be changed after creation
```

---

# Chapter 8: Dictionary

## 🔰 Introduction

A **Dictionary** stores data as **key-value pairs** — like a real dictionary where each word (key) maps to its meaning (value).

> **Real-World Analogy:**
> - **Student Roll Book:** Roll No. 01 → {Name: Raj, Class: 10A, Marks: 90}
> - **Phone Contact Book:** "Mom" → "9876543210"
> - **English Dictionary:** "Python" → "A programming language"

---

## 🔑 Key Concepts

### Creating a Dictionary

```python
# Syntax: {key: value, key: value, ...}
person = {
    "name": "Rahul",
    "age": 20,
    "marks": 95.5,
    "is_student": True
}

# Empty dictionary
empty = {}
empty2 = dict()

# From keyword arguments
student = dict(name="Priya", age=19, grade="A")

# Keys can be: strings, integers, tuples (NOT lists)
mixed_keys = {
    "name": "Alice",
    1: "one",
    (2, 3): "tuple key"
}
```

### Dictionary Properties

| Property | Meaning |
|----------|---------|
| **Key-Value Pairs** | Data stored as paired items |
| **Unique Keys** | No duplicate keys (new value overwrites) |
| **Mutable** | Can add, remove, update |
| **Ordered** | Maintains insertion order (Python 3.7+) |
| **Dynamic** | Size changes as needed |

---

### Accessing Values

```python
person = {"name": "Rahul", "age": 20, "city": "Delhi"}

# Method 1: Direct key access (raises KeyError if key missing)
print(person["name"])       # Rahul
print(person["age"])        # 20

# Method 2: get() — safe access (returns None or default)
print(person.get("name"))        # Rahul
print(person.get("phone"))       # None (no error!)
print(person.get("phone", "N/A"))  # N/A (custom default)
```

---

### Adding & Updating

```python
student = {"name": "Priya", "grade": "B"}

# Add new key-value pair
student["marks"] = 85
student["city"] = "Mumbai"
print(student)  # {'name': 'Priya', 'grade': 'B', 'marks': 85, 'city': 'Mumbai'}

# Update existing value
student["grade"] = "A"    # Overwrites "B"
print(student["grade"])   # A

# Update multiple at once
student.update({"marks": 90, "city": "Pune"})
```

---

### Deleting Items

```python
info = {"name": "Dev", "age": 22, "version": "3.9", "use_case": "AI"}

# del — delete specific key
del info["version"]

# pop() — remove and return value
removed = info.pop("age")
print(removed)   # 22

# popitem() — remove and return last inserted pair
last = info.popitem()
print(last)   # ('use_case', 'AI')

# clear() — remove all items
info.clear()
print(info)   # {}
```

---

### Dictionary Methods (Complete)

```python
profile = {"name": "Sagar", "age": 25, "salary": 50000}

# keys() — returns all keys
print(list(profile.keys()))      # ['name', 'age', 'salary']

# values() — returns all values
print(list(profile.values()))    # ['Sagar', 25, 50000]

# items() — returns key-value pairs as tuples
print(list(profile.items()))     # [('name','Sagar'), ('age',25), ('salary',50000)]

# get() — safe access
print(profile.get("phone", "Not set"))   # Not set

# setdefault() — set value only if key doesn't exist
profile.setdefault("country", "India")
print(profile["country"])   # India
profile.setdefault("name", "Unknown")   # Won't change (key exists)
print(profile["name"])      # Sagar (unchanged)

# update() — merge/update with another dict
profile.update({"skills": ["Python", "SQL"], "age": 26})

# copy() — shallow copy
new_profile = profile.copy()
```

---

### Iterating Over Dictionary

```python
fruits = {"apple": 1.5, "banana": 0.5, "mango": 2.0}

# Iterate over keys (default)
for fruit in fruits:
    print(fruit)              # apple, banana, mango

# Iterate over values
for price in fruits.values():
    print(price)              # 1.5, 0.5, 2.0

# Iterate over key-value pairs
for fruit, price in fruits.items():
    print(f"{fruit}: ₹{price}")   # apple: ₹1.5 etc.
```

---

### Dictionary Comprehension

```python
# Create dict from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)   # {'a': 1, 'b': 2, 'c': 3}

# Squares dict
squares = {i: i**2 for i in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter dict
high_scores = {k: v for k, v in {"Alice": 85, "Bob": 62, "Carol": 91}.items() if v > 80}
print(high_scores)   # {'Alice': 85, 'Carol': 91}
```

---

## 🌍 Practical Example: Contact Book

```python
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"✅ {name} added!")

def find_contact(name):
    return contacts.get(name, "Contact not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"🗑️ {name} deleted")
    else:
        print("Contact not found")

def display_all():
    if not contacts:
        print("No contacts!")
    else:
        for name, phone in contacts.items():
            print(f"📞 {name}: {phone}")

# Usage
add_contact("Mom", "9876543210")
add_contact("Dad", "9123456789")
display_all()
print(find_contact("Mom"))
delete_contact("Dad")
```

---

## 📝 Summary

```
{}             → Create dictionary
dict[key]      → Access value (raises error if missing)
dict.get(k,d)  → Safe access (returns default d)
dict[k] = v    → Add or update
del dict[k]    → Delete key
dict.pop(k)    → Remove & return value
dict.keys()    → All keys
dict.values()  → All values
dict.items()   → All key-value pairs (tuples)
dict.update()  → Merge dictionaries
dict.clear()   → Remove all items
```

---

# Chapter 9: Sets

## 🔰 Introduction

A **Set** is an **unordered collection of unique elements** — duplicates are automatically removed.

> **Real-World Analogy:** A set is like a **bag of unique coins** — you can't have two coins of the same type. It's also like a **Venn diagram** — you can find common/unique elements between groups.

---

## 🔑 Key Concepts

### Creating Sets

```python
# Method 1: Curly braces
fruits = {"apple", "banana", "mango", "apple"}  # duplicate "apple" ignored
print(fruits)   # {'apple', 'banana', 'mango'} — unordered!

# Method 2: set() constructor
nums = set([1, 2, 3, 2, 1])
print(nums)   # {1, 2, 3}

# From string (gets unique chars)
chars = set("python")
print(chars)   # {'p', 'y', 't', 'h', 'o', 'n'}

# Empty set (MUST use set(), not {})
empty = set()    # ✅ Empty set
not_set = {}     # ❌ This is an empty DICTIONARY!
```

### Set Properties

| Property | Meaning |
|----------|---------|
| **Unordered** | No index, no guaranteed order |
| **Unique** | No duplicates allowed |
| **Mutable** | Can add/remove elements |
| **Not subscriptable** | Cannot use `set[0]` (no indexing) |

---

### Set Methods

```python
colors = {"red", "green", "blue"}

# ADDING
colors.add("yellow")          # Add single element
colors.update(["pink", "violet"])  # Add multiple

# REMOVING
colors.remove("red")          # Remove (raises KeyError if missing)
colors.discard("purple")      # Remove safely (no error if missing)
popped = colors.pop()         # Remove and return random element
colors.clear()                # Remove all

# CHECKING
print("red" in colors)        # True/False
print(len(colors))            # Count elements
```

---

### Set Operations (Math-like)

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# UNION — all unique elements from both sets
print(A | B)         # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))    # Same

# INTERSECTION — common elements
print(A & B)               # {4, 5}
print(A.intersection(B))   # Same

# DIFFERENCE — in A but NOT in B
print(A - B)              # {1, 2, 3}
print(A.difference(B))    # Same

# SYMMETRIC DIFFERENCE — in either but NOT in both
print(A ^ B)                        # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))    # Same
```

**Visual Diagram:**
```
    A           B
  ┌─────────────────────┐
  │  1  2  3  │  6  7  8│
  │        │4 5│         │
  └─────────────────────┘
  
A | B  = all elements = {1,2,3,4,5,6,7,8}
A & B  = overlap      = {4,5}
A - B  = only A       = {1,2,3}
A ^ B  = not overlap  = {1,2,3,6,7,8}
```

---

### Set Relationships

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7}

# issubset() — is A a subset of B?
print(A.issubset(B))        # True (all A's elements are in B)

# issuperset() — is B a superset of A?
print(B.issuperset(A))      # True

# isdisjoint() — do A and C share no elements?
print(A.isdisjoint(C))      # True (no common elements)
print(A.isdisjoint(B))      # False (they share 1, 2, 3)
```

---

## 🌍 Practical Examples

```python
# 1. Remove duplicates from a list (fastest method!)
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(sorted(unique_numbers))   # [1, 2, 3, 4, 5]

# 2. Find common interests
alice_hobbies = {"coding", "reading", "gaming", "cooking"}
bob_hobbies = {"gaming", "sports", "coding", "music"}

common = alice_hobbies & bob_hobbies
print(f"Common hobbies: {common}")   # {'coding', 'gaming'}

only_alice = alice_hobbies - bob_hobbies
print(f"Alice's unique: {only_alice}")   # {'reading', 'cooking'}
```

---

## 📝 Summary

```
set()         → Create set (or {val1, val2})
.add(x)       → Add one element
.update(lst)  → Add multiple
.remove(x)    → Remove (error if missing)
.discard(x)   → Remove (no error if missing)
A | B         → Union (all elements)
A & B         → Intersection (common elements)
A - B         → Difference (only in A)
A ^ B         → Symmetric Difference (in either, not both)
```

---

# Chapter 10: Functions

## 🔰 Introduction

A **function** is a reusable block of code that performs a specific task.

> **Real-World Analogy:** A function is like a **machine** — you put in inputs (raw material), it processes them, and gives you output (finished product). You can use the same machine multiple times!

**Why Functions?**
- **Reusability** — Write once, use many times
- **Modularity** — Break complex programs into smaller pieces
- **Readability** — Code is easier to understand
- **DRY Principle** — Don't Repeat Yourself

---

## 🔑 Key Concepts

### Defining & Calling Functions

```python
# Syntax
def function_name(parameters):
    """Docstring — explains what the function does"""
    # code
    return value   # optional

# Example
def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}!"

# Calling the function
result = greet("Rahul")
print(result)   # Hello, Rahul!

print(greet("Priya"))   # Hello, Priya!
```

---

### Types of Arguments

**1. Positional Arguments (most common)**
```python
def add(a, b):
    return a + b

print(add(10, 5))   # 15 (order matters!)
```

**2. Keyword Arguments**
```python
def describe_person(name, age, city):
    return f"{name} is {age} years old from {city}"

# Order doesn't matter with keyword args
print(describe_person(age=20, city="Delhi", name="Raj"))
```

**3. Default Arguments**
```python
def power(base, exponent=2):   # exponent defaults to 2
    return base ** exponent

print(power(3))      # 9  (3^2)
print(power(3, 3))   # 27 (3^3)
```

**4. *args (Variable Positional Arguments)**
```python
def total(*args):
    """Accept any number of arguments"""
    return sum(args)

print(total(1, 2, 3))        # 6
print(total(1, 2, 3, 4, 5))  # 15

# args is a TUPLE inside the function
def show_args(*args):
    print(type(args))   # <class 'tuple'>
    for item in args:
        print(item)
```

**5. **kwargs (Variable Keyword Arguments)**
```python
def user_info(**kwargs):
    """Accept any keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Sagar", age=25, role="Engineer")
# name: Sagar
# age: 25
# role: Engineer
```

**6. Combined Arguments**
```python
def mixed(pos1, pos2, *args, key1="default", **kwargs):
    print(f"Positional: {pos1}, {pos2}")
    print(f"Extra positional: {args}")
    print(f"Keyword: {key1}")
    print(f"Extra keywords: {kwargs}")

mixed(1, 2, 3, 4, key1="hello", x=10, y=20)
```

---

### Return Values

```python
# Return single value
def square(n):
    return n ** 2

# Return multiple values (as tuple)
def min_max(lst):
    return min(lst), max(lst)

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)   # 1 9

# Return None (implicit)
def greet():
    print("Hello!")   # No return → returns None

x = greet()
print(x)   # None
```

---

### Scope (LEGB Rule)

```python
x = "global"        # Global scope

def outer():
    x = "outer"     # Enclosing scope
    
    def inner():
        x = "inner" # Local scope
        print(x)    # inner
    
    inner()
    print(x)        # outer

outer()
print(x)            # global
```

**LEGB = Local → Enclosing → Global → Built-in** (Python looks for variables in this order)

```python
# global keyword — modify global variable inside function
count = 0

def increment():
    global count    # Tell Python to use global count
    count += 1

increment()
print(count)   # 1
```

---

### Lambda Functions (Anonymous Functions)

Single-line functions without a name:

```python
# Syntax: lambda arguments: expression

# Normal function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2
print(double(5))   # 10

# With multiple arguments
add = lambda a, b: a + b
print(add(3, 4))   # 7

# With condition
classify = lambda x: "even" if x % 2 == 0 else "odd"
print(classify(7))   # odd

# Most useful with sorted(), map(), filter()
nums = [5, 2, 8, 1, 9]
print(sorted(nums, key=lambda x: -x))    # [9, 8, 5, 2, 1] (descending)

students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)   # [('Bob', 92), ('Alice', 85), ('Carol', 78)]

# map() — apply function to all elements
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(squares)   # [1, 4, 9, 16]

# filter() — keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evens)   # [2, 4, 6]
```

---

### Decorators

A **decorator** adds extra functionality to an existing function **without modifying its code**.

> **Real-World Analogy:** Like wrapping a gift — you add packaging (decorator) around the original gift (function) without changing the gift itself.

```python
# Creating a decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()                        # Call the original function
        print("After function call")
    return wrapper

# Applying decorator with @
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Practical: Timer decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

slow_function()   # slow_function ran in 1.0012 seconds
```

---

### Generators

Functions that **yield values one at a time** — memory efficient for large sequences.

> **Real-World Analogy:** Like a vending machine — it gives you one item at a time, not all items at once.

```python
# Normal function — returns all at once
def normal_range(n):
    return list(range(n))   # Creates full list in memory

# Generator function — yields one at a time
def count_down(n):
    while n > 0:
        yield n    # ← yield instead of return
        n -= 1

# Usage
gen = count_down(5)
print(next(gen))   # 5
print(next(gen))   # 4
print(next(gen))   # 3

# Or use in for loop
for num in count_down(5):
    print(num)   # 5 4 3 2 1

# Memory advantage: generate() for 1 million numbers
million_nums = (i for i in range(1_000_000))  # Generator expression
# Takes VERY little memory vs list(range(1_000_000))!
```

---

## 🌍 Practical Examples

```python
# 1. Calculator using functions
def calculator(a, op, b):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    if op not in operations:
        return "Invalid operator"
    return operations[op](a, b)

print(calculator(10, "+", 5))   # 15
print(calculator(10, "/", 0))   # Error: Division by zero

# 2. Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## 📝 Summary

```
def name(params): → Define function
return           → Return value (optional)
*args            → Accept any number of positional args (tuple)
**kwargs         → Accept any number of keyword args (dict)
lambda           → Anonymous one-line function
decorator (@)    → Add functionality without modifying function
yield            → Generator — returns one value at a time
global           → Access global variable inside function
```

---

# Chapter 11: Object-Oriented Programming (OOP)

## 🔰 Introduction

**OOP** is a programming paradigm that organizes code around **objects** (real-world entities) rather than functions and procedures.

> **Real-World Analogy:**
> - **Class** = Blueprint of a house (design plan)
> - **Object** = Actual house built from the blueprint
> - Multiple houses (objects) can be built from the same blueprint (class)

**The 4 Pillars of OOP:**
```
1. Encapsulation  → Hiding internal data
2. Inheritance    → Child class inherits from parent
3. Polymorphism   → Same name, different behavior
4. Abstraction    → Hiding complexity
```

---

## 🔑 Key Concepts

### Class and Object

```python
# Defining a class
class Dog:
    # Class attribute (shared by all objects)
    species = "Canis lupus familiaris"
    
    # Constructor (runs when object is created)
    def __init__(self, name, breed, age):
        # Instance attributes (unique to each object)
        self.name = name
        self.breed = breed
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def info(self):
        return f"{self.name} ({self.breed}), Age: {self.age}"

# Creating objects (instances)
dog1 = Dog("Bruno", "German Shepherd", 3)
dog2 = Dog("Luna", "Golden Retriever", 1)

# Accessing attributes
print(dog1.name)      # Bruno
print(dog2.breed)     # Golden Retriever
print(Dog.species)    # Canis lupus familiaris (class attribute)

# Calling methods
print(dog1.bark())    # Bruno says: Woof!
print(dog2.info())    # Luna (Golden Retriever), Age: 1
```

---

### The `__init__` Constructor

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name   # self.x = value sets instance attribute
        self.age = age
        self.grade = grade
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# 3 types of constructors:
# 1. Default (no params except self)
class DefaultConstructor:
    def __init__(self):
        self.value = 0

# 2. Parameterized (with params)
class Parameterized:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 3. Default values
class WithDefaults:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

obj = WithDefaults()   # Uses defaults
obj2 = WithDefaults("Rahul", 20)   # Overrides defaults
```

---

### Encapsulation (Data Hiding)

Controlling access to data:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # Public attribute
        self._account_no = "123"     # Protected (convention: _name)
        self.__balance = balance     # Private (name mangled: __name)
    
    # Getter method
    def get_balance(self):
        return self.__balance
    
    # Setter method with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

account = BankAccount("Rahul", 10000)
# print(account.__balance)  # ❌ AttributeError!
print(account.get_balance())  # ✅ 10000 (use getter)
account.deposit(5000)         # ✅ Deposited ₹5000
account.withdraw(3000)        # ✅ Withdrawn ₹3000
```

---

### Inheritance

A **child class** inherits attributes and methods from a **parent class**:

```python
# Parent class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name} says {self.sound}"
    
    def breathe(self):
        return f"{self.name} breathes air"

# Child class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # Call parent constructor
        self.breed = breed
    
    def fetch(self):
        return f"{self.name} fetches the ball!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")
    
    def purr(self):
        return f"{self.name} is purring..."

# Usage
dog = Dog("Bruno", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())     # Bruno says Woof (inherited)
print(dog.breathe())   # Bruno breathes air (inherited)
print(dog.fetch())     # Bruno fetches the ball! (own method)
print(cat.speak())     # Whiskers says Meow
print(cat.purr())      # Whiskers is purring...
```

**Types of Inheritance:**
```python
# 1. Single Inheritance
class Child(Parent): pass

# 2. Multiple Inheritance
class Child(Parent1, Parent2): pass

# 3. Multilevel Inheritance
class GrandParent: pass
class Parent(GrandParent): pass
class Child(Parent): pass

# 4. Hierarchical — multiple children from one parent
class Cat(Animal): pass
class Dog(Animal): pass
```

---

### Polymorphism

**Same method name, different behavior** based on the object:

```python
class Bird:
    def speak(self):
        return "Generic bird sound"

class Crow(Bird):
    def speak(self):       # Method Override
        return "Caw Caw!"

class Parrot(Bird):
    def speak(self):       # Method Override
        return "Hello Hello!"

class Duck(Bird):
    def speak(self):       # Method Override
        return "Quack Quack!"

# Polymorphism in action
birds = [Crow(), Parrot(), Duck()]

for bird in birds:
    print(bird.speak())   # Different output, same method name!
# Caw Caw!
# Hello Hello!
# Quack Quack!

# len() is polymorphic (works on str, list, dict, etc.)
print(len("Hello"))        # 5
print(len([1, 2, 3]))      # 3
print(len({"a": 1}))       # 1
```

---

### Magic/Dunder Methods

Special methods that start and end with `__`:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):    # Called by print() and str()
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):   # Official representation
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):   # Operator overloading for +
        return Vector(self.x + other.x, self.y + other.y)
    
    def __len__(self):    # Called by len()
        return 2   # 2D vector has 2 components
    
    def __eq__(self, other):   # Called by ==
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)          # Vector(1, 2) — uses __str__
print(v1 + v2)     # Vector(4, 6) — uses __add__
print(len(v1))     # 2 — uses __len__
print(v1 == v1)    # True — uses __eq__
```

---

## 🎯 OOP Visual Summary

```
CLASS (Blueprint)
┌─────────────────────────┐
│ class Car:              │
│   ├── Attributes        │ ← What it HAS (properties)
│   │     ├── brand       │
│   │     ├── model       │
│   │     └── speed       │
│   └── Methods          │ ← What it CAN DO (behavior)
│         ├── start()    │
│         ├── accelerate()│
│         └── brake()    │
└─────────────────────────┘
        │
        │ (blueprint used to create)
        ▼
OBJECT (Instance)
┌─────────────────────────┐
│ my_car = Car()          │
│   ├── brand = "Toyota"  │
│   ├── model = "Camry"  │
│   └── speed = 0        │
└─────────────────────────┘
```

---

## 📝 Summary

```
class          → Define a class (blueprint)
__init__       → Constructor (runs on object creation)
self           → Reference to current object
object = Class()→ Create object (instance)
object.attr    → Access attribute
object.method()→ Call method
super()        → Call parent class method
Encapsulation  → Use __ prefix for private attributes
Inheritance    → class Child(Parent): inherit from parent
Polymorphism   → Same method name, different implementation
```

---

# Chapter 12: File Handling

## 🔰 Introduction

File Handling allows Python to **read, write, and manipulate files** on your computer.

> **Real-World Analogy:** Working with files is like using a notebook:
> - **Read (r)** — Just looking at notebook pages
> - **Write (w)** — Erasing all and writing fresh
> - **Append (a)** — Adding new notes at the end

---

## 🔑 Key Concepts

### File Modes

| Mode | Name | Description | File must exist? |
|------|------|-------------|-----------------|
| `'r'` | Read | Read only | Yes (error if not) |
| `'w'` | Write | Write (overwrites existing) | No (creates new) |
| `'a'` | Append | Add to end | No (creates new) |
| `'x'` | Create | Creates new file | No (error if exists) |
| `'r+'` | Read+Write | Both read and write | Yes (error if not) |
| `'w+'` | Write+Read | Both read and write | No (creates new) |
| `'a+'` | Append+Read | Both append and read | No (creates new) |
| `'b'` | Binary | Use with other modes: `'rb'`, `'wb'` | — |

---

### Opening and Reading Files

```python
# Method 1: Traditional (must remember to close!)
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()   # ← MUST close!

# Method 2: with statement (recommended — auto-closes!)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closed here!

# Different reading methods:
with open("data.txt", "r") as file:
    # read() — reads entire file as one string
    content = file.read()
    
    # readline() — reads one line at a time
    line = file.readline()
    
    # readlines() — reads all lines into a list
    lines = file.readlines()
    
    # Iterate line by line (most memory efficient!)
    for line in file:
        print(line.strip())   # strip() removes \n
```

---

### Writing to Files

```python
# Write mode (w) — OVERWRITES existing content!
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is Python File Handling\n")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append mode (a) — ADDS to existing content
with open("output.txt", "a") as file:
    content = input("Enter content to append: ")
    file.write(content + "\n")
    print("Appended successfully!")
```

---

### File Modes — Differences

```python
# W mode — OVERWRITES (dangerous!)
with open("test.txt", "w") as f:
    f.write("New content")     # Erases old content!

# A mode — APPENDS (safe!)
with open("test.txt", "a") as f:
    f.write("More content")    # Adds to end, keeps old content

# R+ mode — READ AND WRITE (file must exist!)
with open("test.txt", "r+") as f:
    data = f.read()            # First read
    f.write("\nExtra data")    # Then write (overwrites from cursor position)
```

---

### Checking if File Exists

```python
import os

# Check existence before opening (best practice!)
if os.path.exists("data.txt"):
    print("File exists")
    with open("data.txt", "r") as f:
        print(f.read())
else:
    print("File not found")

# Create file only if it doesn't exist
if not os.path.exists("log.txt"):
    with open("log.txt", "w") as f:
        f.write("Log initialized\n")
```

---

### Complete OS Module Guide

```python
import os

# Check existence
os.path.exists("file.txt")          # True/False

# File info
os.path.getsize("file.txt")         # Size in bytes
os.path.getctime("file.txt")        # Creation time

# Directory operations
os.getcwd()                          # Current working directory
os.listdir(".")                      # List all files in current dir
os.mkdir("new_folder")               # Create directory
os.makedirs("a/b/c")                # Create nested directories

# File operations
os.rename("old.txt", "new.txt")     # Rename
os.remove("file.txt")               # Delete file
os.rmdir("empty_folder")            # Delete empty directory

# Path operations
os.path.join("folder", "file.txt")  # OS-safe path: folder/file.txt
os.path.dirname("/path/to/file.txt") # /path/to
os.path.basename("/path/to/file.txt")# file.txt
```

---

### Working with JSON Files

```python
import json

# Writing JSON
data = {
    "name": "Rahul",
    "age": 20,
    "hobbies": ["coding", "gaming"]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)   # indent=4 for pretty printing

# Reading JSON
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])    # Rahul
    print(loaded["hobbies"]) # ['coding', 'gaming']
```

---

## 🌍 Practical Example: File Manager

```python
import os

def read_file(filename):
    if not os.path.exists(filename):
        return "❌ File not found!"
    with open(filename, "r") as f:
        return f.read()

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return f"✅ Written to {filename}"

def append_file(filename, content):
    with open(filename, "a") as f:
        f.write(content + "\n")
    return f"✅ Appended to {filename}"

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return f"🗑️ {filename} deleted"
    return "❌ File not found!"

# Menu-driven file manager
def file_manager():
    while True:
        print("\n=== File Manager ===")
        print("1. Read file")
        print("2. Write file")
        print("3. Append to file")
        print("4. Delete file")
        print("0. Exit")
        
        choice = input("Choice: ")
        
        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4"]:
            filename = input("Enter filename: ")
            if choice == "1":
                print(read_file(filename))
            elif choice == "2":
                content = input("Enter content: ")
                print(write_file(filename, content))
            elif choice == "3":
                content = input("Enter content to append: ")
                print(append_file(filename, content))
            elif choice == "4":
                print(delete_file(filename))

file_manager()
```

---

## ❌ Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` | File doesn't exist in `r` mode | Check with `os.path.exists()` |
| `PermissionError` | No read/write permission | Check file permissions |
| `UnicodeDecodeError` | Wrong encoding | Add `encoding='utf-8'` to open() |
| Forgot to close file | Using `open()` without `close()` | Always use `with` statement |

```python
# Always specify encoding for non-English text
with open("hindi.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 📝 Summary

```
open(file, mode)   → Open a file
'r'                → Read (file must exist)
'w'                → Write (overwrites, creates if missing)
'a'                → Append (adds to end, creates if missing)
'r+'               → Read and Write (file must exist)
with open() as f:  → Auto-close (recommended always!)
f.read()           → Read entire file
f.readline()       → Read one line
f.readlines()      → Read all lines → list
f.write(text)      → Write text to file
f.writelines(lst)  → Write list of strings
os.path.exists()   → Check if file exists
os.remove()        → Delete file
json.dump()        → Write JSON
json.load()        → Read JSON
```

---
