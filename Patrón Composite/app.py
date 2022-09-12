from flask import Flask, jsonify, request

app = Flask(__name__)

from users import users


@app.route('/users')
def getUser():
    return jsonify({'users': users})


@app.route('/users/<string:user_name>')
def getUser(user_name):
    userFound = [user for user in users if user['name'] == user_name]
    if len(userFound) > 0:
        return jsonify({"user": userFound[0]})
    return jsonify({"message": "Usuario inexistente"})


@app.route('/users', methods=['POST'])
def addUser():
    new_user = {
        "nombre": request.json['nombre'],
        "telefono": request.json['telefono'],
        "edad": request.json['edad'],
    }
    users.append(new_user)
    return jsonify({"message":"usuario agregado con exito", "users":users})


@app.route('/users/<string:user_name>',methods=['PUT'])
def editUser(user_name):
    userFound = [user for user in users if user['name'] == user_name]
    if len(userFound)>0:
        userFound[0]['nombre']=request.json['nombre']
        userFound[0]['telefono'] = request.json['telefono']
        userFound[0]['email'] = request.json['email']
        return jsonify({"menssage":"usuario cargado","user":userFound[0]})
    return jsonify({"menssage":"usuario no encontrado"})

@app.route('/users/<string:user_name>',methods=['DELETE'])
def deletetUser(user_name):
    userFound = [user for user in users if user['name'] == user_name]
    if len(userFound)>0:
        users.remove(userFound[0])
        return jsonify({"menssage":"usuario eliminado","users":users})

if __name__ == 'main':
    app.run(debug=True, port=4000)