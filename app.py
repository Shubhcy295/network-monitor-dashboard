from flask import Flask 
import psutil,socket
from datetime import datetime 
import pytz

# Create Flask app(name string)
app = Flask("monitor")

@app.route("/")
def dashboard():

  # System Data
  node = socket.gethostname()
  cpu = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage("/").percent

  # IST Time
  ist = pytz.timezone("Asia/Kolkata")
  current_time = datetime.now(ist).strftime("%d %b %Y - %H:%M IST")

  # Dynamic Colors
  cpu_color = "#f59e0b" if cpu < 70 else "#ef4444"
  mem_color = "#38bdf8" if memory < 75 else "#ef4444"
  disk_color = "#22c55e" if disk < 80 else "#ef4444"

  return f"""

<!DOCTYPE html>
<html>
<head>
<title>System Health Monitor</title>

<style>
body{{
      margin: 0;
      font-family: Arial, sans-serif;
      background: #0f172a;

      background-image: linear-gradient(135deg, #0f172a, #1e293b);

      color: #e2e8f0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
}}

.card{{
   width: 650px;
   padding: 35px;
   background: rgba(255,255,255,0.05);
   border-radius: 16px;
   box-shadow: 0 20px 50px rgba(0,0,0,0.6);
   background-filter: blur(12px);
}}

h1{{
   text-align: center;
   color: #38bdf8;
   margin-bottom: 30px;
}}

h3{{
   margin-top: 25px;
   color: #93c5fd;
}}

.section-title{{
   margin-top: 25px;
   margin-bottom: 10px;
   font-weight: bold;
   color: #94a3b8;
}}

.info{{
   margin-bottom: 8px;
}}

.bar{{
   height: 10px;
   background: #334155;
   border-radius: 10px;
   margin-bottom: 6px 0 20px 0;
   overflow: hidden;
}}

.fill{{
   height: 100%;
   border-radius: 10px;
}}

.footer{{
    text-align: center;
    margin-top: 25px;
    font-size: 13px;
    color: #94a3b8;
}}

</style>
</head>

<body>

   <div class = "card">
    <h1>System Health Monitor</h1>

   <h3>Node Info</h3>
   Host: <b>{node}</b><br>
   Status: Active<br>
   Auto Refresh: 3 Seconds
   
   <h3>System Usage</h3>

     CPU: {cpu}%
     <div class = "bar">
       <div class = "fill" style = "width:{cpu}%;
   background:{cpu_color};"></div>
     </div>

     Memory: {memory}%
     <div class = "bar">
       <div class = "fill" style = "width:{memory}%;
   background:{mem_color};"></div>
     </div>

     Disk:{disk}%
     <div class = "bar">
       <div class = "fill" style="width:{disk}%;
   background:{disk_color};"></div>
     </div>

     <div class = "footer">
       Last Updated: {current_time}
     </div>
   </div>

</body>
</html>
"""

app.run(host = "0.0.0.0", port = 5000, debug = True)
