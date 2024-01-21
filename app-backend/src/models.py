from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

customer_address = db.Table('customer_address',
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'))
)

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    address = db.relationship('Address', secondary=customer_address, backref='address_detail')

class Address(db.Model):
    __tablename__='address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_da_rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    CEP = db.Column(db.String(12), nullable=False)
    complemento = db.Column(db.String(30), nullable=False)
    