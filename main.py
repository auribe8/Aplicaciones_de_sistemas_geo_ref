from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    edad = 18
    users = ['pepe','juan','miguel']
    return render_template('index.html', edad=edad, users=users)

@app.route('/proyectos')
@app.route('/proyectos/<string:nombre>/<int:edad>')
def proyectos(nombre=None,edad=None):
    if nombre is None:
        return render_template('proyectos.html')
    else:
        return render_template('proyectos.html',edad=edad,nombre=nombre)
    

@app.route('/loops')
def loops():
    lista = ['Frutas','Verduras','Limpieza','Abarrotes']
    return render_template('loops.html',lista = lista)

@app.route('/mapa/<float:lat>/<float(signed=True):long>/<string:nombre>',methods=['GET'])
def mapa(lat,long,nombre):
    markers=[
   {
   'lat':lat,
   'lon':long,
   'popup':nombre
    }
   ]
    return render_template('mapa.html',lat=lat,long=long,markers=markers)