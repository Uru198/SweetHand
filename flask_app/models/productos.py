
from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

import re 

class producto:

    def __init__(self, data):
        self.id = data['id']
        self.product = data['product']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    

    @staticmethod
    def valida_producto(formulario):
        es_valido = True
 

        if not re.match('[0-9]',(formulario['price'])):
            flash('El precio debe ser unicamente numeros ', 'productos')
            es_valido = False
        
        return es_valido


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO products (product, price) VALUES (%(product)s, %(price)s) "
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products"
        results = connectToMySQL('sweethand').query_db(query) #Lista de diccionarios 
        products = []
        for product in results:
            products.append(cls(product)) #1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de productss

        return products

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT products.* FROM products  WHERE products.id = %(id)s" #products
        result = connectToMySQL('sweethand').query_db(query, formulario) #Lista de diccionarios
        product = cls(result[0])
        return product

    @classmethod
    def update(cls, formulario):
        query = "UPDATE products SET product=%(product)s, price=%(price)s  WHERE id = %(id)s"
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM products WHERE id = %(id)s"
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result
    
    @classmethod
    def buscar_nombre(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "SELECT id,product,price FROM products  WHERE product like '%' %(product)s'%'"
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result
    
    @classmethod
    def favoritos(cls, formulario): #formulario = {id: 1}
        query = "SELECT product,catalog_id FROM favorites inner join products on favorites.catalog_id =  products.id where user_id = %(user_id)s" #products
        result = connectToMySQL('sweethand').query_db(query, formulario) #Lista de diccionarios
        favorite = cls(result[0])
        return favorite
    