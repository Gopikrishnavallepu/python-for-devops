# Part 3 — Functions & Advanced Concepts

Covers functions, argument passing, *args/**kwargs, lambdas, decorators, generators, closures, recursion, and async (deep lesson in separate notebook earlier).

---

## 1. Functions (def) & return
What: Named reusable code blocks.
Example:
```python
def add(a,b):
    return a+b
```
Interview Qs:
- Differences between positional, keyword-only, and default args.

---

## 2. *args and **kwargs
What: Capture variable arguments.
Example:
```python
def f(*args, **kwargs):
    print(args, kwargs)
```
Interview Qs:
- When to use *args vs list argument? Pros/cons.

---

## 3. Lambda expressions
What: Small anonymous functions.
Example:
```python
sorted(hosts, key=lambda h: int(h.split('-')[-1]))
```
Interview Qs:
- When to prefer lambda vs def.

---

## 4. Decorators
What: Wrap functions to add behaviour.
Example:
```python
def timer(fn):
    def wrapper(*a, **k):
        import time
        s=time.perf_counter()
        res=fn(*a,**k)
        print('time',time.perf_counter()-s)
        return res
    return wrapper
```
Interview Qs:
- How to write a decorator that preserves metadata? (functools.wraps)

---

## 5. Generators & yield
What: Produce values lazily with `yield`.
Example:
```python
def chunks(it, n):
    for i in range(0, len(it), n):
        yield it[i:i+n]
```
Interview Qs:
- Memory benefits and use-cases in ETL/log processing.

---

## 6. Closures
What: Functions capturing outer scope variables.
Example:
```python
def make_inc(step):
    def inc(x):
        return x+step
    return inc
```
Interview Qs:
- Explain lifetimes of closed-over variables.

---

## 7. Recursion
What: Function calling itself. Example: factorial.
Interview Qs:
- When recursion is appropriate vs iterative.

---

## 8. Async Intro
- You created `Day-03/async_await_lesson.ipynb` earlier for a deep dive.

---

## Practice
- Implement a decorator that caches function results (memoize) and test it.