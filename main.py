import random
import time
import os
import platform

sleeptime = 0.75
playerHealth = 25
playerDamage = 1

# Enemies
enemies = [
    {
        "name": "Goblin",
        "health": 20,
        "damage": 2,
        "hit_chance": 0.8  # 80% chance to hit
    },
    {
        "name": "Orc",
        "health": 40,
        "damage": 5,
        "hit_chance": 0.7  # 70% chance to hit
    },
    {
        "name": "Dragon",
        "health": 100,
        "damage": 10,
        "hit_chance": 0.6  # 60% chance to hit
    },
    {
        "name": "Skeleton",
        "health": 25,
        "damage": 4,
        "hit_chance": 0.9  # 90% chance to hit
    }
]

# Weapons
weapons = [
    {
        "name": "Sword",
        "damage_modifier": 4,
        "hit_chance": 0.95  # 96% chance to hit
    },
    {
        "name": "Axe",
        "damage_modifier": 6,
        "hit_chance": 0.85  # 75% chance to hit
    },
    {
        "name": "Bow",
        "damage_modifier": 12,
        "hit_chance": 0.60  # 60% chance to hit
    }
]

# Armors
armors = [{
    "name": "Light Armor",
    "health_modifier": 2
}, {
    "name": "Medium Armor",
    "health_modifier": 4
}, {
    "name": "Heavy Armor",
    "health_modifier": 6
}]


def wait():
  time.sleep(sleeptime)


def clear():
  if platform.system() == 'Linux':
    os.system('clear')
  elif platform.system() == 'Windows':
    os.system('cls')


def loading_dots():
  print(" ", end="", flush=True)
  for _ in range(5):
    time.sleep(0.3)
    print(".", end="", flush=True)
  print()


def start():
  print("Welcome to the dungeon!")
  time.sleep(sleeptime)


start()

username = input("What is your name? ")
print(username + " enters the dungeon\n")

# Choose Weapon
weapon_choice = int(
    input("What weapon do you choose?\n\n 1. Sword\n 2. Axe\n 3. Bow\n\n")) - 1

chosen_weapon = weapons[weapon_choice]
print(f"\nYou have chosen the {chosen_weapon['name']}!")
playerDamage += chosen_weapon["damage_modifier"]
player_hit_chance = chosen_weapon["hit_chance"]
print(
    f"You do {playerDamage} damage per hit with a {player_hit_chance * 100}% chance of hitting!\n"
)

wait()

# Choose Armor
armor_choice = int(
    input(
        "What armor do you choose?\n\n 1. Light Armor\n 2. Medium Armor\n 3. Heavy Armor\n\n"
    )) - 1

chosen_armor = armors[armor_choice]
print(f"\nYou have chosen the {chosen_armor['name']}!")
playerHealth += chosen_armor["health_modifier"]
print(
    f"You have {playerHealth} health points and do {playerDamage} damage per hit!\n"
)


def askready():
  ready = int(input("Ready to enter the dungeon?\n\n 1. Yes\n 2. No\n\n"))
  if ready == 1:
    clear()
    print("You enter the dungeon!")
  else:
    time.sleep(5)
    askready()


askready()


def combat(playerHealth, playerDamage, player_hit_chance, enemy):
  enemyHealth = enemy["health"]
  enemyDamage = enemy["damage"]
  enemy_hit_chance = enemy["hit_chance"]

  print(f"You encounter a wild {enemy['name']}" + "!")

  while playerHealth > 0 and enemyHealth > 0:
    print("\nYour turn!")
    action = int(
        input("Choose an action:\n 1. Attack\n 2. Dodge\n 3. Run\n\n"))

    if action == 1:
      # Player's attack
      if random.random() < player_hit_chance:
        enemyHealth -= playerDamage
        print(f"You dealt {playerDamage} damage to the {enemy['name']}!")
      else:
        print(f"You missed the {enemy['name']}!")

      # Enemy's attack
      if enemyHealth > 0:
        print(f"\nThe {enemy['name']} attacks!")
        if random.random() < enemy_hit_chance:
          playerHealth -= enemyDamage
          print(f"The {enemy['name']} dealt {enemyDamage} damage to you!")
        else:
          print(f"The {enemy['name']} missed you!")
    elif action == 2:
      # Dodge mechanic
      dodge_chance = random.random()
      if dodge_chance < 0.5:
        print(f"You successfully dodged the {enemy['name']}'s attack!")
      else:
        print(f"You failed to dodge the {enemy['name']}'s attack!")
        if random.random() < enemy_hit_chance:
          playerHealth -= enemyDamage
          print(f"The {enemy['name']} dealt {enemyDamage} damage to you!")
        else:
          print(f"The {enemy['name']} missed you!")

    elif action == 3:
      # Run mechanic
      run_chance = random.random()
      if run_chance < 0.3:
        print("You successfully escaped the enemy!")
        return playerHealth
      else:
        print("You failed to escape the enemy!")

    if enemyHealth <= 0:
      print(f"\nYou defeated the {enemy['name']}!")
      break

    if playerHealth <= 0:
      print("\nYou have been defeated!")
      break

  return playerHealth


def random_encounter():
  return random.choice(enemies)


while playerHealth > 0:
  currentEnemy = random_encounter()
  playerHealth = combat(playerHealth, playerDamage, player_hit_chance,
                        currentEnemy)

  if playerHealth <= 0:
    print("You died.\n Game over.")
    break
  else:
    print(
        f"\nYou survived the encounter with {playerHealth} health remaining.\n"
    )
    proceed = input(
        "Do you want to continue further into the dungeon?\n\n 1. Yes\n 2. No\n\n"
    )
    if proceed == "2":
      print("You escaped the dungeon with your life. Well done!")
      break
