#!/usr/bin/env python3

from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize database and migration tools
migrate = Migrate(app, db)
db.init_app(app)

# Initialize Flask-RESTful Api
api = Api(app)

# Routes
@app.route('/')
def index():
    return '<h1>Code Challenge: Pizza Restaurants API</h1>'

# RESTful Resources
class RestaurantsResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        return jsonify([restaurant.to_dict() for restaurant in restaurants])

class RestaurantDetailResource(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)
        restaurant_data = restaurant.to_dict()
        restaurant_data['restaurant_pizzas'] = [rp.to_dict() for rp in restaurant.restaurant_pizzas]
        return jsonify(restaurant_data)

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)
        db.session.delete(restaurant)
        db.session.commit()
        return make_response('', 204)

class PizzasResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        return jsonify([pizza.to_dict() for pizza in pizzas])

class RestaurantPizzaResource(Resource):
    def post(self):
        data = request.get_json()

        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not price or not pizza_id or not restaurant_id:
            return make_response(jsonify({"errors": ["Missing data"]}), 400)

        # Check if the pizza and restaurant exist
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        if not pizza or not restaurant:
            return make_response(jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 400)

        try:
            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
            db.session.add(restaurant_pizza)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({"errors": [str(e)]}), 400)

        return make_response(jsonify(restaurant_pizza.to_dict()), 201)

# Register API resource endpoints
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantDetailResource, '/restaurants/<int:id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzaResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)