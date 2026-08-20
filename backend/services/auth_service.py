import json

USERS_FILE = "users.json"

def validate_user(username, password):

    with open(USERS_FILE, "r") as file:
        users = json.load(file)

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    return False
