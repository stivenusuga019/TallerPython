"""Programa que arroje mayor de edad,
si la edad es mayor o igual a 18,si edad mayor que 65
 muestre usted pertenece ala tercera edad
de lo contrario muestre menor de edad"""


"""edad = int(input("Ingrese su edad: "))

if edad>=18:
    print("Usted es Mayor de Edad")
else:
    print("Usted es Menor de Edad")"""

#Elif Cuando tiene 2 o mas condiciones a evaluar

edad = int(input("Ingrese su edad: "))
if edad>=18 and edad<=64:
    print("Usted es Mayor de Edad")
elif edad>=65 and edad<=90:
    print("Usted Pertenece ala Tercera Edad")
elif edad>=91 and edad<=101:
    print("Usted Esta Apunto De Morir")
elif edad>=102:
    print("Eres Humano o Eres Un Inmortal")
else:
    print("Usted es Menor de Edad")