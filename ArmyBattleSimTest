#army sim 1

# # Import necessary libraries
# import random

# # Define terrain types
# terrain_types = ['forest', 'desert', 'mountain', 'water']

# # Define army classes
# class Army:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#         self.location = None
#         self.terrain_type = None
#         self.fighting_style = None

#     def move(self, location, terrain_type):
#         self.location = location
#         self.terrain_type = terrain_type
#         self.fighting_style = self.get_fighting_style()

#     def get_fighting_style(self):
#         if self.terrain_type == 'forest':
#             return 'guerilla warfare'
#         elif self.terrain_type == 'desert':
#             return 'long-range attacks'
#         elif self.terrain_type == 'mountain':
#             return 'ambush tactics'
#         elif self.terrain_type == 'water':
#             return 'naval warfare'

# # Define battle function
# def battle(army1, army2):
#     if army1.fighting_style == 'guerilla warfare' and army2.fighting_style == 'long-range attacks':
#         return army1
#     elif army1.fighting_style == 'long-range attacks' and army2.fighting_style == 'guerilla warfare':
#         return army2
#     elif army1.fighting_style == 'ambush tactics' and army2.fighting_style == 'naval warfare':
#         return army1
#     elif army1.fighting_style == 'naval warfare' and army2.fighting_style == 'ambush tactics':
#         return army2
#     else:
#         return random.choice([army1, army2])

# # Define main function
# def main():
#     # Create armies
#     army1 = Army('Army 1', 1000)
#     army2 = Army('Army 2', 1000)

#     # Move armies to random locations
#     army1.move((random.randint(0, 100), random.randint(0, 100)), random.choice(terrain_types))
#     army2.move((random.randint(0, 100), random.randint(0, 100)), random.choice(terrain_types))

#     # Print army locations and fighting styles
#     print(f'{army1.name} is located at {army1.location} and fights with {army1.fighting_style}.')
#     print(f'{army2.name} is located at {army2.location} and fights with {army2.fighting_style}.')

#     # Simulate battle
#     winner = battle(army1, army2)

#     # Print winner
#     print(f'The winner is {winner.name}!')

# # Call main function
# if __name__ == '__main__':
#     main()

#Army sim 2

# # Import necessary libraries
# import random
# import time

# # Define terrain types
# terrain_types = ['forest', 'desert', 'mountain', 'water']

# # Define army classes
# class Army:
#     def __init__(self, name, size, terrain_preference):
#         self.name = name
#         self.size = size
#         self.terrain_preference = terrain_preference
#         self.location = None
#         self.fighting_style = None

#     def move_to(self, location):
#         self.location = location
#         print(f"{self.name} moved to {location}.")

#     def set_fighting_style(self, fighting_style):
#         self.fighting_style = fighting_style
#         print(f"{self.name} is now fighting {fighting_style}.")

# # Define battle function
# def battle(army1, army2, terrain):
#     print(f"Battle between {army1.name} and {army2.name} in {terrain} terrain!")
#     time.sleep(1)

#     # Determine army locations based on terrain preference
#     if army1.terrain_preference == terrain:
#         army1_location = "left"
#         army2_location = "right"
#     elif army2.terrain_preference == terrain:
#         army1_location = "right"
#         army2_location = "left"
#     else:
#         army1_location = random.choice(["left", "right"])
#         army2_location = "left" if army1_location == "right" else "right"

#     # Move armies to their locations
#     army1.move_to(army1_location)
#     army2.move_to(army2_location)

#     # Set fighting styles based on terrain
#     if terrain == "forest":
#         army1.set_fighting_style("ranged")
#         army2.set_fighting_style("melee")
#     elif terrain == "desert":
#         army1.set_fighting_style("melee")
#         army2.set_fighting_style("ranged")
#     elif terrain == "mountain":
#         army1.set_fighting_style("defensive")
#         army2.set_fighting_style("offensive")
#     elif terrain == "water":
#         army1.set_fighting_style("naval")
#         army2.set_fighting_style("naval")

