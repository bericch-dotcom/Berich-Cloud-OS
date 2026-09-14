# Berich-Cloud-OS Auth v2.8 - Built on Android
from datetime import datetime

# Fake user database for OS
USERS = {
    "theophilus": {"password": "bericch2026", "role": "admin", "id": "UA2612947"},
    "guest": {"password": "guest123", "role": "viewer", "role": "viewer"}
}

def login(username: str, password: str):
    user = USERS.get(username)
    if not user:
        return {"status": "failed", "message": "User not found"}
    if user["password"] != password:
        return {"status": "failed", "message": "Wrong password"}
    return {
        "status": "success",
        "message": f"Welcome {username}",
        "user": {"username": username, "role": user["role"], "id": user["id"] if "id" in user else "guest"},
        "login_time": datetime.now().isoformat(),
        "token": f"berich-token-{username}-v2.8"
    }

def list_users():
    return [{"username": u, "role": d["role"]} for u, d in USERS.items()]
