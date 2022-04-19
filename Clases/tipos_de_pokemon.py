import random

from Clases.ataque_pokemon import ataque
class tiposDePokemon:
    
    def tierra(self, Diglett, Venusaur): 
        return random.randint(11, 20)
    
    def agua(self, Squirtle):
        return random.randint(11, 20)
    
    def aire(self, Pidgey):
        return random.randint(11, 20)
        
    
    def electricidad(self, Pikachu, Charmeleon):
        return random.randint(11, 20)

