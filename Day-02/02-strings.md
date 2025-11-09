1. String Data Type in Python:

In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
Strings are immutable, meaning you cannot change the characters within a string directly. Instead, you create new strings.
You can access individual characters in a string using indexing, e.g., my_string[0] will give you the first character.
Strings support various built-in methods, such as len(), upper(), lower(), strip(), replace(), and more, for manipulation.
2. String Manipulation and Formatting:

Concatenation: You can combine strings using the + operator.
Substrings: Use slicing to extract portions of a string, e.g., my_string[2:5] will extract characters from the 2nd to the 4th position.
String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and str.format().
Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
String methods: Python provides many built-in methods for string manipulation, such as split(), join(), and startswith().



# Python Strings: Comprehensive Guide with Examples

## 1. String Creation and Basic Operations

### String Creation
```python
# Different ways to create strings
single_quotes = 'Hello DevOps'
double_quotes = "Python Programming"
triple_quotes = '''This string can
span multiple lines'''
doc_string = """Documentation strings
are often written this way"""

# Raw strings (ignore escape characters)
raw_string = r'C:\Users\DevOps\notes.txt'
```

### String Immutability
```python
name = "Python"
# This will raise an error:
# name[0] = 'J'  # TypeError: 'str' object does not support item assignment

# Instead, create a new string
name = 'J' + name[1:]  # 'Jython'
```

### String Indexing and Slicing
```python
text = "Python DevOps"
print(text[0])      # 'P' - first character
print(text[-1])     # 's' - last character
print(text[0:6])    # 'Python' - characters from index 0 to 5
print(text[7:])     # 'DevOps' - characters from index 7 to end
print(text[:6])     # 'Python' - characters from start to index 5
print(text[::2])    # 'Pto eOs' - every second character
print(text[::-1])   # 'spOveD nohtyP' - reverse the string
```

## 2. Common String Operations and Methods

### Length and Case Operations
```python
message = "Hello DevOps World"
print(len(message))           # 17 - string length
print(message.upper())        # "HELLO DEVOPS WORLD"
print(message.lower())        # "hello devops world"
print(message.title())        # "Hello Devops World"
print(message.capitalize())   # "Hello devops world"
```

### String Testing Methods
```python
# String content testing
password = "DevOps2023!"
print(password.isalnum())     # False (contains special character !)
print(password.isalpha())     # False (contains numbers and !)
print(password.isdigit())     # False (contains letters and !)
print("2023".isdigit())      # True

# Prefix/Suffix testing
filename = "deployment.yaml"
print(filename.startswith("deploy"))  # True
print(filename.endswith(".yaml"))     # True
```

### String Searching and Replacing
```python
log_entry = "Error: Failed to connect to database at 192.168.1.100"
print(log_entry.find("Failed"))      # 7 - position of "Failed"
print(log_entry.count("to"))         # 1 - count occurrences
print(log_entry.replace("Error", "WARNING"))  # Replace text

# Split and Join
parts = log_entry.split()            # Split by whitespace
print(parts)  # ['Error:', 'Failed', 'to', 'connect', 'to', 'database', 'at', '192.168.1.100']
new_log = " ".join(parts)            # Join with space
print(new_log == log_entry)          # True
```

## 3. String Formatting Techniques

### F-strings (Python 3.6+)
```python
# DevOps Example
service = "nginx"
status = "running"
port = 80
memory = 128.45

# F-string with expressions
status_msg = f"Service {service} is {status} on port {port}"
print(status_msg)  # "Service nginx is running on port 80"

# F-string with formatting
report = f"Memory Usage: {memory:.1f}MB"
print(report)  # "Memory Usage: 128.5MB"
```

### Format Method
```python
# Template style
template = "Deploying {} version {} to {}"
msg = template.format("app", "2.0.1", "production")
print(msg)  # "Deploying app version 2.0.1 to production"

# Named placeholders
template = "Server: {server}, Status: {status}"
msg = template.format(server="web-01", status="active")
print(msg)  # "Server: web-01, Status: active"
```

### Practical DevOps Examples
```python
# Configuration string parsing
config_line = "DB_HOST=localhost;DB_PORT=5432;DB_NAME=myapp"
config_dict = dict(item.split('=') for item in config_line.split(';'))
print(config_dict)  # {'DB_HOST': 'localhost', 'DB_PORT': '5432', 'DB_NAME': 'myapp'}

# Log parsing
log_line = "2023-11-09T10:15:30 ERROR [web-01] Memory usage exceeded 90%"
timestamp, level, *msg = log_line.split()
server = msg[0].strip('[]')
alert = ' '.join(msg[1:])
print(f"Server {server} reported: {alert}")  # "Server web-01 reported: Memory usage exceeded 90%"

# URL parsing
url = "https://api.example.com/v1/users?status=active"
protocol = url.split('://')[0]
domain = url.split('://')[1].split('/')[0]
path = '/'.join(url.split('://')[1].split('/')[1:]).split('?')[0]
print(f"Protocol: {protocol}, Domain: {domain}, Path: {path}")
```

