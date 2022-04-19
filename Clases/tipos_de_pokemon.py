import random
#importa la clases ataque
from Clases.ataque_pokemon import ataque
class tiposDePokemon:
    #funcion para pokemon tierra que va a tener un indice de defensa entre 11 y 20 
    def tierra(self):
        return random.randint(11, 20)
    #funcion para pokemon agua que va a tener un indice de defensa entre 11 y 20 
    def agua(self):
        return random.randint(11, 20)
    #funcion para pokemon aire que va a tener un indice de defensa entre 11 y 20
    def aire(self):
        return random.randint(11, 20)
        
    #funcion para pokemon electricidad que va a tener un indice de defensa entre 11 y 20
    def electricidad(self):
        return random.randint(11, 20)

