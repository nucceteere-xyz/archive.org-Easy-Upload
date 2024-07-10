import os

from dotenv import load_dotenv
from internetarchive import configure, upload

load_dotenv()

# This is not for the casual user who wants to use it without any errors.
# It's for developers to incorprate it into their code.

email = os.environ["EMAIL"],
passwd = os.environ["PASSWD"],
id = os.environ["ID"],


def main():
  try:
    upload(id, files=['skins.zip'])
  except Exception:
    print("Invalid ID or file")


try:
  configure(email, passwd)
  main()
except Exception:
  print("Invalid e-mail or password")
