class pokemon:

    def id_pokemon(nombre):
        if nombre == "Pikachu":
            return 1
        elif nombre == "Pidgey":
            return 2
        elif nombre == "Squirtle":
            return 3
        elif nombre == "Diglett":
            return 4
        elif nombre == "Venusaur":
            return 5
        elif nombre == "Charmeleon":
            return 6
    

    def nombre_pokemon(id):
        if id == 1:
            return "Pikachu"
        elif id == 2:
            return "Pidgey"
        elif id == 3:
            return "Squirtle"
        elif id == 4:
            return "Diglett"
        elif id == 5:
            return "Venusaur"
        elif id == 6:
            return "Charmeleon"


    def set_tipo_arma(id, valor):
        if id == 1:
            return "cabezazo"
        elif id == 2:
            return "patada"
        elif id == 3:
            return "codazo"
        elif id == 4:
            return "cabezazo"
        elif id == 5:
            return "patada"
        elif id == 6:
            return "codazo"



    def set_puntos_salud(id, valor):
        if id == 1:
            return 69
        elif id == 2:
            return 85
        elif id == 3:
            return 74
        elif id == 4:
            return 82
        elif id == 5:
            return 78
        elif id == 6:
            return 88




    def set_indice_ataque(id, valor):
        if id == 1:
            return 9
        elif id == 2:
            return 8
        elif id == 3:
            return 7
        elif id == 4:
            return 8
        elif id == 5:
            return 7
        elif id == 6:
            return 8



    def set_indice_defensa(id, valor):
        if id == 1:
            return 8
        elif id == 2:
            return 7
        elif id == 3:
            return 6
        elif id == 4:
            return 7
        elif id == 5:
            return 6
        elif id == 6:
            return 7
