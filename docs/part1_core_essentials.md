# Part 1 — Python Core Essentials

This lesson covers the fundamentals every developer and DevOps engineer must know: printing, variables, data types, conversions, math operations and strings. Each section includes: a short definition, layman explanation, small runnable example, and interview question set.

---

## 1. Printing & Comments

What: `print()` sends text to stdout; comments start with `#`.
Why: Show program output and document code.
How:
```python
# Print a message
print('Hello, DevOps!')
```
Interview Qs:
- What does `print()` return? (None)
- When is `print()` appropriate vs logging?

---

## 2. Variables & Assignment

What: Names that hold values.
Why: Store and reuse data.
How:
```python
x = 10
name = 'app-01'
```
Interview Qs:
- Explain Python variable naming rules.
- What is dynamic typing?

---

## 3. Basic Data Types

- int, float, str, bool
- list, tuple, dict, set (details in Part 2)

Example:
```python
count = 5           # int
ratio = 0.75        # float
active = True       # bool
msg = "OK"        # str
```
Interview Qs:
- When to use `float` vs `Decimal`?
- What is `bool` a subclass of?

---

## 4. Type Conversion

What: convert between types using `int()`, `float()`, `str()`, `bool()`.
Example:
```python
s = '123'
n = int(s)  # 123
```
Interview Qs:
- How does `int('12.3')` behave? (ValueError)
- How to safely parse user input?

---

## 5. Math Operations

Operators: `+ - * / // % **`
Example:
```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
print(2 ** 3)  # 8
```
Interview Qs:
- Difference between `/` and `//`.
- How to avoid floating point rounding issues?

---

## 6. Strings (quick)

What: sequence of characters. Immutable.
Example:
```python
s = "deploy-2025"
print(s.split('-'))  # ['deploy', '2025']
```
Interview Qs:
- Why are strings immutable? What advantage?
- Explain f-strings and format.

---

## Practice exercises
1. Read input, convert to int, and print squared value (handle invalid input).
2. Given a version string `v='2.5.1'` split into parts and print as ints.

---

References & next: Part 2 (collections and control flow) will expand on lists/tuples/dicts/sets and looping constructs.