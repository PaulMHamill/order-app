from flask import render_template
from app import app
from models.current_orders import orders

@app.route('/orders')
def index():
    return render_template('index.html', all_orders = orders)

@app.route('/orders/<index>')
def order_index(index):
    return render_template('orders.html', single_order=orders[int(index)])

