from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import db, Restaurant, Pizza, RestaurantPizza
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  
migrate = Migrate(app, db)
db.init_app(app)  

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])


@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')

    if not name or not address:
        return jsonify({'error': 'Name and address are required'}), 400

    restaurant = Restaurant(name=name, address=address)
    db.session.add(restaurant)
    db.session.commit()

    return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address}), 201


@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404

    if request.method == 'GET':
        pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})

    if request.method == 'DELETE':
        try:
            db.session.delete(restaurant)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Cannot delete restaurant with associated pizzas'}), 400

        return '', 204



@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])


@app.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    name = data.get('name')
    ingredients = data.get('ingredients')

    if not name or not ingredients:
        return jsonify({'error': 'Name and ingredients are required'}), 400

    pizza = Pizza(name=name, ingredients=ingredients)
    db.session.add(pizza)
    db.session.commit()

    return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}), 201





@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    pizza_id = data.get('pizza_id')
    price=data.get('price')
    restaurant_id = data.get('restaurant_id')

    if pizza_id is None or restaurant_id is None:
        return jsonify({'error': 'Pizza ID and Restaurant ID are required'}), 400

    restaurant_pizza = RestaurantPizza(pizza_id=pizza_id, restaurant_id=restaurant_id, price=price)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({'message': 'RestaurantPizza created successfully'}), 201




@app.route('/restaurant_pizzas/<int:id>', methods=['DELETE'])
def delete_restaurant_pizza(id):
    restaurant_pizza = RestaurantPizza.query.get(id)
    if restaurant_pizza is None:
        return jsonify({'error': 'RestaurantPizza not found'}), 404

    try:
        db.session.delete(restaurant_pizza)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Cannot delete RestaurantPizza'}), 400

    return '', 204



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)
