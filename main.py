from fastapi import FastAPI
import filesystem

app = FastAPI(
    title="Berich-Cloud-OS",
    version="2.7",
    description="Lightweight Cloud OS built 100% on Android in Ghana | UENR UA2612947"
)

@app.get("/")
def home():
    return {
        "os": "Berich-Cloud-OS v2.7",
        "status": "running on Android",
        "author": "Theophilus Agyemang | UA2612947",
        "endpoints": ["/health", "/about", "/files", "/files/create", "/docs"]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "version": "2.7", "cloud_drive_files": len(filesystem.list_files())}

@app.get("/about")
def about():
    return {
        "project": "Berich-Cloud-OS",
        "built_on": "Android Phone in Kumasi, Ghana",
        "stack": "Python 3.10+ FastAPI",
        "mission": "Journey to Cloud Architect"
    }

@app.get("/files")
def get_files():
    return {"count": len(filesystem.list_files()), "files": filesystem.list_files()}

@app.get("/files/create")
def create_demo():
    return filesystem.create_file("hello.txt", "Hello from Berich-Cloud-OS v2.7!")

@app.get("/files/delete/{filename}")
def delete_file(filename: str):
    return filesystem.delete_file(filename)
