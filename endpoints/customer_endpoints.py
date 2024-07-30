from flask import Blueprint, jsonify

customer_endpoints_get_info_bp = Blueprint('customer_endpoints_get_info_bp', __name__)


@customer_endpoints_get_info_bp.route('/api/customer/get_customer_name')
def get_customer_name():
    data = {'customer_first_name': 'Mohamed', 'customer_last_name': 'Ahmed'}
    return jsonify(data)


@customer_endpoints_get_info_bp.route('/api/customer/get_customer_age')
def get_customer_age():
    data = {'customer_age': 45}
    return jsonify(data)
