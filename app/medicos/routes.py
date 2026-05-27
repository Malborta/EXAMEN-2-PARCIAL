from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Medico
from app.extensions import db

bp_medicos = Blueprint('medicos', __name__)

# LISTAR MEDICOS
@bp_medicos.route('/')
def lista():

    medicos = Medico.query.all()

    return render_template(
        'medicos/lista.html',
        medicos=medicos
    )


# CREAR MEDICO
@bp_medicos.route('/crear', methods=['GET', 'POST'])
def crear():

    if request.method == 'POST':

        nuevo = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad']
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for('medicos.lista'))

    return render_template('medicos/crear.html')


# EDITAR MEDICO
@bp_medicos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    medico = Medico.query.get_or_404(id)

    if request.method == 'POST':

        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']

        db.session.commit()

        return redirect(url_for('medicos.lista'))

    return render_template(
        'medicos/editar.html',
        medico=medico
    )


# ELIMINAR MEDICO
@bp_medicos.route('/eliminar/<int:id>')
def eliminar(id):

    medico = Medico.query.get_or_404(id)

    db.session.delete(medico)
    db.session.commit()

    return redirect(url_for('medicos.lista'))