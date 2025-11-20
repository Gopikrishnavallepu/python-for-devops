# Understanding `if __name__ == "__main__":` and Main Construct Pattern

This lesson explains the file `02-main-construct.py` line by line, then dives deep into **why** and **how** the `if __name__ == "__main__":` pattern works, with real-world examples.

---

## Part 1: Line-by-line explanation of `02-main-construct.py`

### Full code:
```python
def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    print(folder_paths)

    # Print elements in the list
    for folder_path in folder_paths:
       print(folder_path)

if __name__ == "__main__":
    main()
```

---

### Line 1: `def main():`
- **Keyword**: `def` — defines a function.
- **Function name**: `main` — convention for the entry point of a script.
- **Parentheses**: `()` — indicates this function takes no arguments.
- **Colon**: `:` — marks the start of the function body (all indented lines below belong to this function).

**Purpose**: Define a function that will be the primary logic of the script. By wrapping the logic in a function, it becomes:
- Reusable (can call `main()` from other scripts)
- Testable (easier to test functions than loose script code)
- Organized and readable

---

### Line 2: `folder_paths = input("Enter a list of folder paths separated by spaces: ").split()`

**Breaking it down**:

1. **`input(...)`** 
   - Built-in function that displays a prompt and waits for user input.
   - Prompt text: `"Enter a list of folder paths separated by spaces: "`
   - Returns the user's input as a **string** (everything the user types is treated as text).
   - Example: if user types `home documents desktop`, `input()` returns `"home documents desktop"`.

2. **`.split()`**
   - String method that splits a string into a list.
   - By default, `.split()` splits on whitespace (spaces, tabs, newlines) and removes empty strings.
   - Example: `"home documents desktop".split()` returns `['home', 'documents', 'desktop']`.

3. **`folder_paths =`**
   - Assigns the result (a list of strings) to the variable `folder_paths`.

**Example output**:
```python
# User input: home documents downloads
# Result: folder_paths = ['home', 'documents', 'downloads']
```

---

### Line 3: `print(folder_paths)`

- **`print()`** is a built-in function that outputs text to the console.
- **`folder_paths`** is the variable to print (a list).
- This prints the entire list as a single line.

**Example output**:
```
['home', 'documents', 'downloads']
```

---

### Line 5: `# Print elements in the list`

- **`#`** marks a comment.
- Comments are ignored by Python and are only for human readers.
- This comment explains what the next code block does.

---

### Lines 6–7: `for` loop
```python
for folder_path in folder_paths:
   print(folder_path)
```

**Breaking it down**:

1. **`for`** — keyword that starts a loop.
2. **`folder_path`** — a variable that will hold each item in the loop one at a time.
3. **`in folder_paths`** — iterate over the list `folder_paths`.
4. **`:`** — marks the start of the loop body (indented code below).
5. **`print(folder_path)`** — inside the loop, print each item.

**Execution**:
- Iteration 1: `folder_path = 'home'` → print `home`
- Iteration 2: `folder_path = 'documents'` → print `documents`
- Iteration 3: `folder_path = 'downloads'` → print `downloads`

**Example output**:
```
home
documents
downloads
```

---

### Line 9: `if __name__ == "__main__":`

This is the **critical line** that deserves deep explanation. See Part 2 below.

---

### Line 10: `main()`

- Inside the `if` block (indented).
- Calls the `main()` function we defined on line 1.
- This executes all the code in the `main()` function.

---

## Part 2: Deep dive into `if __name__ == "__main__":`

### What is `__name__`?

**`__name__` is a special variable** automatically set by Python for every module (file).

- **`__name__`** stores the module's name.
- When a file is run directly (not imported), `__name__` is set to the string `"__main__"`.
- When a file is imported into another file, `__name__` is set to the module name.

### Example 1: Running a script directly

**File: `my_script.py`**
```python
print(f"__name__ = {__name__}")
```

**Run it directly**:
```bash
python my_script.py
```

