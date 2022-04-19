#funcion para id del pokemón, que es un número entero y único que identifica cada pokemon
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
    
#funcion para nombre del pokemón, que es una cadena de caracteres y que identifica cada pokemon
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

#funcion para tipo de arma que lleva cada pokemon. Hay cuatro tipos de arma: puñetazo, patada, codazo y cabezazo
def tipo_arma(id):
    if id == 1 or id == 4:
        return "cabezazo"
    elif id == 2 or id == 5:
        return "patada"
    elif id == 3 or id == 6: 
        return "codazo"

#funcion para los puntos de salud que tiene el pokemon. Debe de estar entre 1 y 100.
def puntos_salud(id):
    if id == 1 :
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

#funcion para el indice de ataque del Pokemon. Debe estar entre 1 y 10
def indice_ataque(id):
    if id == 1:
        return 8
    elif id == 2:
        return 7
    elif id == 3:
        return 7
    elif id == 4:
        return 9
    elif id == 5:
        return 8
    elif id == 6:
        return 9


#funcion para el indice de defensa del Pokemon. Debe estar entre 1 y 10
def indice_defensa(id):
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