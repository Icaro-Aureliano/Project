from email.policy import default
from app.controllers.find_insert import dbinsert, dbfind, rkfind,image, rockets, quotations, insertquotes, updatequote
from flask import flash, render_template, request, redirect, session, url_for
from app.models.model import Quote
from app import app

@app.route("/index")
@app.route("/")
def index():
    if "logado" not in session or session["logado"] == None:
        return redirect(url_for("login"))
    else:
        name = session["logado"]
        return render_template("index.html", name = name.title(), rockets=rockets(), volta="index", update=0)

@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session['logado'] = None
    return redirect(url_for("index"))

@app.route("/registration")
def regis():
    return render_template("registration.html")

@app.route("/check_user", methods=["POST",])
def checkuser():
        name = request.form["nameuser"]
        if dbfind(name):
            session['logado'] = name
            return redirect(url_for("age"))
        else:
            flash("Pessoa não registrada",)
            return redirect(url_for('login'))

@app.route("/check_rocket", methods=["POST",])
def checkrocket():
        name = request.form["namerock"]
        rocket = rkfind(name)
        
        porcent = request.form["gain"]
        date = request.form["date"]
        try:
            porcent = float(porcent)
        except:
            porcent = None

        launch = None
        if porcent and date != "" and rocket["active"]:
            launch = True
          
        insertquotes({"image": f"assets/{name}.png","rocket":rocket,"date":date,"porcent":porcent, "launch":launch })
        flash("operação concluida")
        return redirect(url_for("quote"))

@app.route("/quotations")
def quote():
    for q in quotations():
        print(type(q["launch"]))
    return render_template("quotations.html", quotes = quotations(), name = session["logado"].title())

@app.route("/update in me", methods=["POST",])
def update():
    name = request.form["nameuser"].lower()
    age = request.form["age"]
    try:
        age = int(age)
        if name.isnumeric():
            raise
        if not dbfind(name):
            dbinsert({"name":name,"age": age})
            flash("Cadastro efetuado")
        else:
            flash("Usuário cadastrado anteriormente")
    except:
        flash("Nome ou idade invalidos")
        return redirect(url_for("regis"))
    return redirect(url_for("login"))

@app.route("/rocket", methods=["POST",])
@app.route("/rocket/<update>", methods=["POST",])
def rocket(update = None):
    name = request.form["namerock"]
    
    v = False
    rocket = None
    for r in rockets():
        if r.name == name:
            rocket = r
            v = True
    
    if update:
        return render_template("rocket.html", image = image(name), name_user = session["logado"].title(), rocket = rocket, volta="quote", proxima="upquote")
    if v:
        return render_template("rocket.html", image = image(name), name_user = session["logado"].title(), rocket = rocket, volta="quote", proxima="checkrocket")
    else:
        flash("Foguete faltando")
        return redirect(url_for("index"))

@app.route("/updating", methods=["POST"])
def upquote():
    quot = request.form["value"]
    print("Quuote >>>>>>>>>> ",quot, type(quot))
    gain = request.form["gain"]
    date = request.form["date"]
    updatequote(quot, date, gain)
    return redirect(url_for("quote"))

@app.route("/age")
def age():
    name = session["logado"]
    return render_template("age.html", age = dbfind(name)["age"], name = name)