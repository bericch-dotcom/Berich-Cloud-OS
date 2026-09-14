
from fastapi import FastAPI
import filesystem
import auth

app = FastAPI(
    title="Berich-Cloud-OS",
    version="2.8",
    description="Lightweight Cloud OS v2.8 with Filesystem + Auth | Built on Android | UENR UA2612947"
)

@app.get("/")
def home():
    return {
        "os": "Berich-Cloud-OS v2.8",
        "status": "Auth & Filesystem Active",
        "author": "Theophilus Agyemang | UA2612947",
        "endpoints": ["/health", "/about", "/files", "/auth/login", "/auth/users", "/docs"]
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "2.8",
        "modules": ["filesystem", "auth"],
        "cloud_drive_files": len(filesystem.list_files())
    }

@app.get("/about")
def about():
    return {
        "project": "Berich-Cloud-OS",
        "built_on": "Android in Kumasi, Ghana",
        "stack": "FastAPI + Python 3.10+",
        "mission": "Journey to Cloud Architect - UENR",
        "current_version": "2.8 Auth Live"
    }

@app.get("/files")
def get_files():
    return {"count": len(filesystem.list_files()), "files": filesystem.list_files()}

@app.get("/files/create")
def create_demo():
    return filesystem.create_file("hello.txt", "Hello from Berich-Cloud-OS v2.8!")

@app.get("/files/delete/{filename}")
def delete_file(filename: str):
    return filesystem.delete_file(filename)

@app.get("/auth/login")
def login(username: str, password: str):
    return auth.login(username, password)

@app.get("/auth/users")
def users():
    return {"count": len(auth.list_users()), "users": auth.list_users()}
