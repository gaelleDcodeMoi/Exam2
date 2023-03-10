from flask import Flask, render_template, request
app = Flask(__name__)

# 127.0.0.1:5000
# 80.240.127.173:5000
@app.route("/<string:name>")
def hello(name=None):
    return f"<h1>Bienvenido a mi app, {name}.</h1><p>Esta es mi primera app de Flask.</p>"

@app.route("/welcome/<string:nombre>")
def api(nombre):
    return f"Bienvenido a mi app, {nombre}."

@app.route("/form", methods=["GET", "POST"])
def form():
    name = None
    age = 0
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        print(name, age)
    return render_template("form.html", name=name, age=age)


# 5001
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001, debug = True)
