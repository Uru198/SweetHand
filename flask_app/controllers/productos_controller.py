from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.productos import producto




@app.route('/new/producto')
def new_producto():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    return render_template('new_producto.html', user=user)


@app.route('/create/producto', methods=['POST'])
def create_producto():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/producto')

    if not producto.valida_producto(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/new/producto')

    producto.save(request.form)

    return redirect('/producto')


@app.route('/edit/producto/<int:id>') #a través de la URL recibimos el ID de la receta
def edit_producto(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/producto')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia de la receta que queremos editar
    formulario_producto = {"id": id}
    productos = producto.get_by_id(formulario_producto)

    return render_template('edit_producto.html', user=user, productos=productos)

@app.route('/update/Producto', methods=['POST'])
def update_producto():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/producto')
    
    if not producto.valida_producto(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/edit/producto/'+request.form['id'])
    
    producto.update(request.form)
    return redirect('/producto')

@app.route('/view/producto/<int:id>') #A través de la URL recibimos el ID de la receta
def show_producto(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/producto')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


    formulario_producto = { "id": id }
    #llamar a una función y debo de recibir la receta
    Producto = producto.get_by_id(formulario_producto)

    return render_template('show_produ_user.html', user=user, producto=Producto)

@app.route('/producto') #A través de la URL recibimos el ID de la receta
def show_all_products():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


  
    #llamar a una función y debo de recibir la receta
    Productos = producto.get_all()

    return render_template('productos.html', user=user, productos=Productos)

@app.route('/delete/producto/<int:id>')
def delete_producto(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    producto.delete(formulario)

    return redirect('/producto')