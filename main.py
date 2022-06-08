import requests

username = input("Please enter a username: ")



GitHub = requests.get("https://api.github.com/users/" + str(username))

if GitHub.status_code == 200:
  print("[+] GitHub: https://github.com/" + str(username))

