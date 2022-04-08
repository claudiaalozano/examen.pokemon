import random 
class pokemon:
    def __init__ (self, id, arma , nombres):
        self.id =id
        self.arma =arma
        self.nombres =nombres
    


id = random.randint(0,2)
nombres = ["Pikachu" , "Pidgey" , "Squirtle"]
arma = ["Puñetazo" , "Patada" , "Codazo" , "Cabezazo"]
indice_salud = (1,100)
indice_ataque = (1,10)
indice_defensa = (1,10)
