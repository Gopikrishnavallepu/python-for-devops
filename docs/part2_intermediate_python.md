# Part 2 — Intermediate Python: Collections & Control Flow

This part explains tuples, lists, sets, dictionaries, control flow (if/elif/else), loops (for/while), comprehensions and common patterns.

---

## 1. Lists
What: Ordered, mutable collection.
Why: Store sequences where order and modification matter.
How:
```python
arr = [1, 2, 3]
arr.append(4)
print(arr[0])  # 1
```
Interview Qs:
- When to use list vs tuple?
- Complexity of `list.insert(0, x)`.

---

## 2. Tuples
What: Ordered, immutable collection.
Why: Lightweight fixed data (e.g., coordinate pair).
How:
```python
pt = (10, 20)
x, y = pt
```
Interview Qs:
- Why use tuples for dict keys?

---

## 3. Sets
What: Unordered unique collection.
Why: Fast membership tests, remove duplicates.
How:
```python
s = {1,2,3}
s.add(4)
```
Interview Qs:
- Difference between set and frozenset.

---

## 4. Dictionaries
What: Key->value mapping (hash table).
Why: Lookup by key.
How:
```python
conf = {'host':'web-01','port':80}
print(conf.get('host'))
```
Interview Qs:
- How hashing affects dict performance.

---

## 5. Control Flow: if / elif / else
Example:
```python
if x>10:
    print('big')
elif x>5:
    print('mid')
else:
    print('small')
```
Interview Qs:
- Short-circuit evaluation explanation.

---

## 6. Loops: for / while
Example for:
```python
for i in range(5):
    print(i)
```
Example while:
```python
i=0
while i<5:
    i+=1
```
Interview Qs:
- When to prefer while over for?

---

## 7. Comprehensions
What: concise constructs to create lists/sets/dicts
Example:
```python
squares = [x*x for x in range(5)]
```
Interview Qs:
- Memory implication vs generator expressions.

---

## 8. Iterators & Generators (intro)
- `iter()` and `next()` and `yield` (full lesson in Part 3)

---

## Practice
- Convert a list of config lines into dicts using comprehension.
- Implement unique host extractor using set comprehension.