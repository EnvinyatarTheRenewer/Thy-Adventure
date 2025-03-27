############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

###### FANTASY GAME: Thy adventure ######

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

###### Charcter design ######

import random
# Basic characteristics:
life_total = 14
short_range_attack = 1
long_range_attack = 1
class_ability_1 = "none"
class_ability_2 = "none"

# Function to generate random stats between 5 and 20
def get_stat():
    return random.randint(5, 20)

# Function to choose race
def choose_race():
    races = {
        "Dwarf": "Stout folk of the mountains, their resilience is unmatched. Dwarves are smaller in stature, slower in movement,\nyet boast great fortitude and might in battle.",
        "Elf": "Graceful and swift, elves are masters of the bow and of wisdom. Their speed is unmatched, and their minds keen.",
        "Hobbit": "Small and unassuming, but quick and discrete. Hobbits are nimble folk, preferring quiet paths to shadowy \nthreats. They are excellent cook and have an unmatched love for food.",
        "Human": "Versatile and ambitious, humans are well-rounded warriors. Adept in both blade and bow, they stand firm but \nlack deep wisdom.",
        "Ent": "Ancient shepherds of the forest, Ents are mighty and wise. Towering over others, they move slowly yet endure \nmuch." 
    }
    
    while True:
        print("\nPlease choose your race:")
        for race, desc in races.items():
            print(f"- {race}: {desc}")
        race = input("What race dost thou choose? ").capitalize()
        if race in races:
            return race
        print("Thou hast spoken unwisely. Choose again.")

# Function to choose class
def choose_class():
    classes = {
        "Wizard": "Wielders of arcane might, wizards command lightning and sway minds with but a word. With a magical staff, they \nmay mend their own wounds.",
        "Rogue": "Masters of subtlety, rogues strike from the shadows and move unseen. Their dexterity and cunning give them an \nedge.",
        "Bard": "Weavers of song and speech, bards inspire allies and break foes' spirits with cutting words. If they wield a \nbagpipe, their charisma grows stronger.",
        "Ranger": "Wilderness warriors, rangers track their foes with ease and wield both bow and blade deftly. They possess the \nknowledge to mend wounds on their journey.",
        "Fighter": "Champions of combat, fighters are clad in armor and strike with great force. Their might is unmatched in \nbattle." 
    }
    
    while True:
        print("\nPlease choose your class:")
        for char_class, desc in classes.items():
            print(f"- {char_class}: {desc}")
        char_class = input("What path dost thou walk? ").capitalize()
        if char_class in classes:
            return char_class
        print("That is not a path known to these lands. Choose again.")

# Function to choose weapons
def choose_weapon():
    weapons = {
        "Pan": {"short_attack": 1},
        "Magical Staff": {"long_attack": 1},
        "Bow": {"long_attack": 2},
        "Sword": {"short_attack": 2},
        "Dagger": {"short_attack": 1},
        "Axe": {"short_attack": 2},
        "Spear": {"long_attack": 2},
        "Sling": {"long_attack": 1}
    }
    
    print("\nYou will have to pick two weapons, traveler. One of reach and one of might. Take heed of your choice, \nfor it may shape thy fate.")
    input("Press Enter when thou art ready.")
    
    print("\nMelee weapons:")
    melee_weapons = {k: v for k, v in weapons.items() if "short_attack" in v}
    for weapon, stats in melee_weapons.items():
        print(f"- {weapon}: Deals +{stats['short_attack']} in close combat.")
    
    while True:
        short_weapon = input("Which weapon dost thou wield in battle? ").title()
        if short_weapon in melee_weapons:
            break
        print("That is not a weapon forged by the smiths of old. Choose again.")
    
    print("\nRanged weapons:")
    ranged_weapons = {k: v for k, v in weapons.items() if "long_attack" in v}
    for weapon, stats in ranged_weapons.items():
        print(f"- {weapon}: Deals +{stats['long_attack']} from afar.")
    
    while True:
        long_weapon = input("And what dost thou fire upon thine enemies? ").title()
        if long_weapon in ranged_weapons:
            break
        print("That is not a weapon known to the marksmen of the realm. Choose again.")
    
    return short_weapon, long_weapon

# Character Creation
print("\nWelcome, traveler. Speak thy name, so that history may remember thee... (chapter 0)")
character_name = input("What is thy name? ")
print("------------------------------------------------------------------------------------------------------------------------")
print(f"\nWell met, {character_name}. Let us forge thy fate in this realm of peril and wonder.")

race = choose_race()
print("------------------------------------------------------------------------------------------------------------------------")
char_class = choose_class()
print("------------------------------------------------------------------------------------------------------------------------")
short_weapon, long_weapon = choose_weapon()
print("------------------------------------------------------------------------------------------------------------------------")

# Draw Stats
input("\nNow, let fate decide thy strengths. Press Enter to reveal thy destiny.")
intelligence = get_stat()
wisdom = get_stat()
charisma = get_stat()
strength = get_stat()
dexterity = get_stat()

# Apply bonuses races
if race == "Dwarf":
    short_range_attack += 2
    if short_weapon == "Axe":
        short_range_attack += 2
    strength += 2
if race == "Elf":
    long_range_attack += 2
    if long_weapon == "Bow":
        long_range_attack += 2
    wisdom += 2
if race == "Hobbit":
    life_total += 3
    long_range_attack -= 2
    if short_weapon == "Pan":
        short_range_attack += 4
if race == "Human":
    long_range_attack += 2
    short_range_attack += 2
    strength += 4
    if wisdom > 2:
        wisdom = wisdom - 2
if race == "Ent":
    wisdom += 2
    strength += 2
    life_total += 7

# Apply bonuses classes
if char_class == "Wizard":
    charisma += 5
    class_ability_1 = "Commanding Voice"
    if long_weapon == "Magical Staff":
        class_ability_2 = "Healing"
        long_range_attack +=2
if char_class == "Rogue":
    class_ability_1 = "Vanishing"
    dexterity += 4
    intelligence += 1
    if short_weapon == "Dagger":
        short_range_attack += 2
if char_class == "Bard":
    charisma += 3
    class_ability_1 = "Bagpipe"
    class_ability_2 = "Bardic Insult"
if char_class == "Ranger":
    strength += 3
    class_ability_1 = "Healing"
    if long_weapon == "Bow":
        long_range_attack += 1
if char_class == "Fighter":
    class_ability_1 = "Gather thy forces"
    strength += 4
    long_range_attack += 1
    short_range_attack += 1

# Attack Power Calculation
if long_weapon == "Magical Staff":
    long_range_attack += 1
if long_weapon == "Bow":
    long_range_attack += 2
if long_weapon == "Sling":
    long_range_attack += 1
if long_weapon == "Spear":
    long_range_attack += 2
if short_weapon == "Pan":
    short_range_attack += 1
if short_weapon == "Sword": 
    short_range_attack += 2
if short_weapon == "Dagger":
    short_range_attack += 1
if short_weapon == "Axe":
    short_range_attack += 2

base_life_total = life_total

# Print Summary
print("\nLuck has spoken. Here are thy stats:")
print(f"\nName: {character_name}")
print(f"Race: {race}")
print(f"Class: {char_class}")
print("\n")
if class_ability_1 == "Healing":
    print("Healing:")
    print("Because of thy class, thou are able to heal yourslef. When cast a healing spell, you win two life point back once \neach two turns (systematic sucess).")
if class_ability_1 == "Bagpipe":
    print("Bagpipe")
    print("Thanks to thy class, you possess an instrument to the measure of your talent: the bagpipe make good use of it \n(CHA, roll above 15).")
if class_ability_1 == "Commanding Voice":
    print("Commanding Voice")
    print("Thanks to your class, when thou shall speak other shall obey (CHA, roll above 15)...")
if class_ability_1 == "Gather thy forces":
    print("Gather thy forces")
    print("Thanks to your class, when thou shall not swing, the next blow shall be even stronger (systematic sucess)...")
if class_ability_1 == "Vanishing":
    print("Vanishing")
    print("For three turns you become as slippery as an eel, the ennemy struggle to hit you (systematic sucess)...")
if class_ability_2 == "Healing":
    print("Healing")
    print("Because of thy class, thou are able to heal yourslef. When cast a healing spell, you win two life point back once \neach two turns (systematic sucess).")
if class_ability_2 == "Bardic Insult":
    print("Bardic Insult")
    print("Thanks to thy class, thy words shall have the power to tear tyrants down (CHA, roll above 15)...")
print(f"Thy long-range damage power is with thy {long_weapon} (ranged) {long_range_attack} (DEX + STR (or INT if spell casting), roll above 15)).")
print(f"Thy short-range damage power is with thy {short_weapon} (melee) {short_range_attack} (STR, roll above 15).")
print(f"\nIntelligence (INT): {intelligence}, Wisdom (WIS): {wisdom}, Charisma (CHA): {charisma}, Strength (STR): {strength}, Dexterity (DEX): {dexterity}")
print(f"Your life total is {life_total}.")
print("------------------------------------------------------------------------------------------------------------------------")

# Twenty faces dice roll function
def roll_dice():
    return random.randint(1, 20)

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

###### Let's sequence the whole adventure ######

are_you_alive = "alive"

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

###### Transition before the orc's fight  ######

# Calculate_bonus function
def calculate_bonus(stat):
    return max(0, stat - 13)

# Calculate bonuses with calculate_bonus
intelligence_bonus = calculate_bonus(intelligence)
wisdom_bonus = calculate_bonus(wisdom)
charisma_bonus = calculate_bonus(charisma)
strength_bonus = calculate_bonus(strength)
dexterity_bonus = calculate_bonus(dexterity)

# Start the adventure
input("\nPress Enter to start your adventure... (chapter 1)")
print("------------------------------------------------------------------------------------------------------------------------")
print("\n\nThe dense canopy above allows only slivers of pale moonlight to filter through, casting eerie shadows over the forest \nfloor. The scent of damp earth and decaying leaves hangs heavy in the air. Every crunch of twigs underfoot echoes \nthrough the silence, setting your nerves on edge. Then, a guttural growl breaks the hush. Ahead, standing in the clearing, \nan orc looms, its scarred green skin glistening in the dim light. Yellow eyes lock onto you with a predator’s hunger, \nand it unsheathes a massive cleaver. The challenge is clear—there will be no words, \nonly steel and blood.")
print("------------------------------------------------------------------------------------------------------------------------")
orc_intimidation = input("\nChoice: \nAttempt to intimidate the orc before engaging; if you want to try type \"Intimidate\" else \npress on Enter. If successful, the orc starts with reduced morale, lowering its attack power. If unsuccessful, \nthe orc's first attack will be a powerful blow (+ CHA). ").title()
if orc_intimidation == "Intimidate":
    orc_intimidation_roll = roll_dice() + charisma_bonus
    if orc_intimidation_roll > 10:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("\nThe power of your aura throws the orc in doubt...\n\n")
    else:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("\nThe orcs is not even slightly unsettled by your demonstration of power...\n\n")
    
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

