# Part 4 — OOP in Python

Covers classes, instances, inheritance, encapsulation, polymorphism, abstract base classes, dataclasses and common patterns used in production code.

---

## 1. Classes & Instances
What: Blueprints (classes) produce objects (instances).
Example:
```python
class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
    def ping(self):
        return True
```
Interview Qs:
- Difference between class and instance attributes.

---

## 2. Inheritance & MRO
What: Subclass extends parent functionality. MRO defines resolution order.
Example:
```python
class WebServer(Server):
    def serve(self):
        pass
```
Interview Qs:
- Explain MRO and the `super()` call.

---

## 3. Encapsulation & Properties
What: Protect internal state and expose via methods or `@property`.
Example:
```python
class C:
    @property
    def value(self):
        return self._value
```
Interview Qs:
- Why use properties vs direct attribute access?

---

## 4. Dataclasses
What: Simple data containers available via `@dataclass`.
Example:
```python
from dataclasses import dataclass
@dataclass
class Config:
    host: str
    port: int
```
Interview Qs:
- Benefits of dataclasses vs namedtuple.

---

## 5. Abstract Base Classes
What: Define interfaces with `abc.ABC`.
Interview Qs:
- When to use ABC vs duck typing?

---

## Practice
- Model a `Deployment` object with methods that update a `replicas` property and implement validation.