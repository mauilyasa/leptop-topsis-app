from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
from topsis import topsis  # Ensure this is the correct path to your topsis module
from sqlalchemy import desc
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laptops.db'  # Use your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    price = db.Column(db.Float)
    performance = db.Column(db.Float)
    battery_life = db.Column(db.Float)
    # Add other columns as needed

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/laptops')
def list_laptops():
    laptops = Laptop.query.all()
    return render_template('list_laptops.html', laptops=laptops)

@app.route('/add_laptop', methods=['GET', 'POST'])
def add_laptop():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        price = float(request.form['price'])
        performance = float(request.form['performance'])
        battery_life = float(request.form['battery_life'])

        new_laptop = Laptop(brand=brand, model=model, price=price, performance=performance, battery_life=battery_life)
        db.session.add(new_laptop)
        db.session.commit()

        return redirect(url_for('add_laptop'))

    return render_template('add_laptop.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        weights = request.form.getlist('weights', type=float)
        impacts = [1, 1, 1]  # Default impacts (1 for beneficial, -1 for non-beneficial)

        laptops = Laptop.query.all()
        data = pd.DataFrame([(laptop.price, laptop.performance, laptop.battery_life) for laptop in laptops])
        
        scores = topsis(data, weights, impacts)
        
        recommendations = sorted(zip(laptops, scores), key=lambda x: x[1], reverse=True)
        
        result = [{'brand': rec[0].brand, 'model': rec[0].model, 'score': rec[1]} for rec in recommendations]
        
        return render_template('recommend.html', recommendations=result)

    return render_template('recommend.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0',port=5000,debug=True)