###### Orc's combat ######

# Reset life total
life_total = base_life_total

# Orc stats
orc_life_total = 20

# Stunned ennemy
stunned_turns = 0

# vanishing effet counter
vanish_turns = 0

# Situation of soldier
gathering_forces = False
cooldowns = {"class_ability_1": 0, "class_ability_2": 0}

# Special option
combat_counter = 0
turn_counter = 0

# Function for the orc's turn and attacks
def orc_attack():
    if stunned_turns > 0:
        print("The orc is still under your influence and does not attack!")
        return 0
    attack_type = random.choice(["short", "long"])
    damage = random.randint(2, 4) - (1 if orc_intimidation == "Intimidate" and orc_intimidation_roll > 10 else 0) + (3 if orc_intimidation == "Intimidate" and orc_intimidation_roll < 10 and Turn == 1 else 0)
    hit_threshold = 11 if attack_type == "long" else 9
    if attack_type == "long":
        print("The orc starts spinning its sling towards thou!")
    if attack_type == "short":
        print("The orc raise his sword...")
    if vanish_turns > 0:
        hit_threshold += 3  # Rogue's vanishing ability makes it harder to hit
    if roll_dice() > hit_threshold:
        print("The orc lands a strike!")
        return damage
    else:
        print("The orc's attack misses!")
        return 0

# Turn counter
Turn = 1

# Combat loop
while life_total > 0 and orc_life_total > 0:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\nChoose your action:")
    print(f"a) Attack with thy {short_weapon}")
    print(f"b) Attack with thy {long_weapon}")
    if class_ability_1 != "none" and cooldowns["class_ability_1"] == 0:
        print(f"c) Use: {class_ability_1}")
    if class_ability_2 != "none" and cooldowns["class_ability_2"] == 0:
        print(f"d) Use: {class_ability_2}")
    
    # Special option
    special_option_available = random.randint(1, 3)
    special_choice = "none"
    if special_option_available >= 2:
        special_options = [
            "x) Special Option: An old rope lies on the ground. Attempt to entangle the orcs (DEX + STR, roll above 10).",
            "x) Special Option: Spot a magical rune on the ground. Channel energy into it (INT + WIS, roll above 11 for a magical \nshockwave that stuns the orcs).",
            "x) Special Option: An ancient banner flutters nearby. Rally thyself for a morale boost (CHA, roll above 10 for a \ntemporary attack bonus during this combat).",
            "x) Special Option: Spot an old weapon on the ground. Retrieve it for an attack boost for the rest of the game \n(DEX, roll above 9).",
            "x) Special Option: A shattered potion vial leaks arcane mist. Manipulate it (INT + WIS, roll above 11 for magical \nprotection)."
        ]
        special_choice = random.choice(special_options)
        print(special_choice)
    
    action = input("What dost thou do? ").lower()
    print("------------------------------------------------------------------------------------------------------------------------")

    # Short range attack
    if action == "a":
        attack_roll = roll_dice() + strength_bonus 
        if attack_roll > 13:
            damage = short_range_attack * (3 if gathering_forces else 1) # adding fighter damage
            print(f"You strike the orc with thy {short_weapon}, dealing {damage} damage!")
            orc_life_total -= damage
            gathering_forces = False  # Reset gather forces effect, since blow has been delivered
        else:
            print("Your attack misses and bounces off the orc's armor!")
    
    # Long range attack
    elif action == "b":
        attack_roll = roll_dice() + dexterity_bonus + (intelligence_bonus if char_class=="Wizard" and long_weapon == "Magical staff" else strength_bonus)
        if attack_roll > 15:
            if long_weapon == "Magical Staff" and char_class == "Wizard": # If the player's class is wizard he may cast spells
                spell_name = input("Name thy damage spell: ")
                print(f"You cast {spell_name}, dealing {long_range_attack} damage to the orc!")
            else:
                print(f"You launch an attack with thy {long_weapon}, dealing {long_range_attack} damage!")
            orc_life_total -= long_range_attack * (3 if gathering_forces else 1)
            gathering_forces = False  # Reset gather forces effect, since blow has been delivered
        else:
            print("Your shot goes wide and misses!")

    # Special action
    elif action == "x" and special_choice != "none":
        roll = roll_dice()
        if "rope" in special_choice:
            entangle_roll = roll + dexterity_bonus + strength_bonus
            if entangle_roll > 10:
                stunned_turns = 2
                print("\nThe orc is entangled! It shall not attack for two turns.")
            else:
                print("\nThy throw misses, and the orc snarls at thee!")
        elif "rune" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                stunned_turns = 2
                print("\nA magical shockwave erupts, stunning the orc!")
            else:
                print("When thou touch the rune to activate it it suddenly vanishes...")
        elif "banner" in special_choice:
            if roll + charisma_bonus > 10:
                strength_bonus += 2
                dexterity_bonus += 2
                print("\nThy rallying cry inspires thee! Attack strength increased!")
            else:
                print("What thou tought to be a banner was a \"want to surrender\" white flag...")
        elif "weapon" in special_choice:
            if roll + dexterity_bonus > 9:
                short_range_attack += 2
                print("\nThou hast found a sturdy weapon, increasing thy attack by two in close combat!")
            else:
                print("In the adrenaline rush thou lost sight of thy weapon")
        elif "potion" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                life_total += 3
                print("\nThe arcane mist envelops thee, restoring some vitality!")
            else:
                print("The potion was simply water...")
    
    # Healing action
    elif action == "c" and class_ability_1 == "Healing" and cooldowns["class_ability_1"] == 0:
        life_total = life_total + 2
        print("You heal yourself for 2 life point!")
        cooldowns["class_ability_1"] = 2
    
    # Stunning ennemy with "Bagpipe" or "Commanding Voice" and turns during
    elif action == "c" and class_ability_1 in ["Bagpipe", "Commanding Voice"] and cooldowns["class_ability_1"] == 0:
        if roll_dice() + charisma_bonus > 15:
            stunned_turns = 2
            print(f"\nYou use {class_ability_1}! The orc is enchanted and cannot attack for {stunned_turns} turns!")
            while stunned_turns > 0:
                stunned_turns -= 1
                print("\nYou may act freely while the orc is under your influence!")
                print(f"a) Attack with thy {short_weapon}")
                print(f"b) Attack with thy {long_weapon}")
                if char_class == "Wizard":
                   print("c) Use: Healing") 
                if char_class == "Bard":
                    print("c) Use: Bardic Insult")
                action = input("Choose your next move: ").lower()
                print("------------------------------------------------------------------------------------------------------------------------")
                if char_class == "Wizard":
                    if action == "a":
                        orc_life_total -= short_range_attack
                        print(f"You strike again, dealing {short_range_attack} damage!")
                    elif action == "b":
                        orc_life_total -= long_range_attack
                        if long_weapon == "Magical Staff" and char_class == "Wizard": # If the player's class is wizard he may cast spells
                            spell_name = input("Name thy damage spell: ")
                            print(f"You cast {spell_name}, dealing {long_range_attack} damage to the orc!")
                        else:
                            print(f"You launch an attack with thy {long_weapon}, dealing {long_range_attack} damage!")
                    elif action == "c":
                        life_total = life_total + 2
                        print("You heal yourself of two lives!")
                    else:
                        print("Invalid action. You wasted a few precious seconds.")
                if char_class == "Bard":
                    if action == "a":
                        orc_life_total -= short_range_attack
                        print(f"You strike again, dealing {short_range_attack} damage!")
                    elif action == "b":
                        orc_life_total -= long_range_attack
                        print(f"You strike again, dealing {long_range_attack} damage!")
                    elif action == "c":
                        insult = input("Hurl thy insult: ")
                        print(f"Your words cut deep! The orc already unable to move takes 5 damage!")
                        orc_life_total -= 5
                    else:
                        print("Invalid action. You wasted a few precious seconds.")
        else:
            print("Your attempt to enchant the orc failed...")
        cooldowns["class_ability_1"] = 2
    
    # Vanishing effect
    elif action == "c" and class_ability_1 == "Vanishing" and cooldowns["class_ability_1"] == 0:
        vanish_turns = 3
        print("You vanish into the shadows, making it harder for the orc to hit you for three turns!")
        cooldowns["class_ability_1"] = 2
    
    # Gather thy forces
    elif action == "c" and class_ability_1 == "Gather thy forces" and cooldowns["class_ability_1"] == 0:
        print("You gather your strength, preparing for a mighty blow next turn!")
        gathering_forces = True
        cooldowns["class_ability_1"] = 2
    
    # Healing ability
    elif action == "d" and class_ability_2 == "Healing" and cooldowns["class_ability_2"] == 0:
        life_total = life_total + 2
        print("You heal yourself for 2 life point!")
        cooldowns["class_ability_2"] = 2
    
    # Bardic insult damage
    elif action == "d" and class_ability_2 == "Bardic Insult" and cooldowns["class_ability_2"] == 0:
        insult = input("Hurl thy insult: ")
        if roll_dice() + charisma_bonus > 10:
            print(f"Your words cut deep! The orc reels in anger, taking 5 damage!")
            orc_life_total -= 5
        else:
            print("The orc just laughs at your weak insult!")
        cooldowns["class_ability_2"] = 2
    
    # In case not the right letter
    else:
        print("Invalid action or ability on cooldown.")
        continue

    # Victory
    if orc_life_total <= 0:
        print(f"\nWith a final blow, the orc collapses. Victory is yours {character_name}!")
        break
    
    # Orc's turn
    orc_damage = orc_attack()
    stunned_turns -= stunned_turns
    if orc_damage > 0:
        print(f"The orc's attack hits you for {orc_damage} damage!")
        life_total = max(0, life_total - orc_damage)
        if Turn == 2 or Turn == 4:
            print("The orc is enraged and attacks a second time!")
            orc_damage = orc_attack()
            if orc_damage > 0:
                print(f"The orc's attack hits you for {orc_damage} damage!")
                life_total = max(0, life_total - orc_damage)
        if life_total>0:
            print(f"You have {life_total} life points remaining.")
    
    # Defeat
    if life_total <= 0:
        print("\nThe orc overpowers thee. Darkness takes thee...")  
        are_you_alive = "dead"
        break
    
    cooldowns = {key: max(0, val - 1) for key, val in cooldowns.items()}
    Turn +=1
