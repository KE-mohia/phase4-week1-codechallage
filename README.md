# Pizza Restaurant API

## Description

The Pizza Restaurant API is a Flask-based web service that allows users to manage pizza restaurants, their menus, and create associations between restaurants and pizzas. This API is designed to handle CRUD (Create, Read, Update, Delete) operations for restaurants, pizzas, and restaurant-pizza relationships.

## Project Setup

### Prerequisites

- Python 3.10.12
- Virtual environment (optional but recommended)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/pizza-restaurant-api.git
Navigate to the project directory:

cd pizza-restaurant-api
Create and activate a virtual environment (optional):

pipenv install && pipenv shell

Install the required dependencies:

Get the required dependancies in the Pipfile
Configure the database URI in app.py (e.g., SQLite or other preferred database).

Initialize the database and apply migrations:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Usage
Start the Flask server:

 flask run

# Endpoints
GET /restaurants: Retrieve a list of restaurants.
GET /restaurants/:id: Retrieve a restaurant by ID along with its pizzas.
DELETE /restaurants/:id: Delete a restaurant and its associated RestaurantPizzas.
GET /pizzas: Retrieve a list of pizzas.
POST /restaurant_pizzas: Create a new RestaurantPizza.

# Author
Wayne keya 

# License
MIT License

Copyright (c) [2023] [wayne keya ]

Permission is hereby granted,free of charge , for any person obtaining a copy of this software and associated documentation files(the "software"),to deal in the Software without restriction ,including without limitaion the rights to use,copy,modify,merge,publish,distribute,sublicense,and/or sell copies of the Software ,and to permit persons to whom the Software is furnished to do so,subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the software.

THE SOFTWAREBIS PROVIDED "AS IS",WITHOUT WARRANTY OF ANY KIND ,EXPRESS OR IMPLIED ,INCUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY ,FITNESS FOR A PURPOSE AND NONIINFRINGEMENT.IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,DAMAGES OR OTHER LIABILITIES,WHETHER IN AN ACTION OF CONTRACT TORT OR OTHERWISE ,ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR USE OTHER DEALINGS IN THE SOFTWARE.