# Part 3 — Functions & Advanced: Model Answers and Code Solutions

This document provides model answers, explanations, and runnable code for the interview questions listed in Part 3 (Functions & Advanced). Copy code blocks into .py files or run them in a REPL.

---

## 1. Function signatures & arguments

Q: Explain positional, keyword, default, and keyword-only arguments. Give examples and use-cases.

A: 
- Positional arguments are specified by order: `f(a, b)`.
- Keyword arguments are provided by name: `f(a=1, b=2)`.
- Default arguments provide a fallback: `def f(a, b=2)`.
- Keyword-only arguments (after `*`) must be provided by name: `def f(a, *, verbose=False)`.

Example:
```python
def deploy(image, replicas=1, *, dry_run=False):
    """Deploy an image. replicas is positional-or-keyword, dry_run is keyword-only."""
    if dry_run:
        print(f"[DRY RUN] Would deploy {image} x{replicas}")
    else:
        print(f"Deploying {image} x{replicas}")

# calls
deploy('app:1.0')
deploy('app:1.0', replicas=3, dry_run=True)
```

Interview tip: Use keyword-only args to make optional flags explicit and avoid positional mistakes.

---

## 2. `*args` and `**kwargs`

Q: What do `*args` and `**kwargs` do? Demonstrate argument unpacking when calling functions.

A: `*args` captures extra positional arguments as a tuple; `**kwargs` captures extra keyword arguments as a dict. Use unpacking to forward arguments: `f(*args, **kwargs)`.

Example:
```python
def log(msg, *tags, **meta):
    print(msg)
    print('tags:', tags)
    print('meta:', meta)

log('Hello', 'urgent', 'infra', user='ops', env='prod')

# forwarding example
def wrapper(*a, **k):
    return log(*a, **k)

wrapper('Hi', 'x', foo='bar')
```

Interview tip: `*`/`**` let you build flexible APIs and decorators that don't tightly couple to a specific signature.

---

## 3. Lambdas & higher-order functions

Q: When are lambdas useful? Give a sorting example using `key=`.

A: Lambdas are handy for short throwaway functions used inline, like sorting keys or simple transformations.

Example:
```python
hosts = ['web-10', 'web-2', 'web-1']
hosts_sorted = sorted(hosts, key=lambda h: int(h.split('-')[-1]))
print(hosts_sorted)  # ['web-1', 'web-2', 'web-10']
```

Interview tip: For complex logic, prefer named functions for readability and testing.

---

## 4. Decorators

Q: Explain decorator syntax and implement a simple `@timer` decorator that measures runtime.

A: Decorators are callables that take a function and return a new function (usually a wrapper). Use `@decorator` syntax to apply.

Example `timer` decorator with `functools.wraps`:
```python
import time
from functools import wraps

def timer(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        t0 = time.perf_counter()
        res = fn(*a, **k)
        t1 = time.perf_counter()
        print(f"{fn.__name__} took {t1-t0:.4f}s")
        return res
    return wrapper

@timer
def busy(n):
    s = 0
    for i in range(n):
        s += i
    return s

if __name__ == '__main__':
    print(busy(100000))
```

Follow-ups & interview tip:
- Show how missing `wraps` hides metadata (name/docstring) and how `wraps` preserves it.
- Discuss thread-safety and side effects in decorators.

---

## 5. Parameterized decorator (`@retry`)

Q: Implement a parameterized decorator `@retry(times=3)`. Discuss testability and edge cases.

Solution (sync, simple):
```python
import time
from functools import wraps

def retry(times=3, delay=0.1, exceptions=(Exception,)):
    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **k):
            last_exc = None
            for attempt in range(1, times+1):
                try:
                    return fn(*a, **k)
                except exceptions as e:
                    last_exc = e
                    if attempt == times:
                        break
                    time.sleep(delay * (2 ** (attempt-1)))
            raise last_exc
        return wrapper
    return deco

# Example usage
counter = {'calls': 0}

@retry(times=4, delay=0.01, exceptions=(RuntimeError,))
def flaky():
    counter['calls'] += 1
    if counter['calls'] < 3:
        raise RuntimeError('transient')
    return 'ok'

if __name__ == '__main__':
    print(flaky())  # 'ok' after retries
```

Testability: Inject a deterministic clock/sleep mock or monkeypatch `time.sleep`, and factor the retry logic into a helper for unit tests.

Edge cases:
- Must not swallow `KeyboardInterrupt` or `SystemExit` unless explicit.
- Should allow backoff strategy and jitter for distributed reliability.

---

## 6. Generators & `yield`

Q: Write a generator to tail a growing log file (like `tail -f`) and explain resource handling.

Solution:
```python
import time

def follow(path):
    with open(path, 'r', encoding='utf-8') as fh:
        # go to end
        fh.seek(0, 2)
        while True:
            line = fh.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line.rstrip('\n')

# Example usage (outside test):
# for ln in follow('/var/log/app.log'):
#     process(ln)
```

Resource handling: Using `with` ensures the file is closed when generator exits if we use `contextlib.closing` or ensure iteration stops. For long-running tails, the generator typically lives as long as the process; consider log rotation handling.

Follow-up: show handling when file is rotated (re-opening when inode changes).

---

## 7. `yield from` and delegating generators

Q: Explain `yield from`.

A: `yield from` delegates part of a generator's operations to a subgenerator, forwarding values, exceptions, and `return` value (PEP 380). Use it to compose generators.

Example:
```python
def subgen():
    yield from range(3)

def main_gen():
    yield 'start'
    yield from subgen()
    yield 'end'

print(list(main_gen()))  # ['start', 0, 1, 2, 'end']
```

Interview tip: `yield from` simplifies writing generators that incorporate other generators and handles exception propagation.

---

