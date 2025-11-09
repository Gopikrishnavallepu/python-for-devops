# Python Keywords — detailed examples and hands-on exercises

This file expands the short `keywords.md` list into practical, runnable examples and notes to help you deeply understand each keyword and how it's used in real-world scripts (DevOps-oriented examples included).

Run the code snippets with Python 3.8+ (copy into a .py file or run in an interactive REPL). Each section has: brief description → example → common pitfalls / real-world usage.

---

## Logical operators: `and`, `or`, `not`

- `and` returns True if both operands are truthy. `or` returns the first truthy operand or the last one. `not` negates.

Example:
```python
a = True
b = False
print(a and b)   # False
print(a or b)    # True
print(not a)     # False

# Short-circuit example: avoid expensive call when left expression suffices
def expensive():
    print('expensive called')
    return True

print(False and expensive())  # expensive not called
print(True or expensive())    # expensive not called
```

Real-world tip: use `or` to provide defaults: `port = env_port or 8080`.

Pitfall: `or`/`and` return the operand value, not strictly booleans — careful when relying on returned value type.

---

## `if`, `elif`, `else`

Conditional branching.

Example:
```python
load = 0.72
if load > 0.9:
    action = 'scale_up'
elif load < 0.2:
    action = 'scale_down'
else:
    action = 'noop'
print(action)
```

Real-world: use `if` blocks to decide deployment strategies or alert levels.

---

## `while`

Loop until condition becomes False.

Example:
```python
retries = 0
while retries < 3:
    success = False
    # try some network call (mocked)
    print('attempt', retries + 1)
    # if success: break
    retries += 1
```

Pitfall: ensure termination (avoid infinite loops). Use timeouts or maximum retries.

---

## `for`, `in`

`for` iterates over any iterable; `in` used for membership and iteration.

Example:
```python
pods = ['web-01', 'web-02', 'worker-01']
for p in pods:
    print('checking', p)

# membership
print('web-02' in pods)  # True
```

Real-world: iterate logs, hosts, or manifest items.

---

## `try`, `except`, `finally`

Exception handling: `try` protects code, `except` catches, `finally` always runs.

Example:
```python
try:
    x = int('not-a-number')
except ValueError as e:
    print('caught', e)
finally:
    print('cleanup if needed')
```

Real-world: wrap network calls and always close resources in `finally` or use `with` (context managers).

---

## `def`, `return`

Define functions and return values.

Example:
```python
def check_service(name):
    # simulate check
    if name == 'nginx':
        return True
    return False

if check_service('nginx'):
    print('service ok')
```

Tip: keep functions small and pure for easier testing.

---

## `class`

Define classes / object oriented structures.

Example:
```python
class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def __repr__(self):
        return f"Server({self.name},{self.ip})"

s = Server('web-01','10.0.0.5')
print(s)
```

Real-world: model resources (Server, Cluster, Deployment) with methods for actions.

---

## `import`, `from`, `as`

Importing modules and aliases.

Example:
```python
import os
from urllib.parse import urlparse as up

print(os.getenv('HOME'))
p = up('https://example.com')
```

Tip: use aliases for long modules (e.g., `import numpy as np`) and to avoid name collisions.

---

## `True`, `False`, `None`

Boolean and null-like values.

Example:
```python
is_ready = True
result = None
if is_ready:
    result = 'ok'
print(result)
```

Pitfall: `None` is singleton — compare with `is` not `==` when identity matters.

---

## `is`

Identity comparison.

Example:
```python
a = None
print(a is None)   # True

x = [1,2]
y = x
z = [1,2]
print(x is y)  # True
print(x is z)  # False (same contents, different objects)
```

Tip: use `is` for `None` checks or when you require identity.

---

## `lambda`

Anonymous inline functions.

Example:
```python
add = lambda a, b: a + b
print(add(2,3))  # 5

# use in sorting
hosts = ['web-10','web-2','web-1']
hosts_sorted = sorted(hosts, key=lambda h: int(h.split('-')[-1]))
print(hosts_sorted)
```

Pitfall: lambdas should be simple; prefer `def` for complex logic.

---

## `with`

Context manager for resource safety.

Example:
```python
with open('deploy.log', encoding='utf-8') as fh:
    for line in fh:
        if 'ERROR' in line:
            print('found error')
```

Real-world: `with` for files, subprocess.Popen (via contextlib), locks, DB connections.

---

## `global`, `nonlocal`

Change variable scoping behavior.

Example (`global`):
```python
counter = 0
def inc():
    global counter
    counter += 1

inc(); inc()
print(counter)  # 2
```

Example (`nonlocal`):
```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

f = outer()
print(f())  # 1
print(f())  # 2
```

Pitfall: prefer passing parameters or returning values to avoid wide-use of `global`.

---

## `return` (already covered above with `def`)

Note: a bare `return` returns `None`.

```python
def f():
    if False:
        return
    # implicit return None

print(f() is None)
```

---

## `is` vs `==`

`==` compares values; `is` compares identity. See `is` examples above.

Example:
```python
a = 1000
b = 1000
print(a == b)  # True
print(a is b)  # Implementation detail: often False for large ints
```

Avoid `is` for numeric or string equality checks.

---

## `with` (covered) — prefer for deterministic cleanup.

---

## `try/except` variations

Catch specific exceptions and use `else` (runs if no exception) and `finally`.

Example:
```python
try:
    x = 1 / 1
except ZeroDivisionError:
    print('bad')
else:
    print('no error')
finally:
    print('always')
```

---

## Other language keywords with examples

Below are the remaining keywords from your list with short, practical examples.

### `return` (already shown) — returns value from function.

### `break` / `continue` (control loop flow)
```python
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)  # prints odd numbers
```

### `pass` (do-nothing placeholder)
```python
def placeholder():
    pass
```

### `yield` (generators)
```python
def lines():
    with open('deploy.log') as fh:
        for ln in fh:
            yield ln.strip()

for ln in lines():
    print(ln)
```

### `assert` (basic checks)
```python
def ensure_positive(x):
    assert x > 0, 'x must be positive'

ensure_positive(10)
```

### `del` (delete a name or slice)
```python
data = [1,2,3]
del data[0]
print(data)  # [2,3]
```

### `raise` (raise exceptions)
```python
def check_age(age):
    if age < 0:
        raise ValueError('invalid age')
```

### `yield from` (delegate generator)
```python
def inner():
    yield from range(3)
print(list(inner()))
```

### `async`, `await` (async IO) — short example
```python
import asyncio

async def hello():
    await asyncio.sleep(0.1)
    return 'done'

print(asyncio.run(hello()))
```

---

## Practical exercises (try these)
1. Write a function that masks secrets in a config line: `API_KEY=abcd1234;DB_PASS=secret` → `API_KEY=****;DB_PASS=****`.
2. Use `with` to safely write a timestamp into a log file and then `tail` the last 5 lines.
3. Implement a retry loop with exponential backoff using `while`, `try/except`, and `break`.

---

## Final tips
- Prefer `with` for resource management.
- Catch specific exceptions, not bare `except:`.
- Avoid global state; prefer returning values or classes that maintain state.
- Use `is None` to test for `None`.

If you'd like, I can expand any of these sections into a standalone lesson with more exercises and test cases. Tell me which keywords you want deeper coverage of (for example: `async/await`, `generators/yield`, or `context managers`).
