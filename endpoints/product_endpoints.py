from flask import Blueprint, jsonify

product_endpoints_get_info_bp = Blueprint('product_endpoints_get_info_bp', __name__)


@product_endpoints_get_info_bp.route('/api/product/get_info')
def get_customer_name():
    data = {'name': 'Laptop', 'Brand': 'DELL'}
    return jsonify(data)
