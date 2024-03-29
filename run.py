import db_connections
import pyrebase
from db_connections import find_flights
from trains_scrape import find_trains
from hotels_scrape import find_hotels
from conversions import find_flt_duration, find_dur_mins, find_dur_mins_tr
from flask import Flask, render_template, request, redirect
from pprint import pprint
from datetime import date
from random import randint
import smtplib, ssl
port = 465  # For SSL
# Create a secure SSL context
context = ssl.create_default_context()

config = {
    "apiKey": "AIzaSyAiPuEH6tsR4h36GJKDzKtv87-2E9u0_oA",
    "authDomain": "bon-voyage-d2ff1.firebaseapp.com",
    "databaseURL": "https://bon-voyage-d2ff1.firebaseio.com",
    "storageBucket": "bon-voyage-d2ff1.appspot.com"
}

sender_email = "bonvoyage6566@gmail.com"
sender_pw = "1711065and66"

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__)
check = {}

#global variables
loggedIn = False
userId = None
userEmail = None
flights = []
clas = 'economy'
pax = '1'
trains = []
tr_pax = '1'
tr_clas = '3A'
hotels = []
roomConf = []
checkin = '2019-11-15'
checkout = '2019-11-22'
priceConf = []
booked_fl = []
booked_tr = []
booked_ht = []

@app.route('/')
def hello_world():
    return render_template('index.html', login = loggedIn)

@app.route('/flights-display', methods = ["GET", "POST"])
def show_flights():
    global flights
    global clas
    global pax
    if request.method == 'POST':
        src = request.form['src']
        print(src)
        des = request.form['des']
        print(des)
        dep_date = request.form['dep_date']
        print(dep_date)
        pax = request.form['adults']
        print(pax)
        # kids = request.form['kids']
        # print(kids)
        clas = request.form['class']
        print(clas)
        flights = find_flights(src, des, dep_date)
    pprint(flights)
    return render_template('flights.html', flights = flights, clas = clas, login = loggedIn)

@app.route('/fl-sort/<typ>/<reverse>')
def sort_fl(typ, reverse):
    global flights
    global clas
    if typ == "price" and reverse == "norm":
        flights = sorted(flights, key = lambda i:i['fare'][clas])
    elif typ == "price" and reverse == "rev":
        flights = sorted(flights, key = lambda i:i['fare'][clas], reverse=True)
    elif typ == "duration" and reverse == "norm":
        flights = sorted(flights, key = lambda i:find_dur_mins(i['duration']))
    elif typ == "duration" and reverse == "rev":
        flights = sorted(flights, key = lambda i:find_dur_mins(i['duration']), reverse=True)
    return redirect('/flights-display')

@app.route('/add-flight/<fltno>')
def add_flight(fltno):
    global booked_fl
    global clas
    global pax
    print(fltno)
    print(flights)
    for fl in flights:
        if fl['fltno'] == fltno:
            print('adding', fltno, 'to booked_fl')
            fl['baseFare'] = fl['fare'][clas]
            fl['clas'] = clas
            fl['pax'] = pax
            fl['totalBaseCost'] = fl['baseFare'] * int(pax)
            fl['tax'] = int(fl['totalBaseCost'] * 0.12)
            fl['bookingCharge'] = int(fl['totalBaseCost'] * 0.04)
            fl['totalPrice'] = fl['totalBaseCost'] + fl['tax'] + fl['bookingCharge']
            added = False
            for el in booked_fl:
                print(el)
                if el['fltno'] == fltno:
                    added = True
            if not added:
                booked_fl.append(fl)
            # print(fl)
            break
    print(booked_fl)
    return redirect('/checkout')
    # return 'done'

@app.route('/trains-display', methods = ["GET", "POST"])
def show_trains():
    global trains
    global tr_pax
    global tr_clas
    if request.method == 'POST':
        src = request.form['src']
        print(src)
        des = request.form['des']
        print(des)
        dep_date = request.form['dep_date']
        print(dep_date)
        tr_pax = request.form['adults']
        print(tr_pax)
        tr_clas = request.form['class']
        print(tr_clas)
        year, month, date = dep_date.split('-')
        trains = find_trains(src, des, date, month, year, tr_clas)
    print(trains)
    return render_template('trains.html', trains = trains, clas = tr_clas)

@app.route('/tr-sort/<typ>/<reverse>')
def sort_tr(typ, reverse):
    global trains
    global tr_clas
    if typ == "price" and reverse == "norm":
        trains = sorted(trains, key = lambda i:int(i['fares'][tr_clas][2:]))
    elif typ == "price" and reverse == "rev":
        trains = sorted(trains, key = lambda i:int(i['fares'][tr_clas][2:]), reverse=True)
    elif typ == "duration" and reverse == "norm":
        trains = sorted(trains, key = lambda i:find_dur_mins_tr(i['duration']))
    elif typ == "duration" and reverse == "rev":
        trains = sorted(trains, key = lambda i:find_dur_mins_tr(i['duration']), reverse=True)
    return redirect('/trains-display')

