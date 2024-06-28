from flask import Blueprint, request, jsonify
from . import db
from .models import Product

main = Blueprint('main', __name__)

@main.route('/home', methods=['GET'])
def home():
    return jsonify({'message': 'Bienvenido a la API de Productos'})

@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'rating': product.rating
    } for product in products]

    return jsonify({'products': product_list})

@main.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data['description'], price=data['price'], rating=data['rating'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Producto agregado exitosamente!'}), 201

