from random import randint
import pyrebase
from conversions import find_flt_duration

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
ap_codes = ['AMD', 'BLR', 'MAA', 'GOI', 'HYD', 'CCU', 'BOM', 'DEL', 'IXZ', 'JAI', 'VNS', 'IXE', 'CJB']

def populate_flights(count):
    ids = db.child('flights').shallow().get()
    ids = list(ids.val())
    for src_ind in range(len(ap_codes)):
        for des_ind in range(len(ap_codes)):
            if src_ind != des_ind:
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
                    data['dep'] = '{:02d}'.format(hr) + ':' + '{:02d}'.format(min)
                    #0 to 6 days monday to sunday
                    days = set()
                    freq = randint(4,7)
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
                    data['arr'] = '{:02d}'.format(hr) + ':' + '{:02d}'.format(min)
                    data['arr_days'] = days
                    data['src'] = ap_codes[src_ind]
                    data['des'] = ap_codes[des_ind]
                    data['duration'] = find_flt_duration(data['dep'], data['arr'], data['dep_days'][0], data['arr_days'][0])
                    fares = dict()
                    fare = randint(3000,8000)
                    fares['economy'] = fare
                    adder = randint(500,2000)
                    fare += adder
                    fares['business'] = fare
                    adder = randint(500,2000)
                    fare += adder
                    fares['first_class'] = fare
                    data['fare'] = fares
                    print('populating', data['src'], data['des'], i)
                    print(data)
                    db.child('flights').child(data['fltno']).set(data)

#db.child('flights').child('dummy').set({'yo':'yooo'})
#populate_flights(3)

#forgot to add fares previously "FACEPALM!!"

# flights = db.child('flights').get()
# counter = 1
# for fl in flights.each():
    # fares = dict()
    # fare = randint(3000,8000)
    # fares['economy'] = fare
    # adder = randint(500,2000)
    # fare += adder
    # fares['business'] = fare
    # adder = randint(500,2000)
    # fare += adder
    # fares['first_class'] = fare
    # print('updating', counter)
    # db.child('flights').child(fl.key()).update({'fare':fares})
#     counter += 1

#decided that its economically better to add duration than to calc everytime

# flights = db.child('flights').get()
# counter = 1
# for fl in flights.each():
#     info = fl.val()
#     time = find_flt_duration(info['dep'], info['arr'], info['dep_days'][0], info['arr_days'][0])
#     dep = '{:02d}'.format(int(info['dep'].split(':')[0])) + ':' + '{:02d}'.format(int(info['dep'].split(':')[1]))
#     arr = '{:02d}'.format(int(info['arr'].split(':')[0])) + ':' + '{:02d}'.format(int(info['arr'].split(':')[1]))
#     print('updating', counter)
#     db.child('flights').child(fl.key()).update({'duration':time, 'dep':dep, 'arr':arr})
#     counter += 1

# cities = ['Agra','Ahmedabad','Alwar','Amritsar','Aurangabad','Bangalore','Bharatpur','Bhavnagar','Bikaner','Bhopal','Bhubaneshwar','Bodhgaya','Calangute','Chandigarh','Chennai','Chittorgarh','Coimbatore','Cuttack','Dalhousie','Dehradun','Delhi','Ernakulam','Faridabad','Gaya','Gangtok','Ghaziabad','Gurgaon','Guwahati','Gwalior','Haridwar','Hyderabad','Imphal','Indore','Jabalpur','Jaipur','Jaisalmer','Jalandhar','Jamshedpur','Jodhpur','Junagadh','Kanpur','Kanyakumari','Khajuraho','Khandala','Kochi','Kodaikanal','Kolkata','Kota','Kottayam','Kovalam','Lucknow','Ludhiana','Madurai','Manali','Mangalore','Margao','Mathura','Mountabu','Mumbai','Mussoorie','Mysore','Manali','Nagpur','Nainital','Noida','Ooty','Orchha','Panaji','Patna','Pondicherry','Porbandar','Port-blair','Pune','Puri','Pushkar','Rajkot','Rameswaram','Ranchi','Sanchi','Secunderabad','Shimla','Surat','Thanjavur','Thiruchchirapalli','Thrissur','Tirumala','Udaipur','Vadodra','Varanasi','Vasco-Da-Gama','Vijayawada','Visakhapatnam']
# print(len(cities))

c_names=[['Nikhil Bharadwaj'],['Gaurang Athavale'],['Kapil Sharma'],['Rohit Sharma'],['Virat Kohli'],['Cheteshwar Pujara'],['Swapnil Pawar'],['Gaurav Bhagwanani'],['Dhruvil Pujara'],['Deep Dama'],['Mihir Gada']]

cards = [['Visa','4'],['Mastercard','55'],['American Express','34'],['Maestro','6759']]

def cc():
    for i in range(len(c_names)):
        data = dict()
        data['name'] = c_names[i][-1]
        x = randint(0,3)
        c_names[i].append(cards[x][0])
        data['card_name'] = c_names[i][-1]
        c_names[i].append(cards[x][1])
        # print(c_names[i])
        while(len(c_names[i][-1])!=16):
            c_names[i][-1]=c_names[i][-1]+str(randint(0,9))
        data['card_no'] = c_names[i][-1]
        m = randint(1,12)
        y = randint(20,25)
        c_names[i].append('{:02d}'.format(m))
        data['card_month'] = c_names[i][-1]
        c_names[i].append('{:02d}'.format(y))
        data['card_year'] = c_names[i][-1]
        c_names[i].append(str(randint(100,999)))
        data['cvv'] = c_names[i][-1]
        db.child('pay-cards').child(data['card_no']).set(data)
        # print(c_names[i])

cc()


