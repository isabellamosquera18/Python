nombre = input("Cual es tu nombre? ")
print("Hola " + nombre)
ingrediente1 = float(input("Ingrese el numero de tazas de agua para una arepa: "))
ingrediente2 = float(input("Ingrese el numero de tazas de harina para una arepa: "))
ingrediente3 = float(input("Ingrese el numero de cucharaditas de sal para una arepa: "))
ingrediente4 = float(input("Ingrese el numero de cucharadas de aceite para una arepa: "))
volumen_precoccion = ingrediente1*250 + ingrediente2 * 250 + ingrediente3 * 5 + ingrediente4 * 15
print ("El volumen precoccion de la arepa es: ")
print( volumen_precoccion)
print("El volumen postcoccion de la arepa es: ")
volumen_postcoccion = volumen_precoccion*0,10
print(volumen_postcoccion)
