@app.route('/add-train/<trno>')
def add_train(trno):
    global booked_tr
    global tr_pax
    global tr_clas
    print(trno)
    print(trains)
    for tr in trains:
        if tr['trn_no'] == trno:
            print('adding', trno, 'to booked_tr')
            tr['pax'] = tr_pax
            tr['clas'] = tr_clas
            tr['baseFare'] = int(tr['fares'][tr_clas][2:])
            tr['totalBaseCost'] = tr['baseFare'] * int(tr_pax)
            tr['tax'] = int(tr['totalBaseCost'] * 0.12)
            tr['bookingCharge'] = int(tr['totalBaseCost'] * 0.04)
            tr['totalPrice'] = tr['totalBaseCost'] + tr['tax'] + tr['bookingCharge']
            booked_tr.append(tr)
            print(tr)
            break
    print(booked_tr)
    return redirect('/checkout')

@app.route('/hotels-display', methods = ['GET', 'POST'])
def show_hotels():
    global hotels
    global roomConf
    global checkin
    global checkout
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        checkin = request.form['checkin']
        print(checkin)
        checkout = request.form['checkout']
        print(checkout)
        roomConf.append(request.form['room1'])
        x = 2
        while True:
            key = 'room' + str(x)
            print('key', key)
            try:
                print(request.form[key])
                roomConf.append(request.form[key])
            except:
                break
            x += 1
        hotels = find_hotels(city, checkin, checkout, str(len(roomConf)), roomConf)
    print(roomConf)
    print(len(hotels))
    try:
        pprint(hotels[0])
    except:
        print('no hotel lmao')
    # pprint(hotels[1])
    # for hotel in hotels:
    #     print(hotel['name'],hotel['priceRange'],sep=':')
    return render_template('hotels.html', hotels=hotels, checkin = checkin, checkout = checkout)

@app.route('/ht-sort/price/<reverse>')
def sort_ht(reverse):
    global hotels
    global clas
    if reverse == "norm":
        hotels = sorted(hotels, key = lambda i:int(i['price'][1:]))
    elif reverse == "rev":
        hotels = sorted(hotels, key = lambda i:int(i['price'][1:]), reverse=True)
    return redirect('/hotels-display')

@app.route('/add-hotel/<hid>/<checkin>/<checkout>')
def add_hotel(hid, checkin, checkout):
    global booked_ht
    global roomConf
    global priceConf
    print(hid)
    yr, month, day = checkin.split('-')
    checkin = date(int(yr), int(month), int(day))
    yr, month, day = checkout.split('-')
    checkout = date(int(yr), int(month), int(day))
    days = (checkout - checkin).days
    print(days)
    print(roomConf)
    print(len(hotels))
    for ht in hotels:
        if str(ht['id']) == hid:
            print('adding', ht, 'to booked_ht')
            base = int(ht['price'][1:])
            adder = randint(300,500)
            priceConf = [0]*len(roomConf)
            for i in range(len(roomConf)):
                if roomConf[i] == '3' or roomConf[i] == 3:
                    priceConf[i] = base + adder
                else:
                    priceConf[i] = base
            ht['roomConf'] = roomConf
            ht['priceConf'] = priceConf
            ht['days'] = days
            ht['roomCount'] = [i for i in range(len(roomConf))]
            ht['finalPriceConf'] = [x*days for x in priceConf]
            ht['totalBaseCost'] = sum(ht['finalPriceConf'])
            ht['tax'] = int(ht['totalBaseCost'] * 0.12)
            ht['bookingCharge'] = int(ht['totalBaseCost'] * 0.04)
            ht['totalPrice'] = ht['totalBaseCost'] + ht['tax'] + ht['bookingCharge']
            booked_ht.append(ht)
            print(ht)
            break
    print(booked_ht)
    return redirect('/checkout')
    # return 'done'

@app.route('/signup',methods=['GET','POST'])
def signup():
    global loggedIn
    global check
    # global verification
    successful = "Successfully Signed In!!"
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        pwd = request.form['password']
        city = request.form['city']
        contact = request.form['contact']
        data = {
            "email" : email,
            "name" : name,
            "city" : city,
            "contact" : contact       
        }
        db.child("users").child(contact).set(data)
        check = auth.create_user_with_email_and_password(email, pwd)
        print(check)
        auth.send_email_verification(check['idToken'])
        verification = auth.get_account_info(check['idToken'])['users'][0]['emailVerified']
        loggedIn = True
    return render_template('index.html', login = verification,s="Verify your account first! We have mailed you the link.")

