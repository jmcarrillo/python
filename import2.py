#!/usr/bin/env python3
import urllib.request
import time

def get_price():

    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where= text. find('>$')
    start_of_price=where + 2
    end_of_price=start_of_price + 4

n    price= float(text[start_of_price:end_of_price])
at(text[start_of_price:end_of_price])

# print("Buy!")

    print(text[start_of_price:end_of_price])

get_price()

else:
# while price> 4.74:

# price= 99.99
# while price> 4.74:
#    time.sleep(90)
else:
else:
# price= 99.99
# while price> 4.74:
#    time.sleep(90)
# price= 99.99
# while price> 4.74:
#    time.sleep(90)
