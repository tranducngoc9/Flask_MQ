from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def ngoc():
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST": #muc dich la de lay cai truyen vao 
        user_name = request.form["name"]
        if user_name: #Neu co nhap name
            return redirect(url_for("hello_user",name = user_name)) #truyen bien name va0
    return render_template("login.html")

@app.route("/user/<name>")
def hello_user(name):
    return f"<h1> Hello {name} </h1>"

if __name__ == "__main__":
    app.run(debug= True)