## 4. String Method Cheatsheet

```python
# Common string methods and their usage
text = "  DevOps Pipeline  "
print(text.strip())          # "DevOps Pipeline" - remove whitespace
print(text.lstrip())         # "DevOps Pipeline  " - remove left whitespace
print(text.rstrip())         # "  DevOps Pipeline" - remove right whitespace

text = "python,java,golang,rust"
print(text.split(','))       # ['python', 'java', 'golang', 'rust']

text = "DevOps"
print(text.center(10, '*'))  # "**DevOps**"
print(text.ljust(10, '-'))   # "DevOps----"
print(text.rjust(10, '-'))   # "----DevOps"

# String validation
print("abc123".isalnum())    # True - alphanumeric
print("ABC".isupper())       # True - all uppercase
print("   ".isspace())       # True - all whitespace
```

Remember: Strings in Python are immutable - methods always return new strings rather than modifying the original. This is important for memory management and thread safety in DevOps applications.

// ...existing code...
# Python Strings — Expanded Reference with Real-world Examples

This file shows how to use Python strings in practical DevOps tasks. All code snippets are runnable on Python 3.8+.

---

## 1. Quick overview
- Strings are sequences of Unicode characters, immutable.
- Create with single, double or triple quotes. Raw strings (r"...") avoid escape processing.
- Common built-in functions: len(), str(), repr(), ord(), chr(), bytes(), bytearray().

---

## 2. Creation & literal forms
```python
single = 'hello'
double = "world"
multi = """line1
line2"""
raw = r'C:\Users\ci\workspace'   # backslashes preserved
bts = b'bytes'                  # bytes literal (not str)
```

Real example: reading a Windows path from env without accidental escapes:
```python
import os
path = os.getenv('APP_PATH', r'C:\Apps\default')  # use raw default
```

---

## 3. Indexing & slicing (practical)
```python
s = "deploy-2025-11-09"
s[0]       # 'd'
s[-2:]     # '09'   # useful to extract day from timestamp-like string
s[7:11]    # '2025'
s[::-1]    # reverse (rare in infra, but handy for quick checks)
```

Example: extract version segment:
```python
tag = "app-2.4.1"
version = tag.split('-', 1)[1]   # '2.4.1'
```

---

## 4. Common built-ins & patterns with examples

- len()
- str(), repr()
- ord()/chr() (unicode codes)
- any(), all(), enumerate(), zip()
- map(), filter()

Examples:
```python
s = "  nginx:1.21.0  "
len(s)                 # length including spaces
clean = s.strip()      # remove surrounding whitespace

# enumerate useful for reporting line numbers
for i, line in enumerate(open('deploy.log'), 1):
    if 'ERROR' in line:
        print(i, line.strip())
```

---

## 5. Case, test & validation
```python
name = "Web-01"
name.lower()           # 'web-01'
name.upper()           # 'WEB-01'
"123".isdigit()        # True
"Ⅳ".isnumeric()        # True (unicode numeric)
"abc123".isalnum()     # True
"   ".isspace()        # True
```

Real use: detect numeric port string:
```python
port_s = os.getenv('PORT', '80')
if port_s.isdigit():
    port = int(port_s)
else:
    raise ValueError("PORT must be numeric")
```

---

## 6. Searching, splitting, partitioning
```python
log = "2025-11-09 ERROR [web-01] out-of-memory"
log.find('ERROR')          # index or -1
log.startswith('2025')     # True
log.endswith('memory')     # False

# split into parts (safe split for logs)
parts = log.split(' ', 3)  # ['2025-11-09', 'ERROR', '[web-01]', 'out-of-memory']
timestamp, level, server, message = parts
server = server.strip('[]')  # 'web-01'

# partition: returns tuple (before, sep, after)
a, sep, b = log.partition('ERROR')
```

---

## 7. Replace, translate, sanitize
```python
s = "user=name;password=secret"
s.replace('secret', '***')   # simple masking

# translate to remove control chars
table = {ord('\n'): None, ord('\r'): None}
clean = s.translate(table)
```

Example: sanitize filename
```python
import re
bad = re.compile(r'[^A-Za-z0-9._-]')
safe = bad.sub('_', "weird:file/name.log")  # 'weird_file_name.log'
```

---

## 8. Join & split performance tip
- Avoid repeated `+` in loops. Use list append + join for many concatenations.
```python
# bad (quadratic cost)
out = ""
for chunk in chunks:
    out += chunk

# good
buf = []
for chunk in chunks:
    buf.append(chunk)
out = ''.join(buf)
```

---

## 9. Formatting: f-strings, format(), % (with examples)
F-strings are recommended for readability and speed (Python 3.6+).
```python
service = "nginx"
pid = 1234
msg = f"{service} (pid={pid}) is running"
```

Format spec examples for numbers:
```python
mem
