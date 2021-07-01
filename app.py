from clases.carta import Carta 
from clases.unidad import Unidad
from clases.efectos import Efecto 

ninja_rojo= Unidad("Ninja Cinturon Rojo",3,4,3)
ninja_negro= Unidad("Ninja Cinturón Negro",4,4,5)

print("el nombre de la carta es: ", ninja_rojo.nombre)
print("la resistencia de la carta es: ", ninja_rojo.resistencia)
print("el costo de la carta es: ", ninja_rojo.costo)
print("el poder de la carta es: ", ninja_rojo.poder)

algoritmo=Efecto("Algoritmo Duro",2,"aumentar la resistencia del objetivo en 3","Resistencia",3)

print("el nombre de la carta es: ", algoritmo.nombre)
print("el costo de la carta es: ", algoritmo.costo)
print("el texto de la carta es: ", algoritmo.texto)
print("el status de la carta es: ", algoritmo.status)
print("el magnitud de la carta es: ", algoritmo.magnitud)