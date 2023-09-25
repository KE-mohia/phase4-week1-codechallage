# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza_restaurant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for better performance