#     # Simulate battle
#     while army1.size > 0 and army2.size > 0:
#         if army1.fighting_style == "ranged":
#             army2.size -= random.randint(1, 10)
#         elif army1.fighting_style == "melee":
#             army2.size -= random.randint(5, 15)
#         elif army1.fighting_style == "defensive":
#             army2.size -= random.randint(1, 5)
#             army1.size += random.randint(1, 5)
#         elif army1.fighting_style == "offensive":
#             army2.size -= random.randint(10, 20)
#             army1.size -= random.randint(1, 5)
#         elif army1.fighting_style == "naval":
#             army2.size -= random.randint(5, 10)
#             army1.size -= random.randint(1, 5)

#         print(f"{army1.name} size: {army1.size}")
#         print(f"{army2.name} size: {army2.size}")
#         time.sleep(1)

#     # Determine winner
#     if army1.size > 0:
#         print(f"{army1.name} wins!")
#     else:
#         print(f"{army2.name} wins!")

# # Create armies
# army1 = Army("Army 1", 100, "forest")
# army2 = Army("Army 2", 100, "desert")

# # Choose terrain
# terrain = random.choice(terrain_types)

# # Start battle
# battle(army1, army2, terrain)

#Army sim 3

# # Import necessary libraries
# import random
# import time

# # Define terrain types
# terrain_types = ['forest', 'desert', 'mountain', 'plains']

# # Define army classes
# class Army:
#     def __init__(self, name, size, terrain_preference):
#         self.name = name
#         self.size = size
#         self.terrain_preference = terrain_preference
#         self.location = None
#         self.health = 100
#         self.morale = 100
#         self.tactics = ['charge', 'defend', 'retreat']
#         self.current_tactic = 'charge'
#         self.target = None

#     def move(self, location):
#         self.location = location

#     def change_tactic(self):
#         self.current_tactic = random.choice(self.tactics)

#     def attack(self, target):
#         damage = random.randint(10, 20)
#         target.health -= damage
#         target.morale -= 10

#     def defend(self):
#         self.morale += 10

#     def retreat(self):
#         self.morale -= 20

# # Define battle class
# class Battle:
#     def __init__(self, army1, army2, terrain):
#         self.army1 = army1
#         self.army2 = army2
#         self.terrain = terrain

#     def start(self):
#         print(f"Battle between {self.army1.name} and {self.army2.name} in {self.terrain} terrain begins!")
#         time.sleep(2)

#         while self.army1.health > 0 and self.army2.health > 0:
#             self.army1.change_tactic()
#             self.army2.change_tactic()

#             if self.army1.current_tactic == 'retreat' and self.army2.current_tactic == 'retreat':
#                 print("Both armies have retreated!")
#                 break

#             if self.army1.current_tactic == 'retreat':
#                 print(f"{self.army1.name} has retreated!")
#                 break

#             if self.army2.current_tactic == 'retreat':
#                 print(f"{self.army2.name} has retreated!")
#                 break

#             if self.army1.current_tactic == 'charge':
#                 self.army1.attack(self.army2)
#                 print(f"{self.army1.name} charges {self.army2.name} and deals damage!")

#             if self.army2.current_tactic == 'charge':
#                 self.army2.attack(self.army1)
#                 print(f"{self.army2.name} charges {self.army1.name} and deals damage!")

#             if self.army1.current_tactic == 'defend':
#                 self.army1.defend()
#                 print(f"{self.army1.name} defends and gains morale!")

#             if self.army2.current_tactic == 'defend':
#                 self.army2.defend()
#                 print(f"{self.army2.name} defends and gains morale!")

#             time.sleep(2)

#         if self.army1.health <= 0 and self.army2.health <= 0:
#             print("Both armies have been defeated!")
#         elif self.army1.health <= 0:
#             print(f"{self.army2.name} has won the battle!")
#         else:
#             print(f"{self.army1.name} has won the battle!")

# # Create armies
# army1 = Army('Red Army', 100, 'forest')
# army2 = Army('Blue Army', 100, 'desert')

# # Create battle
# battle = Battle(army1, army2, random.choice(terrain_types))

# # Start battle
# battle.start()
