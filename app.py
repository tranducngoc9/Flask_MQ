from flask import Flask

app = Flask(__name__)
#Dinh tuyen
@app.route('/')
def hello_world():
    return "<h1> Tran duc ngoc </h1>"
@app.route('/user/<name>')
# bien truyen vao bat buoc phai la name
def hello_user(name):
    return f"<h1> Hello {name} </h1>"

app.route("/blog/<int:blog_id>")
def blog(blog_id):
    return f"<h1> Blog {blog_id} </h1>"

if __name__ == "__main__":
    app.run(debug=True)