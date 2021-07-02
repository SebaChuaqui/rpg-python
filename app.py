from clases.carta import Carta 
from clases.unidad import Unidad
from clases.efectos import Efecto 

jugador1=[]
jugador2=[]

#turno1
ninja_rojo= Unidad("Ninja Cinturon Rojo",3,4,3)
jugador1.append(ninja_rojo)


algoritmo=Efecto("Algoritmo Duro",2,"aumentar la resistencia del objetivo en 3","Resistencia",3)
jugador1.append(algoritmo)
algoritmo.genera_efecto(ninja_rojo)

#turno2

ninja_negro= Unidad("Ninja Cinturón Negro",4,4,5)
promesa=Efecto("Promesa no Manejada",1,"reducir la resistencia del objetivo en 2","Resistencia",-2)
jugador2.append(ninja_negro)
jugador2.append(promesa)
promesa.genera_efecto(ninja_rojo)

#turno3

programacion=Efecto("Programación en pareja",3,"aumentar el poder del objetivo en 2","Poder",2)
jugador1.append(programacion)
programacion.genera_efecto(ninja_rojo)
ninja_rojo.ataque(ninja_negro)

print("el nombre de la carta es: ", ninja_rojo.nombre)
print("la resistencia de la carta es: ", ninja_rojo.resistencia)
print("el costo de la carta es: ", ninja_rojo.costo)
print("el poder de la carta es: ", ninja_rojo.poder) 

print("el nombre de la carta es: ", ninja_negro.nombre)
print("la resistencia de la carta es: ", ninja_negro.resistencia)
print("el costo de la carta es: ", ninja_negro.costo)
print("el poder de la carta es: ", ninja_negro.poder) 
