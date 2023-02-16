#punto 1

num1=int(input("ingrese primer numero: "))
num2=int(input("ingrese segundo numero: "))
sum=num1+num2
res=num1-num2
opcion=0

while opcion !=6:
    print ("""
    escoja la operacion que quiere realizar:
    (1) suma
    (2) resta
    (3) division
    (4) potenciacion
    (5) multiplicación
    (6) raiz cuadrada
    (7) cambiar numeros introducidos   
    (8) salir""")

    opcion = int(input()) 
    if opcion ==1:
        print("El resultado es: ",sum)
    
    if opcion ==2:
        print("El resultado es: ",res)

    if opcion==3:
        if num2==0:
            print("ERROR EN LA DIVISIÓN")
        else:
            print("El resultado es: ",num1/num2)

    if opcion==4:
        print("El resultado es:", pow(num1,num2))

    if opcion==5:
        print ("El resultado es:  ",num1,"*",num2,num1*num2)

    if opcion==6:
        print("El resultado es: ",pow(num1,1/2),pow(num2,0.5))

    if opcion==7:
        num1=int(input("Ingrese Primer nNumero: "))
        num2=int(input("Ingrese Segundo Numero: "))

    if opcion==8:
       break
        
   
#punto 2
