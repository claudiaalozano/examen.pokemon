import random
#importar clase pokemon
from Clases.pokemon import Pokemon
#importar clase tiposDePokemon
from Clases.tipos_de_pokemon import tiposDePokemon
class ataque(Pokemon):
#funcion is_alive(self) de la clase pokemon para saber si esta vivo o no

    def is_alive(self):
        if self.puntos_salud > 0:
            return True
        else:
            return False

#funcion fight_attack(self, id) de la clase pokemon para atacar a otro pokemon
    def fight_attack(self, id):
        if id == 1:
            self.puntos_salud -= self.indice_ataque
        elif id == 2:
            self.puntos_salud -= self.indice_ataque
        elif id == 3:
            self.puntos_salud -= self.indice_ataque
        elif id == 4:
            self.puntos_salud -= self.indice_ataque
        elif id == 5:
            self.puntos_salud -= self.indice_ataque
        elif id == 6:
            self.puntos_salud -= self.indice_ataque
#función  fight_attack(self, Pokémon pokemon_to_attack). Método que implementa el ataque del Pokémon usando un golpe sobre otro Pokémon. Este método se basa en el método fight_defense(self, int points_of_damage) del Pokémon atacado. Se aplicará el índice de ataque del Pokémon atacante como representación del golpe dado. Este método devolverá un booleano True si se ha podido atacar a la criatura Pokémon. 

    def fight_attack(self, pokemon_to_attack):
        if pokemon_to_attack.fight_defense(self.indice_ataque):
            return True
        if self.tipo == "Tierra":
                if random.randint(1, 2) == 1:
                    indice_ataque = self.indice_ataque * 2
                else:
                    indice_ataque = self.indice_ataque
        else:
            return False
        

#funcion fight_defense(self, int points_of_damage). Este método implementa la defensa del Pokémon de un golpe de otro Pokémon. Este método actualiza el atributo de puntos de salud que tiene el Pokémon en base a los puntos de daño recibidos menos el índice de defensa del propio Pokémon. Si el índice de defensa es mayor que los puntos de ataque recibidos, el método devolverá false y el Pokémon no sufrirá ningún daño. Este método devolverá un booleano True si se ha sufrido un ataque por parte de otra criatura Pokémon, y si el pokemon es tipo aire tiene un 50% de probabilidad de que no se sufra daño.
    def fight_defense(self, points_of_damage):
        if self.indice_defensa > points_of_damage:
            return False
        else:
            if self.tipo == "Aire":
                if random.randint(1, 2) == 1:
                    return False
                else:
                    self.puntos_salud -= points_of_damage - self.indice_defensa
                    return True
            else:
                self.puntos_salud -= points_of_damage - self.indice_defensa
                return True
    

