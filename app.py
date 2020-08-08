from flask import Flask, jsonify, request

app = Flask(__name__)


from productos import productos


#Probar nuestro servidor
@app.route('/ping', methods = ['GET'])
def iniciar():
	return jsonify({"message": "pong!"})

#Traer productos
@app.route('/productos', methods = ['GET'])
def getProductos():
	return jsonify({"productos" : productos, "message": "Lista de productos"})

#Traer un unico producto
@app.route('/productos/<string:nombre_producto>')
def getProducto(nombre_producto):
	producto_encontrado = [producto for producto in productos if producto['nombre']== nombre_producto]
	if len(producto_encontrado) == 0:
		return jsonify({"message":"producto no encontrado"})
	return jsonify({"producto": producto_encontrado[0]})

#Guardar productos
@app.route('/productos', methods = ['POST'])
def agregarProducto():
	nuevo_producto = {
		"nombre": request.json['nombre'],
		"precio": request.json['precio'],
		"cantidad" : request.json['cantidad']
	}
	productos.append(nuevo_producto)
	print(productos)
	return jsonify({"messaje" : "agregado correctamente", "productos": productos})

#Modificar producto
@app.route('/productos/<string:nombre_producto>', methods = ['PUT'])
def editarProducto(nombre_producto):
	producto_encontrado = [producto for producto in productos if producto['nombre'] == nombre_producto]
	if len(producto_encontrado) == 0:
		return jsonify({"message":"producto no encontrado"})
	else:
		producto_encontrado[0]['nombre'] = request.json['nombre']
		producto_encontrado[0]['cantidad'] = request.json['cantidad']
		producto_encontrado[0]['precio'] = request.json['precio']
		return jsonify({
			"message":"producto actualizado",
			"producto": producto_encontrado[0]
			})

#Eliminar producto
@app.route('/productos/<nombre_producto>', methods = ['DELETE'])
def borrarProducto(nombre_producto):
	producto_encontrado = [producto for producto in productos if producto['nombre'] == nombre_producto]
	if len(producto_encontrado) == 0:
		return jsonify({"message":"producto no encontrado"})
	productos.remove(producto_encontrado[0])
	return jsonify({"productos": productos})

if __name__ == '__main__':
	app.run(debug = True, port = 4000)

