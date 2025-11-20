# Part 5 — Exception Handling & File I/O

Covers `try/except/else/finally`, raising exceptions, `assert`, custom exceptions, reading/writing files and basic OS operations.

---

## 1. Exceptions: try/except/else/finally
What: Handle runtime errors safely.
Example:
```python
try:
    v = int(input())
except ValueError:
    print('invalid')
else:
    print('ok', v)
finally:
    print('cleanup')
```
Interview Qs:
- Why catch specific exceptions rather than a bare `except:`?

---

## 2. Raising & custom exceptions
Example:
```python
class ConfigError(Exception):
    pass

if not valid:
    raise ConfigError('bad config')
```
Interview Qs:
- When to create custom exceptions?

---

## 3. File I/O
Example read/write:
```python
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

with open('out.txt','w') as f:
    f.write('hello')
```
Interview Qs:
- Why use `with` for file operations?

---

## 4. OS and path utilities
Example:
```python
import os
print(os.path.join('dir','file.txt'))
```
Interview Qs:
- How to handle platform-specific paths? (use pathlib)

---

## Practice
- Write a program that reads a CSV log and writes a summary file, with robust exception handling and tests.