################################################################################################
################################################################################################
################################################################################################

###### Let's sequence the whole adventure ######

if are_you_alive == "dead":
    exit()

################################################################################################
################################################################################################
################################################################################################

###### Transition before the Throll's fight ######

# Calculate bonuses with calculate_bonus
intelligence_bonus = calculate_bonus(intelligence)
wisdom_bonus = calculate_bonus(wisdom)
charisma_bonus = calculate_bonus(charisma)
strength_bonus = calculate_bonus(strength)
dexterity_bonus = calculate_bonus(dexterity)

# Start the adventure
print("------------------------------------------------------------------------------------------------------------------------")
input("\nPress Enter to start the next chapter...")
print("\nThe stench of blood and sweat lingers as you catch your breath, wiping your blades clean. The forest's darkness begins \nto recede as the trees thin, revealing the jagged silhouette of a mountain ahead. The winding path leading downward \nseems safe enough—until a deep, rumbling laughter halts your steps. Two towering figures emerge from the shadows, \ntheir grotesque forms framed by the moonlight. Trolls. Their thick, rock-like skin glistens with dampness, and their \nbeady eyes gleam with malice. One of them grins, revealing jagged teeth. “More meat,” it growls. The other slams a \nboulder-sized fist into its palm. It seems the night’s battles are far from over.\n\n")
print("------------------------------------------------------------------------------------------------------------------------")
flee_or_not = input("Choice: \nTry to outrun the trolls instead of fighting them. If you want to flee type \"Run\" else press Enter. If successful, you \navoid battle. If unsuccessful, you must fight them while fatigued (+ STR). ")
if flee_or_not == "Run":
    flee_sucess = roll_dice() + strength_bonus
    if flee_sucess > 15:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("\nYou dart into the trees, using the uneven terrain and dense underbrush to your advantage. You hear the orcs shouting \nbehind you infuriated to have lost the track of their meal...")
    else:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("\nThe throlls catch up with you, now you have to fight them out of breath...")
################################################################################################
################################################################################################
################################################################################################

###### Throll and sunrise ######

        # Reset life total
        life_total = base_life_total

        # Twenty faces dice roll function
        def roll_dice():
            return random.randint(1, 20)

        # Turn counter until petrification
        turn_counter = 0

        # Stunned ennemy
        stunned_turns = 0

        # vanishing effet counter
        vanish_turns = 0

        # Situation of soldier
        gathering_forces = False
        cooldowns = {"class_ability_1": 0, "class_ability_2": 0}

        # Throlls stats
        throlls = [{"life": 30, "attack_bonus": 0, "hit_threshold": 10} for _ in range(2)]

        # Adventure start
        print("------------------------------------------------------------------------------------------------------------------------")
        print("\n\nAt the base of the mountain, two hulking trolls block thy path! They grin wickedly, gripping massive clubs.")

        # Combat loop
        while life_total > 0 and any(t["life"] > 0 for t in throlls):
            print("\nChoose thy action:")
            print(f"a) Strike one of the two throll with thy {short_weapon}")
            print(f"b) Use thy {long_weapon} to take a shot from afar")
            if class_ability_1 != "none" and cooldowns["class_ability_1"] == 0:
                print(f"c) Use: {class_ability_1}")
            if class_ability_2 != "none" and cooldowns["class_ability_2"] == 0:
                print(f"d) Use: {class_ability_2}")

            # Special option
            special_option_available = random.randint(1, 3)
            special_choice = "none"
            if special_option_available >= 2:
                special_options = [
                    "x) Special Option: An old rope lies on the ground. Attempt to entangle the throlls (DEX + STR, roll above 10).",
                    "x) Special Option: A loose boulder is above thee. Attempt to push it onto the throlls (STR, roll above 12 for full \nsuccess, else partial damage).",
                    "x) Special Option: Spot a magical rune on the ground. Channel energy into it (INT + WIS, roll above 11 for a magical \nshockwave that stuns the throlls).",
                    "x) Special Option: A nearby tree branch looks unstable. Shake it to drop debris onto the throlls \n(Dex + STR, roll above 11).",
                    "x) Special Option: An ancient banner flutters nearby. Rally thyself for a morale boost (CHA, roll above 10 for a \ntemporary attack bonus during this combat).",
                    "x) Special Option: Spot an old weapon on the ground. Retrieve it for an attack boost during the rest of the game \n(DEX, roll above 9).",
                    "x) Special Option: A shattered potion vial leaks arcane mist. Manipulate it (INT + WIS, roll above 11 for magical \nprotection)."
                ]
                special_choice = random.choice(special_options)
                print(special_choice)

            # Action
            action = input("What dost thou do? ").lower()
            print("------------------------------------------------------------------------------------------------------------------------")

            # Short or Long-range Attack
            if action in ["a", "b"]:
                if char_class == "Wizard" and short_weapon == "Magical Staff":
                    spell_name = input("\nName thy damage spell: ")
                attack_roll = roll_dice() + (strength_bonus if action == "a" else dexterity_bonus + (intelligence_bonus if char_class=="Wizard" and long_weapon == "Magical staff" else strength_bonus))
                if attack_roll > 10:
                    damage = (short_range_attack if action == "a" else long_range_attack)* (3 if gathering_forces else 1)
                    gathering_forces = False  # Reset gather forces effect, since blow has been delivered
                    target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                    throlls[target]["life"] -= damage
                    if char_class == "Wizard" and short_weapon == "Magical Staff":
                        print(f"\nYou cast {spell_name}, dealing {damage} damage to the throll!")
                    else:
                        print(f"\nThou smitest the throll's leg, dealing {damage} damage! It howls in pain.")
                else:
                    if action == "a":
                        print("\nYour attack misses and bounces off the throll hard skin!")
                    if action == "b":
                        print("\nYour shot goes just misses the throll head!")

            # Special action
            elif action == "x" and special_choice != "none":
                roll = roll_dice()
                if "rope" in special_choice:
                    entangle_roll = roll + dexterity_bonus + strength_bonus
                    if entangle_roll > 10:
                        stunned_turns = 2
                        print("\nThe throlls are entangled! They shall not attack for two turns.")
                    else:
                        print("\nThy throw misses, and the throll laugh at thee!")
                elif "boulder" in special_choice:
                    boulder_roll = roll + strength_bonus
                    if boulder_roll > 12:
                        for t in throlls:
                            t["life"] -= 5
                        print("\nThe boulder crushes the throlls! They take massive damage!")
                    else:
                        for t in throlls:
                            t["life"] -= 3
                        print("\nThe boulder lands partially, dealing some damage to the throlls.")
                elif "rune" in special_choice:
                    if roll + intelligence_bonus + wisdom_bonus > 11:
                        stunned_turns = 2
                        print("\nA magical shockwave erupts, stunning the throlls!")
                    else:
                        print("When thou touch the rune to activate it it suddenly vanishes...")
                elif "branch" in special_choice:
                    if roll + strength_bonus + dexterity_bonus > 11:
                        for t in throlls:
                            t["life"] -= 2
                        print("\nYou sucessfully hit the weak branch the debris falls, injuring the throlls!")
                    else:
                        print("The branch doesn't budge...")
                elif "banner" in special_choice:
                    if roll + charisma_bonus > 10:
                        strength_bonus += 2
                        dexterity_bonus += 2
                        print("\nThy rallying cry inspires thee ! Attack strength (DEX + STR) increased!")
                    else:
                        print("What thou tought to be a banner was a \"want to surrender\" white flag...")
                elif "weapon" in special_choice:
                    if roll + dexterity_bonus > 9:
                        short_range_attack += 2
                        long_range_attack += 2
                        print("\nThou hast found a sturdy weapon, increasing thy attack by two in close combat!")
                    else:
                        print("In the adrenaline rush thou lost sight of thy weapon")
                elif "potion" in special_choice:
                    if roll + intelligence_bonus + wisdom_bonus > 11:
                        life_total += 4
                        print("\nThe arcane mist envelops thee, restoring some vitality!")
                    else:
                        print("The potion was simply water...")

            # Healing action
            elif action == "c" and class_ability_1 == "Healing" and cooldowns["class_ability_1"] == 0:
                life_total = life_total + 2
                print("\nYou heal yourself for 2 life point!")
                cooldowns["class_ability_1"] = 2
            
            # Stunning ennemy with "Bagpipe" or "Commanding Voice" and turns during
            elif action == "c" and class_ability_1 in ["Bagpipe", "Commanding Voice"] and cooldowns["class_ability_1"] == 0:
                if roll_dice() + charisma_bonus > 15:
                    turn_counter += 2
                    stunned_turns = 2
                    print(f"\nYou use {class_ability_1}! The throlls are enchanted and cannot attack for {stunned_turns} turns!")
                    while stunned_turns > 0:
                        stunned_turns -= 1
                        print("\nYou may act freely while they are under your influence!")
                        print(f"a) Attack with thy {short_weapon}")
                        print(f"b) Attack with thy {long_weapon}")
                        if char_class == "Wizard":
                            print("c) Use: Healing") 
                        if char_class == "Bard":
                            print("c) Use: Bardic Insult")
                        action = input("Choose your next move: ").lower()
                        print("------------------------------------------------------------------------------------------------------------------------")
                        if char_class == "Wizard":
                            if action in ["a", "b"]:
                                if long_weapon == "Magical Staff" and action == "b":
                                    spell_name = input("\nName thy damage spell: ")
                                damage = short_range_attack if action == "a" else long_range_attack
                                target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                                throlls[target]["life"] -= damage
                                if long_weapon == "Magical Staff" and action == "b":
                                    print(f"\nYou cast {spell_name}, dealing {damage} damage to a throll!")
                                else:
                                    print(f"\nThou smitest the throll's arm, dealing {damage} damage! It howls in pain.")
                            elif action == "c":
                                life_total = life_total + 2
                                print("\nYou heal yourself of two life point!")
                            else:
                                print("\nInvalid action. You wasted a few precious seconds.")
                        if char_class == "Bard":
                            if action in ["a", "b"]:
                                damage = short_range_attack if action == "a" else long_range_attack
                                target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                                throlls[target]["life"] -= damage
                                print(f"\nThou smitest a throll's leg, dealing {damage} damage! It howls in pain.")
                            elif action == "c":
                                insult = input("\nHurl thy insult: ")
                                damage = 5
                                target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                                throlls[target]["life"] -= damage
                                print(f"\nThe throll's feelings are hurt, dealing them {damage} damage!")
                            else:
                                print("\nInvalid action. You wasted a few precious seconds.")
                else:
                    print("\nYour attempt to enchant them failed...")

                cooldowns["class_ability_1"] = 2
            
            # Vanishing effect
            elif action == "c" and class_ability_1 == "Vanishing" and cooldowns["class_ability_1"] == 0:
                vanish_turns = 3
                print("\nYou vanish into the shadows, making it harder for the throlls to hit you for three turns!")
                cooldowns["class_ability_1"] = 2
            
            # Gather thy forces
            elif action == "c" and class_ability_1 == "Gather thy forces" and cooldowns["class_ability_1"] == 0:
                print("\nYou gather your strength, preparing for a mighty blow next turn!")
                gathering_forces = True
                cooldowns["class_ability_1"] = 2
            
            # Healing ability
            elif action == "d" and class_ability_2 == "Healing" and cooldowns["class_ability_2"] == 0:
                life_total = life_total + 2
                print("\nYou heal yourself for 2 life point!")
                cooldowns["class_ability_2"] = 2
            
            # Bardic insult damage
            elif action == "d" and class_ability_2 == "Bardic Insult" and cooldowns["class_ability_2"] == 0:
                insult = input("\nHurl thy insult: ")
                insult_roll = roll_dice() + charisma_bonus
                if insult_roll > 10:
                    damage = 5
                    target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                    throlls[target]["life"] -= damage
                    if insult_roll > 10:
                        print(f"\nYour words cut deep! The throll takes 5 damage!")
                    else:
                        print("\nThe throll just laugh at your weak insult!")
                    cooldowns["class_ability_2"] = 2

            # Victory
            if all(t["life"] <= 0 for t in throlls):
                print("\nThe last throll falls! The path is now free for thou to pursue thy adventure...")
                break
            
            # Victory
            if turn_counter > 7:
                print("\nThe sun rises over the mountains, the throlls instantly turn to stone! The path is now free for thou to \npursue thy adventure...")
                break

            # Throlls' turn
            for t in throlls:
                hit_threshold_att = 13
                if vanish_turns > 0:
                    hit_threshold_att += 3
                if t["life"] > 0 and stunned_turns == 0 and roll_dice() + t["attack_bonus"] > hit_threshold_att:
                    throll_damage = random.randint(5, 7)
                    print(f"A throll swings its massive club at you for {throll_damage} damage!")
                    life_total -= throll_damage
            
            cooldowns = {key: max(0, val - 1) for key, val in cooldowns.items()}
            stunned_turns -= 1
            
            # A turn has been played
            turn_counter +=1

            # Life total
            if life_total > 0:
                print(f"You have {life_total} life left...")

            # Defeat
            if life_total <= 0:
                print("\nThe throlls acculate thee against the mountain's side. You find yourself struck one last time by a \nmassive club and instantly die...")  
                break

            # Throll left and turns left
            turn_left = 7 - turn_counter + 2
            if life_total > 0:
                n_t = 0
                for t in throlls:
                    if t["life"] > 0:
                        n_t +=1
                if n_t>1:
                    print(f"There are {n_t} throlls left and there are {turn_left} turn left until the sunrise (the throlls will be petrified)!")
                if n_t == 1:
                    print("There is one throll left!")
