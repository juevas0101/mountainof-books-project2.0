from flask import Blueprint, jsonify, request
from datetime import datetime
from ..models import Customer, db

customer_blueprint = Blueprint('customer', __name__, url_prefix='/customer')

def serialize_customer(customer):
    return {
        'nome': customer.nome,
        'sobrenome': customer.sobrenome,
        'nascimento': customer.nascimento,
        'email': customer.email,
        'password': customer.password,
        'telefone': customer.telefone
    }

@customer_blueprint.route('/singup', methods = ['GET', 'POST'])
def create_customer():
    try:
        if request.method == 'GET':
            customers = Customer.query.all()
            customers_data = [serialize_customer(customer) for customer in customers]
            return jsonify(customers=customers_data)

        elif request.method == 'POST':
            data = request.get_json()
            fields_data = ['nome', 'sobrenome', 'nascimento', 'email', 'password', 'telefone']

            data['nascimento'] = datetime.strptime(data['nascimento'], '%Y-%m-%d').date()

            customer_data = {field: data.get(field) for field in fields_data}
            new_customer = Customer(**customer_data)

            db.session.add(new_customer)
            db.session.commit()

            return jsonify(message='Cliente criado com sucesso', customer=serialize_customer(new_customer)), 201

    except Exception as e:
        return jsonify(error=str(e)), 500
