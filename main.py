# Berich-Cloud-OS v2.5 - All 5 Apps | Theophilus Agyemang - UENR
import os, hashlib, hmac, datetime, random

def banner():
    print("="*50)
    print(" BERICH-CLOUD-OS v2.5 ☁️ | 5-in-1 Cloud OS")
    print(" UENR Computer Engineering | Built on Android")
    print("="*50)
    print(" Apps: chat | calc | umat | login | cloud")
    print(" Type 'help' to start")
    print("="*50)

# --- APP 1: CHAT APP ---
def chat_app():
    print("\n--- Berich Chat AI --- (type 'bye' to exit chat)")
    replies = {
        "hi": "Hi! I'm Berich AI, built on your OS 👋",
        "how are you": "I'm running great on Android!",
        "umat": "UMaT Computer Engineering needs aggregate 12 for best chance",
        "cloud": "Cloud Engineer = AWS + Linux + Python. You are on track!",
        "who are you": "I am Berich-Cloud-OS assistant, built by Theophilus"
    }
    while True:
        msg = input("You: ").lower().strip()
        if msg == "bye":
            print("Berich AI: Bye! Back to OS...\n")
            break
        found = False
        for k in replies:
            if k in msg:
                print(f"Berich AI: {replies[k]}")
                found = True
                break
        if not found:
            print(f"Berich AI: You said '{msg}' - Interesting! Tell me more.")

# --- APP 2: CALCULATOR ---
def calc_app():
    print("\n--- Calculator App ---")
    try:
        a = float(input("First number: "))
        op = input("Operator (+ - * / %): ")
        b = float(input("Second number: "))
        if op == "+": print(f"Result: {a+b}")
        elif op == "-": print(f"Result: {a-b}")
        elif op == "*": print(f"Result: {a*b}")
        elif op == "/": print(f"Result: {a/b if b!=0 else 'Error: /0'}")
        elif op == "%": print(f"Result: {a%b}")
        else: print("Invalid operator")
    except: print("Enter numbers only")

# --- APP 3: UMAT CHECKER ---
def umat_checker():
    print("\n--- UMaT Admission Checker ---")
    name = input("Name: ")
    try:
        agg = int(input("WASSCE Aggregate (6-36): "))
        if 6 <= agg <= 12: print(f"{name}, 🔥 QUALIFIED for BSc Computer Engineering!")
        elif 13 <= agg <= 20: print(f"{name}, Good for Computer Science / IT")
        elif 21 <= agg <= 36: print(f"{name}, Consider Diploma or retake")
        else: print("Aggregate must be 6-36")
    except: print("Enter valid number")

# --- APP 4: SECURED LOGIN ---
def password_matches(pwd: str) -> bool:
    stored = hashlib.sha256("Berich2025!Secure".encode()).hexdigest()
    subm = hashlib.sha256(pwd.encode()).hexdigest()
    return hmac.compare_digest(subm, stored)

def login_app():
    print("\n--- Secured Login System ---")
    user = input("Username: ")
    pwd = input("Password: ")
    if password_matches(pwd):
        print(f"✅ Access granted! Welcome {user}")
        print(f"Login time: {datetime.datetime.now()}")
    else:
        print("❌ Access denied! Hint: Berich2025!Secure")

# --- APP 5: CLOUD OS DASHBOARD ---
def cloud_dashboard():
    print("\n--- Cloud OS Dashboard ---")
    print(f"OS Version: Berich-Cloud-OS v2.5")
    print(f"User: Theophilus Agyemang | UA2612947")
    print(f"System: Android + Python + Linux")
    print(f"Storage: {len(os.listdir('.'))} files in current dir")
    print(f"Uptime: {datetime.datetime.now()}")
    print("Cloud Status: [Simulated] Connected to Berich Cloud ☁️")
    print("Next: AWS S3 Integration coming soon!")

def help_menu():
    print("""
COMMANDS (All 5 Apps):
  chat - Chat App (AI assistant)
  calc - Calculator App
  umat - UMaT Checker
  login - Secured Login
  cloud - Cloud Dashboard
  ls - List files
  pwd - Current directory
  time - Current time
  clear - Clear screen
  help - This menu
  exit - Shutdown OS
""")

banner()
help_menu()

while True:
    cmd = input("\nberich@cloud-os:~$ ").lower().strip()
    if cmd == "help": help_menu()
    elif cmd == "chat": chat_app()
    elif cmd == "calc": calc_app()
    elif cmd == "umat": umat_checker()
    elif cmd == "login": login_app()
    elif cmd == "cloud": cloud_dashboard()
    elif cmd == "ls": print("\n".join(os.listdir(".")))
    elif cmd == "pwd": print(os.getcwd())
    elif cmd == "time": print(datetime.datetime.now())
    elif cmd == "clear":
        os.system('clear')
        banner()
    elif cmd == "exit":
        print("Shutting down Berich-Cloud-OS... See you! 👋")
        break
    else:
        print(f"'{cmd}' not found. Type 'help' for all 5 apps")