else:
    # Reset life total
    life_total = base_life_total

    # Twenty faces dice roll function
    def roll_dice():
        return random.randint(1, 20)

    # Turn counter until petrification
    turn_counter = 0

    # Stunned ennemy
    stunned_turns = 0

    # vanishing effet counter
    vanish_turns = 0

    # Situation of soldier
    gathering_forces = False
    cooldowns = {"class_ability_1": 0, "class_ability_2": 0}

    # Throlls stats
    throlls = [{"life": 30, "attack_bonus": 0, "hit_threshold": 10} for _ in range(2)]

    # Adventure start
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\n\nAt the base of the mountain, two hulking trolls block thy path! They grin wickedly, gripping massive clubs.")

    # Combat loop
    while life_total > 0 and any(t["life"] > 0 for t in throlls):
        print("\nChoose thy action:")
        print(f"a) Strike one of the two throll with thy {short_weapon}")
        print(f"b) Use thy {long_weapon} to take a shot from afar")
        if class_ability_1 != "none" and cooldowns["class_ability_1"] == 0:
            print(f"c) Use: {class_ability_1}")
        if class_ability_2 != "none" and cooldowns["class_ability_2"] == 0:
            print(f"d) Use: {class_ability_2}")

        # Special option
        special_option_available = random.randint(1, 3)
        special_choice = "none"
        if special_option_available >= 2:
            special_options = [
                "x) Special Option: An old rope lies on the ground. Attempt to entangle the throlls (DEX + STR, roll above 10).",
                "x) Special Option: A loose boulder is above thee. Attempt to push it onto the throlls (STR, roll above 12 for full \nsuccess, else partial damage).",
                "x) Special Option: Spot a magical rune on the ground. Channel energy into it (INT + WIS, roll above 11 for a magical \nshockwave that stuns the throlls).",
                "x) Special Option: A nearby tree branch looks unstable. Shake it to drop debris onto the throlls \n(Dex + STR, roll above 11).",
                "x) Special Option: An ancient banner flutters nearby. Rally thyself for a morale boost (CHA, roll above 10 for a \ntemporary attack bonus during this combat).",
                "x) Special Option: Spot an old weapon on the ground. Retrieve it for an attack boost during the rest of the game \n(DEX, roll above 9).",
                "x) Special Option: A shattered potion vial leaks arcane mist. Manipulate it (INT + WIS, roll above 11 for magical \nprotection)."
            ]
            special_choice = random.choice(special_options)
            print(special_choice)

        # Action
        action = input("What dost thou do? ").lower()
        print("------------------------------------------------------------------------------------------------------------------------")

        # Short or Long-range Attack
        if action in ["a", "b"]:
            if char_class == "Wizard" and short_weapon == "Magical Staff":
                spell_name = input("\nName thy damage spell: ")
            attack_roll = roll_dice() + (strength_bonus if action == "a" else dexterity_bonus + (intelligence_bonus if char_class=="Wizard" and long_weapon == "Magical staff" else strength_bonus))
            if attack_roll > 10:
                damage = (short_range_attack if action == "a" else long_range_attack)* (3 if gathering_forces else 1)
                gathering_forces = False  # Reset gather forces effect, since blow has been delivered
                target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                throlls[target]["life"] -= damage
                if char_class == "Wizard" and short_weapon == "Magical Staff":
                    print(f"\nYou cast {spell_name}, dealing {damage} damage to the throll!")
                else:
                    print(f"\nThou smitest the throll's leg, dealing {damage} damage! It howls in pain.")
            else:
                if action == "a":
                    print("\nYour attack misses and bounces off the throll hard skin!")
                if action == "b":
                    print("\nYour shot goes just misses the throll head!")

        # Special action
        elif action == "x" and special_choice != "none":
            roll = roll_dice()
            if "rope" in special_choice:
                entangle_roll = roll + dexterity_bonus + strength_bonus
                if entangle_roll > 10:
                    stunned_turns = 2
                    print("\nThe throlls are entangled! They shall not attack for two turns.")
                else:
                    print("\nThy throw misses, and the throll laugh at thee!")
            elif "boulder" in special_choice:
                boulder_roll = roll + strength_bonus
                if boulder_roll > 12:
                    for t in throlls:
                        t["life"] -= 5
                    print("\nThe boulder crushes the throlls! They take massive damage!")
                else:
                    for t in throlls:
                        t["life"] -= 3
                    print("\nThe boulder lands partially, dealing some damage to the throlls.")
            elif "rune" in special_choice:
                if roll + intelligence_bonus + wisdom_bonus > 11:
                    stunned_turns = 2
                    print("\nA magical shockwave erupts, stunning the throlls!")
                else:
                    print("When thou touch the rune to activate it it suddenly vanishes...")
            elif "branch" in special_choice:
                if roll + strength_bonus + dexterity_bonus > 11:
                    for t in throlls:
                        t["life"] -= 2
                    print("\nYou sucessfully hit the weak branch the debris falls, injuring the throlls!")
                else:
                    print("The branch doesn't budge...")
            elif "banner" in special_choice:
                if roll + charisma_bonus > 10:
                    strength_bonus += 2
                    dexterity_bonus += 2
                    print("\nThy rallying cry inspires thee ! Attack strength (DEX + STR) increased!")
                else:
                    print("What thou tought to be a banner was a \"want to surrender\" white flag...")
            elif "weapon" in special_choice:
                if roll + dexterity_bonus > 9:
                    short_range_attack += 2
                    long_range_attack += 2
                    print("\nThou hast found a sturdy weapon, increasing thy attack by two in close combat!")
                else:
                    print("In the adrenaline rush thou lost sight of thy weapon")
            elif "potion" in special_choice:
                if roll + intelligence_bonus + wisdom_bonus > 11:
                    life_total += 4
                    print("\nThe arcane mist envelops thee, restoring some vitality!")
                else:
                    print("The potion was simply water...")

        # Healing action
        elif action == "c" and class_ability_1 == "Healing" and cooldowns["class_ability_1"] == 0:
            life_total = life_total + 2
            print("\nYou heal yourself for 2 life point!")
            cooldowns["class_ability_1"] = 2
        
        # Stunning ennemy with "Bagpipe" or "Commanding Voice" and turns during
        elif action == "c" and class_ability_1 in ["Bagpipe", "Commanding Voice"] and cooldowns["class_ability_1"] == 0:
            if roll_dice() + charisma_bonus > 15:
                turn_counter += 2
                stunned_turns = 2
                print(f"\nYou use {class_ability_1}! The throlls are enchanted and cannot attack for {stunned_turns} turns!")
                while stunned_turns > 0:
                    stunned_turns -= 1
                    print("\nYou may act freely while they are under your influence!")
                    print(f"a) Attack with thy {short_weapon}")
                    print(f"b) Attack with thy {long_weapon}")
                    if char_class == "Wizard":
                        print("c) Use: Healing") 
                    if char_class == "Bard":
                        print("c) Use: Bardic Insult")
                    action = input("Choose your next move: ").lower()
                    print("------------------------------------------------------------------------------------------------------------------------")
                    if char_class == "Wizard":
                        if action in ["a", "b"]:
                            if long_weapon == "Magical Staff" and action == "b":
                                spell_name = input("\nName thy damage spell: ")
                            damage = short_range_attack if action == "a" else long_range_attack
                            target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                            throlls[target]["life"] -= damage
                            if long_weapon == "Magical Staff" and action == "b":
                                print(f"\nYou cast {spell_name}, dealing {damage} damage to a throll!")
                            else:
                                print(f"\nThou smitest the throll's arm, dealing {damage} damage! It howls in pain.")
                        elif action == "c":
                            life_total = life_total + 2
                            print("\nYou heal yourself of two life point!")
                        else:
                            print("\nInvalid action. You wasted a few precious seconds.")
                    if char_class == "Bard":
                        if action in ["a", "b"]:
                            damage = short_range_attack if action == "a" else long_range_attack
                            target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                            throlls[target]["life"] -= damage
                            print(f"\nThou smitest a throll's leg, dealing {damage} damage! It howls in pain.")
                        elif action == "c":
                            insult = input("\nHurl thy insult: ")
                            damage = 5
                            target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                            throlls[target]["life"] -= damage
                            print(f"\nThe throll's feelings are hurt, dealing them {damage} damage!")
                        else:
                            print("\nInvalid action. You wasted a few precious seconds.")
            else:
                print("\nYour attempt to enchant them failed...")

            cooldowns["class_ability_1"] = 2
        
        # Vanishing effect
        elif action == "c" and class_ability_1 == "Vanishing" and cooldowns["class_ability_1"] == 0:
            vanish_turns = 3
            print("\nYou vanish into the shadows, making it harder for the throlls to hit you for three turns!")
            cooldowns["class_ability_1"] = 2
        
        # Gather thy forces
        elif action == "c" and class_ability_1 == "Gather thy forces" and cooldowns["class_ability_1"] == 0:
            print("\nYou gather your strength, preparing for a mighty blow next turn!")
            gathering_forces = True
            cooldowns["class_ability_1"] = 2
        
        # Healing ability
        elif action == "d" and class_ability_2 == "Healing" and cooldowns["class_ability_2"] == 0:
            life_total = life_total + 2
            print("\nYou heal yourself for 2 life point!")
            cooldowns["class_ability_2"] = 2
        
        # Bardic insult damage
        elif action == "d" and class_ability_2 == "Bardic Insult" and cooldowns["class_ability_2"] == 0:
            insult = input("\nHurl thy insult: ")
            insult_roll = roll_dice() + charisma_bonus
            if insult_roll > 10:
                damage = 5
                target = random.choice([i for i, t in enumerate(throlls) if t["life"] > 0])
                throlls[target]["life"] -= damage
                if insult_roll > 10:
                    print(f"\nYour words cut deep! The throll takes 5 damage!")
                else:
                    print("\nThe throll just laugh at your weak insult!")
                cooldowns["class_ability_2"] = 2

        # Victory
        if all(t["life"] <= 0 for t in throlls):
            print("\nThe last throll falls! The path is now free for thou to pursue thy adventure...")
            break
        
        # Victory
        if turn_counter > 7:
            print("\nThe sun rises over the mountains, the throlls instantly turn to stone! The path is now free for thou to \npursue thy adventure...")
            break

        # Throlls' turn
        for t in throlls:
            hit_threshold_att = 13
            if vanish_turns > 0:
                hit_threshold_att += 3
            if t["life"] > 0 and stunned_turns == 0 and roll_dice() + t["attack_bonus"] > hit_threshold_att:
                throll_damage = random.randint(5, 7)
                print(f"A throll swings its massive club at you for {throll_damage} damage!")
                life_total -= throll_damage
        
        cooldowns = {key: max(0, val - 1) for key, val in cooldowns.items()}
        stunned_turns -= 1
        
        # A turn has been played
        turn_counter +=1

        # Life total
        if life_total > 0:
            print(f"You have {life_total} life left...")

        # Defeat
        if life_total <= 0:
            are_you_alive = "dead"
            print("\nThe throlls acculate thee against the mountain's side. You find yourself struck one last time by a \nmassive club and instantly die...")  
            break

        # Throll left and turns left
        turn_left = 7 - turn_counter + 2
        if life_total > 0:
            n_t = 0
            for t in throlls:
                if t["life"] > 0:
                    n_t +=1
            if n_t>1:
                print(f"There are {n_t} throlls left and there are {turn_left} turn left until the sunrise (the throlls will be petrified)!")
            if n_t == 1:
                print("There is one throll left!")

