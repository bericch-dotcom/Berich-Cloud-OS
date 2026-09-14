
from fastapi import FastAPI
import filesystem
import auth
import terminal

app = FastAPI(title="Berich-Cloud-OS v2.9")

@app.get("/")
def home():
    return {"os": "Berich-Cloud-OS v2.9", "status": "Terminal Live", "shell": "Berich Shell v1.0"}

@app.get("/files")
def get_files():
    return filesystem.list_files()

@app.get("/auth/login")
def login(username: str, password: str):
    return auth.login(username, password)

@app.get("/auth/users")
def users():
    return auth.list_users()

@app.get("/terminal")
def terminal_cmd(cmd: str = "help", username: str = "guest"):
    return terminal.run_command(cmd, username)

@app.get("/terminal/info")
def sys_info():
    return terminal.get_system_info()
