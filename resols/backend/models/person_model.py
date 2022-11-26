from models.connection_pool import MYSQLPool
from flask import request

llave_persona = 0
class PersonModel:
    def __init__(self):
        self.mysql_pool=MYSQLPool()
    
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

    def delete_person(self):
        pass

if __name__=="__main__":
    person_model = PersonModel()