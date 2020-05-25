# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:11:22 2020

@author: ciara
"""


import requests
import csv #, sys

from bs4 import BeautifulSoup

cookies = {
    'ApplicationGatewayAffinity': '1d2ad8ab214d1293a4e31bcd161589fa82a54a39bb7b3be80b503996092d4296',
    'ApplicationGatewayAffinityCORS': '1d2ad8ab214d1293a4e31bcd161589fa82a54a39bb7b3be80b503996092d4296',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,nl;q=0.6',
}

response = requests.get('https://www.corkairport.com/arrivals-departures', headers=headers, cookies=cookies)

#print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')

# writer = csv.writer(sys.stdout)
# writer.writerow([
#     'Arriving From'
#     'Airline',
#     'Scheduled to arrive', 'Latest Update', 'Status'
#     ])


           
with open('flight.csv','w') as f:
           [table] = soup.find_all("table")
           writer = csv.writer(f)
           writer.writerow([
            'Arriving From',
            'Airline', 'Flight No.',
            'Scheduled to arrive', 'Latest Update'
            ])
           for row in table.find_all("tr"):
               writer.writerow(
               [td.string.strip() for td in row.find_all("td")]
           )

    