# Part 6 — Modules, Packages & Imports

Covers how to structure code into reusable modules, packaging, relative/absolute imports, `__init__.py`, and common pitfalls.

---

## 1. Modules & import
What: A module is a .py file. Use `import` or `from .. import`.
Example:
```python
# utils.py
def add(a,b): return a+b

# main.py
from utils import add
print(add(2,3))
```
Interview Qs:
- Explain relative imports and why they can fail when running directly.

---

## 2. Packages & __init__.py
What: A package is a folder containing modules and optional `__init__.py`.
Why: Organize large codebases.

---

## 3. Packaging (setup, pyproject)
- Quick overview of `pyproject.toml`, `setuptools`, and publishing to PyPI.

---

## 4. Import hooks & reload
- `importlib.reload()` for reloading modules during development.

---

## Practice
- Create a small package `mypkg` with `utils` and `cli` modules and demonstrate relative vs absolute imports.