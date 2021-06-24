from django.shortcuts import render
from .liverate import url_get_contents;
from html_table_parser.parser import HTMLTableParser
from bs4 import BeautifulSoup as BS
import requests
import random
# Create your views here.


def rate(request):
        xhtml = url_get_contents('https://www.fresherslive.com/amp/gold-rate-today/kolkata').decode('utf-8')
        #req = requests.post("https://bullions.co.in/location/kolkata/")
        #soup = BS(req.text, "html.parser")
        #d = soup.find('div', attrs = {'class': 'data-meta'}).get_text()
        p = HTMLTableParser()
        p.feed(xhtml)
        gold = p.tables[0]
        gold24 = p.tables[2]
        gold22 = p.tables[1]
        silver = p.tables[4]
        #check the number at gold24[i][2] for positie negative and nill and append it to the list again.
        goldcard24 = (int(gold[1][2][2:3] + gold[1][2][4:])) * 10
        goldcard22 = (int(gold[1][1][2:3] + gold[1][1][4:])) * 10

        silverrate = (int(silver[2][1][2:4] + silver[2][1][5:6])) * 100
        plus = False
        minus = False

        if(gold24[1][2][0] == "+"):
            plus = True
            minus = False
        else:
            plus = False
            minus = True


        context = {'gold': gold, 'gold24': gold24, 'gold22': gold22, 'goldcard24':goldcard24 ,'goldcard22':goldcard22 , 'plus':plus, 'minus': minus,'silverrate':silverrate}
        return render(request, 'liverates/rate.html',context)
