import urllib.request

page = urllib.request.urlopen("http://yahoo.com")
text = page.read().decode("utf8")

print(text)