#################################################################################################
#################################################################################################
#################################################################################################

###### Let's sequence the whole adventure ######

if are_you_alive == "dead":
    exit()

################################################################################################
################################################################################################
################################################################################################

###### Transition before the Goblin's fight ######

# Calculate bonuses with calculate_bonus
intelligence_bonus = calculate_bonus(intelligence)
wisdom_bonus = calculate_bonus(wisdom)
charisma_bonus = calculate_bonus(charisma)
strength_bonus = calculate_bonus(strength)
dexterity_bonus = calculate_bonus(dexterity)

# Start the adventure
print("------------------------------------------------------------------------------------------------------------------------")
input("\nPress Enter to start the next chapter...")
print("\nThe road ahead winds through a narrow mountain pass, the craggy peaks closing in around you. As you press forward, \na sudden whisper of movement stops you in your tracks. From the shadows, a lithe figure emerges, \nclad in dark leather and moving with uncanny grace. An elf—his silver hair catching the starlight—nods at you, \na smirk playing at his lips. \n\n“I’ve been watching you,” he says, twirling a dagger between his fingers. “Not bad. But the road ahead is treacherous, \nand more foes await. I’d say you could use another blade.” \n\nHis name is Alarion, a rogue of elven descent. His keen eyes study you, waiting for a response.\n\n")
alarion_help = input("Choice: Accept Alarion’s help or refuse, if you accept type \"Help\" else type Enter ").title()
print("------------------------------------------------------------------------------------------------------------------------")

################################################################################################
################################################################################################
################################################################################################

###### Alarion and the Goblins ######

# Reset life total
life_total = base_life_total

# Twenty faces dice roll function
def roll_dice():
    return random.randint(1, 20)

# Stunned ennemy
stunned_turns = 0

# vanishing effet counter
vanish_turns = 0

# Situation of soldier
gathering_forces = False
cooldowns = {"class_ability_1": 0, "class_ability_2": 0}

# Goblin stats
goblins = [{"life": 5, "attack_bonus": 1, "hit_threshold": 10} for _ in range(5)]
elf_life = 15

# Special option
combat_counter = 0
turn_counter = 0

if alarion_help == "Help":
    print("\nYou and thy elven companion, Alarion, venture into the ruins of a forgotten fortress. Shadows creep along moss-covered \nstones, and suddenly, a gang of five goblins ambushes thee! Their yellow eyes glint with malice.")
else:
    print("\nYou venture into the ruins of a forgotten fortress. Shadows creep along moss-covered stones, and suddenly, a gang of \nfive goblins ambushes thee! Their yellow eyes glint with malice.")

