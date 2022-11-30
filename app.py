from flask import  Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def hello_world(): 
    return render_template("index.html", content = "Tran Duc Ngoc",
                            cars= ["wave" , "vinfast" , "BMV"]) #In ra content


if __name__ == "__main__":
    app.run(debug= True)