
# Berich-Cloud-OS v3.0 Dashboard UI - Built 100% on Android
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import filesystem
import auth
import terminal
import dashboard

app = FastAPI(
    title="Berich-Cloud-OS",
    version="3.0",
    description="Personal Cloud OS Built 100% on Android - UENR UA2612947"
)

@app.get("/", response_class=HTMLResponse)
def root():
    """Serve v3.0 Dashboard UI"""
    return dashboard.get_dashboard_html()

@app.get("/api")
def api_info():
    return {
        "name": "Berich-Cloud-OS",
        "version": "3.0",
        "status": "Dashboard LIVE",
        "modules": ["filesystem", "auth", "terminal", "dashboard"],
        "endpoints": 9,
        "built_on": "Android",
        "developer": "Theophilus - UA2612947",
        "time": "September 2026 - Kumasi, GH"
    }

# --- Filesystem Module (v2.7) ---
@app.get("/files")
def list_files():
    return filesystem.list_files()

@app.get("/files/{file_id}")
def get_file(file_id: str):
    return filesystem.get_file(file_id)

# --- Auth Module (v2.8) ---
@app.get("/auth/login")
def login(username: str, password: str):
    return auth.login(username, password)

@app.get("/auth/me")
def me(username: str):
    return auth.get_user(username)

# --- Terminal Module (v2.9) ---
@app.get("/terminal")
def run_terminal(cmd: str, username: str = "guest"):
    return terminal.run_command(cmd, username)

@app.get("/terminal/info")
def terminal_info():
    return terminal.get_info()

# --- Dashboard Module (v3.0) ---
@app.get("/dashboard")
def get_dashboard():
    return {"message": "Go to / for UI Dashboard"}

@app.get("/health")
def health():
    return {"status": "UP", "version": "3.0", "uptime": "Building since 6am"}