while life_total > 0 and any(g["life"] > 0 for g in goblins):
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\nChoose thy action:")
    print(f"a) Strike a goblin with thy {short_weapon}.")
    print(f"b) Use thy {long_weapon} to take a shot from afar.")
    if class_ability_1 != "none" and cooldowns["class_ability_1"] == 0:
        print(f"c) Use: {class_ability_1}")
    if class_ability_2 != "none" and cooldowns["class_ability_2"] == 0:
        print(f"d) Use: {class_ability_2}")

    # Special option
    special_option_available = random.randint(1, 3)
    special_choice = "none"
    if special_option_available >= 2:
        special_options = [
            "x) Special Option: A goblin's bag bursts open, revealing explosive powder! Toss it (DEX, roll above 13). Failure may \nharm thee!",
            "x) Special Option: A loose boulder is above thee. Attempt to push it onto the goblins (STR, roll above 12 for full \nsuccess, else partial damage).",
            "x) Special Option: Spot a magical rune on the ground. Channel energy into it (INT + WIS, roll above 11 for a magical \nshockwave that stuns goblins).",
            "x) Special Option: A fallen torch ignites the battlefield. Kick embers at goblins (DEX, roll above 10 for burn damage \nover time).",
            "x) Special Option: A nearby tree branch looks unstable. Shake it to drop debris onto the goblins (Dex + STR, roll \nabove 11).",
            "x) Special Option: An ancient banner flutters nearby. Rally thyself and Alarion for a morale boost (CHA, roll above \n10 for a temporary attack bonus during this combat).",
            "x) Special Option: A forgotten well lies in the shadows. Attempt to push a goblin into it (STR, roll above 12 for \ninstant removal).",
            "x) Special Option: A shattered potion vial leaks arcane mist. Manipulate it (INT + WIS, roll above 11 for magical \nprotection)."
        ]
        special_choice = random.choice(special_options)
        print(special_choice)
    
    action = input("What dost thou do? ").lower()
    print("------------------------------------------------------------------------------------------------------------------------")

    # Short or Long-range Attack
    if action in ["a", "b"]:
        if char_class == "Wizard" and short_weapon == "Magical Staff":
            spell_name = input("\nName thy damage spell: ")
        attack_roll = roll_dice() + (strength_bonus if action == "a" else dexterity_bonus + (intelligence_bonus if char_class=="Wizard" and long_weapon == "Magical staff" else strength_bonus))
        if attack_roll > 10:
            damage = (short_range_attack if action == "a" else long_range_attack)* (3 if gathering_forces else 1)
            gathering_forces = False  # Reset gather forces effect, since blow has been delivered
            target = random.choice([i for i, g in enumerate(goblins) if g["life"] > 0])
            goblins[target]["life"] -= damage
            if char_class == "Wizard" and short_weapon == "Magical Staff":
                print(f"\nYou cast {spell_name}, dealing {damage} damage to the goblin!")
            else:
                print(f"\nThou smitest a goblin, dealing {damage} damage! It howls in pain.")
        else:
            if action == "a":
                print("\nYour attack misses and bounces off the goblin's armor!")
            if action == "b":
                print("\nYour shot goes wide and misses!")
    
    # Special action
    elif action == "x" and special_choice != "none":
        roll = roll_dice()
        if "explosive" in special_choice:
            explosion_roll = roll + dexterity_bonus
            if explosion_roll > 13:
                for g in goblins:
                    g["life"] -= 3
                print("\nThe explosion ravages the goblins, dealing 3 damage to each!")
            else:
                for g in goblins:
                    g["life"] -= 3
                life_total -= 2
                print("\nThe explosion is too close! All goblins take 3 damage, but thou also \nsuffer 2 damage!")
        elif "boulder" in special_choice:
            boulder_roll = roll + strength_bonus
            if boulder_roll > 12:
                for g in goblins:
                    g["life"] -= 3
                print("\nThe boulder crushes the goblins! They take massive damage!")
            else:
                for g in goblins:
                    g["life"] -= 2
                print("\nThe boulder lands partially, dealing some damage to the goblins.")
        elif "rune" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                stunned_turns = 1
                print("\nA magical shockwave erupts, stunning the goblins!")
            else:
                print("When thou touch the rune to activate it it suddenly vanishes...")
        elif "embers" in special_choice:
            if roll + dexterity_bonus > 10:
                for g in goblins:
                    g["life"] -= 1
                print("\nThe embers burn the goblins, dealing damage over time!")
            else:
                print("The wind pushes the embers back at you! You take one damage...")
                life_total -= 1
        elif "branch" in special_choice:
            if roll + strength_bonus + dexterity_bonus > 11:
                for g in goblins:
                    g["life"] -= 2
                print("\nYou sucessfully hit the weak branch the debris falls, injuring the goblins!")
            else:
                print("The branch doesn't budge...")
        elif "banner" in special_choice:
            if roll + charisma_bonus > 10:
                strength_bonus += 2
                dexterity_bonus += 2
                print("\nThy rallying cry inspires thee and Alarion! Attack strength increased!")
            else:
                print("What thou tought to be a banner was a \"want to surrender\" white flag...")
        elif "well" in special_choice:
            if roll + strength_bonus > 12:
                goblins.pop()
                print("\nA goblin is hurled into the darkness below, never to be seen again!")
            else:
                print("Your try to push the goblin failed and you stumble and find thy face \nin the ground.")
        elif "potion" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                life_total += 3
                print("\nThe arcane mist envelops thee, restoring some vitality!")
            else:
                print("The potion was simply water...")
    
    # Healing action
    elif action == "c" and class_ability_1 == "Healing" and cooldowns["class_ability_1"] == 0:
        life_total = life_total + 2
        print("\nYou heal yourself for 2 life point!")
        cooldowns["class_ability_1"] = 2
    
    # Stunning ennemy with "Bagpipe" or "Commanding Voice" and turns during
    elif action == "c" and class_ability_1 in ["Bagpipe", "Commanding Voice"] and cooldowns["class_ability_1"] == 0:
        if roll_dice() + charisma_bonus > 15:
            stunned_turns = 2
            print(f"\nYou use {class_ability_1}! The goblins are enchanted and cannot attack for {stunned_turns} turns!")
            while stunned_turns > 0:
                stunned_turns -= 1
                print("\nYou may act freely while they are under your influence!")
                print(f"a) Attack with thy {short_weapon}")
                print(f"b) Attack with thy {long_weapon}")
                if char_class == "Wizard":
                   print("c) Use: Healing") 
                if char_class == "Bard":
                    print("c) Use: Bardic Insult")
                action = input("Choose your next move: ").lower()
                if char_class == "Wizard":
                    if action in ["a", "b"]:
                        if long_weapon == "Magical Staff" and action == "b":
                            spell_name = input("\nName thy damage spell: ")
                        damage = short_range_attack if action == "a" else long_range_attack
                        target = random.choice([i for i, g in enumerate(goblins) if g["life"] > 0])
                        goblins[target]["life"] -= damage
                        if long_weapon == "Magical Staff" and action == "b":
                            print(f"\nYou cast {spell_name}, dealing {damage} damage to a goblin!")
                        else:
                            print(f"\nThou smitest a goblin, dealing {damage} damage! It howls in pain.")
                    elif action == "c":
                        life_total = life_total + 2
                        print("\nYou heal yourself!")
                    else:
                        print("\nInvalid action. You wasted a few precious seconds.")
                if char_class == "Bard":
                    if action in ["a", "b"]:
                        damage = short_range_attack if action == "a" else long_range_attack
                        target = random.choice([i for i, g in enumerate(goblins) if g["life"] > 0])
                        goblins[target]["life"] -= damage
                        print(f"\nThou smitest a goblin, dealing {damage} damage! It howls in pain.")
                    elif action == "c":
                        insult = input("\nHurl thy insult: ")
                        damage = 5
                        target = random.choice([i for i, g in enumerate(goblins) if g["life"] > 0])
                        goblins[target]["life"] -= damage
                        print(f"\nThy insult hurt he goblin deeply, dealing {damage} damage!")
                    else:
                        print("\nInvalid action. You wasted a few precious seconds.")
        else:
            print("\nYour attempt to enchant them failed...")

        cooldowns["class_ability_1"] = 2
    
    # Vanishing effect
    elif action == "c" and class_ability_1 == "Vanishing" and cooldowns["class_ability_1"] == 0:
        vanish_turns = 3
        print("\nYou vanish into the shadows, making it harder for the goblins to hit you for three turns!")
        cooldowns["class_ability_1"] = 2
    
    # Gather thy forces
    elif action == "c" and class_ability_1 == "Gather thy forces" and cooldowns["class_ability_1"] == 0:
        print("\nYou gather your strength, preparing for a mighty blow next turn!")
        gathering_forces = True
        cooldowns["class_ability_1"] = 2
    
    # Healing ability
    elif action == "d" and class_ability_2 == "Healing" and cooldowns["class_ability_2"] == 0:
        life_total = life_total + 2
        print("\nYou heal yourself for 2 life point!")
        cooldowns["class_ability_2"] = 2
    
    # Bardic insult damage
    elif action == "d" and class_ability_2 == "Bardic Insult" and cooldowns["class_ability_2"] == 0:
        insult = input("\nHurl thy insult: ")
        insult_roll = roll_dice() + charisma_bonus
        if insult_roll > 10:
            damage = 5
            target = random.choice([i for i, g in enumerate(goblins) if g["life"] > 0])
            goblins[target]["life"] -= damage
            if insult_roll > 10:
                print(f"\nYour words cut deep! The goblin dies, taking 5 damage!")
            else:
                print("\nThe goblins just laugh at your weak insult!")
            cooldowns["class_ability_2"] = 2

    # Elf's Turn
    if elf_life>0 and alarion_help == "Help":
        if any(g["life"] > 0 for g in goblins):
            elf_attack_damage = random.randint(1, 3) + 2
            elf_target = random.choice([i for i, g in enumerate(goblins) if g["life"] > 0])
            goblins[elf_target]["life"] -= elf_attack_damage
            print(f"\nAlarion looses an arrow, striking a goblin for {elf_attack_damage} damage!")

    # Victory
    if all(g["life"] <= 0 for g in goblins):
        print("\nThe last goblin falls! The ruined fortress is silent once more...\n")
        break

    # Goblins' Turn
    for g in goblins:
        hit_threshold_att = 12
        if vanish_turns > 0:
            hit_threshold_att += 3
        if g["life"] > 0 and stunned_turns == 0 and roll_dice() + g["attack_bonus"] > hit_threshold_att:
            goblin_damage = random.randint(1, 4)
            print(f"A goblin lunges, slashing thee for {goblin_damage} damage!")
            life_total -= goblin_damage
    if elf_life>0 and alarion_help == "Help":
        alarion_damage = random.randint(1,6)
        elf_life-=alarion_damage
        if elf_life>0:
            print(f"A goblin slashed Alarion! He lost {alarion_damage} life.")
        else:
            print("Viciously, a goblin jumped on Alarion's back and slashed his troath \nright before thy eyes.")
        cooldowns = {key: max(0, val - 1) for key, val in cooldowns.items()}

    # Life total
    if life_total < 0:
        are_you_alive = "dead"
    if life_total > 0:   
        print(f"You have {life_total} life left...")

    # Defeat
    if life_total <= 0:
        print("\nThe goblins overpower thee. Darkness takes thee...\n") 

        break

    if life_total > 0:
        n_goblin = 0
        for g in goblins:
            if g["life"] > 0:
                n_goblin +=1
        if n_goblin>1:
            print(f"There are {n_goblin} goblins left!")
        if n_goblin == 1:
            print("There is one goblin left!")

################################################################################################################
################################################################################################################
################################################################################################################

###### Let's sequence the whole adventure ######

if are_you_alive == "dead":
    exit()

################################################################################################
################################################################################################
################################################################################################

###### Transition 4: The Tavern and Party Recruitment ######

# Calculate bonuses with calculate_bonus
intelligence_bonus = calculate_bonus(intelligence)
wisdom_bonus = calculate_bonus(wisdom)
charisma_bonus = calculate_bonus(charisma)
strength_bonus = calculate_bonus(strength)
dexterity_bonus = calculate_bonus(dexterity)

# Character definitions
characters = {
    "Thorgar": {"class": "Dwarf Fighter", "life": 15, "attack": (5, 10)},
    "Mila": {"class": "Hobbit Bard Healer", "life": 12},
    "Arthros": {"class": "Elf Rogue", "life": 12},
    "Aretra": {"class": "Human Bard", "life": 12},
    "Baldric": {"class": "Dwarf Wizard", "life": 15}
}

def choose_party():
    print("Choose three allies to join thy party in battle:")
    for name, details in characters.items():
        print(f"- {name} ({details['class']})")
    party = []
    while len(party) < 3:
        choice = input("\nEnter the name of a character: ").title()
        if choice in characters and choice not in party:
            party.append(choice)
        else:
            print("Invalid choice or character already selected.")
    return party

