from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Paciente
from app.extensions import db

bp_pacientes = Blueprint('pacientes', __name__)

# LISTAR
@bp_pacientes.route('/')
def lista():

    pacientes = Paciente.query.all()

    return render_template(
        'pacientes/lista.html',
        pacientes=pacientes
    )

# CREAR
@bp_pacientes.route('/crear', methods=['GET', 'POST'])
def crear():

    if request.method == 'POST':

        nuevo = Paciente(
            nombre=request.form['nombre'],
            telefono=request.form['telefono']
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for('pacientes.lista'))

    return render_template('pacientes/crear.html')

# EDITAR
@bp_pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    paciente = Paciente.query.get_or_404(id)

    if request.method == 'POST':

        paciente.nombre = request.form['nombre']
        paciente.telefono = request.form['telefono']

        db.session.commit()

        return redirect(url_for('pacientes.lista'))

    return render_template(
        'pacientes/editar.html',
        paciente=paciente
    )

# ELIMINAR
@bp_pacientes.route('/eliminar/<int:id>')
def eliminar(id):

    paciente = Paciente.query.get_or_404(id)

    db.session.delete(paciente)
    db.session.commit()

    return redirect(url_for('pacientes.lista'))