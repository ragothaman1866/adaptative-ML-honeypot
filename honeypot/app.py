from flask import Flask, request
import pandas as pd
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        log = {
            "ip": request.remote_addr,
            "username": request.form.get("username"),
            "password": request.form.get("password"),
            "time": datetime.datetime.now()
        }
        pd.DataFrame([log]).to_csv("logs/attacks.csv", mode="a", header=False, index=False)

    return '''
    <h2>Admin Login</h2>
    <form method="post">
    <input name="username" placeholder="username">
    <input name="password" type="password" placeholder="password">
    <button>Login</button>
    </form>
    '''

app.run(port=5000)
