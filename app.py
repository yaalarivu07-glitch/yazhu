
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Attendance Management System</title>
    </head>
    <body>
        <h1>Cloud-Based Attendance Management System</h1>
        <h2>Welcome!</h2>
        <p>Our attendance management system is ready.</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
