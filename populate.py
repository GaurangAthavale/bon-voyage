from random import randint
import pyrebase

config = {
    "apiKey": "AIzaSyAiPuEH6tsR4h36GJKDzKtv87-2E9u0_oA",
    "authDomain": "bon-voyage-d2ff1.firebaseapp.com",
    "databaseURL": "https://bon-voyage-d2ff1.firebaseio.com",
    "storageBucket": "bon-voyage-d2ff1.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

airlines = ['air india', 'indigo', 'vistara', 'go air', 'jet airways', 'spicejet']
iata_codes = ['AI', '6E', 'UK', 'G8', '9W', 'SG']
ap_codes = ['AMD', 'ATQ', 'BLR', 'MAA', 'COK', 'GOI', 'GAU', 'HYD', 'CCU', 'BOM', 'DEL', 'TRV', 'IXZ', 'NAG', 'JAI', 'LKO', 'VNS', 'IXE', 'CJB', 'IMF', 'VGA']

def populate_flights(count):
    ids = db.child('flights').shallow().get()
    ids = list(ids.val())
    for i in range(count):
        data = dict()
        comp_ind = randint(0, len(airlines) - 1)
        data['airline'] = airlines[comp_ind]
        data['fltno'] = iata_codes[comp_ind] + '-' + str(randint(101,999))
        #avoid same flight number
        while data['fltno'] in ids:
            data['fltno'] = iata_codes[comp_ind] + '-' + str(randint(101,999))
        ids.append(data['fltno'])
        hr = randint(0, 23)
        min = randint(0, 60)
        data['dep'] = str(hr) + ':' + str(min)
        #0 to 6 days monday to sunday
        days = set()
        freq = randint(1,5)
        while len(days) < freq:
            days.add(randint(0,6))
        days = list(days)
        data['dep_days'] = days
        adder = randint(1,3)
        hr += adder
        min = randint(0, 60)        
        if hr >= 24:
            hr -= 24
            days = [(x+1)%7 for x in days]
        data['arr'] = str(hr) + ':' + str(min)
        data['arr_days'] = days
        src = randint(0, len(ap_codes) - 1)
        des = randint(0, len(ap_codes) - 1)
        while src == des:
            src = randint(0, len(ap_codes) - 1)
        data['src'] = ap_codes[src]
        data['des'] = ap_codes[des]
        print('populating', i)
        print(data)
        db.child('flights').child(data['fltno']).set(data)

populate_flights(5)