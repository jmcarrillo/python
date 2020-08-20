#!/usr/bin/env python3
import urllib.request














page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")
price= text[250:255]
print(price)


















page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")
price= text[250:255]
print(price)




