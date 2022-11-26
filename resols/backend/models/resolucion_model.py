from models.connection_pool import MYSQLPool
from flask import request
from flask import render_template
from flask import send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os.path
import pathlib


class ResolucionModel:
    def __init__(self):
        self.mysql_pool=MYSQLPool()
    
    def tipo_resolucion(self):
        pass

    def get_cantidad(self):
        query=self.mysql_pool.execute('select * from documento;')
        tamanio=len(query)
        return tamanio

 
    def upload_file(self,id):
        if request.method == 'POST':
            directory = 'D:/Luchin/myweb/resols/backend/archivos/'

            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(os.path.join(directory,filename))

            archivo = directory+f.filename
            query = "update documento set archivo ='"+archivo+"'"+" where id="+str(id)+";"
            cursor=self.mysql_pool.execute(query,commit=True)
            # esta función guarda directamente en la carpeta que se ejecuta
            # el backend
            #f.save(secure_filename(f.filename))

            print(f.filename)
            print(type(f.filename))
            print(directory+f.filename)
            print(archivo)
            print(type(archivo))
            return 'file uploaded successfully'
    
    def download_file(self,id):
        query = self.mysql_pool.execute('select archivo from documento where id='+str(id))
        path = query[0][0]

        
        print(path)
        print(type(path))
        
        return send_file(path,as_attachment=True)


    def get_file_distrito(self):
        query=self.mysql_pool.execute('select count(*),distrito from documento group by distrito;')
        data=list()
        contenido=dict()
        for row in query:
                contenido={
                        'cantidad':row[0],
                        'distrito':row[1],
                    }
                data.append(contenido)
                contenido={}
                
        return data

    def get_top5(self):
        query=self.mysql_pool.execute('select * from documento order by id desc limit 5;')
        data=list()
        contenido=dict()
        for row in query:
            contenido={
                    'id':row[0],
                    'nproyecto':row[1],
                    'Femision':row[2],
                    'Fnotificacion':row[3],
                    'concepto':row[4],
                    'descripcion':row[5],
                    'distrito':row[6],
                    'monto':row[7]
                }
            data.append(contenido)
            contenido={}
                
        return data

    def get_last(self):
        query=self.mysql_pool.execute('SELECT * from documento order by id desc limit 1;')
        data=list()
        contenido=dict()
        for row in query:
            contenido={
                    'id':row[0],
                    'nproyecto':row[1],
                    'Femision':row[2],
                    'Fnotificacion':row[3],
                    'concepto':row[4],
                    'descripcion':row[5],
                    'distrito':row[6],
                    'monto':row[7]
                }
            data.append(contenido)
            contenido={}
             
        return data

    def get_monto(self):
        query=self.mysql_pool.execute('select round(sum(monto),2) from documento;')
        data=list()
        contenido=dict()
        for row in query:
            contenido={
                    'total':row[0]
                }
            data.append(contenido)
            contenido={}
             
        return data

    def get_resolucion(self,code):
        if code!=None:
            query=self.mysql_pool.execute('select * from documento where nproyecto="'+str(code)+'"'+";")
            #query2=self.mysql_pool.execute("select a.archivo from resolucion r inner join archivo a on r.id=a.codigo where r.codigo="+str(code)+";")
            data=list()
            contenido=dict()
           
            for row in query:
                contenido={
                    'id':row[0],
                    'nproyecto':row[1],
                    'Femision':row[2],
                    'Fnotificacion':row[3],
                    'concepto':row[4],
                    'descripcion':row[5],
                    'distrito':row[6],
                    'monto':row[7]
                }
                data.append(contenido)
                contenido={}
             
            return data
        else:
            query=self.mysql_pool.execute('select * from documento;')
            data=list()
            contenido=dict()
            for row in query:
                contenido={
                    'id':row[0],
                    'nproyecto':row[1],
                    'Femision':row[2],
                    'Fnotificacion':row[3],
                    'concepto':row[4],
                    'descripcion':row[5],
                    'distrito':row[6],
                    'monto':row[7]
                }
                data.append(contenido)
                contenido={}
                   
            return data
    
    def post_resolucion(self,nproyecto,fecha_emision,fecha_notificacion,concepto,descripcion,distrito,monto,tipo_id):
        entrada={
            'np':nproyecto,
            'fe':fecha_emision,
            'fn':fecha_notificacion,
            'conpto':concepto,
            'desc':descripcion,
            'dis':distrito,
            'monto':monto,
            'tipo_id':tipo_id

        }
        query="insert into documento(nproyecto,fecha_emision,fecha_notificacion,concepto,descripcion,distrito,monto,tipo_id)values(%(np)s,%(fe)s,%(fn)s,%(conpto)s,%(desc)s,%(dis)s,%(monto)s,%(tipo_id)s);"
        cursor=self.mysql_pool.execute(query,entrada,commit=True)
        contenido = {
            'id':cursor.lastrowid,
            'np':entrada['np'],
            'fe':entrada['fe'],
            'fn':entrada['fn'],
            'conpto':entrada['conpto'],
            'desc':entrada['desc'],
            'dis':entrada['dis'],
            'monto':entrada['monto'],
            'tipo_id':entrada['tipo_id']

        }
        print(contenido['np'])
        return contenido

    def put_resolucion(self,id):
        enter ={
            'np':request.json['nproyecto'],
            'fe':request.json['Femision'],
            'fn':request.json['Fnotificacion'],
            'cp':request.json['concepto'],
            'de':request.json['descripcion'],
            'di':request.json['distrito'],
            'monto':request.json['monto']
        }
        query = "update documento set nproyecto=%(np)s,fecha_emision=%(fe)s,fecha_notificacion=%(fn)s,concepto=%(cp)s,descripcion=%(de)s,distrito=%(di)s,monto=%(monto)s where id="+str(id)+";"
        cursor = self.mysql_pool.execute(query,enter,commit=True)
        salida={
            'mensaje':'actualizado'
        }
        return salida
    

    def delete_resolucion(self,id):
        query= self.mysql_pool.execute('delete from documento where id ='+str(id)+';')
        contenido={
            'mensaje':'resolucion eliminada'
        }
        
        return contenido


if __name__=="__main__":
    resolucion_model=ResolucionModel()