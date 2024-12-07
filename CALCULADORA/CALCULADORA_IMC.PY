#UTILICE UNA PAGINA PARA CONVERTIR TEXTO A ASCCI Y PODER PONER UN BANNER
print (" __  .___  ___.   ______ ")
print ("|  | |   \/   |  /      |")
print ("|  | |  \  /  | |  ,----'")
print ("|  | |  |\/|  | |  |     ")
print ("|  | |  |  |  | |  `----.")
print ("|__| |__|  |__|  \______|")
print ("CALCULA TU INDICE DE MASA CORPORAL")
#UTILIZ FLOAT PARA PODER UTILIZAR DECIMALES
estatura = float(input("Introduce tu estatura en metros\n "))
peso = float(input("Introduce tu peso en kilogramos \n "))
imc = peso/(estatura**2)
#UTILIZE {:.1f} PARA QUE SOLO SE MUESTRE UN DECIMAL DE LA OPERACION
print("Tu imc es: {:.1f}".format(imc))
#UTILCE LA SENTENCIA IF PARA MOSTRAR CUAL ES TU ESTADO DE SALUD COMO LO MUESTRA EN LA PAGINA
if imc >=30:
    print("TU TIENES OBESIDAD, TE RECOMENDAMOS CONSULTAR A UN ESPECIALISTA PARA MEJORAR TU CALIDAD DE VIDA")
if imc >=25 and imc <=29.9:
    print("TU TIENES SOBREPESO, TE RECOMENDAMOS CONSULTAR A UN ESPECIALISTA PARA MEJORAR TU CALIDAD DE VIDA")
if imc >=18.5 and imc <=24.9:
    print("¡¡FELCIDADES!! TU ESTADO DE SALUD ES SALUDABLE")
if imc <=18.5:
    print("TU TIENES BAJO PESO, TE RECOMENDAMOS CONSULTAR A UN ESPECIALISTA PARA MEJORAR TU CALIDAD DE VIDA")

