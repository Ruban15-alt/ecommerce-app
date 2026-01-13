import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

