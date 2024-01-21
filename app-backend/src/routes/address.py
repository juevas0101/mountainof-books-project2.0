from flask import Blueprint, jsonify, request
from ..models import Address, db

address_blueprint = Blueprint('address', __name__, url_prefix='/adddress')

def serialize_address(address):
    return {
        'nome_da_rua': address.nome_da_rua,
        'numero': address.numero,
        'CEP': address.CEP,
        'complemento': address.complemento
    }

@address_blueprint.route('/detail_info_customer', methods=['GET', 'POST'])
def create_address():
    try:
        if request.method == 'GET':
            addresses = Address.query.all()
            addresses_data = [serialize_address(address) for address in addresses]
            return jsonify(address=addresses_data)
        
        elif request.method == 'POST':
            data = request.get_json()
            fields_data = ['nome_da_rua', 'numero', 'CEP', 'complemento']

            address_data = {field: data.get(field) for field in fields_data}
            new_address = Address(**address_data)

            db.session.add(new_address)
            db.session.commit()
        
        return jsonify(message='endereço ok', address=serialize_address(new_address)), 201
    
    except Exception as e:
        return jsonify(error=str(e)), 500
