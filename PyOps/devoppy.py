import requests

response = requests.get("https://api.github.com")
print("Status Code:")
print(response)
print(response.status_code)  # 200
print(response.text[:100])   # Partial response
print("Request successful!")  # Confirmation message
# This is a sample Python script.
def main():
    print("This is a sample script.")
if __name__ == "__main__":
    main()
