from flask import render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.favoritos import favoritos
from flask_app.models.users import User
from flask_app.models.productos import producto



@app.route('/new/favoritos')
def new_favorito():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    return render_template('dashboard.html', user=user, )


@app.route('/create/favoritos', methods=['POST'])
def create_favorito():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/dashboard')

    favoritos.save(request.form)
    
    producto.save(request.form)

    return redirect('/dashboard')


@app.route('/edit/favoritos/<int:id>') #a través de la URL recibimos el ID de la receta
def edit_favorito(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/dashboard')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia de la receta que queremos editar


    return render_template('edit_favoritos.html', user=user)

@app.route('/update/Producto', methods=['POST'])
def update_producto():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/favoritos')

    producto.update(request.form)
    return redirect('/favoritos')


@app.route('/view/favoritos/<int:id>') #A través de la URL recibimos el ID de la receta
def show_favorito(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/favoritos')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


    

    return render_template('show_favorito.html', user=user)


@app.route('/delete/favoritos/<int:id>')
def delete_favorito(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    favoritos.delete(formulario)

    return redirect('/favoritos')

