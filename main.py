 
from Clases.ataque_pokemon import ataque
from Clases.pokemon import pokemon
from Clases.tipos_de_pokemon import tiposDePokemon
import csv

if __name__ == "__main__" :
  print("Comienza el juego.")
  
  def elegir_coach():
    with open('coach.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        print(row)
    coach = input("Elige un coach: ")
    return coach
  
  def elegir_pokemon():
    with open('pokemon.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        print(row)
    pokemon = input("Elige un pokemon: ")
    return pokemon
  
  def comenzar_ataques(pokemon_elegido, pokemon_aleatorio):
    ataque_elegido = ataque(pokemon_elegido)
    ataque_aleatorio = ataque(pokemon_aleatorio)
    ataque_elegido.ataque_elegido()
    ataque_aleatorio.ataque_aleatorio()
    return ataque_elegido, ataque_aleatorio
  
  
  def mostrar_pokemon(pokemon_elegido, pokemon_aleatorio):
    print("El pokemon elegido es: ", pokemon_elegido)
    print("El pokemon aleatorio es: ", pokemon_aleatorio)
    print("El pokemon elegido esta vivo: ", pokemon_elegido.is_alive())
    print("El pokemon aleatorio esta vivo: ", pokemon_aleatorio.is_alive())
    print("El pokemon elegido tiene: ", pokemon_elegido.puntos_salud, " puntos de salud")
    print("El pokemon aleatorio tiene: ", pokemon_aleatorio.puntos_salud, " puntos de salud")
    return pokemon_elegido, pokemon_aleatorio
  

  