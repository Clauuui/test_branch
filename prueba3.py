#Python distingue entre mayúsculsa y minúsculas por tanto:
#Edad=0
#edad=0 
#No son lo mismo

#INICIALIZAR
#Esto se refiere a darle un valor a la variable (generalmente 0) antes de ingresar el valor

#a,b,c = 0
#a,b,c = 1,2,3

#VARIABLES EN PYTHON
# Se declaran siempre asignandoles un numero
# No pueden empezar con un numero
#Puedes asignar valores a varial valiabres en una sola línea 
#Python distingue entre mayúsculsa y minúsculas 
# FOR, IF y WHILE no pueden ser usadas para nombres de variables

#a = b = c = 0 
#a,b,c = 0 
#Ambas formas son lo mismo y son válidas 

#TIPOS DE DATOS: NUMEROS

#Enteros int
10, -5, 0 
#Flotantes
2.3, -2.4
#Complejos con la j se representa la parte imaginaria 
#x = 2+3j

#TIPOS DE DATOS: CADENA DE CATACTERES string 
'hola'
"holis"

#TIPOS DE DATOS: BOOLEANOS bool
#Devuelven verdadero o falso

#OPERADORES ARITMETICOS 

suma = 10+5 
resta = 10-5
multiplicacion = 10*5
division = 10/5
division_entera = 10//3 
modulo_restodeladivision = 10%3 
exponenciacion = 2**3 

print('La suma es: ',suma)
print('La resta es: ',resta)
print('La multiplicacion es: ',multiplicacion)
print('La division es: ',division)
print('La division_entera es: ',division_entera)
print('El modulo_resto de la division es: ',modulo_restodeladivision)
print('La exponenciacion es: ',exponenciacion)

#OPERADORES DE COMPARARCION PARA BOOLEANOS
# igual a ==
# diferente de !=
#mayor que, menor que <>
#mayor igual que, menor igual que >= <=

#OPERADORES LOGICOS 
#Permiten combinar expresiones booleanas para crear condiciones mas complejas

# AND devuelve TRUE si ambas expresiones son verdaderas
# OR devuelve TRUE si al menos una de las expresiones es verdadera 
# NOT invierte el valor de la expresion booleana 

y =0
x= 2+3j
z='hola'

x>5 or y < 10 and not(z==3)
#AND siempre se evalua antes que or

#OPERADORES DE ASIGNACION 
#Asignacion simple. Asigna un valor a una variable (=)

#Asignacion con operacion. Combina una operacion aritmetica con la asignacion 
#(+=, -=, *=, /=, %=, etc)

x= x+1
x+=1

