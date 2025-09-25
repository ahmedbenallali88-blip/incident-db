USERS = {
    "djamaie": {"password": "ligature2025", "role": "animateur"},
    "jouad": {"password": "refJ2025", "role": "coordinateur"},
}

def login(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None