**Output**:
```
__name__ = __main__
```

When you run the script directly, Python sets `__name__` to `"__main__"`.

---

### Example 2: Importing the script

**File: `my_script.py`**
```python
print(f"__name__ = {__name__}")
```

**File: `another_script.py`**
```python
import my_script
```

**Run `another_script.py`**:
```bash
python another_script.py
```

**Output**:
```
__name__ = my_script
```

When imported, `__name__` is set to the module name (`"my_script"`), not `"__main__"`.

---

### Why use `if __name__ == "__main__":`?

This pattern solves a common problem:

**Problem**: If your script has code at the top level (not in a function), that code runs **whenever the file is imported**. This is often unwanted.

**Solution**: Wrap the entry point in `if __name__ == "__main__":`. This ensures that code only runs when the file is executed directly, not when imported.

---

### Example 3: Without the guard (bad practice)

**File: `utils.py`**
```python
def add(a, b):
    return a + b

# This runs every time someone imports utils
result = add(2, 3)
print(f"Result: {result}")
```

**File: `main.py`**
```python
from utils import add

print(add(5, 10))
```

**Run `python main.py`**:
```
Result: 5        # From utils.py being imported!
15               # From main.py's print
```

**Problem**: When `main.py` imports `utils.py`, the print statement inside `utils.py` runs automatically. This pollutes the output and wastes resources.

---

### Example 4: With the guard (best practice)

**File: `utils.py`**
```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    # This only runs if utils.py is executed directly
    result = add(2, 3)
    print(f"Result: {result}")
```

**File: `main.py`**
```python
from utils import add

print(add(5, 10))
```

**Run `python main.py`**:
```
15               # Only main.py's output
```

**Run `python utils.py`**:
```
Result: 5        # Only when utils.py is run directly
```

**Benefit**: The test/demo code in `utils.py` only runs when you execute it directly, not when it's imported.

---

## Part 3: Real-world DevOps examples

### Example: Configuration loader script

**File: `config_loader.py`**
```python
import json

def load_config(filename):
    """Load JSON config and return as dict."""
    with open(filename) as f:
        return json.load(f)

def validate_config(config):
    """Check if config has required fields."""
    required_fields = ['host', 'port', 'timeout']
    return all(field in config for field in required_fields)

if __name__ == "__main__":
    # Demo: test the functions when run directly
    import sys
    if len(sys.argv) < 2:
        print("Usage: python config_loader.py <config_file>")
        sys.exit(1)
    
    config = load_config(sys.argv[1])
    if validate_config(config):
        print("Config is valid!")
        print(f"Host: {config['host']}, Port: {config['port']}")
    else:
        print("Config is invalid!")
```

**Use cases**:

1. **Import and use the functions**:
   ```python
   from config_loader import load_config, validate_config
   
   cfg = load_config('app.json')
   # No demo output printed because __name__ != "__main__"
   ```

2. **Run the script directly to test**:
   ```bash
   python config_loader.py app.json
   # Output: Config is valid! Host: localhost, Port: 8080
   ```

---

### Example: Kubernetes pod lister

**File: `k8s_lister.py`**
```python
from kubernetes import client, config

def get_pods(namespace="default"):
    """List pods in a Kubernetes namespace."""
    config.load_incluster_config()  # or load_kube_config() for local testing
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)
    return [pod.metadata.name for pod in pods.items]

if __name__ == "__main__":
    # Demo: list pods when script is run directly
    pods = get_pods("kube-system")
    for pod in pods:
        print(f"Pod: {pod}")
```

**Use cases**:

1. **Test the script**:
   ```bash
   python k8s_lister.py
   # Lists Kubernetes pods in kube-system namespace
   ```

2. **Import and use in another script**:
   ```python
   from k8s_lister import get_pods
   
   production_pods = get_pods("production")
   # No demo output printed
   ```

---

## Part 4: Common patterns and variations

