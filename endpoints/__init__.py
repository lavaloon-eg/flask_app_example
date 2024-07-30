from flask import Flask
from .customer_endpoints import customer_endpoints_get_info_bp
from .product_endpoints import product_endpoints_get_info_bp


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.register_blueprint(customer_endpoints_get_info_bp)
    app.register_blueprint(product_endpoints_get_info_bp)
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    return app
