from flask import Flask
from controllers.games_controller import order_blueprint

app = Flask(__name__)
app.register_blueprint(order_blueprint)
