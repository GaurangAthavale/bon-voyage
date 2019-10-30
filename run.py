from db_connections import find_flights
from trains_scrape import find_trains
from hotels_scrape import find_hotels
from conversions import find_flt_duration
from flask import Flask, render_template, request
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/flights-display', methods = ["GET", "POST"])
def show_flights():
    flights = []
    if request.method == 'POST':
        typ = request.form['type']
        print(typ)
        src = request.form['src']
        print(src)
        des = request.form['des']
        print(des)
        dep_date = request.form['dep_date']
        print(dep_date)
        ret_date = request.form['ret_date']
        print(ret_date)
        adults = request.form['adults']
        print(adults)
        kids = request.form['kids']
        print(kids)
        clas = request.form['class']
        print(clas)
        flights = find_flights(src, des, dep_date)
    return render_template('flights.html', flights = flights, clas = clas)

@app.route('/trains-display', methods = ["GET", "POST"])
def show_trains():
    trains = []
    if request.method == 'POST':
        typ = request.form['type']
        print(typ)
        src = request.form['src']
        print(src)
        des = request.form['des']
        print(des)
        dep_date = request.form['dep_date']
        print(dep_date)
        ret_date = request.form['ret_date']
        print(ret_date)
        adults = request.form['adults']
        print(adults)
        kids = request.form['kids']
        print(kids)
        clas = request.form['class']
        print(clas)
        year, month, date = dep_date.split('-')
        trains = find_trains(src, des, date, month, year, clas)
        print(trains)
    return render_template('trains.html', trains = trains, clas = clas)

@app.route('/hotels-display', methods = ['GET', 'POST'])
def show_hotels():
    hotels = []
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        checkin = request.form['checkin']
        print(checkin)
        checkout = request.form['checkout']
        print(checkout)
        room1 = request.form['room1']
        print(room1)
        room2 = request.form['room2']
        print(room2)
        hotels = find_hotels(city, checkin, checkout, '2', [room1, room2])
        print(len(hotels))
        pprint(hotels[0])
        pprint(hotels[1])
        # for hotel in hotels:
        #     print(hotel['name'],hotel['priceRange'],sep=':')
    return render_template('hotels.html', hotels=hotels)

@app.route('/checkout')
def checkout():
    return render_template('booking.html')

@app.errorhandler(404)
def error_handle(error):
    return 'Page not found'

if __name__ == '__main__':
    app.run(debug = True)
