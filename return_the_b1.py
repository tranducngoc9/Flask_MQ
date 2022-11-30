from flask import Flask , redirect, url_for #redirect de chuyen huong trang

app = Flask(__name__)
#Dinh tuyen
@app.route('/')
def hello_world():
    return "<h1> Day la giao dien chinh :v </h1>"  #RETURN SE tra ve 1 cai trang

@app.route("/admin")
def hello_admin():
    return "<h1> Hello Admin ngoc </h1>"

@app.route('/user/<name>')
# bien truyen vao bat buoc phai la name
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin")) #chuyen huong trang
    return f"<h1> Hello {name} </h1>"

# @app.route("")

# @app.route("/blog/<int:blog_id>")
# def blog(blog_id):
#     return f"<h1> Blog {blog_id} </h1>"

if __name__ == "__main__":
    app.run(debug=True)