#punto 1
"""peso_payaso = 95
peso_muñeca = 70
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))"""


#punto 2
"""n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")"""

 #punto 3

"""edad = int(input("¿Cuál es tu edad? "))
ingreso = float(input("¿Cuales son tus ingresos mensuales?"))
if edad >= 18 and ingreso >= 2500000:
    print("No tienes que cotizar")    
else:
    print("No eres mayor de edad,No Tienes que cotizar")"""


#Punto 4

"""nota = float(input("¿Cuál es su nota de desarrollo de software: "))
nota1 = float(input("¿Cuál es su nota de matemáticas: "))
nota2 = float(input("¿Cuál es su nota de lógica programación: "))
sumanotas = nota + nota1 + nota2 
promedio = sumanotas / 3
if promedio >= 3:
    print("Usted aprobo la notas", round(promedio,1))    
else:
    print("Usted Reprobo la notas",round(promedio,1))"""

#punto 5

edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 10:
    precio = 0

elif edad >= 11 and edad <= 18:
    precio = 24660
  
else:
    precio = 48000
# Mostrar precio
print("El precio de la entrada es","COl:$",precio)
   