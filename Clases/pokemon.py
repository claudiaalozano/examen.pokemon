class pokemon:
    def __init__(self, nombre, id, ataque, defensa, salud):
        self.nombre = nombre
        self.id = id
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
    def atacar(self, pokemon):
        pokemon.salud -= self.ataque
    def defender(self, pokemon):
        self.salud -= pokemon.ataque
    def get_nombre(self):
        return self.nombre
    def get_id(self):
        return self.id
    def get_ataque(self):
        return self.ataque
    def get_defensa(self):
        return self.defensa
    def get_salud(self):
        return self.salud
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_id(self, id):
        self.id = id
    def set_ataque(self, ataque):
        self.ataque = ataque
    def set_defensa(self, defensa):
        self.defensa = defensa
    def set_salud(self, salud):
        self.salud = salud

    
    def is_alive(self):
        if self.salud > 0:
            return True
        else:
            return False

    def __str__(self):
        return "Nombre: " + self.nombre + "\nID: " + str(self.id) + "\nAtaque: " + str(self.ataque) + "\nDefensa: " + str(self.defensa) + "\nSalud: " + str(self.salud)
        