### Pattern 1: Simple entry point
```python
def main():
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

---

### Pattern 2: With command-line arguments
```python
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <arg1> <arg2>")
        return
    
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # Process args

if __name__ == "__main__":
    main()
```

---

### Pattern 3: With argument parsing (professional)
```python
import argparse

def main(args):
    print(f"Processing {args.input_file} with mode {args.mode}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("--mode", default="fast", help="Processing mode")
    args = parser.parse_args()
    main(args)
```

---

### Pattern 4: With error handling
```python
import sys

def main():
    try:
        # Your code here
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    print("Success!")

if __name__ == "__main__":
    main()
```

---

## Part 5: Summary checklist

| Concept | Explanation |
|---------|-------------|
| `def main():` | Defines the entry point function; allows reuse and testing. |
| `input()` | Gets user input as a string. |
| `.split()` | Splits a string into a list of words. |
| `print()` | Outputs text. |
| `for ... in ...` | Iterates over a list or sequence. |
| `__name__` | Special variable; `"__main__"` when file is run directly. |
| `if __name__ == "__main__":` | Guard that prevents code from running on import; only runs when executed directly. |

---

## Part 6: Practice exercises

1. **Exercise 1**: Modify `02-main-construct.py` to ask for file extensions (e.g., `.txt`, `.py`) and only print paths with that extension.
   
   **Hint**: Use `.endswith()` method on strings.

2. **Exercise 2**: Create a script that defines a function to validate IP addresses. Use `if __name__ == "__main__":` to test it with a list of sample IPs.
   
   **Hint**: Use regex or simple validation like `len(parts) == 4` after splitting on `"."`.

3. **Exercise 3**: Create a DevOps utility script that:
   - Defines a function to check if a port is open on a host.
   - Uses `if __name__ == "__main__":` to accept a hostname and port as command-line arguments.
   - Prints "Port is open" or "Port is closed".
   
   **Hint**: Use `socket` module or `subprocess` to check with `telnet`/`nc`.

---

## Solutions

### Exercise 1 Solution
```python
def main():
    ext = input("Enter file extension (e.g., .txt): ")
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    matching = [p for p in folder_paths if p.endswith(ext)]
    print(matching)
    
    for path in matching:
        print(path)

if __name__ == "__main__":
    main()
```

### Exercise 2 Solution
```python
import re

def is_valid_ip(ip):
    """Check if IP is valid IPv4 format."""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, ip))

if __name__ == "__main__":
    test_ips = ['192.168.1.1', '256.1.1.1', '10.0.0.1', 'not.an.ip']
    for ip in test_ips:
        result = "valid" if is_valid_ip(ip) else "invalid"
        print(f"{ip}: {result}")
```

### Exercise 3 Solution
```python
import socket
import sys

