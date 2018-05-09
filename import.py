
print("Bienvenidos a su practica!")

x = int(input("Introduce un número entero: "))

if x < 10:
   print('Pequeño')
   print('Hecho')

if x%2 == 0 :
   print('x es par')
else :
   print('x es impar')
page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")

print(text)
