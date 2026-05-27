from app.extensions import db


class Medico(db.Model):

    __tablename__ = 'medico'

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    especialidad = db.Column(
        db.String(100),
        nullable=False
    )

    citas = db.relationship(
        'Cita',
        backref='medico',
        lazy=True
    )


class Paciente(db.Model):

    __tablename__ = 'paciente'

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    telefono = db.Column(
        db.String(20),
        nullable=False
    )

    citas = db.relationship(
        'Cita',
        backref='paciente',
        lazy=True
    )


class Cita(db.Model):

    __tablename__ = 'cita'

    id = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(
        db.String(20),
        nullable=False
    )

    hora = db.Column(
        db.String(20),
        nullable=False
    )

    medico_id = db.Column(
        db.Integer,
        db.ForeignKey('medico.id'),
        nullable=False
    )

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey('paciente.id'),
        nullable=False
    )