# Start the adventure
print("------------------------------------------------------------------------------------------------------------------------")
input("Press Enter to start the next chapter...")
print("\nThe ruins behind you still smolder with the aftermath of battle, the last echoes of your fight against the goblins \nfading into the night. As you leave the battlefield, you encounter a battered traveler on the road. His torn cloak and \ntrembling hands tell a tale of desperation. \"You—you're an adventurer, right?\" he stammers, his eyes darting around \nnervously. \"I barely escaped. A dragon—huge, monstrous—it took over the dwarven mines to the north. It’s hoarding gold, \nslaughtering anyone who dares to enter.\" \n\nHis voice shakes. \"A few of us made it out, but many were not so lucky. If someone doesn’t slay it soon, there won’t be \na village left. If you’re looking for a real fight, this is it.\" \n\nThe weight of his words settles in. A dragon. A true test of skill and strength. If you take on this quest, you’ll \nneed allies. \n\nAhead, nestled at the foot of the mountain, a rustic tavern flickers with warm light, the promise of rest and strong \ndrink beckoning. Stepping inside, the scent of ale and roasted meat fills your lungs. Laughter and hushed \nconversations mingle with the clinking of mugs. \n\nSeated at various tables are warriors and adventurers of all kinds, their weapons resting against their chairs. Some \nglance your way, their interest piqued. The barkeep, a burly woman with arms like tree trunks, gestures toward the crowd. \n\"You said you were looking for strong arms to defeat a dragon? You’ll find 'em here.\" \n\nAt a far table, Thorgar, a burly dwarf fighter, nurses a tankard, his massive axe propped against the wall. His gruff \nvoice rumbles. \"I don’t fight for free. But if it’s a dragon you’re after... that’s a challenge worth taking.\" \n\nNearby, Mila, a sprightly hobbit bard, strums her lute, humming a tune that makes the air feel lighter. She tilts her \nhead. \"A dangerous road? Sounds like you could use a bit of luck—and a healer who can carry a tune.\" \n\nAgainst the bar, Arthros, an elf rogue sharpens his twin daggers, his golden eyes assessing you. \"Am I still here? -Ye...\nGold and glory? Sounds fun. Just don’t expect me to stick around if things get ugly.\" \n\nLeaning against a pillar, Aretra, a human bard, swirls her drink, watching you with an amused smile. \"A tale of heroes \nand dragons? Count me in. But I hope you like stories, because I’ll be singing of this for years.\" \n\nIn a corner, deep in thought, Baldric, a dwarf wizard, absentmindedly mutters an incantation, making his drink levitate. \nHis eyes flicker with arcane power as he meets your gaze. \"A dragon? Fascinating. I wonder what spells I might test on \nsuch a beast.\"\n")
party = choose_party()
print("------------------------------------------------------------------------------------------------------------------------")

################################################################################################
################################################################################################
################################################################################################

###### Dragons's combat ######

# Setting life total
life_total = base_life_total

# Dragon stats
dragon_life = 60

def dragon_attack():
    attacks = ["Breath of Fire", "Breath of Fire", "Tail Swing", "Claw Slash"]
    chosen_attack = random.choice(attacks)
    roll = roll_dice()
    if vanish_turns > 0:
            roll -= 2
    if magical_shield == True:
        print("\nMila sucessfuly shields thous and thy party for this turn, giving you a brief moment to recover...")
        return {"type": "none", "damage": 0}
    if stunned_turns > 0:
        print("\nThe dragon is still under your influence and fails to attack you!")
        return {"type": "none", "damage": 0}
    print("")
    if chosen_attack == "Breath of Fire" and roll > 10:
        print("The dragon unleashes a fiery breath upon the party!")
        return {"type": "fire", "damage": random.randint(1, 4)}
    elif chosen_attack == "Tail Swing":
        return {"type": "tail", "damage": random.randint(3, 5)}
    elif chosen_attack == "Claw Slash":
        return {"type": "claw", "damage": random.randint(3, 5)}
    return {"type": "miss", "damage": 0}

# Stunned ennemy
stunned_turns = 0

# Vanishing effet counter
vanish_turns = 0

# Magical shield
magical_shield = False

# Situation of soldier
gathering_forces = False
cooldowns = {"class_ability_1": 0, "class_ability_2": 0}

# Special option
combat_counter = 0
turn_counter = 0

# Roll buff
roll_buff = False

# Death of party members
def check_for_deaths(party):
    dead_members = [member for member in party if characters[member]['life'] <= 0]
    
    for member in dead_members:
        print(f"\n{member}, the valiant {characters[member]['class']}, has fallen...")
        print(f"As the dragon's mighty blow lands, {member} staggers, their weapon slipping from weary hands. \n"
              "With a final glance towards their companions, they collapse, their name now bound to legend.\n")
        party.remove(member)  # Remove from party
    
    return party

# Start the adventure
print("\nYou just arrived in the dragon's lair. The air was thick with the scent of ancient stone and the acrid tang of \nsmoldering embers. Shadows danced upon the cavern walls, cast by the flickering glow of molten rivers that traced their \nway through the depths of the mountain. The weight of ages pressed down upon you, for this was no ordinary cave—it was \nthe lair of a beast older than kings, older than empires, a creature of legend and terror. Before you, upon a mound of \nsundered armor and charred bones, lay the dragon. Its scales shimmered like tempered bronze, each one etched with the scars \nof battles long forgotten. Twin pools of molten gold stared at you, unblinking, as if already measuring the worth \nof your courage. The air shuddered as it exhaled, sending tendrils of smoke curling through the cavern, whispering promises \nof fire and ruin. Behind you stood your chosen companions, each gripping their weapon or instrument with white-knuckled \nresolve. The time for caution had passed; the time for song and steel had come. If fate was kind, your names would be spoken \nof in hushed reverence across the lands. If not, you would be but another tale lost to the dragon’s hoard.")

# Turn counter
Turn = 1

