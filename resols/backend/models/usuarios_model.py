from models.connection_pool import MYSQLPool
from flask import request

llave_persona = 0
llave_usuario = 0

class UsuarioModel:
    def __init__(self):
        self.mysql_pool=MYSQLPool()
    
    def get_usuarios(self):
        query=self.mysql_pool.execute("""select u.id,u.nickname,u.contraseña,ur.rol_id from usuario u
        inner join usuario_rol ur on u.id=ur.usuario_id;""")
        data =list()
        contenido=dict()
        for row in query:
            contenido={
                'id':row[0],
                'nickname':row[1],
                'contrasena':row[2],
                'rol_id':row[3]
            }
            data.append(contenido)
            contenido={}
        return data

    def post_person(self,nombre,apellido,dni,direccion):
        entrada={
            'name':nombre,
            'last_name':apellido,
            'dni':dni,
            'address':direccion
        }
        query="""insert into persona(nombres,apellidos,dni,direccion)
        values(%(name)s,%(last_name)s,%(dni)s,%(address)s);"""
        cursor=self.mysql_pool.execute(query,entrada,commit=True)
        contenido={
            'id':cursor.lastrowid,
            'nombre':entrada['name'],
            'apellidos':entrada['last_name'],
            'dni':entrada['dni'],
            'direccion':entrada['address']
        }
        global llave_persona
        llave_persona = cursor.lastrowid
        print(llave_persona,"  <--salida de persona")
        return contenido

    def post_usuarios(self,nickname,contraseña,email_user):
        fk = llave_persona
        print(llave_persona,"- --llegada")
        entrada={
            'nickname':nickname,
            'contraseña':contraseña,
            'persona_id':fk,
            'email':email_user
        }
        
        query="""insert into usuario(nickname,contraseña,persona_id,email_usuario)
        values(%(nickname)s,%(contraseña)s,%(persona_id)s,%(email)s);"""
        cursor=self.mysql_pool.execute(query,entrada,commit=True)
        contenido={
            'id':cursor.lastrowid,
            'nickname':entrada['nickname'],
            'contraseña':entrada['contraseña'],
            'persona_id':entrada['persona_id'],
            'email':entrada['email']
        }
        global llave_usuario
        llave_usuario = cursor.lastrowid
        print("salida user",llave_usuario)
        return contenido
    
    def post_rol_user(self,rol):
        fk = llave_usuario
        print("llegada rol-usuario-->",fk)
        entrada={
            'usuario_id':fk,
            'rol_id':rol
        }
        query="""insert into usuario_rol(usuario_id,rol_id)
        values(%(usuario_id)s,%(rol_id)s);"""
        cursor=self.mysql_pool.execute(query,entrada,commit=True)

    def get_usuarios_dos(self):
        query=self.mysql_pool.execute("""select u.id,u.nickname,u.email_usuario,p.nombres,p.apellidos from usuario u
        inner join persona p on u.persona_id=p.id;""")

        data =list()
        contenido=dict()
        for row in query:
            contenido={
                'id':row[0],
                'nickname':row[1],
                'email_usuario':row[2],
                'nombres':row[3],
                'apellidos':row[4]
            }
            data.append(contenido)
            contenido={}
        return data
    
    def post_login(self,nickname,contrasena):
        query =self.mysql_pool.execute('select u.id,u.nickname,u.contraseña,ur.rol_id from usuario u inner join usuario_rol ur on u.id=ur.usuario_id where u.nickname="'+str(nickname)+'"'+' and u.contraseña="'+str(contrasena)+'"')
        contenido=dict()
        if query:
            contenido={
                'nickname':query[0][1],
                'rol':query[0][3],
                'message':'ok'
            }
        else:
            contenido={
                'message':'incorrecto'
            }

        return contenido
    

if __name__=="__main__":
    usuario_model=UsuarioModel()
