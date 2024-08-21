import random as rm
import time as t
pokemon_dictionary = {
    "a": ["Pikachu", 50, "Electric"],
    "b": ["Charmander", 55, "Fire"],
    "c": ["Bulbasaur", 60, "Poison"],
    "d": ["Squirtle", 58, "Water"],
    "e": ["Jigglypuff", 45, "Normal"],
    "f": ["Eevee", 52, "Normal"],
    "g": ["Snorlax", 80, "Normal"],
    "h": ["Gengar", 70, "Poison"],
    "i": ["Machamp", 75, "Fighting"],
    "j": ["Mewtwo", 90, "Psychic"]
    }
def character_selection ():
    while True:
        print("Please select your pokemon:")
        counter = 1
        for key in pokemon_dictionary:
            str_print = f"{key}). {pokemon_dictionary[key][0]}" + (" "*(13 - len(pokemon_dictionary[key][0])))
            if counter == 2:
                str_print += "\n"
                counter = 0
            print (str_print, end="")
            counter += 1

        character_selection_input = input("")
        if character_selection_input.lower() in list(pokemon_dictionary.keys()):
            print(f"Your Pokemon is {pokemon_dictionary[character_selection_input.lower()][0]}")
            break
        else:
            print("No Selection Made")
            continue
    opponent_selection()

def opponent_selection():
    opponent_pokemon = rm.choice(list(pokemon_dictionary.keys()))
    print(f"Your Opponent's Pokemon is", end="")
    for i in range(3):
        t.sleep(0.8)
        print(".", end="")
    t.sleep(0.8)
    print(f"{pokemon_dictionary[opponent_pokemon][0]}!")





user_input = input("Welcome to Pokemon Battle Simulator (Terminal Edition)\n"
              "a). Play\n"
              "b). Help\n")

if user_input.lower() == "a":
    character_selection()
elif user_input.lower() == "b":
    print("Under Construction")
else:
    print("Invalid input selection")

