import db-connections
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/flights-display')
def show_flights():
    return render_template('flights.html')

@app.route('/flights')
def find_flights():
    return render_template('search-flights.html')

@app.route('/checkout')
def checkout():
    return render_template('booking.html')

@app.errorhandler(404)
def error_handle(error):
    return 'Page not found'

if __name__ == '__main__':
    app.run(debug = True)
