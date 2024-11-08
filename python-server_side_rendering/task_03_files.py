from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_file(file_path):
    try:
        products = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Open JSON file
    with open('items.json', 'r') as file:
        # Convert JSON to Python dictionary
        data=json.load(file)
    # Get items from dictionary and if not found, return an empty list
    items=data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')
    
    # Select source file
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')
    
    # If no products found or error reading
    if not products:
        return render_template('product_display.html', error='No products found or error reading file.')

    #  Filter products by id
    if id:
        products = [product for product in products if str(product.get('id')) == id]
        if not products:
            return render_template('product_display.html', error='Product not found.')

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)