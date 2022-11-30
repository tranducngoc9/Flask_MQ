from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"]  = "ngoctranss" #de bao mat neu ko se ko chay
app.permanent_session_lifetime = timedelta(minutes=1) # Sau 1 phut ko lam gi se bi day ra

@app.route("/")
def ngoc():
    return render_template("tym.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST": #muc dich la de lay cai truyen vao 
        session.permanent = True
        user_name = request.form["name"]
        if user_name: #Neu co nhap name
            session["user"] = user_name  # luu giu nguoi dung vao session
            return redirect(url_for("hello_user",name = user_name)) #truyen bien name va0
    if "user" in session:  #neu nguoi dung van o trong session thi ko log_out
        name = session["user"]
        return f"<h1> Hello {name} </h1>"
    return render_template("login.html")

@app.route("/logout")
def log_out():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user/<name>")
def hello_user(name):
    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name} </h1>"
    else:
        return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug= True)

