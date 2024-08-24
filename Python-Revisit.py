# TO Do LIST
# Fix the typing effect to enable 'end' argument
# Make the same pokemon opponent stay if player lost
# If possible, make an 'add pokemon' feature that lets user add a customized name and the system will assign a base power to it
# Create a system where a win streak != forever winning
# CLEAN CODE!!!!

# INDICATE EVERY GLOBAL VARIABLE TO BE ARGUMENTS OF EACH FUNCTIONS !



import random as rm
import time as t
from tabulate import tabulate



def game_start():
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

    voicelines = [
    "After a destructive attack, the battlefield is in ruins!",
    "*Explosions echo through the arena!*",
    "In the blink of an eye, the tide of battle has turned!",
    "With a flash of lightning, the attack lands perfectly!",
    "The air is filled with tension as the Pokémon brace themselves!",
    "*The crowd gasps in shock!* What an unexpected move!",
    "Amidst the chaos, the Pokémon stands tall and unyielding!",
    "In an instant, the opponent's defenses are shattered!",
    "*A roar shakes the stadium!* This battle is far from over!",
    "With a single decisive strike, victory is within reach!"
    ]

    ending_voicelines = [
    "It's all over! What a battle that was!",
    "After a fierce struggle, we finally have a winner!",
    "The dust has settled, and victory belongs to one Trainer!",
    "With the last move, the battle comes to an explosive end!",
    "*Cheering erupts!* The winner stands tall in the arena!",
    "What an incredible display of strategy and power! The winner emerges!",
    "The losing Pokémon falls, and the battle is decided!",
    "After an intense showdown, the Trainer's journey ends here!",
    "The final attack lands, and the battle is won!",
    "It's a crushing defeat for one Trainer, but what an unforgettable battle!"
    ]
    battle_outcome = ""
    battle_history = []
    table_head = ["Match\nID", "User\nPokemon","User\nBase Power", "Buff/Nerf\n Points", "User\nFinal Power", "Opponent's\nPokemon","User\nBase Power", "Buff/Nerf\n Points", "Opponent's\nFinal Power", "Battle\nOutcome", "Post-User\nFinal Power", "Post-Opponent's\nFinal Power"]
    
    def typing_effect(text, delay=0.1): # Need to fix, Should consider putting 'end = ""' argument
        for char in text:
            print(char, end="", flush=True)
            t.sleep(delay)
        print()

    def character_selection (): # Done: Able to save Player's Pokemon
        while True:
            typing_effect("Please select your pokemon:")
            counter = 1
            for key in pokemon_dictionary:
                str_print = f"{key}). {pokemon_dictionary[key][0]}" + (" "*(13 - len(pokemon_dictionary[key][0])))
                if counter == 2:
                    str_print += "\n"
                    counter = 0
                print (str_print, end="")
                counter += 1
            character_selection_input = input("")
            if character_selection_input.lower() in pokemon_dictionary:
                typing_effect(f"Your Pokemon is {pokemon_dictionary[character_selection_input.lower()][0]}!")
                player_pokemon = pokemon_dictionary[character_selection_input.lower()]
                return player_pokemon
                
            else:
                print("No Selection Made")
                continue

    def opponent_character_selection(): #Done: Able to save Opponent's Pokemon
        opponent_selection = rm.choice(list(pokemon_dictionary.keys()))
        print(f"Your Opponent's Pokemon is", end="")
        for i in range(3):
            t.sleep(0.8)
            print(".", end="", flush = True)
        t.sleep(0.8)
        print(f"{pokemon_dictionary[opponent_selection][0]}!")
        opponent_pokemon = pokemon_dictionary[opponent_selection]
        return opponent_pokemon
    def power_computation(player_pokemon, opponent_pokemon, player_power_base = 0 , opponent_power_base = 0): #Done: Able to save player and opponent power base
        if player_power_base == 0:
            player_power_base = player_pokemon[1]
        if opponent_power_base == 0:
            opponent_power_base = opponent_pokemon[1]
        return player_power_base, opponent_power_base
    def element_interaction_buffsandnerfs(player_pokemon, opponent_pokemon, player_power_base, opponent_power_base): #Done: Able to save final power of both player and opponent
        if (opponent_pokemon[2] in type_interactions[player_pokemon[2]][0]) or (opponent_pokemon[2] in type_interactions[player_pokemon[2]][1]):
            print("Element Interaction Found!")
            if opponent_pokemon[2] in type_interactions[player_pokemon[2]][0]:
                player_buffornerf = rm.randint(0, 45)
                opponent_buffornerf = rm.randint(-15, 0)
                player_power_base += player_buffornerf
                opponent_power_base += opponent_buffornerf
                print(
                    f"Player's pokemon element ({player_pokemon[2]}) is very effective against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                    f"Player's Final Power: {player_power_base}\n" 
                    f"Opponent's Final Power: {opponent_power_base}")
            elif opponent_pokemon[2] in type_interactions[player_pokemon[2]][1]:
                player_buffornerf = rm.randint(-15, 0)
                opponent_buffornerf = rm.randint(0, 45)
                opponent_power_base += opponent_buffornerf
                player_power_base += player_buffornerf
                print(
                    f"Player's pokemon element ({player_pokemon[2]}) is ineffective against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                    f"Player's Final Power: {player_power_base}\n"
                    f"Opponent's Final Power: {opponent_power_base}")
        else:
            player_buffornerf = rm.randint(-20, 45)
            opponent_buffornerf = rm.randint(-20, 45)
            opponent_power_base += opponent_buffornerf
            player_power_base += player_buffornerf
            print(
                f"Player's pokemon element ({player_pokemon[2]}) only deals normal damage against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                f"Player's Final Power: {player_power_base}\n"
                f"Opponent's Final Power: {opponent_power_base}")
        return player_power_base, opponent_power_base, player_buffornerf, opponent_buffornerf
    def battle (player_pokemon , opponent_pokemon , final_player_power, final_opponent_power, voicelines = voicelines, ending_voicelines = ending_voicelines, match_id = 0):
        print("Commencing Battle in...", end= "")
        for i in range(3,0,-1):
            t.sleep(1)
            print(f"{i}", end="", flush = True)
            t.sleep(0.4)
            print(".", end="", flush = True)
            t.sleep(0.4)
            print(".", end="", flush = True)
            t.sleep(0.4)
            print(".", end="", flush = True)
        print()
        used_voiceline = []
        for _ in range(rm.randint(1,5)):
            t.sleep(rm.uniform(1,2))
            voicelines_num = rm.randint(1,9)
            while voicelines_num in used_voiceline:
                voicelines_num = rm.randint(1,9)
            typing_effect(voicelines[voicelines_num])
            used_voiceline.append(voicelines_num)
        typing_effect(rm.choice(ending_voicelines))
        post_opponent_power_base = 0
        post_player_power_base = 0
        
        if final_player_power > final_opponent_power:
            print("You Won!")
            print("As a result, your pokemon will now absorb the power base of the opponent's pokemon", end= "")
            for i in range(3):
                t.sleep(0.8)
                print(".", end="", flush= True)
            print()
            post_player_power_base +=  final_player_power + final_opponent_power
            print("Absorbed!")
            t.sleep(0.5)
            typing_effect(f"Your Pokemon ({player_pokemon[0]}) has a total of {post_player_power_base} base power!")
            battle_outcome = "won"
            post_opponent_power_base = 0
            
        elif final_player_power < final_opponent_power:
            print("You Lost.")
            print("As a result, your pokemon's base power will be absorbed by the opponent's pokemon", end= "")
            for i in range(3):
                t.sleep(0.8)
                print(".", end="", flush= True)
            print()
            post_opponent_power_base += final_player_power + final_opponent_power
            print("Absorbed.")
            t.sleep(0.8)
            typing_effect(f"Opponent's Pokemon ({opponent_pokemon[0]}) has a total of {post_opponent_power_base} base power!")
            battle_outcome = "lost"
            post_player_power_base = 0
            
        else:
            print("Nobody won.")
            print("Both of your pokemon died from the fight.")
            battle_outcome = "tie" 
            post_opponent_power_base = 0
            post_player_power_base = 0
            
        match_id += 1
        return battle_outcome , post_player_power_base, post_opponent_power_base, match_id
        # battle_history.append([match_id, player_pokemon[0], player_power_base, opponent_pokemon[0], opponent_power_base, battle_outcome, final_player_power_base, final_opponent_power_base])
        # if battle_outcome == "win":
        #     opponent_power_base = 0
        # elif battle_outcome =="lost":
        #     player_power_base = 0
        # elif battle_outcome == "tie":
        #     player_power_base = 0
        #     opponent_power_base  = 0
        
    user_input = input("Welcome to Pokemon Battle Simulator (Terminal Edition)\n"
              "a). Play\n"
              "b). Help\n")

    if user_input.lower() == "a":
        while True:
            player_pokemon = character_selection()
            opponent_pokemon = opponent_character_selection()
            player_power_base , opponent_power_base = power_computation(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon)
            final_player_power, final_opponent_power, player_buffornerf, opponent_buffornerf = element_interaction_buffsandnerfs(player_pokemon = player_pokemon, opponent_pokemon = opponent_pokemon, player_power_base = player_power_base, opponent_power_base = opponent_power_base)
            battle_outcome, post_player_power_base, post_opponent_power_base, match_id = battle(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon, final_player_power= final_player_power, final_opponent_power= final_opponent_power)
            battle_history.append([match_id, player_pokemon[0],player_power_base ,f"+{player_buffornerf}" if player_buffornerf > 0 else player_buffornerf, final_player_power, opponent_pokemon[0], opponent_power_base,f"+{opponent_buffornerf}"if opponent_buffornerf > 0 else opponent_buffornerf, final_opponent_power, battle_outcome, post_player_power_base, post_opponent_power_base])
            player_power_base = post_player_power_base
            opponent_power_base = post_opponent_power_base
            while True:
                typing_effect("Do you want to continue battling?")
                print(f"Enter the following keys of your selection:\n'c' : Change Character\n'x' : Exit Program\n'm' : Monitor History\n", end = "")
                if battle_outcome == "won":
                    print(f"'y' : Continue")
                user_choice = input()
                if user_choice.lower() == "m":
                    print(tabulate(battle_history, headers= table_head, tablefmt="pretty"))
                    input("Enter any key to go back.")
                    continue
                elif user_choice.lower() =="y":
                    if battle_outcome == "won":
                        opponent_pokemon = opponent_character_selection()
                        player_power_base, opponent_power_base = power_computation(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon, player_power_base= player_power_base, opponent_power_base= opponent_power_base)
                        final_player_power, final_opponent_power = element_interaction_buffsandnerfs(player_pokemon = player_pokemon, opponent_pokemon = opponent_pokemon, player_power_base = player_power_base, opponent_power_base = opponent_power_base)
                        battle_outcome, post_player_power_base, post_opponent_power_base, match_id = battle(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon, final_player_power= final_player_power, final_opponent_power= final_opponent_power, match_id= match_id)
                        battle_history.append([match_id, player_pokemon[0], final_player_power, opponent_pokemon[0], final_opponent_power, battle_outcome, post_player_power_base, post_opponent_power_base])
                        player_power_base = post_player_power_base
                        opponent_power_base = post_opponent_power_base
                        continue
                    else:
                        print("Invalid Input.")
                   
                elif user_choice.lower()== "x":
                    quit()

                else:
                    print("Invalid Input.")
        
        
    elif user_input.lower() == "b":
        print("Under Construction")
    else:
        print("Invalid input selection")
    
    
# 

    
#     
    
#     
#     
#     
#     # table_head = ["Match ID", "User Pokemon", "User Final Power", "Opponent's Pokemon", "Opponent's Final Power", "Battle Outcome", "Post-User Final Power", "Post-Opponent's Final Power"]
#     
game_start()

