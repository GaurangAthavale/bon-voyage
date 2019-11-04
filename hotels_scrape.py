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
    hotel_counter = 1
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
            info['id'] = hotel_counter
            hotel_counter += 1
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
                am_list = row.find_all('div',{'class':'amenityWrapper__amenity'})
                amenities = []
                for amenity in am_list:
                    amenities.append(amenity.find('span').text.strip())
                info['amenities'] = amenities[:-1]
                if 'ratingValue' not in info:
                    info['ratingValue'] = 'NEW'
                discounted,og = info['priceRange'].split('-')
                #print(discounted, og)
                discounted = discounted.strip()
                og = og.strip()
                # print(discounted[1:], og[1:])
                if int(discounted[1:]) < int(og[1:]):
                    info['price'] = discounted
                    info['old'] = og
                else:
                    info['price'] = og
                # print(info['price'])
                dtr = requests.get(info['url'])
                dtsoup = BeautifulSoup(dtr.text, 'html.parser')
                desctag = dtsoup.find('div',{'class':'c-u43rea'})
                if desctag:
                    loc = desctag.text.find('Special Features')
                    info['description'] = desctag.text[8:loc].strip()
                    # print(info['description'])
                policies_ul = dtsoup.find('ul',{'class':'c-f0mxva'})
                if policies_ul:
                    policies_li = policies_ul.find_all('li')
                    policies = []
                    for p in policies_li[1:]:
                        policies.append(p.text)
                    info['policies'] = policies
                    print(info['policies'])
                hotel_list.append(info)
        if hotels > 0 and pgno < 4:
            pgno += 1
        else:
            break
    return hotel_list

# ans = find_hotels('mumbai','07-12-2019','10-12-2019','2',['1','2'])
# print(len(ans))
# for a in ans:
#     print(a['id'])