
from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class favoritos:

    def __init__(self, data):
        
        self.catalog_id = data['catalog_id']


    @classmethod
    def save_favorito(cls, formulario):
        query = "INSERT INTO favorites (user_id, catalog_id) VALUES (%(user_id)s, %(catalog_id)s) "
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM favorites"
        results = connectToMySQL('sweethand').query_db(query) #Lista de diccionarios 
        favorites = []
        for favorite in results:
            favorites.append(cls(favorite)) #1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de productss

        return favorites

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT product,first_name,catalog_id FROM favorites inner join products on favorites.catalog_id =  products.id join users where user_id = %(user_id)s" #products
        result = connectToMySQL('sweethand').query_db(query, formulario) #Lista de diccionarios
        favorite = cls(result[0])
        return favorite


    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM favorites WHERE user_id = %(user_id)s and catalog_id = %(product)s"
        result = connectToMySQL('sweethand').query_db(query, formulario)
        return result
    
 
    
   
