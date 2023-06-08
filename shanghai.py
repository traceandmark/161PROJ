from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/flavors/<shangrice_flavor>')
def flavors(shangrice_flavor):
    flavor = shangrice_flavor
    return render_template("products.html", name = flavor )

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/flavors/<shangrice_flavor>/<database_flavor>')
def database(shangrice_flavor,database_flavor):
    flavor = shangrice_flavor
    data = database_flavor
    return render_template("database.html", name = flavor, name2 = data )

@app.route('/flavors/<shangrice_flavor>/<database_flavor>/<database_type>')
def databasetype(shangrice_flavor,database_flavor,database_type):
    flavor = shangrice_flavor
    data = database_flavor
    datatype = database_type
    return render_template("databasetype.html", name = flavor, name2 = data, name3 = datatype )

if __name__ == "__main__":
    app.run(debug=True)


