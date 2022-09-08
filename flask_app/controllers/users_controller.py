from email import message
from itertools import product
import json
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

from flask_app.models.productos import producto
from flask_app.models.favoritos import favoritos

#Importación del modelo
from flask_app.models.users import User
#from flask_app.models.recipes import Recipe

#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/producto')
def productos():
    return render_template('productos.html')

@app.route('/compras')
def compras():
    return render_template('/dashboardClientesCompras.html')


@app.route('/favoritos')
def favorito():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


  
    #llamar a una función y debo de recibir la receta
    Productos = producto.get_all()
    
        
    favorito = favoritos.get_all()
       

    return render_template('favoritos.html', user=user, productos=Productos, favorito=favorito)

@app.route('/favoritosClientes')
def favorito_cliente():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

  
    #llamar a una función y debo de recibir la receta
    Productos = producto.get_all()
    
    

    return render_template('favoritos_Clientes.html', user=user, productos=Productos)




@app.route('/catalogo')
def show_all_products_in_users():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) 

    Productos = producto.get_all()

    return render_template('Catalogo.html', user=user, productos=Productos)

@app.route('/registrate', methods=['POST'])
def registrate():
    if not User.valida_usuario(request.form):
        return redirect('/registro')
  

    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "address": request.form['address'],
        "phone": request.form['phone'],
        "password": pwd,
        "rol": request.form['rol']
    }

  #request.form = FORMULARIO HTML
    id = User.save(formulario) #recibo el identificador de mi nuevo usuario
    
    session['user_id'] = id
    
    
    return redirect('/dashboard')

@app.route('/favoritosguarda', methods=['POST'])
def favorito_guarda():
    

    favoritos.save_favorito(request.form)
    favoritos.get_all()
    favoritos.get_by_id(request.form)

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    #Verificar que el email EXISTA
    #request.form RECIBIMOS DE HTML
    #request.form = {email: elena@cd.com, password: 123}
    user = User.get_by_email(request.form) #Recibiendo una instancia de usuario o Falso

    if not user:
        flash('E-mail no encontrado', 'login')
        return redirect('/')
   

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')
        

    session['user_id'] = user.id

    return redirect('/dashboard')



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    
    users = User.get_all()
    
    #recipes = Recipe.get_all()

    return render_template('dashboard.html', user=user, users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/update', methods=['POST']) #/delete/1
def update(): #id = 1
    User.actualizar(request.form)
    return redirect('/dashboard')

@app.route('/edit/<int:id>') #/delete/1
def edit(id): #id = 1
    data = { #formulario = {"id":1}
        "id": id
    }
    user = User.buscar_usuario(data)
    print(user)
    return render_template('edit_perfil.html', user=user)

@app.route('/view/user/<int:id>') #A través de la URL recibimos el ID de la receta
def show_usuario(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/dashboard')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    return render_template('show_usuario.html', user=user)

@app.route('/delete/<int:id>') #/delete/1
def delete(id): #id = 1
    formulario = { #formulario = {"id":1}
        "id": id
    }
    User.borrar(formulario)
    return redirect('/')


