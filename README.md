# Pizza Restaurants API

# Author
Neema Naledi

## Description
This is a Flask API for managing pizza restaurants and their associated pizzas. The API allows users to retrieve, create, and delete restaurant and pizza data.

## Getting Started

### Prerequisites
- Python 3
- Node.js (for the frontend)
- Flask
- Flask-SQLAlchemy

### Installation
1. Clone this repository:
   ```bash
   git clone git@github.com:veenaledi/Challenge-4-pizza.git
  
  Navigate to the project directory: cd code-challenge

2. Install dependencies and activate the virtual environment:
    ```bash
    pipenv install
    pipenv shell
    npm install --prefix client
    ```
3. Initialize and upgrade the database:
    ```bash
    export FLASK_APP=server/app.py
    flask db init
    flask db upgrade head
    python server/seed.py
    ```
4. Run the Flask API:
    ```bash
    python server/app.py
    ```
5. Run the React app:
    ```bash
    npm start --prefix client
    ```

## API Endpoints
GET /restaurants - Get a list of all restaurants.
GET /restaurants/<int:id> - Get a specific restaurant by ID.
DELETE /restaurants/<int:id> - Delete a specific restaurant by ID.
GET /pizzas - Get a list of all pizzas.
POST /restaurant_pizzas - Create a new restaurant-pizza association.


## Usage
1. To use this project, instantiate the Customer, Coffee, and Order classes and utilize their methods to manage the coffee shop’s operations. The relationships between customers, their orders, and the coffees they order are maintained through these classes and their methods.

## Testing
You can run tests using pytest:
pytest -x

## Technologies Used
Python

## Contributions
Contributions to the Pizza Restaurants API are welcome! 
If you have any suggestions, bug fixes, or additional features you'd like to add, please feel free to submit a pull request or open an issue.

## Acknowledgments
Inspiration

## Support
For support, email neema.ambuku@student.moringaschool.com


