# Part 7 — DevOps Python Applications

Focuses on using Python for DevOps tasks: HTTP requests, cloud SDKs (boto3), subprocess/CLI automation, log parsing, and simple Infrastructure-as-Code automation patterns.

---

## 1. HTTP automation (requests / httpx)
What: Call REST APIs.
Example with requests:
```python
import requests
r = requests.get('https://api.example.com/health')
print(r.status_code, r.json())
```
Interview Qs:
- Sync vs async HTTP clients; when to use each.

---

## 2. AWS automation (boto3)
Example:
```python
import boto3
s3 = boto3.client('s3')
s3.list_buckets()
```
Interview Qs:
- How to handle credentials securely (IAM roles, profiles, env vars).

---

## 3. Subprocess & CLI automation
Example:
```python
import subprocess
subprocess.run(['kubectl','get','pods'], check=True)
```
Interview Qs:
- How to capture stdout/stderr and handle errors.

---

## 4. Log parsing & metrics
Example:
```python
with open('app.log') as fh:
    for ln in fh:
        if 'ERROR' in ln:
            alert(ln)
```
Interview Qs:
- Strategies for scaling log parsing (streams, generators, streaming libraries).

---

## 5. IaC & templating
- Use Python to generate k8s manifests or Terraform templates (Jinja2 templating).

---

## Practice
- Build a small script that calls a cloud API, saves results to JSON, and uploads to S3. Include error handling and unit tests.