# Python DevOps Interview Answers — Parts 1–7

This document answers the interview questions listed across Parts 1–7 (Core → DevOps apps). Each question includes a concise, interview-friendly answer, a short explanation, and a tiny code example where helpful.

---

## Part 1 — Core Essentials

Q: What does `print()` return?

A: `print()` returns `None`.

- Explanation: `print()` writes to stdout and does not return a value. Use it for quick debugging; prefer `logging` for production.
- Example:
```python
r = print('hi')
assert r is None
```

Q: When is `print()` appropriate vs `logging()`?

A: Use `print()` for quick debugging, demos, or scripts. Use `logging` in libraries and production code because logging supports levels, handlers, formatting, and can be configured instead of printing to stdout.

Q: Explain Python variable naming rules.

A: Variable names must start with a letter or underscore, followed by letters, digits, or underscores. They are case-sensitive. Avoid names that shadow built-ins.

Q: What is dynamic typing?

A: Variables are not bound to types; objects have types. A variable name can refer to objects of different types over time.

Q: When to use `float` vs `Decimal`?

A: Use `float` for general scientific calculations where binary floating point is fine. Use `decimal.Decimal` for financial or precise decimal arithmetic to avoid rounding errors.

Example:
```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.2')  # exact 0.3
0.1 + 0.2  # 0.30000000000000004
```

Q: `int('12.3')` behaviour and how to safely parse user input?

A: `int('12.3')` raises `ValueError`. Use `float()` first or parse with try/except.

```python
s='12.3'
try:
    n=int(s)
except ValueError:
    n=int(float(s))  # or handle error
```

Q: Difference between `/` and `//`.

A: `/` is true division (float result). `//` is floor division (integer-like if both operands int; result truncated toward negative infinity).

Q: How to avoid floating point rounding issues?

A: Use `decimal.Decimal` or rational approximations (fractions.Fraction) for exact arithmetic, or round results when appropriate.

Q: Why are strings immutable? Advantages?

A: Immutability simplifies reasoning, enables safe reuse, allows strings to be hashable (usable as dict keys), and improves performance (interning, sharing memory). For modifications, create new strings or use `list`/`io.StringIO` for many edits.

Q: Explain f-strings and `str.format()` briefly.

A: f-strings (Python 3.6+) are concise and evaluated at runtime: `f"{var}"`. `str.format()` works on older Python versions and supports named placeholders. f-strings are generally faster and more readable.

---

## Part 2 — Intermediate Python

Q: When to use list vs tuple?

A: Use lists for mutable sequences you modify (append/pop). Use tuples for fixed-size records, keys in dicts, or when immutability is desired (safety). Tuples may be slightly faster and communicate intent.

Q: Complexity of `list.insert(0, x)`?

A: O(n) — inserting at the front requires shifting all elements. Use `collections.deque` for efficient append/pop from both ends (O(1)).

Q: Why use tuples as dict keys?

A: Tuples are immutable and hashable (if elements are hashable), so they can be used as dictionary keys to represent compound keys (e.g., coordinates).

Q: Difference between set and frozenset?

A: `set` is mutable, `frozenset` is immutable and hashable (can be used as dict keys or elements of other sets). Use `frozenset` for fixed membership where hashing is required.

Q: Memory implication: list comprehension vs generator expression.

A: List comprehensions build the whole list in memory. Generator expressions yield items lazily and use constant memory, which is preferable for large data streams.

---

## Part 3 — Functions & Advanced Concepts

Q: Differences between positional, keyword-only, and default args.

A: Positional args are supplied by position. Default args provide default values if not passed. Keyword-only args (after `*` in the signature) must be passed by keyword, improving clarity and avoiding positional confusion.

Example:
```python
def f(a, b=2, *, mode='fast'):
    pass
```

Q: `*args` vs `list` argument — when to use which?

A: `*args` collects positional args into a tuple for flexible interfaces. Passing a list is fine when the number of items is already in a collection. Use `*` to allow call-site convenience: `f(1,2,3)` vs `f([1,2,3])`.

Q: When to prefer `lambda` vs `def`?

A: Use `lambda` for short anonymous functions (single expression) passed inline (sorting key). Use `def` for multi-line logic, readability, or reusability.

Q: How to write a decorator that preserves metadata?

A: Use `functools.wraps` inside the decorator to copy `__name__`, `__doc__`, and other metadata from the original function.

Example:
```python
from functools import wraps

def deco(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper
```

Q: Generators memory benefits and use-cases.

A: Generators yield items lazily (one at a time) so they don't store the full sequence in memory. Use them for streaming logs, large file processing, or pipelines.

Q: Explain closures and lifetime of closed-over variables.

A: A closure is a function object that captures variables from its defining scope. The closed-over variables live as long as the closure exists (they're stored in the function object's `__closure__`). This allows stateful functions without global variables.

Example:
```python
def make_counter():
    count=0
    def inc():
        nonlocal count
        count+=1
        return count
    return inc

c=make_counter()
print(c(), c())  # 1 2
```

Q: When recursion is appropriate vs iterative?

A: Recursion is good for naturally recursive problems (tree traversals, divide-and-conquer). Iteration is usually more memory-efficient in Python because recursion depth is limited and function call overhead can be higher.

Q: async — when to use and basics?

