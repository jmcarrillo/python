#!/usr/bin/env python3
import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")

print(text)

print("¡¡¡Hola!!!")
