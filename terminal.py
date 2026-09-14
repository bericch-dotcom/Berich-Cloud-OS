# Berich-Cloud-OS Terminal v2.9 - Built on Android
import filesystem
import auth
from datetime import datetime
import platform

def run_command(cmd: str, username: str = "guest"):
    cmd = cmd.strip().lower()
    
    if cmd == "ls" or cmd == "dir":
        files = filesystem.list_files()
        return {"command": cmd, "output": files, "count": len(files)}
    
    elif cmd == "pwd":
        return {"command": cmd, "output": "/berich-cloud-os/v2.9"}
    
    elif cmd == "whoami":
        return {"command": cmd, "output": username, "role": auth.USERS.get(username, {}).get("role", "unknown")}
    
    elif cmd == "date":
        return {"command": cmd, "output": datetime.now().isoformat()}
    
    elif cmd == "help":
        return {"command": cmd, "output": ["ls - list files", "pwd - current dir", "whoami - current user", "date - system time", "help - this list", "clear - clean"]}
    
    elif cmd == "clear":
        return {"command": cmd, "output": "Terminal cleared - Berich-Cloud-OS v2.9"}
    
    else:
        return {"command": cmd, "error": f"Command '{cmd}' not found. Type 'help'."}

def get_system_info():
    return {
        "os": "Berich-Cloud-OS v2.9 Terminal",
        "kernel": "FastAPI 0.104",
        "shell": "Berich Shell v1.0",
        "uptime": "Active since 6:56am"
    }
