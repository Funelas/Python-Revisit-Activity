# Note before using :
# Install tabulate first by typing the code below in your terminal
# pip install tabulate 

import random as rm
import time as t
from tabulate import tabulate



def game_start():
    # List of the Available Pokemons to be picked
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
    "j": ["Mewtwo", 90, "Psychic"],
    "k": ["Articuno", 70, "Ice"],
    "l": ["Geodude", 40, "Rock"],
    "m": ["Umbreon", 60, "Dark"],
    "n": ["Steelix", 75, "Steel"],
    "o": ["Clefairy", 60, "Fairy"],
    "p": ["Butterfree", 60, "Bug"],
    "q": ["Leafeon", 65, "Grass"],
     "r": ["Jolteon", 65, "Electric"],
    "s": ["Electrode", 60, "Electric"],
    "t": ["Vulpix", 50, "Fire"],
    "u": ["Arcanine", 80, "Fire"],
    "v": ["Lapras", 80, "Water"],
    "w": ["Gyarados", 95, "Water"],
    "x": ["Nidoking", 81, "Poison"],
    "y": ["Hitmonchan", 50, "Fighting"],
    "z": ["Alakazam", 55, "Psychic"]
    }
    
    # List of the Interactions of some Elements
    type_interactions = {
    "Electric": [
        ["Water"],                         # Strong Against
        []                                # Weak Against
    ],
    "Fire": [
        ["Grass", "Bug", "Ice", "Steel"], # Strong Against
        ["Water", "Rock", "Fire"]         # Weak Against
    ],
    "Poison": [
        ["Grass", "Fairy"],               # Strong Against
        ["Poison", "Psychic"]             # Weak Against
    ],
    "Water": [
        ["Fire", "Rock"],                 # Strong Against
        ["Electric", "Grass"]             # Weak Against
    ],
    "Normal": [
        [],                              # Strong Against
        ["Rock", "Steel"]                 # Weak Against
    ],
    "Fighting": [
        ["Normal", "Ice", "Rock", "Dark", "Steel"], # Strong Against
        ["Psychic", "Fairy"]              # Weak Against
    ],
    "Psychic": [
        ["Fighting", "Poison"],           # Strong Against
        ["Bug", "Dark"]                   # Weak Against
    ],
    "Ice": [
        ["Grass", "Dragon"],              # Strong Against
        ["Fire", "Steel"]                 # Weak Against
    ],
    "Rock": [
        ["Fire", "Bug", "Ice"],           # Strong Against
        ["Fighting", "Steel"]             # Weak Against
    ],
    "Dark": [
        ["Psychic", "Dark"],              # Strong Against
        ["Fighting", "Bug", "Fairy"]     # Weak Against
    ],
    "Steel": [
        ["Ice", "Rock", "Fairy"],         # Strong Against
        ["Fire", "Water", "Electric"]    # Weak Against
    ],
    "Fairy": [
        ["Fighting", "Bug", "Dark"],      # Strong Against
        ["Poison", "Steel"]               # Weak Against
    ],
    "Bug": [
        ["Grass", "Psychic", "Dark"],     # Strong Against
        ["Fire", "Rock"]                  # Weak Against
    ],
    "Grass": [
        ["Water", "Rock"],                # Strong Against
        ["Fire", "Bug"]                   # Weak Against
    ]
}

    # List of possible Voicelines during battle
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

    #List of possible ending voicelines during battle
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
    battle_history = [] # Storage of the data that will be displayed in rows of the table
    
    # Header of the table (argument for the tabulate method)
    table_head = ["Match\nID", "User\nPokemon","User\nBase Power", "Buff/Nerf\n Points", "User\nFinal Power", "Opponent's\nPokemon","User\nBase Power", "Buff/Nerf\n Points", "Opponent's\nFinal Power", "Battle\nOutcome", "Post-User\nFinal Power", "Post-Opponent's\nFinal Power"]
    
    def typing_effect(text, delay=0.1, end = False): # Used to show typing effect when printing a statement.
        for char in text:
            print(char, end="", flush=True)
            t.sleep(delay)
        if end:
            print(end= "")
        else:
            print()

    def character_selection (): # Used to select a character for the player.
        while True:
            typing_effect("Please select your pokemon:")
            counter = 1
            for key in pokemon_dictionary: # Display every pokemon within our dictionary with the format : <letter-key>). <Pokemon-Name> (<Pokemon-Element)
                pokemon_string = f"{key}). {pokemon_dictionary[key][0]} ({pokemon_dictionary[key][2]})"
                str_print = pokemon_string + (" "*(30 - len(pokemon_string)))
                if counter == 3:
                    str_print += "\n"
                    counter = 0
                print (str_print, end="")
                counter += 1
            print()
            character_selection_input = input("User Input: ")
            if character_selection_input.lower() in pokemon_dictionary: # Check if user input is available
                typing_effect(f"Your Pokemon is {pokemon_dictionary[character_selection_input.lower()][0]}!")
                player_pokemon = pokemon_dictionary[character_selection_input.lower()]
                return player_pokemon
                
            else:
                print("No Selection Made")
                continue

    def opponent_character_selection(): # Used to generate a pokemon to the opponent
        opponent_selection = rm.choice(list(pokemon_dictionary.keys())) # Edit and put the letter of your choice pokemon if you want it to be set manually rather than randomly (original = rm.choice(list(pokemon_dictionary.keys())) )
        typing_effect(f"Your Opponent's Pokemon is", end= True)
        for i in range(3):
            t.sleep(0.8)
            print(".", end="", flush = True)
        t.sleep(0.8)
        typing_effect(f"{pokemon_dictionary[opponent_selection][0]}!")
        opponent_pokemon = pokemon_dictionary[opponent_selection]
        return opponent_pokemon
    def power_computation(player_pokemon, opponent_pokemon, player_power_base , opponent_power_base): # This is used to compute for a new power base if either the opponent or the player has been lost. If the power is 0, they will be having the base power of their pokemon, else they will have the current power of their pokemon.
        if player_power_base == 0:
            player_power_base = player_pokemon[1]
        if opponent_power_base == 0:
            opponent_power_base = opponent_pokemon[1]
        return player_power_base, opponent_power_base
    def element_interaction_buffsandnerfs(player_pokemon, opponent_pokemon, player_power_base, opponent_power_base): # Used for computing the random variation to the power of the pokemon
        # The mechanics of the power variation will depend on how great a pokemon's power is. This procedure will make greater powered pokemons to be less susceptible to random variation, therefore only getting minor buff or nerf. In summary, the greater your power, the less prone you are from getting a big buff or nerf, giving chance to newly selected pokemon to win even though one has already big power.
        # For example Pikachu has 50 power and Machamp has 200 power, this mechanics will make Pikachu be able to receive buff ranging from 0 - 200, while only making Machamp be only receiving power ranging from 0 - 50 ( This will be the exact case if it happens that both of the pokemons' element does not have any interaction.)
        lower_limit = player_power_base if player_power_base < opponent_power_base else opponent_power_base
        if (opponent_pokemon[2] in type_interactions[player_pokemon[2]][0]) or (opponent_pokemon[2] in type_interactions[player_pokemon[2]][1]):
            typing_effect("Element Interaction Found!")
            if opponent_pokemon[2] in type_interactions[player_pokemon[2]][0]:      
                player_buffornerf = rm.randint(0, opponent_power_base)
                opponent_buffornerf = rm.randint(-lower_limit, 0)
                player_power_base += player_buffornerf
                opponent_power_base += opponent_buffornerf
                typing_effect(
                    f"Player's pokemon element ({player_pokemon[2]}) is very effective against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                    f"Player's Final Power: {player_power_base}\n" 
                    f"Opponent's Final Power: {opponent_power_base}")
            elif opponent_pokemon[2] in type_interactions[player_pokemon[2]][1]:
                player_buffornerf = rm.randint(-lower_limit, 0)
                opponent_buffornerf = rm.randint(0, player_power_base)
                opponent_power_base += opponent_buffornerf
                player_power_base += player_buffornerf
                typing_effect(
                    f"Player's pokemon element ({player_pokemon[2]}) is ineffective against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                    f"Player's Final Power: {player_power_base}\n"
                    f"Opponent's Final Power: {opponent_power_base}")
        else:
            player_buffornerf = rm.randint(-lower_limit, opponent_power_base)
            opponent_buffornerf = rm.randint(-lower_limit, player_power_base)
            opponent_power_base += opponent_buffornerf
            player_power_base += player_buffornerf
            typing_effect(
                f"Player's pokemon element ({player_pokemon[2]}) only deals normal damage against Opponent's pokemon element ({opponent_pokemon[2]})\n"
                f"Player's Final Power: {player_power_base}\n"
                f"Opponent's Final Power: {opponent_power_base}")
        return player_power_base, opponent_power_base, player_buffornerf, opponent_buffornerf
    
    def battle (player_pokemon , opponent_pokemon , final_player_power, final_opponent_power, voicelines = voicelines, ending_voicelines = ending_voicelines): # Used for simulating the battle, showing voicelines and the conclusion of the battle
        typing_effect("Commencing Battle in...", end= True, delay= 0.05)
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
        used_voiceline = [] # Storage of voicelines that's been already used
        for _ in range(rm.randint(1,5)): # Shows how many times the voiceline will run
            t.sleep(rm.uniform(1,2))
            voicelines_num = rm.randint(1,9) # Process of selection of voiceline
            while voicelines_num in used_voiceline: # If voiceline is already in the used_voiceline storage, the voiceline will be rerolled
                voicelines_num = rm.randint(1,9)
            typing_effect(voicelines[voicelines_num], delay= 0.05)
            used_voiceline.append(voicelines_num) # Adding the used voiceline in the storage
        typing_effect(rm.choice(ending_voicelines))
        post_opponent_power_base = 0    # Intialization
        post_player_power_base = 0      # Intialization 
        
        if final_player_power > final_opponent_power:
            typing_effect("You Won!")
            typing_effect("As a result, your pokemon will now absorb the power base of the opponent's pokemon", end= True)
            for i in range(3):
                t.sleep(0.8)
                print(".", end="", flush= True)
            print()
            post_player_power_base +=  final_player_power + final_opponent_power
            typing_effect("Absorbed!")
            t.sleep(0.5)
            typing_effect(f"Your Pokemon ({player_pokemon[0]}) has a total of {post_player_power_base} base power!")
            battle_outcome = "won"
            post_opponent_power_base = 0
            opponent_pokemon = ""
            
        elif final_player_power < final_opponent_power:
            typing_effect("You Lost.")
            typing_effect("As a result, your pokemon's base power will be absorbed by the opponent's pokemon", end= True)
            for i in range(3):
                t.sleep(0.8)
                print(".", end="", flush= True)
            print()
            post_opponent_power_base += final_player_power + final_opponent_power
            typing_effect("Absorbed.")
            t.sleep(0.8)
            typing_effect(f"Opponent's Pokemon ({opponent_pokemon[0]}) has a total of {post_opponent_power_base} base power!")
            battle_outcome = "lost"
            post_player_power_base = 0
            player_pokemon = ""
            
        else:
            print("Nobody won.")
            print("Both of your pokemon was exhausted from the fight.")
            battle_outcome = "tie" 
            post_opponent_power_base = 0
            post_player_power_base = 0
            
        
        return battle_outcome , post_player_power_base, post_opponent_power_base
    def play (player_pokemon, opponent_pokemon, player_power_base, opponent_power_base, match_id):
        match_id += 1
        if player_pokemon == "":
            player_pokemon = character_selection()
        if opponent_pokemon == "":
            opponent_pokemon = opponent_character_selection()
        player_power_base , opponent_power_base = power_computation(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon, player_power_base= player_power_base, opponent_power_base= opponent_power_base)
        final_player_power, final_opponent_power, player_buffornerf, opponent_buffornerf = element_interaction_buffsandnerfs(player_pokemon = player_pokemon, opponent_pokemon = opponent_pokemon, player_power_base = player_power_base, opponent_power_base = opponent_power_base)
        battle_outcome, post_player_power_base, post_opponent_power_base = battle(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon, final_player_power= final_player_power, final_opponent_power= final_opponent_power)
        battle_history.append([match_id, player_pokemon[0],player_power_base ,f"+{player_buffornerf}" if player_buffornerf > 0 else player_buffornerf, final_player_power, opponent_pokemon[0], opponent_power_base,f"+{opponent_buffornerf}"if opponent_buffornerf > 0 else opponent_buffornerf, final_opponent_power, battle_outcome, post_player_power_base, post_opponent_power_base]) # Process of adding data to our battle history storage, which will also be the basis for the rows of our table 
        player_power_base = post_player_power_base
        opponent_power_base = post_opponent_power_base
        return player_pokemon, opponent_pokemon , player_power_base, opponent_power_base , battle_outcome, match_id
        
    
    
    def main_menu():
        match_id = 0
        while True:
            typing_effect("Welcome to Pokemon Battle Simulator (Terminal Edition)", delay= 0.05)
            print("a). Play\nb). Help\n")
            user_input = input("User Input: ")
            if user_input.lower() == "a":
                player_pokemon = ""
                opponent_pokemon = ""
                player_power_base = 0
                opponent_power_base = 0
                play_break = False # Will be used to break the while loop starting from when the play() function is called
                while True:
                    player_pokemon, opponent_pokemon, player_power_base, opponent_power_base, battle_outcome, match_id = play(player_pokemon= player_pokemon, opponent_pokemon= opponent_pokemon, player_power_base= player_power_base, opponent_power_base= opponent_power_base, match_id= match_id)
                    while True:
                        typing_effect("Do you want to continue battling?")
                        print("Enter the following keys of your selection:\n'n' : New / Change Character\n'x' : Exit Program\n'm' : Monitor History\n'r' : Restart\n'u' : Main Menu\n", end = "")
                        if battle_outcome == "won":
                            print("'c' : Continue")
                        user_choice = input("User Input: ")
                        if user_choice.lower() == "m":
                            print(tabulate(battle_history, headers= table_head, tablefmt="pretty")) # Process of tabulating the data we currently have
                            input("Enter any key to go back.")
                            continue
                        elif user_choice.lower() =="c":
                            if battle_outcome == "won": # Rerunning the same code but this time, player will still have the same pokemon with the same power
                                opponent_pokemon = ""
                                opponent_power_base = 0
                                break
                            else:
                                print("Invalid Input.")
                                continue
                        elif user_choice.lower() == "n":
                            if battle_outcome == "won":
                                typing_effect("Are you sure?")
                                typing_effect("WARNING: You will lose your pokemon's current power if you proceed.")
                                print("Press the key of your preferred selection:\n'b' : Go back\n'p' : Proceed")
                                change_input = input("User Input: ")
                                if change_input.lower() == "b":
                                    continue
                                elif change_input.lower() == "p": # Rerunning the code but this time, both the opponent and the player will change pokemon
                                    opponent_pokemon = ""
                                    opponent_power_base = 0
                            # Rerunning the code but only changing the player's pokemon and the opponent's pokemon stays the same
                            player_pokemon = ""
                            player_power_base = 0
                            break
                        
                        elif user_choice.lower()== "x": # Used to closing the program
                            while True:
                                typing_effect("Are you sure?")
                                typing_effect("WARNING: You will lose your whole progress if you quit.")
                                print("Press the key of your corresponding selection:\n'b' : Go back\n'q' : Quit")
                                quit_input = input("User Input: ")
                                if quit_input.lower() == 'q':
                                    typing_effect("Thank you for playing the game! See you next time.")
                                    t.sleep(1)
                                    quit()
                                elif quit_input.lower() == 'b':
                                    break 
                                else:
                                    print('Invalid Input')
                                    continue
                        elif user_choice.lower() == 'r': # Used for restarting both player and opponent pokemon and power bases
                            while True:
                                typing_effect("Are you sure?")
                                typing_effect("WARNING: Restarting will reset both the pokemon and power bases of both the player and opponent")
                                print("Press the key of your preferred selection:\n'b' : Go back\n'p' : Proceed")
                                change_input = input("User Input: ")
                                if change_input.lower() == "b":
                                    break
                                elif change_input.lower() == "p":
                                    opponent_pokemon = ""
                                    opponent_power_base = 0
                                    player_pokemon = ""
                                    player_power_base = 0
                                break
                            break
                        elif user_choice.lower() == 'u': # Used for going back to the main menu
                            while True:
                                typing_effect("Are you sure?")
                                typing_effect("WARNING: Going back to the main menu will reset the player and the opponent's pokemon and power bases")
                                print("Press the key of your preferred selection:\n'b' : Go back\n'p' : Proceed")
                                menu_choice = input()
                                if menu_choice.lower() == "b":
                                    break
                                elif menu_choice.lower() == "p":
                                    opponent_pokemon = ""
                                    opponent_power_base = 0
                                    player_pokemon = ""
                                    player_power_base = 0
                                    match_id = match_id
                                    play_break = True # Used to enable break in the play loop when the player proceeds
                                    break
                            break
                        else:
                            print("Invalid Input.")
                            continue 
                        
                    if play_break: # A gate if the play loop will either close or continue to run
                        break
                    
            elif user_input.lower() == "b": # The Help Information Content
                print("""Welcome to Pokemon Battle Simulator (Terminal Edition) where you fight with a randomly generated pokemon and rely
on RNG (Random Number Generator) to win the battles!
To start, you will be choosing your pokemon by entering the corresponding letter of the pokemon.

Example:
a). Pikachu         b). Charmander

Entering 'a' will have you selecting Pikachu, otherwise, the corresponding pokemon of your selected letter.
After you choose a pokemon, the computer will prompt a message showing the pokemon selected by the opponent which is
randomly selected. \n\n""")
                input("Enter any key to continue: ")
                
                print("""\n\nAfter both the player and the opponent has selected a pokemon, they will be assessed if their elements have interaction.
The following are the Elements and their Interactions:
        
Electric Type:                          Fire Type:                                          Grass Type:
- Strong Against: Water                 - Strong Against: Grass, Bug, Ice, Steel            - Strong Against: Water, Rock    
- Weak Against: None                    - Weak Against: Water, Rock, Fire                   - Weak Against: Fire, Bug 

Poison Type:                            Water Type:                                         Bug Type:                                
- Strong Against: Grass, Fairy          - Strong Against: Fire, Rock                        - Strong Against: Grass, Psychic, Dark   
- Weak Against: Poison, Psychic         - Weak Against: Electric, Grass                     - Weak Against: Fire, Rock        

Normal Type:                            Fighting Type:                                      Fairy Type:
- Strong Against: None                  - Strong Against: Normal, Ice, Rock, Dark, Steel    - Strong Against: Fighting, Bug, Dark
- Weak Against: Rock, Steel             - Weak Against: Psychic, Fairy                      - Weak Against: Poison, Steel

Psychic Type:                           Ice Type:                                           Steel Type: 
- Strong Against: Fighting, Poison      - Strong Against: Grass, Dragon                     - Strong Against: Ice, Rock, Fairy   
- Weak Against: Bug, Dark               - Weak Against: Fire, Steel                         - Weak Against: Fire, Water, Electric

Rock Type:                              Dark Type:
- Strong Against: Fire, Bug, Ice        - Strong Against: Psychic, Dark 
- Weak Against: Fighting, Steel         - Weak Against: Fighting, Bug, Fairy
    \n""")
                input("Enter any key to continue: ")
                print("""\nChoosing a good elemental pokemon might also be one of the way to have your win!

If you are faced with an element that you are STRONG against, you will have a chance to have a buff points ranging from 0 to the number equal
to the opponent's base power, which is pretty big if you are against someone who have high power base. Beside this buff, the opponent's pokemon will
also receive a nerf points ranging from negative number equal to the base power of the weaker pokemon up to 0.

Example:
Player has a Machamp Pokemon ( Base power of 75 )
Opponent has an Articuno Pokemon ( Base power of 70 )
Machamp's Element is STRONG against Articuno's Element

Machamp's Final power = Machamp's base power + random number ranging from 0 to 70 ( Base power of the opponent )
Articuno's Final power = Articuno's base power - random number ranging from 0 to 70 ( Base power of the weaker pokemon )


On the other hand, if you are faced with a pokemon that you are WEAK against, the buff and nerf system will happen vice versa. 


If somehow the player and the opponent's pokemon elements does not have any interaction with each other, they will rather receive either a buff or a nerf ranging from negative value equal to the base power of the weaker pokemon up to the base power of the player or opponent.

Example:
Player has a Articuno Pokemon ( Base power of 75 )
Opponent has a Hitmonchan Pokemon ( Base power of 50 )

Articuno's Final power = Articuno's base power + random number ranging from -50 ( Base power of the weaker pokemon ) to 50 ( Base power of the opponent pokemon )
Hitmonchan's Final power = Hitmonchan's base power + random number ranging from -50 ( Base power of the weaker pokemon ) to 70 ( Base power of the player pokemon )

This system can help improve battle fairness when it comes to winsreaks/losestreaks. The randomness also helps lowering chance of a tie.\n""")
                input("Enter any key to continue: ")
                print("""\nAfter the final power of each pokemons are computed, they will now engage to a combat. Take note that the pokemon
that has the LARGER or GREATER power will WIN.\n""")
                input("Enter any key to continue: ")
                print("""\nAfter the combat, the pokemon with the greater power will consume the power of the weaker one. Therefore increasing 
your odds to win the next games. But if you happen to lose, your opponent will be the one to absorb your power, which can be troublesome
to your next game.\n""")
                input("Enter any key to continue: ")
                print("""\nAfter the winning pokemon absorbs the power of the losing pokemon, the battle is officially over. You will be 
prompted then with a message with the following:
Enter the following keys of your selection:
'n' : Change Character
'x' : Exit Program
'm' : Monitor History
'r' : Restart
'u' : Main Menu
'c' : Continue (If you happen to win the battle)

Choosing 'n' will have you change your pokemon. WARNING: If you choose to change your pokemon when you won a battle will
make you lose the power you currently have. This will still make you face the same opponent.
Choosing 'x' will make you exit the program and lose all the progress you and the opponent made.
Choosing 'm' will have you look at the history tab of all the matches you and the opponent made. You can look at all the
details such as pokemon used, base power, final power, buff or nerf points and more. 
Choosing 'r' will make you restart the game, setting both the opponent and player pokemon new and their power bases back to their 
original value.
Choosing 'u' will have you go back to the main menu.
Choosing 'c' will have you continue battling with the same pokemon you used in the previous battle with the absorbed
power from all the pokemon you fought previously.\n
    """)
                input("Enter any key to continue: ")
                print("""\n[Some tips]
If you have lost, take note of their element and compare which pokemon element they are weak against. You can use this to
have an edge in the battle
If you are stuck and think that the battle is unwinnable, just restart the program by closing or rerunning it. 
~~More updates in the future. GOOD LUCK AND HAVE FUN!!!~~\n""")
                input("Enter any key to continue: ")
                continue
            else:
                print("Invalid input selection")
    main_menu()
game_start() # To call the start of the game