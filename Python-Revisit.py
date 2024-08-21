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

type_interactions = {
    "Electric": [
        ["Water", "Flying"],  # Strong Against
        ["Ground"]            # Weak Against
    ],
    "Fire": [
        ["Grass", "Bug", "Ice", "Steel"],  # Strong Against
        ["Water", "Rock", "Fire"]          # Weak Against
    ],
    "Poison": [
        ["Grass", "Fairy"],                # Strong Against
        ["Poison", "Ground", "Psychic"]    # Weak Against
    ],
    "Water": [
        ["Fire", "Ground", "Rock"],       # Strong Against
        ["Electric", "Grass"]             # Weak Against
    ],
    "Normal": [
        [],                              # Strong Against
        ["Rock", "Steel"]                 # Weak Against
    ],
    "Fighting": [
        ["Normal", "Ice", "Rock", "Dark", "Steel"],  # Strong Against
        ["Flying", "Psychic", "Fairy"]               # Weak Against
    ],
    "Psychic": [
        ["Fighting", "Poison"],           # Strong Against
        ["Bug", "Ghost", "Dark"]          # Weak Against
    ]
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
            player_pokemon = pokemon_dictionary[character_selection_input.lower()]
            break
        else:
            print("No Selection Made")
            continue
    opponent_selection = rm.choice(list(pokemon_dictionary.keys()))
    print(f"Your Opponent's Pokemon is", end="")
    for i in range(3):
        t.sleep(0.8)
        print(".", end="")
    t.sleep(0.8)
    print(f"{pokemon_dictionary[opponent_selection][0]}!")
    opponent_pokemon = pokemon_dictionary[opponent_selection]

    player_power_base = player_pokemon[1]
    opponent_power_base = opponent_pokemon[1]
    if (opponent_pokemon[2] in type_interactions[player_pokemon[2]][0]) or (opponent_pokemon[2] in type_interactions[player_pokemon[2]][1]):
        print("Element Interaction Found!")
        if opponent_pokemon[2] in type_interactions[player_pokemon[2]][0]:
            player_power_base += rm.randint(0, 45)
            opponent_power_base -= rm.randint(0, 15)
            print(
                f"Player's pokemon element ({player_pokemon[2]}) is very effective against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                f"Player's Final Power: {player_power_base}\n"
                f"Opponent's Final Power: {opponent_power_base}")
        elif opponent_pokemon[2] in type_interactions[player_pokemon[2]][1]:
            opponent_power_base += rm.randint(0, 45)
            player_power_base -= rm.randint(0, 15)
            print(
                f"Player's pokemon element ({player_pokemon[2]}) is ineffective against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                f"Player's Final Power: {player_power_base}\n"
                f"Opponent's Final Power: {opponent_power_base}")
    else:
        opponent_power_base += rm.randint(-20, 45)
        player_power_base += rm.randint(-20, 45)
        print(
            f"Player's pokemon element ({player_pokemon[2]}) only deals normal damage against Opponent's pokemon element ({opponent_pokemon[2]})\n"
            f"Player's Final Power: {player_power_base}\n"
            f"Opponent's Final Power: {opponent_power_base}")

user_input = input("Welcome to Pokemon Battle Simulator (Terminal Edition)\n"
              "a). Play\n"
              "b). Help\n")

if user_input.lower() == "a":
    character_selection()
elif user_input.lower() == "b":
    print("Under Construction")
else:
    print("Invalid input selection")