## 8. Closures & `nonlocal`

Q: Explain `nonlocal` with a closure example that keeps state.

Solution:
```python
def make_counter(initial=0):
    count = initial
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

if __name__ == '__main__':
    c = make_counter()
    print(c(), c(), c())  # 1 2 3
```

Pitfalls: Late binding in closures inside loops — common bug when creating lambdas in loop. Fix with default args: `lambda x, i=i: i`.

---

## 9. Recursion

Q: When is recursion practical in Python? Show an example and discuss limits.

A: Recursion is good for tree/graph traversals, parsing, divide-and-conquer where depth is manageable. Python has recursion depth limits (default ~1000); large depth causes `RecursionError`. Use iterative solutions or increase recursion limit carefully.

Example (tree traversal):
```python
def sum_tree(node):
    if node is None:
        return 0
    return node.value + sum(sum_tree(ch) for ch in node.children)
```

Interview tip: Mention memoization for exponential recursion (Fibonacci) and iterative conversion.

---

## 10. Async (deep)

Q: Explain `async`/`await` basics and how to run blocking code.

A: `async def` defines a coroutine; `await` suspends until awaited coroutine completes. The event loop schedules coroutines; `asyncio.create_task` runs a coroutine concurrently.

Example showing concurrency and `run_in_executor`:
```python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

async def io_bound(n):
    await asyncio.sleep(n)
    return n

async def main():
    t0 = time.perf_counter()
    tasks = [asyncio.create_task(io_bound(0.5)), asyncio.create_task(io_bound(0.2))]
    res = await asyncio.gather(*tasks)
    print('res', res, 'time', time.perf_counter()-t0)

# Blocking work in executor
def blocking(x):
    time.sleep(x)
    return x

async def run_blocking(loop):
    with ThreadPoolExecutor() as pool:
        res = await loop.run_in_executor(pool, blocking, 0.5)
        print('blocking returned', res)

if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(run_blocking(asyncio.get_event_loop()))
```

Cancellation & timeouts: use `asyncio.wait_for` and handle `asyncio.CancelledError` in cleanup.

---

## 11. Advanced prompt: Async & Sync retry decorator (combined)

Q: Implement a `retry` decorator that works for both sync and async functions (detect coroutine vs normal function) and supports exponential backoff.

Solution (supports sync and async):
```python
import asyncio
import time
import inspect
from functools import wraps

def retry_any(times=3, base_delay=0.1, exceptions=(Exception,)):
    def deco(fn):
        if inspect.iscoroutinefunction(fn):
            @wraps(fn)
            async def awrapper(*a, **k):
                last_exc = None
                for attempt in range(1, times+1):
                    try:
                        return await fn(*a, **k)
                    except exceptions as e:
                        last_exc = e
                        if attempt == times:
                            break
                        await asyncio.sleep(base_delay * (2 ** (attempt-1)))
                raise last_exc
            return awrapper
        else:
            @wraps(fn)
            def wrapper(*a, **k):
                last_exc = None
                for attempt in range(1, times+1):
                    try:
                        return fn(*a, **k)
                    except exceptions as e:
                        last_exc = e
                        if attempt == times:
                            break
                        time.sleep(base_delay * (2 ** (attempt-1)))
                raise last_exc
            return wrapper
    return deco

# Usage examples
@retry_any(times=4)
def flaky_sync():
    print('sync try')
    raise RuntimeError('fail')

@retry_any(times=4)
async def flaky_async():
    print('async try')
    raise RuntimeError('fail')

# For testing, wrap in try/except to show behavior.
```

Testing notes: Use `pytest.mark.asyncio` to test async variant and monkeypatch `time.sleep`/`asyncio.sleep` for deterministic timing.

---

## 12. Advanced prompt: Thread-safe memoization decorator

Q: Design a caching decorator that is thread-safe and optionally persistent on disk.

Solution (in-memory, thread-safe with lock):
```python
import threading
from functools import wraps

def memoize(thread_safe=True, maxsize=None):
    cache = {}
    lock = threading.RLock()
    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **k):
            key = (a, tuple(sorted(k.items())))
            if thread_safe:
                with lock:
                    if key in cache:
                        return cache[key]
            else:
                if key in cache:
                    return cache[key]
            res = fn(*a, **k)
            with lock:
                cache[key] = res
                # optional eviction if maxsize reached
                if maxsize and len(cache) > maxsize:
                    cache.pop(next(iter(cache)))
            return res
        return wrapper
    return deco

# Example usage
@memoize()
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(30))
```

Persistence note: To persist cache to disk, serialize `cache` with `shelve`, `pickle` or a lightweight DB; ensure you handle invalidation and serialization of arguments.

---

## 13. Practice & Tests

For each code snippet above, create minimal tests using `pytest` examples. Example test for `timer` and `retry` decorators should assert behavior rather than exact timing — for example, that the wrapped function returns expected values and that retries occur (monkeypatch sleep to speed tests).

Example pytest for retry (sync):
```python
import pytest
from docs.part3_solutions import retry_any

class Flaky:
    def __init__(self, fail):
        self.count = 0
        self.fail = fail
    def __call__(self):
        self.count += 1
        if self.count <= self.fail:
            raise RuntimeError('fail')
        return 'ok'

@retry_any(times=3)
def call_flaky(obj):
    return obj()

def test_retry_sync():
    f = Flaky(fail=2)
    assert call_flaky(f) == 'ok'
```

---

## Closing notes
- These solutions are intentionally pragmatic and include testing suggestions.
- If you'd like, I can:
  - generate a `tests/` folder with unit tests for each snippet,
  - convert these examples into runnable scripts and a combined `lesson_runner.py`, or
  - expand into Part 7 solutions next (DevOps apps).

Tell me which of these you'd like me to do next.
