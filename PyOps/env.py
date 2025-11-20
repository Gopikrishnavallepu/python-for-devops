import os
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_user = os.getenv('DB_USER', 'admin')
db_password = os.getenv('DB_PASSWORD', 'password')
print(f"Connecting to database at {db_host}:{db_port} as {db_user}")