# Berich-Cloud-OS v3.0 Dashboard - Built on Android
def get_dashboard_html():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Berich-Cloud-OS v3.0</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:monospace;background:#0a0a0a;color:#00ff88;margin:0;padding:20px}
.header{border:2px solid #00ff88;padding:15px;border-radius:10px;margin-bottom:20px}
.card{background:#111;border:1px solid #00ff88;padding:15px;border-radius:8px;margin:10px 0}
button{background:#00ff88;color:#000;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;font-weight:bold;margin:5px}
button:hover{background:#00cc6a}
#terminal{background:#000;color:#0f0;padding:15px;border-radius:8px;min-height:100px;margin-top:10px;white-space:pre-wrap}
.badge{display:inline-block;background:#00ff88;color:#000;padding:3px 8px;border-radius:12px;font-size:12px}
</style>
</head>
<body>
<div class="header">
<h1>☁️ Berich-Cloud-OS v3.0 <span class="badge">DASHBOARD LIVE</span></h1>
<p>Built 100% on Android 🇬🇭 | UENR UA2612947 | Theophilus</p>
<p>Modules: filesystem + auth + terminal + dashboard</p>
</div>

<div class="card">
<h3>💻 Berich Shell v1.0</h3>
<button onclick="runCmd('ls')">ls</button>
<button onclick="runCmd('pwd')">pwd</button>
<button onclick="runCmd('whoami')">whoami</button>
<button onclick="runCmd('date')">date</button>
<button onclick="runCmd('help')">help</button>
<div id="terminal">$ Ready... Click a command above</div>
</div>

<div class="card">
<h3>🔐 Auth</h3>
<p>Admin: theophilus / bericch2026</p>
<button onclick="testAuth()">Test Login</button>
<div id="auth-result"></div>
</div>

<div class="card">
<h3>📁 Files</h3>
<button onclick="loadFiles()">List Files</button>
<div id="files"></div>
</div>

<script>
async function runCmd(cmd){
 document.getElementById('terminal').innerText = '$ '+cmd+'\\nLoading...';
 let res = await fetch('/terminal?cmd='+cmd+'&username=theophilus');
 let data = await res.json();
 document.getElementById('terminal').innerText = '$ '+cmd+'\\n'+JSON.stringify(data, null, 2);
}
async function loadFiles(){
 let res = await fetch('/files');
 let data = await res.json();
 document.getElementById('files').innerText = JSON.stringify(data, null, 2);
}
async function testAuth(){
 let res = await fetch('/auth/login?username=theophilus&password=bericch2026');
 let data = await res.json();
 document.getElementById('auth-result').innerText = JSON.stringify(data, null, 2);
}
</script>
</body>
</html>
    """