def is_port_open(host, port):
    """Check if a port is open on a host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <host> <port>")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    if is_port_open(host, port):
        print(f"Port {port} is open on {host}")
    else:
        print(f"Port {port} is closed on {host}")
```

---

## Key Takeaways

1. **`if __name__ == "__main__":` is essential** for professional Python scripts.
2. It separates **library code** (functions) from **test/demo code**.
3. It allows your script to be both **executable** (run directly) and **importable** (used by other scripts).
4. Always wrap your main logic in a `main()` function and call it under the guard.
5. This pattern is the foundation of professional Python development.


Excellent question, Gopi 👏 — this one shows deep understanding when you answer it well in an interview.
Let’s break it down **step by step in layman terms** and **with DevOps context + real code examples**.

---

## 🧩 The Line:

```python
if __name__ == "__main__":
```

---

## 💡 Simple Meaning (Layman Explanation)

Think of a Python file as a **script** and sometimes as a **reusable module**.

* When you **run a Python file directly**, Python sets a special built-in variable called `__name__` to `"__main__"`.
* When you **import that same file into another Python file**, its `__name__` becomes the **module name** instead (not `"__main__"`).

So this line acts like a **“gatekeeper”** — it tells Python:

> “Only run this part of the code if this file is being run directly — not when imported by someone else.”

---

### 🧠 Analogy

Imagine you have a washing machine.

* Sometimes you use it directly to wash clothes (main function).
* Sometimes a technician uses the same machine internally for testing one part of it (imported as a module).

The `if __name__ == "__main__":` block ensures **the full washing cycle runs only when you press start**, not every time the technician touches a part.

---

## ⚙️ Example 1 — Basic Script

```python
# file: greetings.py

def say_hello():
    print("👋 Hello from greetings module!")

if __name__ == "__main__":
    print("Running directly...")
    say_hello()
```

### 🔹 When you run directly:

```bash
$ python greetings.py
```

Output:

```
Running directly...
👋 Hello from greetings module!
```

### 🔹 When you import it:

```python
# file: main.py
import greetings
```

Output:

```
👋 (nothing printed!)
```

Because the code inside:

```python
if __name__ == "__main__":
```

didn’t execute when imported.

---

## ⚙️ Example 2 — DevOps Real-World Context

Let’s say you wrote a Python script that **automates EC2 instance creation** using Boto3.

```python
# file: ec2_manager.py
import boto3

def create_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-0abcd1234abcd1234',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    print("✅ EC2 Instance Created:", instance[0].id)

# This ensures automation runs only when you run ec2_manager.py directly
if __name__ == "__main__":
    create_instance()
```

Now:

* If you **run `python ec2_manager.py`**, it will actually create an EC2 instance.
* But if you **import `create_instance()` into another script (say, a CI/CD pipeline tool)** — it will not create an instance automatically, unless explicitly called.

---

## ⚙️ Example 3 — For Jenkins or Automation Scripts

Suppose you have a file `deploy_app.py` that includes deployment functions.

```python
# deploy_app.py
def deploy():
    print("🚀 Deploying application...")

def rollback():
    print("🔁 Rolling back deployment...")

if __name__ == "__main__":
    deploy()
```

When Jenkins executes:

```bash
python deploy_app.py
```

👉 Deployment runs.

But when another automation file imports it like:

```python
from deploy_app import rollback
rollback()
```

👉 It only runs rollback, not deploy automatically.

This makes scripts **modular and safe for reuse** in larger DevOps automation workflows.

---

## 🧠 Why It Matters in DevOps

| Reason                 | Benefit                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| **Modular Automation** | Allows you to reuse functions across different pipelines or tools                         |
| **Safe Importing**     | Prevents scripts from executing destructive actions (like deleting servers) when imported |
| **Testing Ready**      | You can test functions independently without triggering main automation                   |
| **Readability**        | Clearly separates script’s “entry point” from logic                                       |

---

## 💬 Interview-Ready STAR Answer

**Q:** What is the purpose of `if __name__ == "__main__":` in Python scripts?

**A (STAR format):**

* **Situation:** While developing automation scripts in Python for AWS provisioning, we needed to reuse functions like creating EC2 instances and uploading files to S3 in multiple pipelines.
* **Task:** Prevent these scripts from executing automatically when imported into another Python automation module.
* **Action:** Used the `if __name__ == "__main__":` block to define a controlled entry point for each script — it runs only when the file is executed directly.
* **Result:** Our CI/CD automation became safer, more modular, and reusable — no accidental resource creation or execution during imports.

---

## ✅ Summary

| Concept                      | Meaning                                                 | In DevOps                             |
| ---------------------------- | ------------------------------------------------------- | ------------------------------------- |
| `__name__`                   | Built-in variable that tells how a file is being used   | Helps control behavior                |
| `"__main__"`                 | Value of `__name__` when script runs directly           | Entry point for automation            |
| `if __name__ == "__main__":` | Guard clause to run main code only if executed directly | Prevents unwanted runs during imports |

---

Would you like me to show how this is used in **real multi-file DevOps project structure** —
for example, separating `utils.py`, `aws_tasks.py`, and `main.py` with `if __name__ == "__main__":` controlling execution flow?
