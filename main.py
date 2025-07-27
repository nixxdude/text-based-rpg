class Weapon:
    def __init__(self, name, attacks):
        self.name = name
        self.attacks = {}

class Player:
    def __init__(self, name, hp, strength, speed, mana, equipped_weapon, player_class, inventory, coins):
        self.name = name
        self.hp = hp
        self.damage = equipped_weapon.damage
        self.strength = strength
        self.speed = speed
        self.mana = mana
        self.equipped_weapon = equipped_weapon
        self.player_class = player_class
        self.inventory = inventory
        self.coins = coins

player = Player("placeholder", 30, 1, 1, 30,)

class PlayerClass:
    def __init__(self, name, hp_buff, strength_buff, speed_buff, mana_buff, disabled_weapons):
        self.name = name
        self.hp_buff = hp_buff
        self.strength_buff = strength_buff
        self.speed_buff = speed_buff
        self.mana_buff = mana_buff
        self.disabled_weapons = disabled_weapons
    
    def add_bonuses(PlayerClass):
        Player.health = Player.health + PlayerClass.hp_buff
        Player.strength = Player.strength + PlayerClass.strength_buff
        Player.speed = Player.speed + PlayerClass.speed_buff
        Player.mana = Player.mana + PlayerClass.mana_buff