while dragon_life > 0 and life_total > 0:
    print(f"\nYour Life total: {life_total}")
    for ally in party:
        print(f"{ally}'s Life total: {characters[ally]['life']}")
    
    # Party Attacks first
    for ally in party:
        roll = roll_dice() + (3 if roll_buff == True else 0)
        if ally == "Aretra" and roll >= 10:
            print("\nAretra plays her ukulele, boosting the party's rolls!")
            roll_buff = True
        elif ally == "Aretra" and roll < 10:
            roll_buff = False
            print("\nAretra plays unintentionnaly a false note breaking the rallying effect...")
        elif ally == "Thorgar" and roll >= 10:
            damage = random.randint(*characters[ally]['attack'])
            print(f"\nThorgar swings his axe and deals {damage} damage!")
            dragon_life -= damage
        elif ally == "Thorgar" and roll < 10:
            print(f"\nThorgar swings his axe and miss the dragon's tail!")
        elif ally == "Mila":
            if random.choice([True, False, False, False]) and roll >= 10:
                print("\nMila casts a magical shield, protecting the party from the next attack!")
                magical_shield = True
            elif roll >= 10:
                heal = random.randint(1, 3)
                print(f"\nMila heals the party for {heal} life!")
                life_total = life_total + heal
                for member in party:
                    characters[member]['life'] = characters[member]['life'] + heal
            else:
                print("\nMila fails to heal properly and only heals herself.")
                characters["Mila"]["life"] = characters["Mila"]["life"] + random.randint(3, 6)
        elif ally == "Arthros" and roll >= 10:
            print("\nArthros distracts the dragon, making it harder for the dragon to hit for two turns!")
            vanish_turns = 2
        elif ally == "Arthros" and roll < 10:
            dragon_life -= 3
            print("\nArthros slashes the dragon's wing for three!")
        elif ally == "Baldric" and roll >= 10:
            print("\nBaldric casts a fireball, dealing 10 damage!")
            dragon_life -= 10
        elif ally == "Baldric" and roll < 10:
            damage = random.randint(2, 6)
            print(f"\nBaldric's fireball backfires! The party takes {damage} damage and the dragon 10 damage.")
            life_total -= damage
            for member in party:
                characters[member]['life'] -= damage
            dragon_life -= random.randint(4, 7)
    
    # Check for Defeat due to backlash damage:
    if life_total <= 0:
        print("Thou have been killed by Baldric's fireball...")
        break

    # Remove party dead members
    print("------------------------------------------------------------------------------------------------------------------------")
    party = check_for_deaths(party)

    # Victory
    if dragon_life <= 0:
        print(f"\nThe dragon lets out a final, earth-shaking roar as its massive form collapses, the ground trembling \nbeneath its weight. For a moment, silence hangs over the battlefield—then, a rush of wind sweeps \nthrough the scorched land, carrying the fading embers of battle into the sky.\n")
        break
    
    # Player's turn
    print("------------------------------------------------------------------------------------------------------------------------")
    input("\nClick Enter to enter thy turn.")
    print("\nChoose your action:")
    print(f"a) Attack with thy {short_weapon}")
    print(f"b) Attack with thy {long_weapon}")
    if class_ability_1 != "none" and cooldowns["class_ability_1"] == 0:
        print(f"c) Use: {class_ability_1}")
    if class_ability_2 != "none" and cooldowns["class_ability_2"] == 0:
        print(f"d) Use: {class_ability_2}")
    
    # Special option
    special_option_available = random.randint(1, 3)
    special_choice = "none"
    if special_option_available >= 2:
        special_options = [
            "x) Special Option: Spot a magical rune on the ground. Channel energy into it (INT + WIS, roll above 11 for a \nmagical shockwave that stuns the dragon).",
            "x) Special Option: An ancient banner flutters nearby. Rally thyself and your party members for a morale boost (CHA, roll \nabove 10 for a temporary attack bonus during this combat).",
            "x) Special Option: A shattered potion vial leaks arcane mist. Manipulate it (INT + WIS, roll above 11 for \nmagical protection).",
            "x) Special Option: You lure the dragon into stepping on a hidden explosive you planted. \n(INT + DEX, roll above 12)",
            "x) Special Option: Battlefield Control – You use your surroundings to your advantage (knocking down pillars, \ntriggering a rockslide, etc.). If you roll higher than 13 (INT + WIS), the dragon takes damage and is stunned for one turn."
        ]
        special_choice = random.choice(special_options)
        print(special_choice)
    
    action = input("What dost thou do? ").lower()
    print("------------------------------------------------------------------------------------------------------------------------")
    
    # Short range attack
    if action == "a":
        attack_roll = roll_dice() + strength_bonus + (3 if roll_buff == True else 0)
        if attack_roll > 13:
            damage = short_range_attack * (3 if gathering_forces else 1) # adding fighter damage
            print(f"You strike the dragon with thy {short_weapon}, dealing {damage} damage!")
            dragon_life -= damage
            gathering_forces = False  # Reset gather forces effect, since blow has been delivered
        else:
            print("Your attack misses and bounces off the dragon's scales!")
    
    # Long range attack
    elif action == "b":
        attack_roll = roll_dice() + dexterity_bonus + (intelligence_bonus if char_class=="Wizard" and long_weapon == "Magical staff" else strength_bonus) + (3 if roll_buff == True else 0)
        if attack_roll > 15:
            if long_weapon == "Magical Staff" and char_class == "Wizard": # If the player's class is wizard he may cast spells
                spell_name = input("Name thy damage spell: ")
                print(f"You cast {spell_name}, dealing {long_range_attack} damage to the enraged dragon!")
            else:
                print(f"You launch an attack with thy {long_weapon}, dealing {long_range_attack} damage!")
            dragon_life -= long_range_attack * (3 if gathering_forces else 1)
            gathering_forces = False  # Reset gather forces effect, since blow has been delivered
        else:
            print("Your shot goes wide and misses!")

    # Special action
    elif action == "x" and special_choice != "none":
        roll = roll_dice() + (3 if roll_buff == True else 0)
        if "rope" in special_choice:
            entangle_roll = roll + dexterity_bonus + strength_bonus
            if entangle_roll > 10:
                stunned_turns = 2
                print("\nThe orc is entangled! It shall not attack for two turns.")
            else:
                print("\nThy throw misses, and the orc snarls at thee!")
        elif "rune" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                stunned_turns = 1
                print("\nA magical shockwave erupts, stunning the dragon!")
            else:
                print("When thou touch the rune to activate it it suddenly vanishes...")
        elif "banner" in special_choice:
            if roll + charisma_bonus > 10:
                strength_bonus += 2
                dexterity_bonus += 2
                print("\nThy rallying cry inspires thee! Attack strength increased!")
            else:
                print("\nWhat thou tought to be a banner was a \"want to surrender\" white flag...")
        elif "weapon" in special_choice:
            if roll + dexterity_bonus > 9:
                short_range_attack += 2
                print("\nThou hast found a sturdy weapon, increasing thy attack by two in close combat!")
            else:
                print("\nIn the adrenaline rush thou lost sight of thy weapon")
        elif "potion" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                life_total += 3
                print("\nThe arcane mist envelops thee, restoring some vitality!")
            else:
                print("\nThe potion was simply water...")
        elif "explosive" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                dragon_life -= 10
                print("\nThe dragon steps right where the wanted... Booom, the dragon takes 10 damage!")
            else:
                print("\nThe explosive goes off without any prior warning, harming no one.")
        elif "Control" in special_choice:
            if roll + intelligence_bonus + wisdom_bonus > 11:
                stunned_turns += 1
                print("\nThe time solwy freezes around you, as you as you wreak havoc around you!")
            else:
                print("\nYou are blinded by the reflection of a golden armor plate...")
        
    
    # Healing action
    elif action == "c" and class_ability_1 == "Healing" and cooldowns["class_ability_1"] == 0:
        life_total = life_total + 2
        print("You heal yourself for 2 life point!")
        cooldowns["class_ability_1"] = 2
    
    # Stunning ennemy with "Bagpipe" or "Commanding Voice" and turns during
    elif action == "c" and class_ability_1 in ["Bagpipe", "Commanding Voice"] and cooldowns["class_ability_1"] == 0:
        if roll_dice() + charisma_bonus + (3 if roll_buff == True else 0) > 15:
            stunned_turns = 2
            print(f"\nYou use {class_ability_1}! The dragon is enchanted and cannot attack for {stunned_turns} turns!")
            while stunned_turns > 0:
                stunned_turns -= 1
                print("\nYou (only you) may act freely while the dragon is under your influence!")
                print(f"a) Attack with thy {short_weapon}")
                print(f"b) Attack with thy {long_weapon}")
                if char_class == "Wizard":
                   print("c) Use: Healing") 
                if char_class == "Bard":
                    print("c) Use: Bardic Insult")
                action = input("Choose your next move: ").lower()
                print("------------------------------------------------------------------------------------------------------------------------")
                if char_class == "Wizard":
                    if action == "a":
                        dragon_life -= short_range_attack
                        print(f"You strike again, dealing {short_range_attack} damage!")
                    elif action == "b":
                        dragon_life -= long_range_attack
                        if long_weapon == "Magical Staff" and char_class == "Wizard": # If the player's class is wizard he may cast spells
                            spell_name = input("Name thy damage spell: ")
                            print(f"You cast {spell_name}, dealing {long_range_attack} damage to the dragon!")
                        else:
                            print(f"You launch an attack with thy {long_weapon}, dealing {long_range_attack} damage!")
                    elif action == "c":
                        life_total = life_total + 2
                        print("You heal yourself of two lives!")
                    else:
                        print("Invalid action. You wasted a few precious seconds.")
                if char_class == "Bard":
                    if action == "a":
                        orc_life_total -= short_range_attack
                        print(f"You strike again, dealing {short_range_attack} damage!")
                    elif action == "b":
                        orc_life_total -= long_range_attack
                        print(f"You strike again, dealing {long_range_attack} damage!")
                    elif action == "c":
                        insult = input("Hurl thy insult: ")
                        print(f"Your words cut deep! The dragon already unable to move takes 5 damage!")
                        orc_life_total -= 5
                    else:
                        print("Invalid action. You wasted a few precious seconds.")
        else:
            print("Your attempt to enchant the enraged dragon failed...")
        cooldowns["class_ability_1"] = 2
    
    # Vanishing effect
    elif action == "c" and class_ability_1 == "Vanishing" and cooldowns["class_ability_1"] == 0:
        vanish_turns = 3
        print("You vanish into the shadows, making it harder for the dragon to hit you for three turns!")
        cooldowns["class_ability_1"] = 2
    
    # Gather thy forces
    elif action == "c" and class_ability_1 == "Gather thy forces" and cooldowns["class_ability_1"] == 0:
        print("You gather your strength, preparing for a mighty blow next turn!")
        gathering_forces = True
        cooldowns["class_ability_1"] = 2
    
    # Healing ability
    elif action == "d" and class_ability_2 == "Healing" and cooldowns["class_ability_2"] == 0:
        life_total = life_total + 2
        print("You heal yourself for 2 life point!")
        cooldowns["class_ability_2"] = 2
    
    # Bardic insult damage
    elif action == "d" and class_ability_2 == "Bardic Insult" and cooldowns["class_ability_2"] == 0:
        insult = input("Hurl thy insult: ")
        if roll_dice() + charisma_bonus > 10:
            print(f"Your words cut deep! The dragon reels in anger, taking 5 damage!")
            dragon_life -= 5
        else:
            print("The dragon just ignores your weak insult!")
        cooldowns["class_ability_2"] = 2
    
    # In case not the right letter
    else:
        print("Invalid action or ability on cooldown.")
        continue

    # Victory
    if dragon_life <= 0:
        print(f"\nThe dragon lets out a final, earth-shaking roar as its massive form collapses, the ground trembling \nbeneath its weight. For a moment, silence hangs over the battlefield—then, a rush of wind sweeps \nthrough the scorched land, carrying the fading embers of battle into the sky.\n")
        break
    
    # Dragon Attacks Three
    print("------------------------------------------------------------------------------------------------------------------------\n")
    for _ in range(2):
        attack = dragon_attack()
        if attack["type"] == "fire":
            print(f"The dragon's fiery breath scorches the battlefield, dealing {attack['damage']} damage to everyone!")
            life_total -= attack["damage"]
            for member in party:
                characters[member]['life'] -= attack["damage"]
        elif attack["type"] == "tail":
            targets = random.sample(["player"] + party, 2)
            for target in targets:
                if target == "player":
                    print(f"The dragon's tail slams into you, dealing {attack['damage']} damage!")
                    life_total -= attack["damage"]
                else:
                    print(f"The dragon's tail strikes {target}, dealing {attack['damage']} damage!")
                    characters[target]['life'] -= attack["damage"]
        elif attack["type"] == "claw":
            target = random.choice(["player"] + party)
            if target == "player":
                print(f"The dragon's claws tear into you, dealing {attack['damage']} damage!")
                life_total -= attack["damage"]
            else:
                print(f"The dragon's claws rip into {target}, dealing {attack['damage']} damage!")
                characters[target]['life'] -= attack["damage"]
    if random.randint(1,4) == 1:
        attack = dragon_attack()
        if attack["type"] == "fire":
            print(f"The dragon's fiery breath scorches the battlefield, dealing {attack['damage']} damage to everyone!")
            life_total -= attack["damage"]
            for member in party:
                characters[member]['life'] -= attack["damage"]
        elif attack["type"] == "tail":
            targets = random.sample(["player"] + party, 2)
            for target in targets:
                if target == "player":
                    print(f"The dragon's tail slams into you, dealing {attack['damage']} damage!")
                    life_total -= attack["damage"]
                else:
                    print(f"The dragon's tail strikes {target}, dealing {attack['damage']} damage!")
                    characters[target]['life'] -= attack["damage"]
        elif attack["type"] == "claw":
            target = random.choice(["player"] + party)
            if target == "player":
                print(f"The dragon's claws tear into you, dealing {attack['damage']} damage!")
                life_total -= attack["damage"]
            else:
                print(f"The dragon's claws rip into {target}, dealing {attack['damage']} damage!")
                characters[target]['life'] -= attack["damage"]
    # Remove party dead members
    print("------------------------------------------------------------------------------------------------------------------------")
    party = check_for_deaths(party)

    # Check for Defeat
    if life_total <= 0:
        print("Thou have been slain by the dragon...")
        are_you_alive = "dead"
        break

    # Count turn for x ability
    turn_counter += 1
    
    # Reset parameters
    cooldowns = {key: max(0, val - 1) for key, val in cooldowns.items()}
    Turn +=1
    magical_shield = False

#########################################################################################################
#########################################################################################################
#########################################################################################################

###### End of the story #######
if are_you_alive == "alive":
    print("------------------------------------------------------------------------------------------------------------------------")
    print(f"You stand victorious. The beast, once an unstoppable force of destruction, is no more. \n\nA hush falls over your allies as they take in the sight. Then, one by one, they begin to cheer—some \nraising their weapons high, others collapsing to their knees in exhausted relief. The once-darkened air begins to \nclear, the heavy weight of doom lifting at last.\n\n{character_name}, the Dragonslayer. A title earned in fire and blood... \n\nAs the echoes of battle fade, the world around you begins to change. The world will tell \nstories of this day for generations. Some will call it legend. But you? \nYou were there. You lived it. \n\nThe journey was long. The fight was brutal. But you have won. \n\nThe End.\n")

#########################################################################################################
#########################################################################################################
#########################################################################################################
