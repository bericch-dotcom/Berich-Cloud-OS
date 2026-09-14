
# Berich-Cloud-OS v3.1 Process Manager - Interview Ready
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import filesystem, auth, terminal, dashboard, processes

app = FastAPI(title="Berich-Cloud-OS", version="3.1", description="Personal Cloud OS - Built 100% on Android - UENR UA2612947")

@app.get("/", response_class=HTMLResponse)
def root():
    return dashboard.get_dashboard_html()

@app.get("/api")
def api_info():
    return {"name": "Berich-Cloud-OS", "version": "3.1", "status": "Process Manager LIVE", "modules": ["filesystem", "auth", "terminal", "dashboard", "processes"], "endpoints": 12, "built_on": "Android", "developer": "Theophilus - UA2612947"}

# Filesystem
@app.get("/files")
def list_files(): return filesystem.list_files()
@app.get("/files/{file_id}")
def get_file(file_id: str): return filesystem.get_file(file_id)

# Auth
@app.get("/auth/login")
def login(username: str, password: str): return auth.login(username, password)
@app.get("/auth/me")
def me(username: str): return auth.get_user(username)

# Terminal
@app.get("/terminal")
def run_terminal(cmd: str, username: str = "guest"): return terminal.run_command(cmd, username)
@app.get("/terminal/info")
def terminal_info(): return terminal.get_info()

# Processes - NEW v3.1
@app.get("/processes")
def list_proc(): return processes.list_processes()
@app.get("/processes/{pid}")
def get_proc(pid: int): return processes.get_process(pid)
@app.get("/processes/kill/{pid}")
def kill_proc(pid: int): return processes.kill_process(pid)

@app.get("/health")
def health(): return {"status": "UP", "version": "3.1", "modules_running": 5}
