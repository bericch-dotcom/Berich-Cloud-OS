# Berich-Cloud-OS v4.0 Process Manager
from datetime import datetime
_processes = [
    {"pid": 101, "name": "filesystem", "status": "running", "uptime": "00:28:14", "cpu": "2%"},
    {"pid": 102, "name": "auth", "status": "running", "uptime": "00:18:42", "cpu": "1%"},
    {"pid": 103, "name": "terminal", "status": "running", "uptime": "00:14:00", "cpu": "3%"},
    {"pid": 104, "name": "dashboard", "status": "running", "uptime": "00:00:45", "cpu": "5%"},
]
def list_processes():
    return {"count": len(_processes), "processes": _processes, "timestamp": datetime.now().isoformat()}
def get_process(pid: int):
    for p in _processes:
        if p["pid"] == pid: return p
    return {"error": f"PID {pid} not found"}
def kill_process(pid: int):
    global _processes
    _processes = [p for p in _processes if p["pid"] != pid]
    return {"message": f"Process {pid} terminated", "remaining": len(_processes)}
