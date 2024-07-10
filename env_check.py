import os

from dotenv import load_dotenv

load_dotenv()

print(f"E-Mail: {os.environ.get('EMAIL')}")
print(f"Password: {os.environ.get('PASSWD')}")
print(f"Identifier: {os.environ.get('ID')}")
