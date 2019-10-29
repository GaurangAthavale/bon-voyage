import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

def find_hotels(city, checkin, checkout, rooms, guests):
    inc,inb,ina = checkin.split('-')
    outc,outb,outa = checkout.split('-')
    roomConf = ''
    for i in range(int(rooms)):
        roomConf += ('&roomConfig='+guests[i])
    pgno = 1
    hotel_list = []
    while True:
        url = 'https://www.oyorooms.com/hotels-in-'+city+'/?checkin='+ina+'%2F'+inb+'%2F'+inc+'&checkout='+outa+'%2F'+outb+'%2F'+outc+'&page='+str(pgno)+roomConf
        print(url)

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)
        
        hotels = 0
        for row in soup.find_all('div',{'class':'hotelCardListing'}):
            hotels += 1
            info = {}
            imageSection = row.find('div', {'class':'hotelCardListing__imgCardWrapper'})
            images = imageSection.find_all('img')
            nonlz = False
            img_links = []
            for img in images:
                src = img['src']
                if 'lazy' not in src:
                    img_links.append(src)
                    nonlz = True
            # print(img_links)
            info['imgs'] = img_links
            # print(nonlz)
            if nonlz:
                description = row.find('div', {'class':'listingHotelDescription'})
                metas = description.find_all('meta')
                for meta in metas:
                    # print(meta['itemprop'],':',meta['content'])
                    info[meta['itemprop']] = meta['content']
                nametag = row.find('h3')
                info['name'] = nametag.text
                # print(nametag)
                address = row.find('span',{'class':'u-line--clamp-2'})
                info['address'] = address.text
                hotel_list.append(info)
        if hotels > 0 and pgno < 4:
            pgno += 1
        else:
            break
    return hotel_list

# find_hotels('kolkata','07-12-2019','10-12-2019','2',['1','2'])