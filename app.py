ffrom datetime import datetime
import csv
import os

app = Flask(__name__)
FILE = "visitors.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        csv.writer(f).writerow(["Time", "Device"])

@app.route("/")
def home():
    return """
    <html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <body style="background:#100b20;color:white;
    font-family:Arial;text-align:center;padding:40px">
    <h1 style="color:#bd8cff">VISITOR TRACKER</h1>
    <p>موقع تجريبي لإحصائيات الزيارات.</p>
    <p>عند المتابعة سيتم تسجيل نوع الجهاز ووقت الزيارة فقط.</p>
    <form action="/visit" method="POST">
    <label>
    <input type="checkbox" required>
    أوافق على تسجيل المعلومات الموضحة
    </label><br><br>
    <button style="padding:14px;background:#9254ff;
    color:white;border:0;border-radius:10px">
    متابعة
    </button>
    </form>
    </body></html>
    """

@app.route("/visit", methods=["POST"])
def visit():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE, "a", newline="") as f:
        csv.writer(f).writerow([now, "Visitor"])

    return "تم تسجيل الزيارة بنجاح!"

if __name__ == "__main__":
    app.run()rom flask import Flask, request from datetime import 
















