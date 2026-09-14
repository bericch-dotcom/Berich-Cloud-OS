"""
Berich-Cloud-OS v2.5
Author: Theophilus Agyemang (Bericch)
UENR Computer Engineering | Cloud Architect in Progress
Built from Kumasi, Ghana 🇬🇭
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(
    title="Berich-Cloud-OS",
    description="Lightweight Cloud OS for UENR/UMaT Students",
    version="2.5"
)

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
        <head><title>Berich-Cloud-OS</title></head>
        <body style="font-family:sans-serif; text-align:center; padding-top:50px; background:#0d1117; color:white;">
            <h1>☁️ Berich-Cloud-OS v2.5</h1>
            <p>System Status: <span style="color:#2ea043;">● ONLINE</span></p>
            <p>Author: Theophilus Agyemang (Bericch)</p>
            <p>Location: Kumasi, GH | UENR</p>
            <p><a href="/health" style="color:#58a6ff;">Check /health</a> | <a href="/docs" style="color:#58a6ff;">API Docs</a></p>
        </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "system": "Berich-Cloud-OS",
        "version": "2.5",
        "author": "Theophilus Agyemang",
        "timestamp": datetime.now().isoformat(),
        "location": "Kumasi, Ghana",
        "uptime": "100%"
    }

@app.get("/about")
def about():
    return {
        "name": "Berich-Cloud-OS",
        "mission": "Build Ghana's student cloud infrastructure",
        "stack": ["Python", "FastAPI", "Cloud Native"],
        "institution": "UENR / UMaT Aspirant"
    }
