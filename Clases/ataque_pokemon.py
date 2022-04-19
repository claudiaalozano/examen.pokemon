import random

from Clases.pokemon import Pokemon

from Clases.tipos_de_pokemon import tiposDePokemon
class ataque(Pokemon):


    def is_alive(self):
        if self.puntos_salud > 0:
            return True
        else:
            return False


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
    

