
# Berich-Cloud-OS v4.0 ☁️
**Personal Cloud OS Built 100% on Android Phone** 🇬🇭

![Version](https://img.shields.io/badge/version-3.1-green)
![Built On](https://img.shields.io/badge/built%20on-Android-brightgreen)
![Stack](https://img.shields.io/badge/stack-FastAPI%20%2B%20Python-blue)

> Built by Theophilus (UENR UA2612947) - Kumasi, GH
> No laptop. Only Android phone (Acode + Pydroid 3)

### 🚀 Live Demo
- Dashboard: `/` - Clickable Terminal UI
- API Docs: `/docs` (Swagger)
- Health: `/health`

### 🏗️ Architecture - 5 Modules
I designed Berich-Cloud-OS as a modular OS kernel:

| Module | File | Purpose | Endpoints |
|---|---|---|---|
| Filesystem | `filesystem.py` | Virtual file storage | `/files`, `/files/{id}` |
| Auth | `auth.py` | RBAC, login, roles | `/auth/login`, `/auth/me` |
| Terminal | `terminal.py` | Linux-like shell (ls, pwd, whoami, date) | `/terminal?cmd=ls` |
| Dashboard | `dashboard.py` | Web UI, HTML/CSS/JS | `/` |
| Processes | `processes.py` | PID, status, kill | `/processes` |

**Total: 12 REST endpoints**

### ⚙️ Tech Stack
- **Backend:** FastAPI, Python 3
- **Frontend:** Vanilla HTML/CSS/JS (no frameworks - lightweight for mobile)
- **Dev Environment:** Acode Editor + Pydroid 3 + Termux on Android
- **Version Control:** Git + GitHub

### 🧠 How I Built It (Workflow)
This project demonstrates modern AI-accelerated development:
1.  **I architected** the module breakdown and endpoint design
2.  **I used AI as pair programmer** to generate boilerplate faster
3.  **I tested every module live** on Pydroid 3 at 7:13am-7:28am
4.  **I own every line** - can explain, debug, and extend live

> In 2026, using AI is industry standard. What matters is architecture ownership and ability to explain/debug.

### 📈 Release History
- **v2.7** - Filesystem module
- **v2.8** - Auth + RBAC
- **v2.9** - Terminal (ls, pwd, whoami, date, help) - TEST PASSED 7:14am
- **v3.0** - Dashboard UI - LIVE 7:28am
- **v3.1** - Process Manager - 12 endpoints

### 🎯 Interview Ready
**Q: Can you explain your code?**
A: Yes, walk through any module. Example: `terminal.py` uses command parser → role check → mock fs.

**Q: How would you scale this?**
A: Add DB (SQLite), Docker, JWT auth, WebSockets for real process monitoring, deploy to Render.

**Q: Did AI build this?**
A: I architected it. AI accelerated coding, I validated all releases on Android. Commit history proves it.

### 🔜 Next - v4.0 Final
- Add persistence (SQLite)
- File upload
- Deployment link
- Demo video

---
**Contact:** github.com/bericch-dotcom/Berich-Cloud-OS
**Location:** Kumasi, GH | **Time Built:** Early mornings on Android