A: Use `async/await` for IO-bound concurrency (network calls, disk IO) where many tasks wait. Not ideal for CPU-bound tasks unless combined with executors.

---

## Part 4 — OOP in Python

Q: Difference between class and instance attributes.

A: Class attributes are shared across all instances; instance attributes are unique per instance. Use class attributes for constants or defaults.

Example:
```python
class A:
    shared = []  # class attribute
    def __init__(self):
        self.ind = []  # instance attribute
```

Q: Explain MRO and the `super()` call.

A: MRO (method resolution order) determines the order Python searches base classes for a method. For multiple inheritance, Python uses C3 linearization. `super()` returns a proxy to call the next method in MRO, enabling cooperative multiple inheritance.

Example:
```python
class A: pass
class B(A): pass
class C(B): pass
C.mro()
```

Q: Why use `@property` over direct attributes?

A: `@property` provides controlled access with getter/setter semantics while preserving attribute-like syntax, allowing validation or computed values later without changing the API.

Q: Dataclasses vs namedtuple?

A: Dataclasses (`@dataclass`) provide mutable, typed containers with auto-generated methods and better readability. `namedtuple` creates immutable tuple-like records. Dataclasses are preferred for complex records; `namedtuple` is lightweight for simple cases.

---

## Part 5 — Exceptions & File I/O

Q: Why catch specific exceptions rather than bare `except:`?

A: Catching specific exceptions prevents hiding bugs and avoids catching unexpected exceptions (like KeyboardInterrupt). It makes error handling explicit.

Q: When to create custom exceptions?

A: Create custom exceptions to provide clearer semantics for your API, to distinguish error types, and to allow callers to catch specific failure modes.

Q: Why use `with` for file operations?

A: `with` ensures deterministic resource cleanup (file close) even on exceptions. It uses context managers to manage enter/exit logic.

Example:
```python
with open('file.txt') as f:
    data=f.read()
```

Q: Why prefer `pathlib` to `os.path`?

A: `pathlib` offers an OO API with clearer methods (`Path.read_text()`, `Path.exists()`), better cross-platform handling, and convenient path operations.

---

## Part 6 — Modules, Packages & Imports

Q: Explain relative imports and why they can fail when running directly.

A: Relative imports (`from .module import X`) rely on the package context (the module being part of a package). When running a module directly (`python pkg/module.py`), Python doesn't set the package context, causing relative imports to fail. Run the package via `python -m pkg.module` or use absolute imports.

Q: What is `__init__.py` for?

A: Historically it marked a directory as a package and can also execute package initialization code and expose the package API. With namespace packages, `__init__.py` may be optional, but it's still commonly used.

Q: Quick overview of `pyproject.toml` and packaging.

A: `pyproject.toml` specifies build-system requirements and metadata. Tools like Poetry, setuptools, and Flit read it to build packages. Use `pip install .` or `python -m build` in projects following PEP 517/518.

---

## Part 7 — DevOps Python Applications

Q: Sync vs async HTTP clients; when to use each?

A: Use synchronous clients (`requests`) for simple scripts or when concurrency isn't needed. Use async clients (`httpx` async mode, aiohttp) when you need to make many concurrent network calls; they reduce latency by overlapping IO.

Q: How to handle AWS credentials securely?

A: Use IAM roles for EC2/ECS/lambda; prefer instance/profile credentials over embedding secrets. Use environment variables or AWS profiles for local dev, store secrets in Secrets Manager or a vault, and avoid hard-coding credentials.

Q: How to capture stdout/stderr and handle errors with `subprocess`?

A: Use `subprocess.run([...], capture_output=True, text=True, check=True)` to capture and raise on non-zero exit. Inspect `CompletedProcess.stdout` and `.stderr`.

Example:
```python
import subprocess
res = subprocess.run(['ls','-la'], capture_output=True, text=True)
print(res.stdout)
```

Q: Strategies for scaling log parsing?

A: Use streaming (line-by-line generators), external tools (Fluentd, Logstash), or distributed processing (Spark). For Python, use generators, process logs in chunks, or use `mmap` for large files.

Q: IaC templating best practice?

A: Prefer declarative tools (Terraform) for infra. For templating, use Jinja2 templates with strict input validation and avoid ad-hoc string concatenation. Keep templates in source control and parameterize secrets via environment/secret stores.

---

## Closing: How to use these answers in interviews (STAR)

- Situation: Briefly set the context (project, constraints). Example: "We needed to automate daily infra reports across 50 servers." 
- Task: Say what you were asked to accomplish. Example: "I needed to collect metrics reliably and produce a summary." 
- Action: Describe the concrete steps and Python keywords/techniques used (e.g., "I used generators to stream logs, `asyncio` to parallelize API calls, and `boto3` to upload results."). Mention trade-offs and why you chose the approach. 
- Result: Quantify the outcome: "Reduced runtime from 2 hours to 20 minutes; zero failures in 30 days." 

When answering interview questions, reference a keyword (e.g., `with`, `try/except`, `async/await`) and tie it to the impact on reliability, performance, or maintainability.

---

If you'd like, I can:
- Expand each Q/A into longer explanations with multiple code examples and pitfalls.
- Create a printable PDF or split this into per-part Q/A files.
- Generate small unit tests for code examples to verify behavior.

Which would you like next?