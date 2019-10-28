import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

#change the following 5 variables as per requirements
# source_stn = 'KYN'
# dest_stn = 'NZM'
# date = '25'
# month = '10'
# year = '2019'

def find_trains(source_stn, dest_stn, date, month, year, clas):
    url = 'https://www.railyatri.in/booking/trains-between-stations?from_code='+source_stn+'&from_name=SRC+&journey_date='+date+'%2F'+month+'%2F'+year+'%2F'+'&to_code='+dest_stn+'&to_name=DST+&user_id=1&user_token=6'
    print(date, month, year)
    #print(url)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    trains = []
    for row in soup.select('tr.tbs-main-row'):
        data = {}
        title = row.find('p', {'class': 'train-name-title'}).text.strip('\n')
        data['trn_no'] = title[:5]
        data['trn_name'] = title[8:]
        data['schedule'] = 'https://erail.in/train-enquiry/'+title[:5]
        #https://www.cleartrip.com/trains/12137/
        spans = row.find_all('span')[:6]
        data['source'] = spans[0].text
        data['departure time'] = spans[1].text
        data['destination'] = spans[3].text
        data['arrival time'] = spans[4].text
        data['duration'] = spans[5].text
        data['fares'] = {}
        classes = row.find_all('div', {'class': 'coach'})
        for i in range(len(classes)//2):
            # pair = {}
            deets = classes[i].find_all('p')
            classs = deets[0].text
            price = deets[1].text
            if price == '₹ NA':
                continue
            data['fares'][classs] = price
        if len(data['fares']) != 0 and clas in data['fares']:		#railyatri shows some trains with no availabilities
            trains.append(data)

    #trains = json.dumps(trains)
    #trains = json.loads(trains)

    return trains