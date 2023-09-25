from app import db
from models import Pizza, Restaurant

# Function to create pizzas and restaurants
def create_seed_data():
    # Create pizzas
    margarita = Pizza(name="Margarita", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Create restaurants
    pizza_palace = Restaurant(name="Pizza Palace", address="123 Main St")
    dominion_pizza = Restaurant(name="Dominion Pizza", address="456 Elm St")

    # Add pizzas and restaurants to the session
    db.session.add_all([margarita, pepperoni, pizza_palace, dominion_pizza])

    # Commit the changes to the database
    db.session.commit()

if __name__ == "__main__":
    # Initialize the Flask app and database
    from app import app
    app.app_context().push()
    db.create_all()

    # Call the function to create seed data
    create_seed_data()

    print("Seed data created successfully.")