@app.route('/checkout')
def checkout():
    global booked_fl
    global booked_tr
    global booked_ht
    global loggedIn
    pprint(booked_ht)
    pprint(booked_fl)
    pprint(booked_tr)
    totalCost = 0
    for el in booked_fl:
        totalCost += el['totalPrice']
    for el in booked_tr:
        totalCost += el['totalPrice']
    for el in booked_ht:
        totalCost += el['totalPrice']
    return render_template('booking.html', hotels = booked_ht, flights = booked_fl, trains = booked_tr, totalCost = totalCost, login = loggedIn)

@app.route('/login',methods=['GET','POST'])
def login():
    global loggedIn
    global userId
    global userEmail
    # verification = False
    unsucessful = 'Please enter correct credentials!'
    if(request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        loggedIn = False
        successful = 'Login Successful'+'\nWelcome! '+str(email)
        try:
            check = auth.sign_in_with_email_and_password(email,password)
            # auth.send_email_verification(check['idToken'])
            print(auth.get_account_info(check['idToken']))
            verification = auth.get_account_info(check['idToken'])['users'][0]['emailVerified']
            print(verification)
            if(verification == False):
                return render_template('index.html',s="Verify your account first! We have mailed you the link.", login = False)
            else:
                loggedIn = True
                users = db.child('users').get()
                print(users)
                print('here')
                for user in users.each():
                    if user.val()['email'] == email:
                        print('found')
                        print(user.key())
                        userId = user.key()
                print(userId)
                userEmail = email
                print(userEmail)
                return render_template('index.html',s=successful, login = True)
        except:
            return render_template('login.html', us=unsucessful, login = False)
    return render_template('login.html')

@app.route('/logout')
def logout():
    global loggedIn
    userId = None
    userEmail = None
    loggedIn = False
    return render_template('index.html', login = False)

@app.route('/pay',methods=['GET','POST'])
def pay():
    global booked_fl
    global booked_tr
    global booked_ht
    if request.method == 'POST':
        number = str(request.form['number'])
        name = str(request.form['name'])
        cvv = str(request.form['cvc'])
        expiry = str(request.form['expiry'])
        number = number.replace(' ', '')
        name = name.lower()
        mon, yr = expiry.replace(' ', '').split('/')
        print(number)
        print(name)
        print(cvv)
        print(expiry, mon, yr)
        valid = False
        cards = db.child("pay-cards").get()
        if cards is None:
            print('no cards')
        else:
            for card in cards.each():
                print(card.key())
                if(number == card.key()):  
                    print('number matched')
                    if(name == card.val()['name'].lower()):
                        print('name matched')
                        if(mon == card.val()['card_month'] and yr == card.val()['card_year']):
                            print('expiry matched')
                            if(cvv == card.val()['cvv']):
                                print('cvv matched')
                                valid = True
        if valid:
            print('put all the booked stuff to the db')
            users = db.child('users').get()
            userObject = None
            for user in users.each():
                if user.key() == userId:
                    userObject = user
            print(userObject.val())
            if len(booked_fl) > 0:
                if 'booked-flights' not in userObject.val():
                    fl = booked_fl
                else:
                    fl = userObject.val()['booked-flights']
                    fl.append(booked_fl)
                data = db.child('users').child(userId).update({'booked-flights':fl})
            if len(booked_tr) > 0:
                if 'booked-trains' not in userObject.val():
                    tr = booked_tr
                else:
                    tr = userObject.val()['booked-trains']
                    tr.append(booked_tr)
                data = db.child('users').child(userId).update({'booked-trains':tr})
            if len(booked_ht) > 0:
                if 'booked-hotels' not in userObject.val():
                    ht = booked_ht
                else:
                    ht = userObject.val()['booked-hotels']
                    ht.append(booked_ht)
                data = db.child('users').child(userId).update({'booked-hotels':ht})
            booked_tr = []
            booked_fl = []
            booked_ht = []
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender_email, sender_pw)
                receiver_email = userEmail
                message = """Subject: Bon Voyage Booking Details
                Your booking has been done, thank you for using Bon Voyage!"""
                server.sendmail(sender_email, receiver_email, message)
            return render_template('index.html', s="Your booking has been done", login = loggedIn)
        else:
            pprint(booked_ht)
            pprint(booked_fl)
            pprint(booked_tr)
            totalCost = 0
            for el in booked_fl:
                totalCost += el['totalPrice']
            for el in booked_tr:
                totalCost += el['totalPrice']
            for el in booked_ht:
                totalCost += el['totalPrice']
            return render_template('booking.html', hotels = booked_ht, flights = booked_fl, trains = booked_tr, totalCost = totalCost, wrongCardDeets = True)
    return 'done'

@app.errorhandler(404)
def error_handle(error):
    return 'Page not found'

if __name__ == '__main__':
    app.run(debug = True)
