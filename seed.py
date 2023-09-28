from app import db
from models import Pizza, Restaurant

# Function to create pizzas and restaurants
def create_seed_data():
    # Create pizzas
   
    periperi= Pizza(name="periperi", ingredients="Dough, Cheese, chicken Bacon")
    hawaaian=Pizza(name="Hawaaian", ingredients="Dough, cheese, bacon, pineapples")
   

    # Create restaurants
    pizza_palace = Restaurant(name="Pizza Palace", address="123 Main St")
    
    pizza_inn = Restaurant(name="Pizza inn", address="Moi ave")

    # Add pizzas and restaurants to the session
    db.session.add_all([ periperi, hawaaian, pizza_palace, pizza_inn])

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