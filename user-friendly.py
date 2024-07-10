import os

from dotenv import load_dotenv
from internetarchive import configure, upload

load_dotenv()

try:
  global email
  email = os.environ["EMAIL"],
except Exception:
  email = input("Enter your e-mail\n")

try:
  global passwd
  passwd = os.environ["PASSWD"],
except Exception:
  passwd = input("Enter your password\n")

try:
  global id
  id = os.environ["ID"],
except Exception:
  id = input("Enter your item's identifier\n")


def main():
  print(
      "This code does not access any part of the internet other than archive.org."
  )
  print("Your credentials are never sent to anyone and are stored on your computer.")
  upload(id, files=['skins.zip'])


try:
  configure(email, passwd)
  main()
except Exception:
  print("Invalid e-mail or password")
