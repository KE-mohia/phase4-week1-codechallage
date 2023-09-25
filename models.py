# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.schema import CheckConstraint

db = SQLAlchemy()

# Define RestaurantPizza model with validations
class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    # Define the check constraint for price
    _table_args_ = (CheckConstraint('price >= 1 AND price <= 30'),)

# Define Restaurant model with validations
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

# Define Pizza model
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

# Define the association table for RestaurantPizza
restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'), primary_key=True),
    extend_existing=True  # Place this argument before the column definitions
)
