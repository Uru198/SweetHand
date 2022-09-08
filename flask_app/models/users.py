from asyncio.windows_events import NULL
from flask_app.config.mysqlconnection import  connectToMySQL

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.address = data['address']
        self.phone = data['phone']
        self.password = data['password']
        self.rol = data['rol']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email, address, phone, password, rol) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(address)s, %(phone)s, %(password)s, %(rol)s)"
        result = connectToMySQL('sweethand').query_db(query, formulario) #me regresan el nuevo ID de la persona registrada
        return result

    @staticmethod
    def valida_usuario(formulario):
        #formulario = { DICCIONARIO
        #   first_name = "Elena",    
        #   last_name = "De Troya",    
        #   email = "elena@codingdojo.com",    
        #   password = "123",    
        #   confirm_password = "234",    
        #}
        es_valido = True
        
        if len(formulario['first_name']) < 3:
            flash("Nombre debe de tener almenos 3 caracteres", "registro1")
            es_valido = False
            
        if len(formulario['last_name']) < 3:
            flash("Apellido debe de tener almenos 3 caracteres", "registro2")
            es_valido = False
            
        #verificar que el email tenga el formato correcto - EXPRESIONES REGULARES
        if not EMAIL_REGEX.match(formulario['email']):
            flash("E-mail invalido", "registro3")
            es_valido = False
            
        if not re.search('[#]',formulario['address']):
            flash("Su direccion debe contener este simbolo #", "registro4")
            es_valido = False      
            
        if len(formulario['phone']) != 10:
            flash("Su telefono debe tener 10 numeros", "registro5")
            es_valido = False 
            
        #Password con al menos 6 caracteres
        if len(formulario['password']) < 6:
            flash("contraseña debe tener al menos 6 caracteres", "registro6")
            es_valido = False
            
        if formulario['password'] != formulario['confirmar_password']:
            flash('Contraseñas no coinciden', 'registro7')
            es_valido = False
            
        #consultar si ya existe ese correo electronico
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('sweethand').query_db(query, formulario)
        if len(result) >= 1:
            flash("E-mail registrado previamente", "registro8")
            es_valido = False
            
            
        return es_valido
        


    @classmethod
    def get_by_email(cls, formulario):
        #formulario = {
        #      email: elena@cd.com
        #      password: 123
        #}
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('sweethand').query_db(query, formulario) #Los SELECT regresan una lista
        if len(result) < 1: #NO existe registro con ese correo
            #result = []
            return False
        else:
            #result = [
            #    {id: 1, first_name: elena, last_name:de troya.....} -> POSICION 0
            #]
            user = cls(result[0])  #User({id: 1, first_name: elena, last_name:de troya.....})
            return user
    
    @classmethod
    def get_by_id(cls, formulario):
        #formulario = {id: 4}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('sweethand').query_db(query, formulario) #RECIBIMOS UNA LISTA
        print(result)
        user = cls(result[0]) #creamos una instancia de usuario
        return user
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('sweethand').query_db(query)#Regresa una lista de diccionarios
        users = []
        for us in results:
            users.append(cls(us))#1 - cls(us) creando una instancia de user. 2- esa instancia la agrego a la lista de 
            
        return users      
    
    @classmethod
    def actualizar(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, address =  %(address)s, phone =  %(phone)s  WHERE id = %(id)s"
        result = connectToMySQL('sweethand').query_db(query, data)
        return result  
    
    @classmethod
    def buscar_usuario(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return cls(result[0])
    
    @classmethod
    def borrar(cls, formulario):
        #formulario = {id: "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        #DELETE FROM users WHERE id = 1
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result
    
    
    
    