from flask import Flask, redirect, url_for, render_template, request, session ,flash
#flah de dua ra thong bao goi la flash_message
#reder_template de dua den trang html   
#session de luu giu nguoi dung    
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"]  = "ngoctranss" #de bao mat neu ko se ko chay
app.permanent_session_lifetime = timedelta(seconds=5) # Sau 5s ko lam gi se bi day ra

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST": #muc dich la de lay cai truyen vao 
        global user_name
        user_name = request.form["name"]
        session.permanent = True
        
        if user_name: #Neu co nhap name
            session["user"] = user_name  # luu giu nguoi dung vao session
            flash(" Ban da Login thanh cong!", "info")
            return render_template("user.html", user = user_name)
            
    if "user" in session:  #neu nguoi dung van o trong session thi ko log_out
        name = session["user"]
        flash("Ban da Login !", "info")
        
        return render_template("user.html", user =user_name)
    return render_template("login.html")

@app.route("/logout")
def log_out():
    flash("Ban da LogOut!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user/<name>")
def hello_user(name):
    if "user" in session:
        name = session["user"]
        flash("Ban da Login !", "info")
        return render_template("user.html", user = name)
    else:
        flash("Ban chua Login!", "info")
        return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug= True)
