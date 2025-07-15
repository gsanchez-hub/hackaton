from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route('/productos', methods=['GET'])
def get_productos():
    productos = [
        {"id": 1, "nombre": "Producto A", "precio": 10.0},
        {"id": 2, "nombre": "Producto B", "precio": 20.0}
    ]
    return jsonify(productos)
 
if __name__ == '__main__':
    app.run(debug=True)