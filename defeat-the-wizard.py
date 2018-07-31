import time
print("DEFEAT THE WIZARD!")
print("~~**~~##%%##~~**~~\n")
time.sleep(1)
player_class = ""
enemy = "Black Wizard"

while player_class != "warrior" or player_class != "wizard":
    print("What type of person are you?\n\nType either 'Wizard' or 'Warrior:")
    player_class = input()
    player_class = player_class.lower()
    if player_class == "warrior":
        print("\nYou are a Warrior. A brave swordsman from the clan Algonia!\n\nThe " + enemy + " has destroyed your home and now you seek revenge!\n")
        player_class = "Warrior"
    elif player_class == "wizard":
        print("\nYou are a White Wizard. You have seen the barbaric ways that the " + enemy + " treats humans and you have vowed to destroy him with your white magic!\n")
        player_class = "Wizard"
    else:
        print("\nInvalid selection. Please type either 'Wizard' or 'Warrior'.\n")
        print("\n-----------------------------------------\n")
        continue
    break
    
attack = "Attack"
defend = "Defend"
dmg = 55
full_health = 250
health = full_health
mana = 100
super_smash = dmg*1.7
full_enemy_health = 190
enemy_health = full_enemy_health
thunderbolt_damage = 42
dfd = thunderbolt_damage*0.5
dfd = int(dfd)
battle_choice_made = False
current_health = 'print("Health = " + str(health) + "/" + str(full_health))'
current_enemy_health = 'print("Enemy Health = " + str(enemy_health) + "/" + str(full_enemy_health))'

print("You have arrived to battle the " + enemy + ". Prepare to fight with all your might! \n")

while health > 0 or enemy_health > 0:
    
    print("##########################################################")
    print("#                                                        #")
    print("# [" + attack + "] [" + defend + "]                                      #")
    print("#                                                        #")
    print("# What would you like to do?                             #")
    print("# 'A' for attack or 'D' for defend:                      #")
    battle_choice = input("# ")
    battle_choice = battle_choice.lower()
    battle_choice_made = True
    print("##########################################################")
    
    while battle_choice_made == True:
        if battle_choice == "d":
            print("\nYou will receive 50% less damage the next time you are attacked.\n")
            last_choice = "D"
            if enemy_health > 0:
                print("The " + enemy + " takes aim and strikes you with a mighty thunderbolt.")
                print("Luckily, your defense has protected you.\n")
                health = health-dfd
                exec(current_health)
                exec(current_enemy_health)
                print("")
            else:
                exec(current_health)
                exec(current_enemy_health)
                print("")
        elif battle_choice == "a":
            enemy_health = enemy_health-dmg
            print("\nYou unleash a powerful blow against the evil Wizard!\n")
            exec(current_enemy_health)
            print("")
            last_choice = "A"
            if enemy_health > 0:
                print("The " + enemy + " takes aim and strikes you with a mighty thunderbolt.\n")
                health = health-thunderbolt_damage
                exec(current_health)
                exec(current_enemy_health)
                print("")
            else:
                exec(current_health)
                exec(current_enemy_health)
                print("")
        else:
            print("\nInvalid selection. Please type either 'A' or 'D'.\n")
        break

    if health <= 0:
        print("~~**~~##%%##~~**~~\n")
        print("Oh no! The evil " + enemy + " has felled you! You must try again to defeat him!\n\n")
        break

    if enemy_health <= 0:
        print("~~**~~##%%##~~**~~\n")
        print("And so the mighty hero defeated the evil " + enemy + " restoring peace to the land!\n")
        print("Though the power of the wizard was great, your powers were even stronger! Congratulations!\n")
        print("You are the winner!\n")
        time.sleep(3)
        break
    
print("Game Over\n\nTry Again?")
