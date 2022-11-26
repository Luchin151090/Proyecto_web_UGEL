from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin


#importamos las clases models
from models.resolucion_model import ResolucionModel
model_re = ResolucionModel()

from models.usuarios_model import UsuarioModel
model_user = UsuarioModel() 



#decoradores para los endpoints
blue_print = Blueprint('blue_print',__name__)

# ENDPOINTS DOCUMENTOS
@blue_print.route('/resolucion/cantidad',methods=['GET'])
@cross_origin()
def get_cantidad():
    content = model_re.get_cantidad()
    return jsonify(content)


@blue_print.route('/upload_file/<int:id>',methods=['POST'])
@cross_origin()
def post_file(id):
    content = model_re.upload_file(id)
    return jsonify(content)

@blue_print.route('/download_file/<int:id>',methods=['GET'])
@cross_origin()
def get_file(id):
    content = model_re.download_file(id)
    return content

@blue_print.route('/resolucion/top',methods=['GET'])
@cross_origin()
def get_top():
    content = model_re.get_top5()
    return jsonify(content)

@blue_print.route('/resolucion/distritos',methods=['GET'])
@cross_origin()
def get_distrito_register():
    content = model_re.get_file_distrito()
    return jsonify(content)

@blue_print.route('/resolucion/monto',methods=['GET'])
@cross_origin()
def get_monto():
    content = model_re.get_monto()
    return jsonify(content)


@blue_print.route('/resolucion/last_register',methods=['GET'])
@cross_origin()
def get_last():
    content = model_re.get_last()
    return jsonify(content)


@blue_print.route('/resolucion/',methods=['GET'])
@blue_print.route('/resolucion/<codigo>',methods=['GET'])
@cross_origin()
def get_resolucion(codigo=None):
    content = model_re.get_resolucion(codigo)
    return jsonify(content)

@blue_print.route('/create/resolucion',methods=['POST'])
@cross_origin()
def post_resolucion():
    content = model_re.post_resolucion(
        request.json['nproyecto'],
        request.json['Femision'],
        request.json['Fnotificacion'],
        request.json['concepto'],
        request.json['descripcion'],
        request.json['distrito'],
        request.json['monto'],
        request.json['tipo_id']

    )
    return jsonify(content)

@blue_print.route('/update/resolucion/<int:id>',methods=['PUT'])
@cross_origin()
def put_resolucion(id):
    content = model_re.put_resolucion(id)
    return jsonify(content)

@blue_print.route('/delete/resolucion/<int:id>',methods=['DELETE'])
@cross_origin()
def delete_resolucion(id):
    content=model_re.delete_resolucion(id)
    return jsonify(content)


# ENDPOINTS USUARIOS
@blue_print.route('/usuarios',methods=['GET'])
@cross_origin()
def get_usuarios():
    content=model_user.get_usuarios()
    return jsonify(content)

@blue_print.route('/usuarios_control',methods=['GET'])
@cross_origin()
def get_usuarios_control():
    content=model_user.get_usuarios_dos()
    return jsonify(content)

@blue_print.route('/login',methods=['POST'])
@cross_origin()
def post_login():
    content=model_user.post_login(
        request.json['nickname'],
        request.json['contraseña']
    )
    return jsonify(content)

@blue_print.route('/create/person',methods=['POST'])
@cross_origin()
def post_person():
    content = model_user.post_person(
        request.json['nombre'],
        request.json['apellido'],
        request.json['dni'],
        request.json['direccion']
    )
    return jsonify(content)

@blue_print.route('/create/user',methods=['POST'])
@cross_origin()
def post_user():
    content=model_user.post_usuarios(
        request.json['nickname'],
        request.json['contraseña'],
        request.json['email_user']
    )
    return jsonify(content)

@blue_print.route('/create/rol_user',methods=['POST'])
@cross_origin()
def post_rol_user():
    content=model_user.post_rol_user(
        request.json['rol_id']
    )
    return jsonify(content)