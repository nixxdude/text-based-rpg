import sys, os, time, pickle

class Player:
    def __init__(self, name, max_hp, current_hp, equipped_weapon, strength, coins):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.equipped_weapon = equipped_weapon
        self.damage = equipped_weapon.damage
        self.strength = strength
        self.inventory = {}
        self.coins = coins

class Weapon:
    def __init__(self, name, desc, damage, shop_cost):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.shop_cost = shop_cost

# wooden_baton = Weapon('Wooden Baton', '')


# def start():
#     print('Hello, user.')
#     check_save_path = os.path.exists('saves')
#     if check_save_path == False:
#         os.mkdir('saves')
#     else:
#         pass
#     check_save = os.path.exists('saves/savefile.dat')
#     if check_save == True:
#         pickle.load

# start()
