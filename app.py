from flask import Flask

#Crear instancia
app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola mundo'
    
@app.route('/alumnos')
def getAlumnos():
    return 'Aqui van los alumnos'

if __name__ == '__main__':
    app.run(debug=True)
