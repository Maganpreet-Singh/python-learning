# NumPy Complete Notes 📘

A complete, beginner-friendly guide to NumPy — covering everything from the basics to advanced concepts, interview questions, and mini projects.

---

## Table of Contents

1. [Introduction to NumPy](#1-introduction-to-numpy)
2. [Installation and Setup](#2-installation-and-setup)
3. [Understanding Arrays](#3-understanding-arrays)
4. [Dimensions in NumPy](#4-dimensions-in-numpy)
5. [Creating Arrays](#5-creating-arrays)
6. [Array Attributes](#6-array-attributes)
7. [Data Types in NumPy](#7-data-types-in-numpy)
8. [Indexing and Slicing](#8-indexing-and-slicing)
9. [Reshaping Arrays](#9-reshaping-arrays)
10. [Mathematical Operations](#10-mathematical-operations)
11. [Statistical Functions](#11-statistical-functions)
12. [Aggregation Operations (axis)](#12-aggregation-operations-axis)
13. [Random Module](#13-random-module)
14. [Array Manipulation](#14-array-manipulation)
15. [Sorting and Searching](#15-sorting-and-searching)
16. [Boolean Masking and Filtering](#16-boolean-masking-and-filtering)
17. [Broadcasting](#17-broadcasting)
18. [Universal Functions (ufuncs)](#18-universal-functions-ufuncs)
19. [Copy vs View](#19-copy-vs-view)
20. [Handling Missing Values](#20-handling-missing-values)
21. [NumPy Performance](#21-numpy-performance)
22. [NumPy Best Practices](#22-numpy-best-practices)
23. [Frequently Asked Interview Questions](#23-frequently-asked-interview-questions)
24. [Cheat Sheet](#24-cheat-sheet)
25. [Practice Exercises](#25-practice-exercises)
26. [Mini Projects](#26-mini-projects)
27. [Summary](#27-summary)

---

## 1. Introduction to NumPy

### What is NumPy?

**NumPy** stands for **Numerical Python**. It is a Python library used for working with large amounts of numerical data quickly and efficiently using a special data structure called an **array**.

Think of NumPy as a **turbo-charged calculator** that can perform mathematical operations on millions of numbers in a fraction of a second — without writing a single loop.

> 💡 **Note:** NumPy is the foundation on which most data science and machine learning libraries (Pandas, Scikit-learn, TensorFlow, PyTorch) are built.

### Why NumPy Was Created

Before NumPy existed, programmers and scientists who worked with large numerical datasets (like weather data, stock prices, or medical records) faced three big problems while using plain Python:

1. **Slow performance** when handling large datasets
2. **High memory usage**
3. **No direct/easy way to perform mathematical operations** on a whole collection of numbers at once

NumPy was created by **Travis Oliphant** in 2005 to solve exactly these problems. The two main goals behind NumPy were:

- Allow Python to handle large amounts of numerical data **quickly**
- Remove the need for slow loops by introducing **fast, vectorized calculations**

### Problems with Python Lists

Python's built-in `list` is flexible, but it has serious limitations for numerical computing:

| Problem | Explanation |
|---|---|
| **Slow speed** | Python lists are not optimized for numerical/mathematical operations. Looping over large lists takes a lot of time. |
| **High memory usage** | Lists store extra information (type, size, reference count) for every single element, which wastes memory. |
| **No direct math operations** | You cannot directly add, subtract, or multiply two lists element by element. You need a `for` loop. |
| **Mixed data types** | Lists can hold different data types together, which makes them flexible but slower because Python has to check the type of each item during operations. |

**Example of the problem:**

```python
temperatures = [31.8, 33.0, 35.2, 36.6, 32.0]

total = 0
for temp in temperatures:
    total += temp

average = total / len(temperatures)
print(average)   # 33.72
```

This works fine for 5 values, but imagine doing this for **1 million temperature readings** — the loop would become extremely slow.

**The same task with NumPy:**

```python
import numpy as np

temperatures = np.array([31.8, 33.0, 35.2, 36.6, 32.0])
average = np.mean(temperatures)
print(average)   # 33.72
```

No loop needed, much faster, and the code is shorter.

### Advantages of NumPy

| Feature | Why it matters |
|---|---|
| ⚡ **Speed** | NumPy arrays can be hundreds to thousands of times faster than Python lists for numerical operations. |
| 💾 **Less memory** | NumPy stores data in a compact, fixed-type, contiguous block of memory. |
| ➕ **Easy math operations** | You can add, subtract, multiply entire arrays directly — no loops required. |
| 🌍 **Industry standard** | Almost every data science / AI / ML library is built on top of NumPy. |
| 🧮 **Vectorization** | Operations apply automatically to every element at once. |
| 📐 **Broadcasting** | Allows operations between arrays of different shapes without manually resizing them. |

### Real-World Applications

NumPy is used almost everywhere numbers are involved:

- 📊 **Data Science & Data Analysis** — cleaning, processing, and analyzing large datasets
- 🤖 **Machine Learning & AI** — libraries like TensorFlow and PyTorch use array-like structures inspired by/built on top of NumPy concepts
- 💹 **Stock Market & Finance** — calculating trends, returns, moving averages
- 🧬 **Medical & Scientific Research** — analyzing DNA sequences, detecting diseases, lab data analysis
- 🖼️ **Image Processing** — images are represented as arrays of pixel values (used in OpenCV, Photoshop-like tools, computer vision)

### The NumPy Ecosystem

NumPy is the **foundation** of the entire Python data science stack:

```
        NumPy (foundation - arrays & math)
           │
   ┌───────┼─────────┬───────────┐
   │               │             │
Pandas        Matplotlib    Scikit-learn
(data tables)  (plotting)   (machine learning)
```

- **Pandas** uses NumPy arrays internally for its DataFrames and Series
- **Matplotlib / Seaborn** use NumPy arrays to plot graphs
- **Scikit-learn, TensorFlow, PyTorch** all accept and process data in NumPy-array-like formats

---

## 2. Installation and Setup

### Installing NumPy using pip

Open your terminal or command prompt and run:

```bash
pip install numpy
```

If you are using Jupyter Notebook, run this in a notebook cell:

```bash
!pip install numpy
```

> 📝 **Note:** If you're using **Google Colab**, NumPy comes **pre-installed** — you don't need to install it separately.

To upgrade to the latest version:

```bash
pip install --upgrade numpy
```

### Importing NumPy

Once installed, you need to import it into your Python script before using it:

```python
import numpy
```

### Alias Convention (np)

By convention, almost everyone imports NumPy with the short alias `np`. This is **optional**, but it is a globally followed standard, and you should always use it:

```python
import numpy as np
```

This way, instead of writing `numpy.array()` every time, you can simply write `np.array()` — making your code shorter and easier to read.

### Checking the Version

To check which version of NumPy is installed on your system:

```python
import numpy as np
print(np.__version__)
```

**Output:**

```
2.4.4
```

> 💡 **Tip:** Always check the version when debugging — some functions behave differently or get deprecated across versions.

---

## 3. Understanding Arrays

### What is an Array?

An **array** is a collection of values (usually numbers) of the **same data type**, stored together in an organized, efficient way in memory.

Instead of creating five separate variables to store five students' marks:

```python
mark1 = 85
mark2 = 90
mark3 = 87
mark4 = 91
mark5 = 76
```

You can store them all in a **single array**:

```python
import numpy as np
marks = np.array([85, 90, 87, 91, 76])
```

This makes it possible to apply operations (like finding the average, maximum, minimum) on **all values at once**, without creating extra variables.

### Array vs List

| Feature | Python List | NumPy Array |
|---|---|---|
| Data type | Can hold mixed types (`int`, `str`, `float` together) | Must hold a **single** data type |
| Speed | Slower | Much faster |
| Memory usage | Higher | Lower (more efficient) |
| Mathematical operations | Needs loops | Direct, built-in support (vectorized) |
| Storage | Scattered references in memory | Contiguous (continuous) block in memory |
| Printing style | Has commas: `[1, 2, 3]` | No commas: `[1 2 3]` |

**Example:**

```python
python_list = [1, 2, 3, 4, 5]
print(python_list)        # [1, 2, 3, 4, 5]

import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5])
print(numpy_array)        # [1 2 3 4 5]
```

Notice: the NumPy array prints **without commas** — this is a visual hint that its data is stored in a tightly packed, efficient format.

### Why Arrays Are Faster

1. **Fixed data type** — Since every element is the same type, NumPy doesn't need to check the type of each element during operations (Python lists do this, which slows things down).
2. **Contiguous memory** — All elements are stored next to each other in memory, so the CPU can access and process them much faster (this also enables vectorized, SIMD-based operations under the hood).
3. **Vectorization** — Mathematical operations are applied to the whole array at once using optimized, pre-compiled C code instead of a Python-level loop.

### Memory Efficiency

A Python list stores **extra overhead** for every element — type information, reference counts, and pointers to the actual object in memory. A NumPy array stores **just the raw values**, back-to-back, using a fixed amount of memory per element.

This is why:
- A list of 1 million integers might use **much more memory** than...
- ...a NumPy array storing the same 1 million integers.

### Visual Explanation

**Python List (scattered, with overhead):**

```
list = [10, 20, 30]

Memory:  [ptr]──▶ object(10, type, refcount)
         [ptr]──▶ object(20, type, refcount)
         [ptr]──▶ object(30, type, refcount)
```

**NumPy Array (contiguous, compact):**

```
array = [10, 20, 30]

Memory:  | 10 | 20 | 30 |   ← stored back-to-back, same type, fixed size
```

> ✅ **Key takeaway:** NumPy arrays trade flexibility (mixed types) for **speed and memory efficiency** — which is exactly what you want when working with large numerical datasets.

---

## 4. Dimensions in NumPy

NumPy arrays can have different numbers of **dimensions**, also called **axes**. Understanding dimensions is one of the most important foundational concepts in NumPy.

### 1D Arrays

**Definition:** A 1D (one-dimensional) array is simply a list of numbers stored in a single row. It has only one axis.

**Diagram:**

```
Index:    0    1    2    3    4
Array:  [10,  20,  30,  40,  50]
```

**Syntax & Example:**

```python
import numpy as np
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)
print(arr_1d.ndim)
```

**Output:**

```
[10 20 30 40 50]
1
```

**Use cases:** Storing a simple list of values — temperatures of different cities, a single column of marks, a sequence of stock prices for one company, etc.

### 2D Arrays

**Definition:** A 2D (two-dimensional) array is like a table — it has **rows** and **columns**. Think of an Excel sheet or a chessboard.

**Diagram:**

```
         col0  col1  col2
row0  [   1     2     3  ]
row1  [   4     5     6  ]
```

**Syntax & Example:**

```python
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
print(arr_2d.ndim)
print(arr_2d.shape)
```

**Output:**

```
[[1 2 3]
 [4 5 6]]
2
(2, 3)
```

**Use cases:** Storing tabular data — spreadsheets, grayscale images (rows × columns of pixel values), matrices for mathematics.

> 📝 **Note:** A **matrix** is simply a fancy mathematical name for a 2D array — a table of numbers arranged in rows and columns. Matrices are used heavily in mathematics, physics, and machine learning for operations like addition, subtraction, and multiplication.

### 3D Arrays

**Definition:** A 3D (three-dimensional) array is like a **stack of 2D arrays** (multiple tables stacked on top of each other) — imagine a stack of Excel sheets.

**Diagram:**

```
Layer 0:        Layer 1:
[1 2]           [5 6]
[3 4]           [7 8]
```

**Syntax & Example:**

```python
import numpy as np
arr_3d = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
print(arr_3d)
print(arr_3d.ndim)
print(arr_3d.shape)
```

**Output:**

```
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
3
(2, 2, 2)
```

**Use cases:** Color images (height × width × color channels), video frames (frame × height × width), batches of data in deep learning.

### Multi-Dimensional Arrays

**Definition:** Any array with **more than 3 dimensions** (4D, 5D, and beyond) is called a multi-dimensional array. Each additional dimension adds another "layer" of storage.

**Syntax & Example:**

```python
import numpy as np
arr_4d = np.zeros((2, 3, 4, 5))
print(arr_4d.ndim)
print(arr_4d.shape)
```

**Output:**

```
4
(2, 3, 4, 5)
```

**Use cases:** Used heavily in **deep learning** (batches of color images: batch_size × height × width × channels), MRI/medical scans, and 3D modeling/scientific simulations.

> ⚠️ **Common confusion:** Don't mix up **size** (total number of elements) with **shape** (how the elements are arranged across dimensions) — they are different attributes, covered in detail in [Section 6](#6-array-attributes).

---

## 5. Creating Arrays

NumPy provides many ways to create arrays, depending on what kind of data you need.

### `np.array()`

Converts a Python list (or list of lists) into a NumPy array.

```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr)
```

**Output:**

```
[1 2 3]
```

**Use case:** Converting existing Python data (lists/tuples) into NumPy arrays.

### `np.zeros()`

Creates an array filled entirely with **zeros**. Useful as a placeholder array that you fill in later.

```python
import numpy as np
arr = np.zeros((2, 3))
print(arr)
```

**Output:**

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

**Use case:** Initializing an array before filling it with real/future values.

### `np.ones()`

Creates an array filled entirely with **ones**.

```python
import numpy as np
arr = np.ones((2, 3))
print(arr)
```

**Output:**

```
[[1. 1. 1.]
 [1. 1. 1.]]
```

**Use case:** Default/baseline values, masks, or initial weight matrices.

### `np.full()`

Creates an array filled with a **specific custom value** that you choose.

```python
import numpy as np
arr = np.full((2, 3), 7)
print(arr)
```

**Output:**

```
[[7 7 7]
 [7 7 7]]
```

**Use case:** When you want every cell pre-filled with a particular default number (e.g., a default score, a constant in a simulation).

### `np.empty()`

Creates an array **without initializing its values** — it just reserves memory space. The values you see are random "leftover" data from memory and should **not be relied upon**.

```python
import numpy as np
arr = np.empty((2, 2))
print(arr)
```

**Output (values will vary each time — uninitialized memory):**

```
[[4.48350113e-315 0.00000000e+000]
 [6.92325931e-310 6.92325932e-310]]
```

> ⚠️ **Warning:** Never assume `np.empty()` gives zeros — always fill it with real values before using it in calculations.

**Use case:** When you need an array fast and plan to overwrite every value immediately (slightly faster than `zeros()` because it skips initialization).

### `np.arange()`

Works like Python's built-in `range()`, but returns a NumPy array. Syntax: `np.arange(start, stop, step)`.

```python
import numpy as np
arr = np.arange(0, 10, 2)
print(arr)
```

**Output:**

```
[0 2 4 6 8]
```

> 📝 **Note:** Just like `range()`, the `stop` value is **excluded**.

**Use case:** Generating a quick sequence of numbers (e.g., index values, time steps).

### `np.linspace()`

Generates a specific **number of evenly spaced values** between a start and stop value (stop is **included** by default). Syntax: `np.linspace(start, stop, num)`.

```python
import numpy as np
arr = np.linspace(0, 10, 5)
print(arr)
```

**Output:**

```
[ 0.   2.5  5.   7.5 10. ]
```

**Use case:** Creating evenly spaced points for graphs/plots, simulations, or time intervals.

### `np.eye()`

Creates an **identity matrix** — a square matrix with 1s on the diagonal and 0s everywhere else.

```python
import numpy as np
arr = np.eye(3)
print(arr)
```

**Output:**

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

**Use case:** Linear algebra operations, machine learning (identity matrices appear in many ML formulas).

### `np.identity()`

Works almost exactly like `np.eye()` but is specifically meant for creating a square identity matrix.

```python
import numpy as np
arr = np.identity(4)
print(arr)
```

**Output:**

```
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

**Use case:** Same as `np.eye()` — mathematical/matrix operations.

### `np.random.rand()`

Generates an array of random floating-point numbers between **0 and 1** (uniform distribution).

```python
import numpy as np
np.random.seed(42)
arr = np.random.rand(2, 3)
print(arr)
```

**Output:**

```
[[0.37454012 0.95071431 0.73199394]
 [0.59865848 0.15601864 0.15599452]]
```

**Use case:** Simulations, generating dummy/test data, initializing random weights in ML models.

### `np.random.randint()`

Generates random **integers** within a given range. Syntax: `np.random.randint(low, high, size)`.

```python
import numpy as np
np.random.seed(42)
arr = np.random.randint(1, 10, size=5)
print(arr)
```

**Output:**

```
[8 5 4 8 8]
```

**Use case:** Generating random test scores, dice rolls, sample IDs, etc.

### `np.random.randn()`

Generates random numbers from a **standard normal (Gaussian/bell-curve) distribution** — mean 0, standard deviation 1. Values can be negative.

```python
import numpy as np
np.random.seed(42)
arr = np.random.randn(2, 3)
print(arr)
```

**Output:**

```
[[ 0.49671415 -0.1382643   0.64768854]
 [ 1.52302986 -0.23415337 -0.23413696]]
```

**Use case:** Statistical simulations, noise generation, machine learning model initialization.

### Comparison Table — Array Creation Functions

| Function | Returns | Customizable Value? | Typical Use |
|---|---|---|---|
| `np.array()` | Array from existing data | N/A | Convert list → array |
| `np.zeros()` | All zeros | ❌ | Placeholder array |
| `np.ones()` | All ones | ❌ | Default/mask array |
| `np.full()` | All same custom value | ✅ | Custom default value |
| `np.empty()` | Uninitialized garbage values | ❌ | Fast allocation, overwrite later |
| `np.arange()` | Sequence with fixed step | ✅ (step) | Quick number sequence |
| `np.linspace()` | Fixed count of evenly spaced values | ✅ (count) | Evenly spaced points |
| `np.eye()` / `np.identity()` | Identity matrix | ❌ | Linear algebra |
| `np.random.rand()` | Random floats [0, 1) | N/A | Random testing data |
| `np.random.randint()` | Random integers | ✅ (range) | Random whole numbers |
| `np.random.randn()` | Random floats (normal distribution) | N/A | Statistical simulation |

---

## 6. Array Attributes

Array attributes let you inspect the structure of an array — how many elements it has, what shape it is, and what type of data it stores. Understanding your array's structure **before** performing operations on it is essential (just like a warehouse manager needs to know how many products they have, what type, and how they are organized before doing any calculations).

### `shape`

**Meaning:** Returns a tuple showing the number of elements along each dimension (rows, columns, etc.).

**Syntax:** `array.shape`

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
```

**Output:**

```
(2, 3)
```

This means: 2 rows, 3 columns.

### `size`

**Meaning:** Returns the **total number of elements** in the array (regardless of shape/dimensions).

**Syntax:** `array.size`

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)
```

**Output:**

```
6
```

### `ndim`

**Meaning:** Returns the **number of dimensions (axes)** of the array.

**Syntax:** `array.ndim`

```python
import numpy as np
a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2], [3, 4]])
print(a1.ndim)
print(a2.ndim)
```

**Output:**

```
1
2
```

### `dtype`

**Meaning:** Returns the **data type** of the elements stored in the array.

**Syntax:** `array.dtype`

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.dtype)
```

**Output:**

```
int64
```

### `itemsize`

**Meaning:** Returns the **size (in bytes) of a single element** in the array.

**Syntax:** `array.itemsize`

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.itemsize)
```

**Output:**

```
8
```

(Each `int64` element takes 8 bytes.)

### `nbytes`

**Meaning:** Returns the **total memory (in bytes)** used by all elements in the array (`itemsize × size`).

**Syntax:** `array.nbytes`

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.nbytes)
```

**Output:**

```
48
```

(8 bytes × 6 elements = 48 bytes)

### Quick Reference Table

| Attribute | Meaning | Example Output (for a 2×3 int64 array) |
|---|---|---|
| `shape` | Rows × columns per dimension | `(2, 3)` |
| `size` | Total number of elements | `6` |
| `ndim` | Number of dimensions | `2` |
| `dtype` | Data type of elements | `int64` |
| `itemsize` | Bytes per single element | `8` |
| `nbytes` | Total bytes used (`itemsize × size`) | `48` |

---

## 7. Data Types in NumPy

NumPy arrays must contain elements of the **same data type**. NumPy automatically detects the type from your data, but you can also assign or convert types manually.

### Common Data Types

| Type | Description | Example |
|---|---|---|
| `int` (`int32`/`int64`) | Whole numbers | `1, 2, -5, 100` |
| `float` (`float32`/`float64`) | Decimal numbers | `1.5, 3.14, -2.0` |
| `bool` | True/False values | `True, False` |
| `string` (`<U...`) | Text data | `"apple", "data"` |
| `object` | Mixed/generic Python objects | Any Python object |

### Checking the Data Type

```python
import numpy as np
print(np.array([1, 2, 3]).dtype)              # int64
print(np.array([1.0, 2.0, 3.0]).dtype)        # float64
print(np.array([True, False]).dtype)          # bool
print(np.array(['a', 'bb', 'ccc']).dtype)      # <U3
```

**Output:**

```
int64
float64
bool
<U3
```

> 📝 **Note:** `<U3` means "Unicode string, max length 3 characters" — NumPy automatically picks the size needed to fit the longest string.

### Data Type Conversion — `astype()`

If you need to convert an array's data type into another type (e.g., float → int, or text → number), use `.astype()`.

**Syntax:** `array.astype(new_type)`

```python
import numpy as np
arr = np.array([1.7, 2.9, 3.2])
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)
```

**Output:**

```
[1 2 3]
int64
```

> ⚠️ **Warning:** Converting `float → int` **truncates** (cuts off) the decimal part — it does **not** round the number. `1.7` becomes `1`, not `2`.

**When to use `astype()`:**
- Validating data before performing calculations (e.g., making sure all values are integers, not floats)
- Converting text-like numeric data into actual numbers for calculations
- Reducing memory usage (e.g., converting `float64` → `float32` when high precision isn't needed)

---

## 8. Indexing and Slicing

Indexing and slicing let you access specific elements or portions of an array — one of the most important skills for working with data.

### Indexing — Accessing a Single Element

**Definition:** Indexing means selecting **one specific element** from an array using its position number (index).

> 📝 **Important:** NumPy uses **zero-based indexing** — just like Python lists. The first element is at index `0`, not `1`.

```
Index:    0    1    2    3    4
Array:  [10,  20,  30,  40,  50]
```

#### Positive Indexing (left to right)

```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # first element
print(arr[2])   # third element
```

**Output:**

```
10
30
```

#### Negative Indexing (right to left)

Negative indexing starts from `-1` (the **last** element), not from `0`.

```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[-1])   # last element
```

**Output:**

```
50
```

> ⚠️ **Warning:** Using an index number that doesn't exist in the array (e.g., `arr[10]` on a 5-element array) raises an `IndexError: index out of range`.

#### Row and Column Access (2D Arrays)

For a 2D array, you need **two** index values: `array[row, column]`.

```python
import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d[1, 2])    # row 1, column 2
print(arr2d[0])       # entire row 0
print(arr2d[:, 1])    # entire column 1
```

**Output:**

```
6
[1 2 3]
[2 5 8]
```

### Slicing — Accessing Multiple Elements (a Sub-array)

**Definition:** Slicing lets you extract a **range/portion** of an array, rather than just a single value.

**Syntax:** `array[start:stop:step]`

| Part | Meaning |
|---|---|
| `start` | Index to begin from (included) |
| `stop` | Index to stop at (**excluded** — NumPy goes up to `stop - 1`) |
| `step` | Gap between elements (default is `1`) |

```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])     # start=1, stop=4
print(arr[:3])       # from beginning to index 2
print(arr[::2])      # every 2nd element
print(arr[::-1])     # entire array reversed
```

**Output:**

```
[20 30 40]
[10 20 30]
[10 30 50]
[60 50 40 30 20 10]
```

> ✅ **Tip:** Reversing an array using `arr[::-1]` is much faster and cleaner than writing a `for`/`while` loop to reverse it manually. Interviewers often ask: *"How do you reverse an array without using a loop?"* — this is the answer.

#### Range Slicing on 2D Arrays

```python
import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])
```

**Output:**

```
[[2 3]
 [5 6]]
```

This selects rows 0–1 and columns 1–2 — like selecting a rectangular block from an Excel sheet.

### Fancy Indexing

**Definition:** Fancy indexing lets you select **multiple, non-sequential elements at once** by passing a **list of index positions**.

```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = arr[[0, 2, 4]]
print(result)
```

**Output:**

```
[10 30 50]
```

> 📝 **Note:** Fancy indexing always returns a **copy** of the data — modifying the result will **not** affect the original array.

### Boolean Masking (Condition-Based Filtering)

**Definition:** Boolean masking lets you filter elements based on a **condition**. The condition produces `True`/`False` for every element, and only the elements where the condition is `True` are returned.

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = arr[(arr > 2) & (arr < 5)]
print(result)
```

**Output:**

```
[3 4]
```

> ✅ **Tip:** Boolean masking is significantly faster than using loops to filter data, and it is used extensively in data cleaning and machine learning pipelines.

---

## 9. Reshaping Arrays

### `reshape()`

**Definition:** Changes the **shape** (dimensions) of an array **without changing its data** or the total number of elements.

> ⚠️ **Rule:** The total number of elements **before and after reshaping must match**. You cannot reshape a 6-element array into a shape that needs 8 elements.

**Syntax:** `array.reshape(rows, columns)`

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
```

**Output:**

```
[[1 2 3]
 [4 5 6]]
```

**Diagram:**

```
Before:  [1, 2, 3, 4, 5, 6]            (1D, shape (6,))

After reshape(2,3):
         [1, 2, 3]
         [4, 5, 6]                     (2D, shape (2,3))
```

> 📝 **Note:** `reshape()` usually returns a **view** (not a copy) of the original data whenever possible — meaning that changing values in the reshaped array can also change the original array's data.

### `flatten()`

**Definition:** Converts a multi-dimensional array into a **1D array**. Returns a **copy** — the original array is **not affected** by changes to the flattened result.

```python
import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.flatten())
```

**Output:**

```
[1 2 3 4 5 6]
```

### `ravel()`

**Definition:** Also converts a multi-dimensional array into 1D — but returns a **view** whenever possible, meaning changes to the result **can** affect the original array.

```python
import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.ravel())
```

**Output:**

```
[1 2 3 4 5 6]
```

#### `flatten()` vs `ravel()` — Key Difference (common interview question!)

| Function | Returns | Affects Original Array? | Speed |
|---|---|---|---|
| `flatten()` | Copy | ❌ No | Slightly slower (extra memory used) |
| `ravel()` | View (when possible) | ✅ Yes | Slightly faster |

### `transpose()` and `.T`

**Definition:** Flips an array over its diagonal — turns rows into columns and columns into rows.

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.transpose())
print(arr.T)        # shorthand for transpose()
```

**Output:**

```
[[1 4]
 [2 5]
 [3 6]]
[[1 4]
 [2 5]
 [3 6]]
```

**Diagram:**

```
Original (2x3):        Transposed (3x2):
[1 2 3]                 [1 4]
[4 5 6]                 [2 5]
                         [3 6]
```

**Use case:** Linear algebra, matrix multiplication, converting row-based data into column-based data (and vice versa).

---

## 10. Mathematical Operations

One of NumPy's biggest strengths is performing math operations on entire arrays at once — **without loops**. This is called **element-wise** operation.

### Array vs Scalar Operations

A **scalar** is a single number. When you perform a math operation between an array and a scalar, NumPy applies that operation to **every element**.

```python
import numpy as np
x = np.array([10, 20, 30])

print(x + 5)     # Addition
print(x - 5)     # Subtraction
print(x * 2)     # Multiplication
print(x / 2)     # Division
print(x // 3)    # Floor Division
print(x % 3)     # Modulus
print(x ** 2)    # Power/Exponent
```

**Output:**

```
[15 25 35]
[ 5 15 25]
[20 40 60]
[ 5. 10. 15.]
[ 3  6 10]
[1 2 0]
[100 400 900]
```

### Array vs Array Operations

When two arrays have the **same shape**, operations are applied **element-by-element** (position 0 with position 0, position 1 with position 1, and so on).

```python
import numpy as np
y = np.array([1, 2, 3])
z = np.array([10, 20, 30])

print(y + z)
print(y * z)
```

**Output:**

```
[11 22 33]
[10 40 90]
```

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | `arr + 5` |
| `-` | Subtraction | `arr - 5` |
| `*` | Multiplication | `arr * 2` |
| `/` | Division | `arr / 2` |
| `//` | Floor Division | `arr // 3` |
| `%` | Modulus (remainder) | `arr % 3` |
| `**` | Power/Exponent | `arr ** 2` |

> ✅ **Tip:** Before NumPy, you would need a `for` loop and an empty list to do this — with NumPy, it's a single line of code, and it runs much faster, especially on large datasets.

---

## 11. Statistical Functions

Statistical (aggregation) functions let you summarize a dataset with a single value — total, average, smallest, largest, and so on.

### `np.sum()`

**Purpose:** Adds up all the elements.

**Syntax:** `np.sum(array)`

```python
import numpy as np
s = np.array([10, 20, 30, 40, 50])
print(np.sum(s))
```

**Output:** `150`

**Real-world use case:** Calculating the total revenue from a list of daily sales.

### `np.mean()`

**Purpose:** Calculates the average value.

**Syntax:** `np.mean(array)`

```python
print(np.mean(s))
```

**Output:** `30.0`

**Real-world use case:** Finding the average marks of students, average temperature of a city.

### `np.median()`

**Purpose:** Finds the **middle value** when the data is sorted (less affected by extreme outliers than the mean).

**Syntax:** `np.median(array)`

```python
print(np.median(s))
```

**Output:** `30.0`

**Real-world use case:** Median household income (less skewed by a few very rich/poor outliers compared to the average).

### `np.min()`

**Purpose:** Finds the smallest value.

**Syntax:** `np.min(array)`

```python
print(np.min(s))
```

**Output:** `10`

**Real-world use case:** Finding the lowest stock price in a month.

### `np.max()`

**Purpose:** Finds the largest value.

**Syntax:** `np.max(array)`

```python
print(np.max(s))
```

**Output:** `50`

**Real-world use case:** Finding the highest-selling product's price.

### `np.std()`

**Purpose:** Calculates the **standard deviation** — how spread out the values are from the mean. A small value means the data is tightly clustered; a large value means it is spread out.

**Syntax:** `np.std(array)`

```python
print(np.std(s))
```

**Output:** `14.142135623730951`

**Real-world use case:** Measuring how consistent a factory's product weights are.

### `np.var()`

**Purpose:** Calculates the **variance** — the square of the standard deviation. It also measures spread, but in squared units.

**Syntax:** `np.var(array)`

```python
print(np.var(s))
```

**Output:** `200.0`

**Real-world use case:** Used internally in many statistics and machine learning formulas (e.g., calculating risk in finance).

### Quick Reference Table

| Function | Purpose | Example Output (on `[10,20,30,40,50]`) |
|---|---|---|
| `np.sum()` | Total of all values | `150` |
| `np.mean()` | Average value | `30.0` |
| `np.median()` | Middle value | `30.0` |
| `np.min()` | Smallest value | `10` |
| `np.max()` | Largest value | `50` |
| `np.std()` | Spread from mean (standard deviation) | `14.142...` |
| `np.var()` | Spread squared (variance) | `200.0` |

---

## 12. Aggregation Operations (axis)

When working with 2D (or higher) arrays, you often want to calculate statistics **per row** or **per column**, instead of for the entire array. This is controlled using the `axis` parameter.

| Axis | Direction | Meaning |
|---|---|---|
| `axis=0` | ⬇️ Top to bottom | Operates **down the columns** (column-wise) |
| `axis=1` | ➡️ Left to right | Operates **across the rows** (row-wise) |
| (none) | — | Operates on the **entire** array, flattened |

**Diagram:**

```
              axis=1 ➡
        ┌───┬───┬───┐
 axis=0 │ 1 │ 2 │ 3 │
   ⬇    ├───┼───┼───┤
        │ 4 │ 5 │ 6 │
        └───┴───┴───┘
```

```python
import numpy as np
m = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(m, axis=0))   # column-wise sum
print(np.sum(m, axis=1))   # row-wise sum
```

**Output:**

```
[5 7 9]
[ 6 15]
```

**Explanation:**
- `axis=0` adds column-wise: `1+4=5`, `2+5=7`, `3+6=9`
- `axis=1` adds row-wise: `1+2+3=6`, `4+5+6=15`

> ✅ **Tip:** A common trick to remember: `axis=0` moves **down** (through rows), `axis=1` moves **across** (through columns) — and `axis=0` collapses rows, `axis=1` collapses columns into single per-row results.

This works with all aggregation functions — `np.mean(m, axis=0)`, `np.max(m, axis=1)`, etc.

---

## 13. Random Module

The `np.random` module generates random numbers — useful for simulations, testing, shuffling data, and initializing machine learning models.

### `np.random.rand()`

Generates random floats between 0 and 1 (uniform distribution).

```python
import numpy as np
print(np.random.rand(3))
```

**Example Output:**

```
[0.5488135  0.71518937 0.60276338]
```

### `np.random.randn()`

Generates random floats from a standard normal (bell-curve) distribution — values can be negative.

```python
print(np.random.randn(3))
```

**Example Output:**

```
[ 0.49671415 -0.1382643   0.64768854]
```

### `np.random.randint()`

Generates random whole numbers (integers) within a specified range.

**Syntax:** `np.random.randint(low, high, size)`

```python
print(np.random.randint(1, 10, size=5))
```

**Example Output:**

```
[6 3 8 1 9]
```

### `np.random.seed()`

**Purpose:** Makes random number generation **reproducible**. Without a seed, you get different random numbers every time you run your code. With a seed, you get the **exact same** "random" numbers every time — useful for testing and sharing reproducible results with others.

```python
import numpy as np

np.random.seed(0)
print(np.random.rand(3))   # first run

np.random.seed(0)
print(np.random.rand(3))   # second run — identical output!
```

**Output:**

```
[0.5488135  0.71518937 0.60276338]
[0.5488135  0.71518937 0.60276338]
```

> ✅ **Tip:** Always set a seed (e.g., `np.random.seed(42)`) in tutorials, tests, and shared notebooks so that results are reproducible for everyone.

---

## 14. Array Manipulation

Real-world datasets are rarely static — you often need to add new values, remove unnecessary ones, or combine/split datasets. Unlike Python lists, **NumPy arrays have a fixed size**, so every "modification" function actually returns a **brand-new array** rather than changing the array in place.

### `np.append()`

Adds value(s) to the **end** of an array.

```python
import numpy as np
a = np.array([1, 2, 3])
result = np.append(a, [4, 5])
print(result)
```

**Output:**

```
[1 2 3 4 5]
```

### `np.insert()`

Inserts value(s) at a **specific position (index)**.

**Syntax:** `np.insert(array, index, value, axis=None)`

```python
import numpy as np
a = np.array([1, 2, 3])
result = np.insert(a, 1, 99)
print(result)
```

**Output:**

```
[ 1 99  2  3]
```

For 2D arrays, use `axis=0` to insert a new **row**, or `axis=1` to insert a new **column**:

```python
import numpy as np
arr2d = np.array([[1, 2], [3, 4]])
result = np.insert(arr2d, 1, [5, 6], axis=0)
print(result)
```

**Output:**

```
[[1 2]
 [5 6]
 [3 4]]
```

### `np.delete()`

Removes value(s) at a **specific index**.

**Syntax:** `np.delete(array, index, axis=None)`

```python
import numpy as np
a = np.array([1, 2, 3])
result = np.delete(a, 1)
print(result)
```

**Output:**

```
[1 3]
```

> 📝 **Note:** Unlike Python lists, NumPy does **not** support removing an element "in-place" by its value — you must use the index, and it always returns a new array.

### `np.concatenate()`

Joins two or more arrays along a specified axis.

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.concatenate((a, b))
print(result)
```

**Output:**

```
[1 2 3 4 5 6]
```

### `np.stack()`, `np.vstack()`, `np.hstack()`

These combine arrays into a new array, but along different "directions":

| Function | Direction | Description |
|---|---|---|
| `np.vstack()` | Vertical (rows) | Stacks arrays **on top of each other** |
| `np.hstack()` | Horizontal (columns) | Stacks arrays **side by side** |
| `np.stack()` | New axis | Joins arrays along a brand-new axis |

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))
print(np.hstack((a, b)))
```

**Output:**

```
[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]
```

### `np.split()`

Divides one array into multiple **equal-sized** sub-arrays.

**Syntax:** `np.split(array, number_of_parts)`

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
result = np.split(arr, 3)
print(result)
```

**Output:**

```
[array([1, 2]), array([3, 4]), array([5, 6])]
```

> ⚠️ **Warning:** If the array **cannot be split evenly** into the requested number of parts, NumPy raises a `ValueError`. For example, splitting a 6-element array into 20 parts is impossible.

---

## 15. Sorting and Searching

### `np.sort()`

Returns a **sorted copy** of an array (ascending order by default).

```python
import numpy as np
arr = np.array([5, 2, 9, 1, 7])
print(np.sort(arr))
```

**Output:**

```
[1 2 5 7 9]
```

### `np.argsort()`

Returns the **indices** that would sort the array — useful when you need to know the original positions after sorting.

```python
print(np.argsort(arr))
```

**Output:**

```
[3 1 0 4 2]
```

This means: the smallest value is at original index `3`, the next smallest is at index `1`, and so on.

### `np.where()`

Returns the **indices** where a condition is `True`. Can also be used like an if-else for arrays.

**Syntax:** `np.where(condition)` or `np.where(condition, value_if_true, value_if_false)`

```python
arr = np.array([5, 2, 9, 1, 7])
print(np.where(arr > 4))
```

**Output:**

```
(array([0, 2, 4]),)
```

This means elements at indices `0, 2, 4` (values `5, 9, 7`) satisfy the condition `> 4`.

You can also use it to replace values conditionally:

```python
print(np.where(arr > 4, "High", "Low"))
```

**Output:**

```
['High' 'Low' 'High' 'Low' 'High']
```

### `np.searchsorted()`

Finds the **index** where a value should be inserted into a **sorted** array to keep it sorted.

```python
sorted_arr = np.array([1, 3, 5, 7, 9])
print(np.searchsorted(sorted_arr, 6))
```

**Output:**

```
3
```

(`6` should be inserted at index `3`, between `5` and `7`, to keep the array sorted.)

**Use case:** Efficiently finding the correct insertion point in large sorted datasets (e.g., binary search–style lookups), much faster than scanning the whole array.

---

## 16. Boolean Masking and Filtering

Boolean masking is one of the most practically useful NumPy skills — it lets you filter data based on conditions, just like filtering rows in a spreadsheet.

### How It Works

A condition applied to an array produces a **Boolean array** (`True`/`False` for every element). Using this Boolean array as an index returns only the elements where the value is `True`.

```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

mask = arr > 20
print(mask)
print(arr[mask])
```

**Output:**

```
[False False  True  True  True]
[30 40 50]
```

### Filtering with a Single Condition

```python
print(arr[arr > 20])
```

**Output:**

```
[30 40 50]
```

### Filtering with Multiple Conditions

Use `&` (AND) and `|` (OR) — **not** Python's `and`/`or` — to combine conditions on arrays. Each condition must be wrapped in parentheses.

```python
print(arr[(arr > 20) & (arr < 50)])
print(arr[(arr == 10) | (arr == 50)])
```

**Output:**

```
[30 40]
[10 50]
```

> ⚠️ **Warning:** Using Python's regular `and`/`or` keywords with NumPy arrays will raise an error or give incorrect results. Always use `&` and `|` for element-wise array conditions.

### Real-World Example

Imagine an employee dataset where you want to find everyone earning more than ₹50,000:

```python
import numpy as np
salaries = np.array([45000, 60000, 38000, 72000, 51000])
high_earners = salaries[salaries > 50000]
print(high_earners)
```

**Output:**

```
[60000 72000 51000]
```

> ✅ **Tip:** Boolean masking is roughly **10x faster** than using a loop with `if` conditions to filter data — and is heavily used in data cleaning and machine learning preprocessing pipelines.

---

## 17. Broadcasting

### What is Broadcasting?

**Broadcasting** is a NumPy feature that allows you to perform mathematical operations on arrays of **different shapes**, without writing a loop and without manually resizing either array. NumPy automatically "stretches" the smaller array so it matches the shape of the larger one.

**Why it's needed:** Without broadcasting, applying an operation to arrays of different shapes would require manually looping through each element — slow and tedious, especially for large datasets.

### Example of the Problem (without broadcasting / using a loop)

```python
prices = [100, 200, 300]
discount = 10
final_prices = []

for price in prices:
    final_prices.append(price - (price * discount / 100))

print(final_prices)
```

**Output:**

```
[90.0, 180.0, 270.0]
```

### The Same Task Using Broadcasting

```python
import numpy as np
prices = np.array([100, 200, 300])
discount = 10   # a single scalar value
final_prices = prices - (prices * discount / 100)
print(final_prices)
```

**Output:**

```
[ 90. 180. 270.]
```

No loop, no empty list — NumPy automatically applies the scalar `discount` to **every** element.

### Broadcasting Rules

NumPy follows **three rules** to decide if (and how) two arrays of different shapes can be broadcast together:

**Rule 1 — Matching Dimensions:** If both arrays have the **exact same shape**, the operation happens normally, element by element.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
```

**Output:** `[5 7 9]`

**Rule 2 — Expanding Single Elements:** If one array has size `1` along a dimension, NumPy "stretches" (expands) it to match the other array's size along that dimension.

```python
a = np.array([1, 2, 3])
b = 10
print(a + b)
```

**Output:** `[11 12 13]`

Here, the scalar `10` is "expanded" to `[10, 10, 10]` behind the scenes, then added.

**Rule 3 — Incompatible Shapes:** If the shapes don't match **and** neither has a size of `1` in the mismatched dimension, NumPy **cannot** broadcast them, and raises a `ValueError`.

```python
a = np.array([1, 2, 3])
b = np.array([1, 2])
print(a + b)
```

**Output:**

```
ValueError: operands could not be broadcast together with shapes (3,) (2,)
```

> ✅ **Fix:** If you get this error, check your array shapes using `.shape`, and use `.reshape()` to make the dimensions compatible.

### 1D to 2D Broadcasting

```python
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

result = matrix + vector
print(result)
```

**Output:**

```
[[11 22 33]
 [14 25 36]]
```

**Diagram:**

```
matrix (2x3)        vector (1x3, stretched to 2x3)
[1 2 3]        +     [10 20 30]    →   [11 22 33]
[4 5 6]               [10 20 30]        [14 25 36]
```

NumPy automatically repeats the 1D vector across every row of the matrix.

> 💡 **Why broadcasting is powerful:** It lets you write clean, fast, one-line code for operations that would otherwise need nested loops — making your programs both shorter and dramatically faster, especially on large datasets.

---

## 18. Universal Functions (ufuncs)

**Universal functions (ufuncs)** are NumPy functions that operate **element-wise** on arrays — applying a mathematical function to every single element automatically, without a loop.

### `np.sqrt()` — Square Root

```python
import numpy as np
x = np.array([1, 4, 9, 16])
print(np.sqrt(x))
```

**Output:**

```
[1. 2. 3. 4.]
```

### `np.exp()` — Exponential (e^x)

```python
print(np.exp(np.array([0, 1, 2])))
```

**Output:**

```
[1.         2.71828183 7.3890561 ]
```

### `np.log()` — Natural Logarithm

```python
print(np.log(np.array([1, np.e, np.e**2])))
```

**Output:**

```
[0. 1. 2.]
```

### `np.sin()`, `np.cos()`, `np.tan()` — Trigonometric Functions

```python
print(np.sin(0))     # 0.0
print(np.cos(0))     # 1.0
print(np.tan(0))     # 0.0
```

### `np.abs()` — Absolute Value

```python
print(np.abs(np.array([-1, -2, 3])))
```

**Output:**

```
[1 2 3]
```

### Quick Reference Table

| Function | Purpose |
|---|---|
| `np.sqrt()` | Square root of each element |
| `np.exp()` | e raised to the power of each element |
| `np.log()` | Natural logarithm (base e) |
| `np.sin()`, `np.cos()`, `np.tan()` | Trigonometric functions |
| `np.abs()` | Absolute (positive) value |

> ✅ **Tip:** Ufuncs are implemented in optimized, pre-compiled C code — this is one of the biggest reasons NumPy math operations are so much faster than equivalent Python loops using the `math` module.

---

## 19. Copy vs View

This is a **very common interview topic** and a frequent source of bugs for beginners.

### `copy()`

Creates a **completely independent** new array. Changing the copy does **not** affect the original array, and vice versa.

```python
import numpy as np
original = np.array([1, 2, 3, 4])
copy_arr = original.copy()
copy_arr[0] = 99

print("Original:", original)
print("Copy:", copy_arr)
```

**Output:**

```
Original: [1 2 3 4]
Copy: [99  2  3  4]
```

### `view()`

Creates a **new array object** that **shares the same underlying data/memory** as the original. Changing the view **does** affect the original array (and vice versa).

```python
import numpy as np
original = np.array([1, 2, 3, 4])
view_arr = original.view()
view_arr[0] = 99

print("Original:", original)
print("View:", view_arr)
```

**Output:**

```
Original: [99  2  3  4]
View: [99  2  3  4]
```

### Difference Table

| Feature | `copy()` | `view()` |
|---|---|---|
| Memory | New, independent memory | Shares memory with original |
| Changes affect original? | ❌ No | ✅ Yes |
| Speed | Slightly slower (extra memory allocation) | Faster (no duplication) |
| Use case | When you need a fully separate array | When you want to save memory and don't need independence |

> ⚠️ **Warning:** Many NumPy operations (like slicing, `reshape()`, and `ravel()`) return a **view** by default, not a copy. If you modify a sliced/reshaped array without realizing it's a view, you might accidentally change your original data! When in doubt, use `.copy()` explicitly to be safe.

---

## 20. Handling Missing Values

Real-world data is messy — it often contains missing or invalid entries. NumPy gives you tools to detect and handle these gracefully so your calculations don't break.

### `np.nan` — "Not a Number"

`np.nan` represents a **missing or undefined** numeric value — for example, an empty cell in a spreadsheet, or the result of an invalid calculation like `0/0`.

```python
import numpy as np
data = np.array([1, 2, np.nan, 4, np.nan])
print(data)
```

**Output:**

```
[ 1.  2. nan  4. nan]
```

> ⚠️ **Warning:** You **cannot** compare `np.nan` directly using `==` (e.g., `np.nan == np.nan` returns `False`!). Always use `np.isnan()` to detect missing values.

### `np.isnan()`

Detects which elements are `np.nan`. Returns a Boolean array.

```python
print(np.isnan(data))
```

**Output:**

```
[False False  True False  True]
```

### `np.nanmean()`, `np.nanmax()`, `np.nanmin()`

These calculate statistics while **ignoring** any `np.nan` values — regular `np.mean()`, `np.max()`, `np.min()` would return `nan` if even a single value is missing.

```python
print(np.nanmean(data))
print(np.nanmax(data))
print(np.nanmin(data))
```

**Output:**

```
2.3333333333333335
4.0
1.0
```

### Replacing Missing/Invalid Values — `np.nan_to_num()`

Replaces `np.nan` (and infinite values) with usable numbers.

```python
cleaned = np.nan_to_num(data, nan=0)
print(cleaned)
```

**Output:**

```
[1. 2. 0. 4. 0.]
```

### Handling Infinite Values — `np.isinf()`

`np.inf` represents an **infinitely large** number (e.g., the result of dividing by zero). `np.isinf()` detects such values, similar to `np.isnan()`.

```python
arr = np.array([2, np.inf, -np.inf, 5])
print(np.isinf(arr))
```

**Output:**

```
[False  True  True False]
```

> ✅ **Tip:** Machine learning models typically **cannot process** `nan` or `inf` values — always clean your data with these functions before feeding it into any model or further calculation.

---

## 21. NumPy Performance

### Why NumPy Is Fast

1. **Vectorization** — Operations are applied to the whole array at once, using optimized, pre-compiled C code under the hood — instead of looping through elements one-by-one in pure Python.
2. **Contiguous memory** — Array elements are stored next to each other in memory, which allows the CPU to process them very efficiently (and take advantage of modern CPU optimizations like SIMD).
3. **Fixed data type** — Since every element has the same type, NumPy doesn't need to check each element's type during operations (unlike Python lists).
4. **Memory efficiency** — Less memory usage means less overhead and faster access overall.

### Vectorization in Action

**Without vectorization (using a loop):**

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [x + y for x, y in zip(list1, list2)]
print(result)
```

**Output:** `[5, 7, 9]`

**With vectorization (NumPy):**

```python
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result)
```

**Output:** `[5 7 9]`

Both give the same result, but the NumPy version is dramatically faster on large datasets because there's no Python-level loop involved.

### Benchmark Example — Lists vs NumPy

```python
import numpy as np
import time

n = 2_000_000

# Using plain Python lists
list1 = list(range(n))
list2 = list(range(n))
start = time.time()
result_list = [list1[i] + list2[i] for i in range(n)]
list_time = time.time() - start

# Using NumPy arrays
arr1 = np.arange(n)
arr2 = np.arange(n)
start = time.time()
result_arr = arr1 + arr2
numpy_time = time.time() - start

print(f"Python list time: {list_time:.4f} sec")
print(f"NumPy array time: {numpy_time:.4f} sec")
```

**Example Output:**

```
Python list time: 0.6553 sec
NumPy array time: 0.1063 sec
```

In this run, NumPy was about **6x faster** — and the speed advantage grows even larger with bigger datasets and more complex operations. (Exact numbers vary depending on your machine, but NumPy is consistently and significantly faster.)

> 💡 **Note:** For simple element-wise addition, NumPy can be anywhere from a few times to over 100x faster than pure Python, depending on the size of the data and the complexity of the operation.

---

## 22. NumPy Best Practices

### Naming Conventions

- Always import NumPy with the standard alias: `import numpy as np`
- Use clear variable names for arrays (e.g., `salaries`, `temperatures`) instead of generic names like `a`, `b` in real projects (short names are fine for quick examples/practice).

### Performance Tips

- ✅ **Avoid Python loops** wherever possible — use vectorized operations instead.
- ✅ Use **broadcasting** instead of manually resizing arrays.
- ✅ Use **boolean masking** instead of `if` conditions inside loops.
- ✅ Pre-allocate arrays with `np.zeros()` / `np.empty()` when you know the final size, instead of repeatedly using `np.append()` in a loop (`append()` creates a new array every time, which is slow for large datasets).
- ✅ Use built-in aggregation functions (`np.sum()`, `np.mean()`, etc.) instead of manually summing through loops.

### Memory Tips

- Use the smallest data type that fits your data (e.g., `int8` instead of `int64` if your values are small) to save memory on large datasets.
- Be aware of whether an operation returns a **copy** or a **view** — use `.copy()` explicitly when you need full independence from the original array.
- Use `.nbytes` to check how much memory your array is actually using.

### Common Mistakes

| Mistake | Why it's a problem | Fix |
|---|---|---|
| Using `and`/`or` instead of `&`/`\|` for array conditions | Raises errors or gives wrong results | Use `&` and `\|`, with parentheses around each condition |
| Comparing `np.nan` with `==` | Always returns `False`, even `nan == nan` | Use `np.isnan()` |
| Assuming `reshape()`/`ravel()`/slicing always return a copy | They often return a **view**, so changes can silently affect the original array | Use `.copy()` when independence is needed |
| Forgetting the `axis` parameter | Aggregation functions default to operating on the *entire* flattened array | Always specify `axis=0` or `axis=1` for row/column-wise results |
| Mixing data types in an array | NumPy will "upcast" everything to a single common type, which can cause unexpected behavior | Keep arrays homogeneous; convert explicitly with `.astype()` |
| Using `np.empty()` and expecting zeros | Returns uninitialized garbage memory, not zeros | Use `np.zeros()` if you need a clean starting array |

### Interview Tips

- Be ready to explain `copy()` vs `view()`, and `flatten()` vs `ravel()` — these are extremely common interview questions.
- Practice explaining **broadcasting rules** with a simple example — interviewers love this topic because it tests real understanding, not memorization.
- Know the **time complexity advantage** of vectorized operations vs loops, even just qualitatively ("vectorized operations avoid the overhead of Python-level loops by using compiled C code").
- Be comfortable explaining **why arrays are faster than lists** in your own words — fixed type, contiguous memory, vectorization.

---

## 23. Frequently Asked Interview Questions

**Q1. What is NumPy, and why is it used?**
NumPy (Numerical Python) is a Python library for fast numerical computing using a powerful n-dimensional array object called `ndarray`. It's used because it offers much faster performance and lower memory usage than plain Python lists, plus built-in support for vectorized math and broadcasting.

**Q2. What is the difference between a Python list and a NumPy array?**
A Python list can hold mixed data types and is slower because of per-element type checking and scattered memory storage. A NumPy array requires a single data type, stores data in contiguous memory, and supports fast, vectorized mathematical operations.

**Q3. Why are NumPy arrays faster than Python lists?**
Because of (1) fixed/homogeneous data types — no per-element type checking, (2) contiguous memory storage — better CPU cache usage, and (3) vectorization — operations run in optimized, pre-compiled C code instead of Python-level loops.

**Q4. What is `ndarray`?**
`ndarray` (n-dimensional array) is NumPy's core data structure — a grid of values, all of the same type, indexed by a tuple of non-negative integers (its shape).

**Q5. How do you create a NumPy array?**
Using `np.array()`, passing a Python list or nested list: `np.array([1, 2, 3])`.

**Q6. What is the difference between `shape` and `size`?**
`shape` returns a tuple describing the array's dimensions (rows, columns, etc.), while `size` returns the **total number of elements** in the array, regardless of its shape.

**Q7. What is the difference between `ndim` and `shape`?**
`ndim` tells you **how many dimensions/axes** an array has (a single number), while `shape` tells you **the size along each of those dimensions** (a tuple).

**Q8. What does `dtype` mean?**
It refers to the **data type** of the elements stored in a NumPy array, such as `int64`, `float64`, or `bool`.

**Q9. How do you change the data type of an array?**
Using the `.astype()` method — for example, `arr.astype(int)` or `arr.astype(float)`.

**Q10. What is broadcasting in NumPy?**
Broadcasting is NumPy's mechanism for performing arithmetic operations on arrays of different shapes by automatically "stretching" the smaller array to match the shape of the larger one, without explicitly copying data or writing loops.

**Q11. What are the rules of broadcasting?**
(1) If shapes match exactly, operate element-wise normally. (2) If one array has size 1 along a dimension, it is stretched/expanded to match the other array. (3) If shapes don't match and neither has size 1 in the differing dimension, broadcasting fails with a `ValueError`.

**Q12. What is vectorization?**
Vectorization means applying an operation to an entire array at once (internally using optimized C loops) instead of using explicit Python-level `for` loops — resulting in much faster code.

**Q13. What is the difference between `copy()` and `view()`?**
`copy()` creates a completely independent array — changes to it do not affect the original. `view()` creates a new array object that shares the same underlying memory — changes to it **do** affect the original array, and vice versa.

**Q14. What is the difference between `flatten()` and `ravel()`?**
Both convert a multi-dimensional array into 1D. `flatten()` always returns a **copy** (original array is unaffected by changes). `ravel()` returns a **view** whenever possible (changes can affect the original array). `ravel()` is generally faster.

**Q15. How do you reverse a NumPy array without using a loop?**
By slicing with a step of `-1`: `arr[::-1]`.

**Q16. What is the difference between `np.zeros()` and `np.empty()`?**
`np.zeros()` creates an array filled with `0`. `np.empty()` creates an array without initializing values — it contains random "leftover" memory data and is slightly faster because it skips initialization, but its values should never be assumed/used before being explicitly set.

**Q17. How do you find missing values in an array?**
Using `np.isnan(array)`, which returns a Boolean array marking `True` wherever a value is `np.nan`.

**Q18. Why can't you compare `np.nan` using `==`?**
Because, by the IEEE floating-point standard, `np.nan` is defined to never be equal to anything — including itself. `np.nan == np.nan` evaluates to `False`. You must use `np.isnan()` instead.

**Q19. What is the difference between `np.mean()` and `np.nanmean()`?**
`np.mean()` returns `nan` if even one value in the array is `np.nan`. `np.nanmean()` ignores `np.nan` values and calculates the mean of the remaining valid values.

**Q20. What does the `axis` parameter do in aggregation functions?**
It controls the direction of the operation: `axis=0` operates column-wise (down the columns), and `axis=1` operates row-wise (across the rows). Without specifying `axis`, the function operates on the entire flattened array.

**Q21. How do you combine two arrays in NumPy?**
Using `np.concatenate()`, `np.vstack()` (stack vertically/by rows), or `np.hstack()` (stack horizontally/by columns).

**Q22. How do you split an array into equal parts?**
Using `np.split(array, number_of_parts)`. It raises a `ValueError` if the array cannot be split evenly.

**Q23. What is fancy indexing?**
Selecting multiple, non-sequential elements from an array at once using a list of index positions, e.g., `arr[[0, 2, 4]]`. It always returns a copy.

**Q24. What is boolean masking?**
A technique for filtering array elements based on a condition. The condition produces a Boolean array, and using it as an index returns only the elements where the condition is `True`. E.g., `arr[arr > 10]`.

**Q25. How do you apply multiple conditions when filtering a NumPy array?**
By using the `&` (AND) and `|` (OR) operators (not Python's `and`/`or`), with each condition wrapped in parentheses: `arr[(arr > 10) & (arr < 50)]`.

**Q26. What is the use of `np.where()`?**
It returns the indices where a condition is `True`, or can be used to conditionally select between two values: `np.where(condition, value_if_true, value_if_false)`.

**Q27. What is the difference between `np.sort()` and `np.argsort()`?**
`np.sort()` returns the array values sorted in order. `np.argsort()` returns the **indices** that would sort the array, keeping track of original positions.

**Q28. Can you reshape any array into any shape?**
No. The total number of elements must remain the same before and after reshaping — e.g., a 6-element array can become shape `(2,3)` or `(3,2)` or `(6,)`, but not `(2,4)` (which needs 8 elements).

**Q29. What does `reshape(-1, 1)` mean?**
Using `-1` tells NumPy to **automatically calculate** that dimension's size based on the total number of elements and the other specified dimensions. `reshape(-1, 1)` converts an array into a single column (2D array with 1 column, however many rows are needed).

**Q30. What is an identity matrix, and how do you create one in NumPy?**
A square matrix with `1`s on the main diagonal and `0`s everywhere else. Created using `np.eye(n)` or `np.identity(n)`.

**Q31. What is the difference between `np.random.rand()` and `np.random.randn()`?**
`np.random.rand()` generates random floats from a **uniform** distribution between 0 and 1. `np.random.randn()` generates random floats from a **standard normal (bell-curve)** distribution centered at 0, which can include negative values.

**Q32. Why do we use `np.random.seed()`?**
To make random number generation **reproducible** — calling the same seed before generating random numbers will always produce the exact same sequence of "random" values, which is useful for testing and sharing reproducible results.

**Q33. What is a ufunc (universal function)?**
A NumPy function that operates element-wise on arrays, implemented in optimized C code — examples include `np.sqrt()`, `np.exp()`, `np.log()`, and `np.sin()`.

**Q34. How is a NumPy array stored differently in memory compared to a Python list?**
A NumPy array stores raw values directly in one contiguous block of memory with a fixed type and size per element. A Python list stores **references (pointers)** to separate Python objects scattered across memory, each carrying extra overhead (type info, reference count).

**Q35. What real-world libraries/fields are built on top of NumPy?**
Pandas (data analysis), Matplotlib (plotting), Scikit-learn (machine learning), and many deep learning frameworks rely on NumPy-style array operations as their foundation.

---

## 24. Cheat Sheet

### Importing

```python
import numpy as np
```

### Array Creation

| Function | Example |
|---|---|
| `np.array()` | `np.array([1,2,3])` |
| `np.zeros()` | `np.zeros((2,3))` |
| `np.ones()` | `np.ones((2,3))` |
| `np.full()` | `np.full((2,3), 7)` |
| `np.empty()` | `np.empty((2,2))` |
| `np.arange()` | `np.arange(0,10,2)` |
| `np.linspace()` | `np.linspace(0,10,5)` |
| `np.eye()` / `np.identity()` | `np.eye(3)` |
| `np.random.rand()` | `np.random.rand(2,3)` |
| `np.random.randint()` | `np.random.randint(1,10,size=5)` |
| `np.random.randn()` | `np.random.randn(2,3)` |

### Attributes

| Attribute | Meaning |
|---|---|
| `.shape` | Dimensions (rows, cols, ...) |
| `.size` | Total number of elements |
| `.ndim` | Number of dimensions |
| `.dtype` | Data type of elements |
| `.itemsize` | Bytes per element |
| `.nbytes` | Total bytes used |

### Indexing & Slicing

| Syntax | Meaning |
|---|---|
| `arr[i]` | Element at index `i` |
| `arr[-1]` | Last element |
| `arr[i:j]` | Slice from `i` to `j-1` |
| `arr[i:j:k]` | Slice with step `k` |
| `arr[::-1]` | Reversed array |
| `arr2d[r, c]` | Row `r`, column `c` |
| `arr2d[:, c]` | Entire column `c` |
| `arr2d[r, :]` | Entire row `r` |
| `arr[[0,2,4]]` | Fancy indexing |
| `arr[arr > 5]` | Boolean masking |

### Reshaping

| Function | Meaning |
|---|---|
| `arr.reshape(r,c)` | Change shape (returns view if possible) |
| `arr.flatten()` | Convert to 1D (copy) |
| `arr.ravel()` | Convert to 1D (view) |
| `arr.T` / `arr.transpose()` | Transpose rows/columns |

### Math & Stats

| Function | Meaning |
|---|---|
| `+ - * / // % **` | Element-wise math operators |
| `np.sum()` | Total |
| `np.mean()` | Average |
| `np.median()` | Middle value |
| `np.min()` / `np.max()` | Smallest / largest |
| `np.std()` / `np.var()` | Standard deviation / variance |
| `axis=0` / `axis=1` | Column-wise / row-wise |

### Array Manipulation

| Function | Meaning |
|---|---|
| `np.append(arr, val)` | Add to end |
| `np.insert(arr, i, val)` | Insert at index |
| `np.delete(arr, i)` | Remove at index |
| `np.concatenate((a,b))` | Join arrays |
| `np.vstack((a,b))` | Stack vertically |
| `np.hstack((a,b))` | Stack horizontally |
| `np.split(arr, n)` | Split into `n` equal parts |

### Sorting & Searching

| Function | Meaning |
|---|---|
| `np.sort(arr)` | Sorted copy |
| `np.argsort(arr)` | Indices that would sort |
| `np.where(cond)` | Indices where condition is true |
| `np.searchsorted(arr, val)` | Insertion index in sorted array |

### Missing/Invalid Values

| Function | Meaning |
|---|---|
| `np.nan` | Missing value placeholder |
| `np.isnan(arr)` | Detect `nan` values |
| `np.nanmean()` / `np.nanmax()` / `np.nanmin()` | Stats ignoring `nan` |
| `np.nan_to_num(arr)` | Replace `nan`/`inf` with numbers |
| `np.isinf(arr)` | Detect infinite values |

### Copy vs View

| | Independent? | Affects Original? |
|---|---|---|
| `.copy()` | ✅ Yes | ❌ No |
| `.view()` | ❌ No (shares memory) | ✅ Yes |

---

## 25. Practice Exercises

> 💡 **Tip:** Try to solve each question on your own before checking any solution. Use `print()` after every step to see what's happening.

### Beginner Level (15 Questions)

1. Create a 1D NumPy array containing the numbers 1 to 10.
2. Create a 2D array of shape `(3, 3)` filled with zeros.
3. Create an array of 5 elements, all equal to `9`, using `np.full()`.
4. Create an array using `np.arange()` containing even numbers from 2 to 20.
5. Find the `shape`, `size`, and `ndim` of a 2D array of your choice.
6. Access the 3rd element of a 1D array using positive indexing.
7. Access the last element of an array using negative indexing.
8. Slice out the first 4 elements of an array.
9. Reverse a 1D array using slicing (no loops allowed).
10. Create a 2D array and access a single row and a single column separately.
11. Add `10` to every element of an array using broadcasting.
12. Create two arrays of the same shape and add them together.
13. Find the `mean`, `min`, and `max` of an array of marks: `[56, 78, 90, 45, 67]`.
14. Convert a list `[1.5, 2.7, 3.9]` into a NumPy array and then convert its dtype to `int`.
15. Create an identity matrix of size `5 x 5`.

### Intermediate Level (15 Questions)

1. Reshape a 1D array of 12 elements into a `(3, 4)` 2D array.
2. Flatten a 2D array back into 1D using both `flatten()` and `ravel()`, and explain the difference.
3. Use boolean masking to extract all even numbers from an array of 1 to 20.
4. Use `np.where()` to replace all negative numbers in an array with `0`.
5. Create a 2D array and find the sum of each row and each column separately using `axis`.
6. Generate a `4x4` array of random integers between 1 and 100 using a fixed seed (so results are reproducible).
7. Concatenate two 1D arrays and then split the result back into 2 equal parts.
8. Stack two arrays vertically and then horizontally, and observe the difference in shape.
9. Insert a new row into a 2D array at index 1.
10. Delete the second column from a 2D array.
11. Create an array with some missing values (`np.nan`) and replace them with the array's mean (ignoring the `nan`s).
12. Sort an array of exam scores and also find the indices that would sort it (`argsort`).
13. Create two arrays of different shapes that successfully broadcast together. Print the result and explain why it worked.
14. Create two arrays of incompatible shapes and observe (and explain) the broadcasting error.
15. Demonstrate the difference between `copy()` and `view()` with a working code example.

### Advanced Level (10 Questions)

1. Simulate rolling a six-sided die 1000 times using `np.random.randint()` and find how many times each face (1–6) appeared.
2. Given a 2D array representing students' marks across 3 subjects (rows = students, columns = subjects), calculate each student's average and each subject's class average.
3. Create a function that standardizes an array (subtract mean, divide by standard deviation) using only NumPy operations — no loops.
4. Given an array with missing values and outliers, clean it by (a) filling missing values with the median, and (b) capping values beyond 3 standard deviations from the mean.
5. Implement matrix multiplication of two 2D arrays using NumPy (research and use the appropriate operator/function) and explain how it differs from element-wise multiplication.
6. Write vectorized code (no loops) to calculate the Euclidean distance between two points represented as NumPy arrays.
7. Create a `5x5` array and extract its diagonal elements without using a loop (hint: explore `np.diag()`).
8. Given a 1D array of timestamps (numbers), use `np.searchsorted()` to find where a new value should be inserted to keep the array sorted.
9. Compare the execution time of summing 5 million numbers using a Python loop vs. `np.sum()`, and report the speed difference.
10. Build a small "outlier remover" function: given any 1D array, return only the values that fall within 2 standard deviations of the mean.

---

## 26. Mini Projects

### Project 1: Student Marks Analyzer

**Problem statement:** Given a 2D array where each row represents a student and each column represents marks in a subject, analyze the data to find each student's total and average marks, the topper, and each subject's class average.

**Approach:**
1. Store the marks data in a 2D NumPy array.
2. Use `axis=1` to calculate each student's total/average marks (row-wise).
3. Use `axis=0` to calculate each subject's class average (column-wise).
4. Use `np.argmax()` on the row totals to find the index of the topper.

**NumPy concepts used:** 2D arrays, `axis`-based aggregation (`np.sum`, `np.mean`), `np.argmax()`, indexing.

### Project 2: Weather Data Analyzer

**Problem statement:** Given a week's worth of daily temperature readings for multiple cities, find the hottest/coldest city, the average temperature per city, and which days had temperatures above a certain threshold.

**Approach:**
1. Store data as a 2D array (rows = cities, columns = days).
2. Use aggregation functions with `axis` to compute per-city and per-day statistics.
3. Use boolean masking to find days/cities exceeding a temperature threshold.
4. Handle any missing readings using `np.isnan()` and `np.nanmean()`.

**NumPy concepts used:** 2D arrays, aggregation with `axis`, boolean masking, missing value handling.

### Project 3: Sales Data Dashboard

**Problem statement:** Given monthly sales figures for several products across several months, calculate total sales per product, best/worst performing month, and month-over-month growth.

**Approach:**
1. Represent the data as a 2D array (rows = products, columns = months).
2. Use `axis=1` for total sales per product, `axis=0` for total sales per month.
3. Use slicing to compare consecutive months for growth calculations (`sales[:, 1:] - sales[:, :-1]`).
4. Use `np.argmax()`/`np.argmin()` to identify best/worst months.

**NumPy concepts used:** 2D arrays, aggregation, slicing, broadcasting, `np.argmax()`/`np.argmin()`.

### Project 4: Stock Market Calculator

**Problem statement:** Given a list of daily closing prices for a stock, calculate daily returns, the highest/lowest price, volatility (standard deviation), and a simple moving average.

**Approach:**
1. Store closing prices as a 1D array.
2. Calculate daily returns using slicing: `(prices[1:] - prices[:-1]) / prices[:-1]`.
3. Use `np.std()` on the returns to measure volatility.
4. Implement a simple moving average using slicing and `np.mean()` over rolling windows.

**NumPy concepts used:** 1D arrays, slicing, broadcasting, statistical functions.

### Project 5: Image Matrix Operations

**Problem statement:** Represent a small grayscale image as a 2D array of pixel values (0–255) and perform basic image-processing operations: brightening, inverting colors, and cropping a region.

**Approach:**
1. Represent the image as a 2D (or 3D, for color) NumPy array.
2. Brighten the image by adding a constant value (with clipping using `np.clip()` to stay within 0–255).
3. Invert colors using `255 - image`.
4. Crop a region using 2D slicing (`image[r1:r2, c1:c2]`).

**NumPy concepts used:** 2D/3D arrays, broadcasting, slicing, `np.clip()`.

---

## 27. Summary

### Key Takeaways

- NumPy is the **foundation** of numerical computing, data science, and machine learning in Python.
- NumPy arrays (`ndarray`) are **faster** and more **memory-efficient** than Python lists because of fixed data types, contiguous memory, and vectorization.
- **Indexing, slicing, and boolean masking** let you access and filter data without loops.
- **Broadcasting** allows operations between arrays of different shapes automatically.
- **Vectorization** is the core reason NumPy code is so much faster than equivalent pure-Python loops.
- Understanding the difference between a **copy** and a **view** prevents subtle, hard-to-find bugs.
- NumPy provides built-in tools to handle **missing values** (`np.nan`) and **infinite values** (`np.inf`) safely.

### Most Important Functions to Remember

```
np.array()        np.zeros()       np.ones()
np.arange()       np.linspace()    np.reshape()
np.sum()          np.mean()        np.std()
np.sort()         np.where()       np.concatenate()
np.isnan()        np.nan_to_num()  np.random.randint()
```

### Learning Roadmap After NumPy

1. **Pandas** — for working with labeled, tabular data (DataFrames), built on top of NumPy.
2. **Matplotlib / Seaborn** — for data visualization and plotting.
3. **Scikit-learn** — for classical machine learning algorithms.
4. **SciPy** — for advanced scientific and mathematical computing.
5. **TensorFlow / PyTorch** — for deep learning, where array/tensor operations are conceptually very similar to NumPy.

> 🎯 **Final tip:** Concepts alone are not enough — practice writing NumPy code daily on real or sample datasets. The fastest way to master NumPy is to **use it**, not just read about it.

---

*End of NumPy Complete Notes.*
