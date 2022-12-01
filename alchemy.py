from flask import Flask, redirect, url_for, render_template, request, session ,flash
#flah de dua ra thong bao goi la flash_message
#reder_template de dua den trang html   
#session de luu giu nguoi dung    
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path


app = Flask(__name__)
app.config["SECRET_KEY"]  = "ngoctranss" #de bao mat neu ko se ko chay
#config duong dan noi ma se luu database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_ngoc.db"
#Theo soi su thay doi
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(seconds=5) # Sau 5s ko lam gi se bi day ra

db = SQLAlchemy(app)

#Để tạo ra được bảng trong Alchemy thì ta phải ta sử dụng ORM bằng cách dùng lập trình hướng đối tượng
#Tạo bảng dữ liệu  User gồm id, name, email
class User(db.Model):
    # Trường ID , name, email
    use_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    # id Không cần truyền vì đây nó là trường tự tăng
    def __init__(self, name, email):
        self.name = name
        self.email = email

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
            return redirect(url_for("user", user = user_name))
            
    if "user" in session:  #neu nguoi dung van o trong session thi ko log_out
        name = session["user"]
        return redirect(url_for("user", user = user_name))
    return render_template("login.html")

@app.route("/logout")
def log_out():
    flash("Ban da LogOut!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user/<name>")
def user(name):
    if "user" in session:
        name = session["user"]
        return render_template("user.html", user = name)
    else:
        flash("Ban chua Login!", "info")
        return redirect(url_for("login"))


if __name__ == "__main__":
    #Check xem database da ton tai hay chua
    if not path.exists("user_ngoc.db"):
        db.create_all(app = app)
        print("created database!")
    app.run(debug= True)
