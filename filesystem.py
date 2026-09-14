# Berich-Cloud-OS Filesystem v2.7 - Built on Android
import os
from datetime import datetime

BASE_DIR = "cloud_drive"

os.makedirs(BASE_DIR, exist_ok=True)

def list_files():
    files = os.listdir(BASE_DIR)
    result = []
    for f in files:
        path = os.path.join(BASE_DIR, f)
        stat = os.stat(path)
        result.append({
            "name": f,
            "size_kb": round(stat.st_size/1024, 2),
            "created": datetime.fromtimestamp(stat.st_ctime).isoformat()
        })
    return result

def create_file(filename, content=""):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w") as file:
        file.write(content)
    return {"message": f"{filename} created", "path": path}

def delete_file(filename):
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return {"message": f"{filename} deleted"}
    return {"error": "File not found"}
