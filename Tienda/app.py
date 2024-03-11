from flask import Flask, render_template
from Conexion_Bd import conectar

app = Flask(__name__)

# Configura la conexión a la base de datos
conn = conectar()

@app.route('/')
def index():
    # Consulta todos los productos desde la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Productos')
    productos = cursor.fetchall()
    cursor.close()
    
    # Renderiza la plantilla HTML y pasa los productos como argumento
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
