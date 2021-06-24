import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd


# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url,headers={'User-Agent': 'Mozilla/5.0'})
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()

# defining the html contents of a URL.
#xhtml = url_get_contents('https://www.goodreturns.in/gold-rates/kolkata.html#Today+24+Carat+Gold+Rate+Per+Gram+in+Kolkata+%28INR%29').decode('utf-8')

# Defining the HTMLTableParser object
#p = HTMLTableParser()

# feeding the html contents in the
# HTMLTableParser object
#p.feed(xhtml)

# Now finally obtaining the data of
# the table required
#gold22 = p.tables[0]
#gold24 = p.tables[1]
#print(gold22)

# converting the parsed data to
# datframe
#print("\n\nPANDAS DATAFRAME\n")
#print(pd.DataFrame(p.tables[0]))
#print(pd.DataFrame(p.tables[1]))
