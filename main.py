from tkinter.messagebox import *
from mLib import *
from time import *
import math as mth
import random as rnd
import os
import sys
import json

cls()



class Item:
    def __init__(self, name, type, description = ""):
        self.name = name
        self.type = type
        self.description = description

class Room:
    def __init__(self, name, boss, nextRoom, final, enemies, chest = None, npc = None, shop = None, puzzle = None, loot=[], piano = None):
        self.name = name
        self.boss = boss
        self.nextRoom = nextRoom
        self.final = final
        self.chest = chest
        self.enemies = enemies
        self.npc = npc
        self.shop = shop
        self.puzzle = puzzle
        self.loot = loot
        self.piano = piano




class Weapon:
    def __init__(self, name, atk, type, description = ""):
        self.name = name
        self.atk = atk
        self.type = type
        self.description = description

class Armor:
    def __init__(self, name, dfn, type, description = ""):
        self.name = name
        self.dfn = dfn
        self.type = type
        self.description = description

class Food:
    def __init__(self, name, heal, text, type, description = ""):
        self.name = name
        self.heal = heal
        self.text = text
        self.type = type
        self.description = description


class Enemy:
    def __init__(self, name, hp, maxHP, atk, exp, text, boss = False, instSpare = False):
        self.name = name
        self.hp = hp
        self.maxHP = maxHP
        self.atk = atk
        self.exp = exp
        self.text = text
        self.boss = boss
        self.instSpare = instSpare

class Magic:
    def __init__(self, name, cost, atk, heal):
        self.name = name
        self.cost = cost
        self.atk = atk
        self.heal = heal

class Chest:
    def __init__(self, items):
        self.items = items
        self.opened = False



class NPC:
    def __init__(self, name, dialogue, items=None, trade=False):
        self.name = name
        self.dialogue = dialogue
        self.items = items if items else []
        self.trade = trade

class Piano:
    def __init__(self, name):
        self.name = name
        


class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def show_items(self):
        print(f"\n=== {self.name} ===")
        for idx, (item, price) in enumerate(self.items):
            print(f"[{idx}] {item.name} — {price} gold")
        print("[b] Back")


class Puzzle:
    def __init__(self, question, answer, hint=None):
        self.question = question
        self.answer = answer
        self.hint = hint

    def check(self, user_input):
        return str(user_input).strip().lower() == str(self.answer).strip().lower()

switches = Puzzle(
    question="Press switches(F, Y, B) in correct sequence.",
    answer="B F Y",
    hint="Think about sequence"
)

code = Puzzle(
    question="ENTER CODE",
    answer="3457",
    hint="Robot knows code."
)

nothing = Item(name = "", type = "internal")

stick = Weapon(name = "Stick", atk = 2, type = "weapon", description = "Just wooden stick. +2 ATK")

noteknife = Weapon(name = "Note Blade", atk = 5, type = "weapon", description = "A blade made from musical notes. +5 ATK.")

scienceStaff = Weapon(name = "Science Staff", atk = 7, type = "weapon", description = "An old staff... +7 ATK")

scrap = Weapon(name = "Scrap", atk = 12, type = "weapon", description = "A long, sharp metal pipe. +12 ATK")
rustDagger = Weapon(name = "Rusted Dagger", atk = 14, type = "weapon", description = "A rusted steel dagger. There is cat drawn on its blade. +14 ATK")

electricRod = Weapon(name = "Electric Rod", atk = 16, type = "weapon", description = "A long, blue glass pipe with energy inside it. +16 ATK")

oldStaff = Weapon(name = "Old Staff", atk = 26, type = "weapon", description = "An old, wooden staff. There is a cat drawn on it. +26 ATK")

debugWP = Weapon(name = "Debug Stick", atk = 10**40-1, type = "weapon", description = "just smal stick. +NaN ATK")


bandage = Armor(name = "Bandage", dfn = 2, type = "armor", description = "Made of premium materials. +2 DEF")

boneArmor = Armor(name = "Bone Armor", dfn = 4, type = "armor", description = "An armor made from bones. +4 DEF")

catCloak = Armor(name = "Cat Cloak", dfn = 5, type = "armor", description = "A red, big cloak with cat drawed on its back. +5 DEF")

labCoat = Armor(name = "Lab Coat", dfn = 8, type = "armor", description = "An white, old lab coat. +8 DEF")

forceField = Armor(name = "Force Field", dfn = 14, type = "armor", description = "An smal electrical device. +14 DEF")

locket = Armor(name = "The Locket", dfn = 18, type = "armor", description = "An locket in shape of heart. Its made from gold.\nThere are photo with three cats and text: 'Don't forget.' inside it... +18 DEF")


dumplings = Food(name = "Dumplings", heal = 40, text = "Not very tasty.", type = "food", description = "Just dumplings with meat. Heals 40 HP.")
cheesecake = Food(name = "Cheesecake", heal = 100, text = "Very sweet.", type = "food", description = "An extremely big cheesecake. Heals 100 HP.")
susdog = Food(name = "Suspicous Dog", heal = 999999, text = "Is it legal?", type = "food", description = "A dog? Heals ??? HP.")
bread = Food(name = "Bread", heal = 25, text = "Bread. Just bread.", type = "food", description = "Just bread. Heals 25 HP.")
flakes = Food(name = "Flakes", heal = 10, text = "Very bitter.", type = "food", description = "A flakes made by cats. Heals 10 HP.")
susbottle = Food(name = "Suspicous Flask", heal = -999999999999, text = "...", type = "kill", description = "An glass flask. There are written: 'Hydrochloric Acid'")
spooderSoup = Food(name = "Spooder Soup", heal = 65, text = "Disgusting.", type = "food", description = "An very suspicous soup. Heals 65 HP.")
spooderBread = Food(name = "Spooder Bread", heal = 20, text = "Normal bread are better.", type = "food", description = "A purple bread. Heals 20 HP.")

energyDrink = Food(name = "Energy Drink", heal = 55, text = "Very bitter.", type = "food", description = "A metal bottle with energy drink. Heals 55 HP.")

mintTea = Food(name = "Mint Tea", heal = 999999999, text = "This is the best tea ever.", type = "food", description = "A cup of mint tea. Heals ??? HP.")



nukeButton = Item("Red Button", type = "nukeTrigger", description = "A red button with nuke sticker on it. I wouldn't recommend pressing it...")

oldPiano = Piano(name = "Old Piano")

dogChest = Chest(items=[susdog, dumplings, boneArmor])
pianoChest = Chest(items=[noteknife])
catChest = Chest(items=[flakes, dumplings, flakes, catCloak, cheesecake])
labChest = Chest(items=[susbottle, energyDrink, scienceStaff, labCoat])
warehouseChest = Chest(items=[scrap, rustDagger])
chargeChest = Chest(items=[electricRod, forceField])
finalChest = Chest(items=[mintTea, locket, oldStaff])


smolDoge = Enemy(name = "Smol Doge", hp = 15, maxHP = 15, atk = 1, exp = 6, text = "is barking and jumping around you!", instSpare = True)
dog = Enemy(name = "Just Dog", hp = 20, maxHP = 20, atk = 3, exp = 12, text = "is.... BARK! BARK! BARK!")
doge = Enemy(name = "Doge", hp = 160, maxHP = 450, atk = 8, exp = 120, text = "is barking and trying defeat you.", boss = True)

bob = Enemy(name = "bob", hp = 120, maxHP = 120, atk = 5, exp = 45, text = "is here to defeat you!")
leo = Enemy(name = "Leopold", hp = 75, maxHP = 75, atk = 2, exp = 25, text = "is failing on your head!")

smolSpooder = Enemy(name = "Smol Spooder", hp = 5, maxHP = 5, atk = 1, exp = 3, text = "is running across the room.", instSpare = True)

spooder = Enemy(name = "Big Spooder", hp = 50, maxHP = 50, atk = 8, exp = 40, text = "crawled from the hole.")
fastSpooder = Enemy(name = "Spooder, but faster", hp = 45, maxHP = 45, atk = 6, exp = 60, text = "is running around you.")
hugeSpooder = Enemy(name = "   H U G E    S P O O D E R", hp = 230, maxHP = 230, atk = 11, exp = 175, text = "   A T T A C K S.", boss = True)

smolRobot = Enemy(name = "Smol Robot", hp = 30, maxHP = 30, atk = 7, exp = 15, text = "is sweeping floor and encountered you.")
terminator = Enemy(name = "TERMINATOR", hp = 670, maxHP = 670, atk = 17, exp = 560, text = "IS WANTS TO TERMINATE YOU!", boss = True)

lordcat = Enemy(name = "Lord Cat", hp = 800, maxHP = 800, atk = 23, exp = 720, text = "is want to defeat you.", boss = True)

annoyDog = NPC(
    name="Annoying Dog",
    dialogue=[
        "Bark!",
        "Be careful there!",
        "Bark!"
    ]
)

basik = NPC(
    name = "Basik",
    dialogue=[
        "meow",
        "lord cat is strong",
        "be careful..."
    ]
)


cactus = NPC(
    name="Cactus",
    dialogue=[
        "Meow. I am a Cactus.",
        "Don't be surprised, I really am a cat named Cactus..",
        "I'm here to give you some advice: be careful with the piano.",
        "Sometimes music opens doors that are better left unopened..."
    ]
)

spiid = NPC(
    name = "Spiid",
    dialogue=[
        "abebebebebe....................",
        "biiiii cariifullll.........",
        "....orr hugii spiiidiiirrrr wiillll eattt youuuuuu........."
    ]
)

oldRobot = NPC(
    name = "Old Robot",
    dialogue=[
        r"GU/-\RD|\|3R 1.24 IS R<EAD@ TO @6TAC|<...    AND D3FE|\|D...",
        r"ST/T*$: D7MAG/D...",
        r"COD\de: 34.. ,hb 57... f8798)(*67^#)#.....",
        r"ERR@R;*$^&jjjb  ;F><?dk.............",
        "...",
        "..."
        
    ]
)


catShop = Shop("cat's shopp", [
    (flakes, 5),
    (dumplings, 20),
    (bread, 10)
])

spooderSale = Shop("Spooder Sale", [
    (spooderBread, 5),
    (spooderSoup, 15)
])

finalRoom = Room(name = "The Lord's House", boss = lordcat, nextRoom = "", final = True, enemies = [smolSpooder], loot = [bread], chest = finalChest)
chargeRoom = Room(name = "The Charging Room", boss = terminator, nextRoom = finalRoom, final = False, enemies = [smolRobot], loot = [scrap], chest = chargeChest)
warehouse = Room(name = "The Warehouse", boss = None, nextRoom = chargeRoom, final = False, chest = warehouseChest, enemies = [smolRobot], puzzle = code, npc = [oldRobot], loot = [scrap, nukeButton])
spiderRoom = Room(name = "The Spooders Lair", boss = hugeSpooder, nextRoom = warehouse, final = False, enemies = [smolSpooder, spooder, fastSpooder], npc = [spiid], shop = spooderSale, loot = [spooderBread, spooderSoup])
lab = Room(name = "The Secret Lab", boss = None, nextRoom = spiderRoom, final = False, chest = labChest, enemies = [smolSpooder], puzzle = switches, loot = [susbottle])
catRoom = Room(name = "The Cat Room", boss = None, nextRoom = lab, final = False, chest = catChest, enemies = [bob, leo], npc = [basik, cactus], shop = catShop, loot = [flakes, dumplings, bread])
pianoRoom = Room(name = "The Piano Room", boss = None, nextRoom = catRoom, final = False, chest = pianoChest, enemies = [smolSpooder], loot = [flakes], piano = oldPiano)
dogRoom = Room(name = "The Dog Room", boss = doge, nextRoom = pianoRoom, final = False, chest = dogChest, enemies = [smolDoge, dog], npc = [annoyDog], loot = [dumplings, susdog])

roomOfDog = Room(name = "Room of Dog", boss = None, nextRoom = "", final = False, chest = None, enemies = [], npc = [], loot = [])

lv = 1
exp = 0
maxHP = 100
hp = 100
maxMP = 100
mp = 0
inventory = [nothing, nothing, nothing, nothing, nothing, nothing, nothing, nothing]
weapon = stick
armor = bandage
atk = 0
atkFin = 0
dfn = 0
dfnFin = 0
room = dogRoom
monsters = 70
bosses = 4
gold = 0
name = ""
gender = ""
atk_bonus = 0
mp_bonus = 0
appearance = ""


kills = 0
spared = 0
pacifist_eligible = True
dirtyHacker = False


bolt = Magic(name = "Lighting Bolt", cost = 70, atk = 10**40-1, heal = 0)
healer = Magic(name = "Heal", cost = 60, atk = 0, heal = 60)
fireball = Magic(name = "Fireball", cost = 40, atk = 25, heal = 0)
shield = Magic(name = "Shield", cost = 30, atk = 0, heal = 0)
meteor = Magic(name = "Meteor", cost = 100, atk = 50, heal = 0)





neutral_battle_messages = [
    "Wind howls through the chamber.",
    "The walls tremble slightly.",
    "A distant echo answers the clash.",
    "Shadows twist around you.",
    "Your heartbeat echoes in your ears.",
    "Dust rises from the ancient floor.",
    "The air grows colder.",
    "Sometimes, violence isn't the answer. But you already know that, right?"
]



CRIT_CHANCE = 0.3
CRIT_MULTIPLIER = 5.0


def updateHP():
    global hp
    global maxHP
    
    maxHP = 90 + 10 * lv

def updateLV():
    global lv
    
    if exp == 0:
        lv = 1
    else:
        lv = int((exp / 20) ** 0.5) + 1

def updateATK():
    global atk
    global atkFin
    
    atk = weapon.atk + atk_bonus
    atkFin = atk + lv - 1

def updateDFN():
    global dfn
    global dfnFin
    
    dfn = armor.dfn
    dfnFin = dfn + lv - 1

def updateMP():
    global maxMP
    global mp
    
    maxMP = 100 * lv + mp_bonus

def exp_for_level(level):
    if level <= 1:
        return 0
    return 20 * (level - 1) ** 2


def get_exp_to_next_level():
    current_lv = lv
    next_lv = current_lv + 1
    current_exp_threshold = exp_for_level(current_lv)
    next_exp_threshold = exp_for_level(next_lv)
    return next_exp_threshold - exp



def heal(hpHeal, text, name, type):
    global hp
    global maxHP

    if type == "kill":
        print("You drinked Suspicous Flask....")
        sleep(2.3)
        hp = 0
        gameover()

    print(f"You ate {name}. {text}")
    sleep(1.2)
    if hp + hpHeal < maxHP:
        print(f"Recovered {hpHeal} HP({hp+hpHeal}/{maxHP}).")
    else:
        print(f"HP maxed out.")

    hp = min(hp + hpHeal, maxHP)


def printa(text, delay=0.05, effect=None, newline=True):
    if effect == "glitch":
        for char in text:
            print(char, end='', flush=True)
            sleep(delay * rnd.uniform(0.5, 2.0))
            if rnd.random() < 0.1:
                print(rnd.choice(["░", "▒", "▓", "█"]), end='', flush=True)
                sleep(0.1)
    elif effect == "whisper":
        for char in text:
            print(char, end='', flush=True)
            sleep(delay * 2)
    elif effect == "fade":
        for i in range(1, len(text) + 1):
            print(text[:i], end='\r', flush=True)
            sleep(delay * 0.8)
        print()     
    elif effect == "shout":
        print(text.upper(), flush=True)
        sleep(delay * 0.3)
    else:
        for char in text:
            print(char, end='', flush=True)
            sleep(delay)
    if newline:
        print()


def blink(text, iterations=10, delay=0.1):
    for _ in range(iterations):
        sys.stdout.write(text + "\r")
        sys.stdout.flush()
        sleep(delay)
        sys.stdout.write(" " * len(text) + "\r")
        sys.stdout.flush()
        sleep(delay)




def printsta(lines, delay_between=2.0, text_delay=0.05, effect=None):

    cls()
    print("\n" + "="*40)
    for line in lines:
        printa(line, text_delay, effect=effect)
        sleep(delay_between)
    print("="*40)
    sleep(1)


def show_credits():
    credits_text = [
        "",
        "Credits:",
        "Game Design: Alex",
        "Programming: Alex",
        "Special Thanks:",
        "- You, for playing",
        "- My cat, for the moral support",
        "- Alexey Evgenevich, for the idea",
        "",
        "The End."
    ]
    printsta(credits_text, delay_between=1.5, text_delay=0.07)

def show_about():
    cls()
    print("\n=== ABOUT ===")
    print("Game: THE UNDERGROUND")
    print("Version: 1.0")
    print("Developer: Alex")
    print("Genre: Text-based RPG")
    print("\nDescription:")
    print("A dark fantasy adventure through mysterious underground chambers.")
    print("Face monsters, solve puzzles, and choose your path — violence or peace.")
    print("\nSpecial Thanks:")
    print("- You, for playing!")
    print("- My cat, for moral support")
    print("- Alexey Evgenevich, for the idea")
    print("\n© 2026 Alex. All rights reserved.")
    input("\nPress Enter to return...")




def final_consequence():
    global pacifist_eligible, kills, spared

    
    if kills == 0 and pacifist_eligible:
        print("A strange feeling... No dust on your hands.")
        print("The air is calm. You sense a hidden path.")
    else:
        print("The ground trembles. The weight of your actions follows you.")
    


def get_weapon_by_name(name):
    weapons = {w.name: w for w in [stick, noteknife, scienceStaff, scrap, rustDagger, electricRod, oldStaff, debugWP]}
    return weapons.get(name, stick)


def get_armor_by_name(name):
    armors = {a.name: a for a in [bandage, boneArmor, catCloak, labCoat, forceField, locket]}
    return armors.get(name, bandage)

def get_item_by_name(name):
    items = {i.name: i for i in [dumplings, cheesecake, susdog, bread, flakes, susbottle, spooderBread, spooderSoup, energyDrink, mintTea, nukeButton]}
    return items.get(name, nothing)
    
def get_room_by_name(name):
    rooms = {i.name: i for i in [dogRoom, pianoRoom, catRoom, lab, spiderRoom, warehouse, chargeRoom, finalRoom]}
    return rooms.get(name, roomOfDog)
 

def save_game(filename="save.json"):
    current_save = {
        "name": name,
        "gender": gender,
        "atk_bonus": atk_bonus,
        "mp_bonus": mp_bonus,
        "appearance": appearance,
        "room": room.name,
        "hp": hp,
        "mp": mp,
        "lv": lv,
        "exp": exp,
        "gold": gold,
        "weapon": weapon.name,
        "armor": armor.name,
        "inventory": [item.name for item in inventory],
        "kills": kills,
        "spared": spared,
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(current_save, f, indent=2)
    
    print("\nFile saved!")
    


def load_game(filename="save.json"):
    global name, room, hp, mp, lv, exp, gold, weapon, armor, inventory, kills, spared

    
    if not os.path.exists(filename):
        print("There are no save files!")
        sleep(0.5)
        return False
    
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    name = data["name"]
    gender = data["gender"]
    atk_bonus = data["atk_bonus"]
    mp_bonus = data["mp_bonus"]
    appearance = data["appearance"]
    room = get_room_by_name(data["room"])
    hp = data["hp"]
    mp = data["mp"]
    lv = data["lv"]
    exp = data["exp"]
    gold = data["gold"]
    
    weapon = get_weapon_by_name(data["weapon"])
    armor = get_armor_by_name(data["armor"])
    inventory = [get_item_by_name(name) for name in data["inventory"]]
    
    kills = data["kills"]
    spared = data["spared"]
    
    
    print("\nFile loaded!")
    sleep(0.5)
    return True


def gameover():
    cls()
    print("GAME OVER!")
    printa(f"{name}, don't give up!")
    sleep(0.3)
    printa("Save the DETERMINATION!")
    sleep(0.6)
    print()
    input("Press Enter to continue...")
    sleep(1.5)
    
    if load_game():
        pass
    else:
        exit()

def show_ending():
    global kills, spared, pacifist_eligible, lv
    
    if dirtyHacker == True:
        if pacifist_eligible and kills == 0:
            printa("How you do this?")
            print("\n[HACKED PACIFIST ENDING]")
            print("Peace settles over The Underground.")
            sleep(5)
            show_credits()

        elif monsters == 0 and bosses == 0:
            printa("Silence. Only the echo of your steps remains.", 0.3)
            printa("Dirty hacker... stop it please...", 0.3)
            print("\n[HACKED GENOCIDE ENDING]")
            print("The Underground is empty. Was it worth it?")
            sleep(5)
            show_credits()
        else:
            printa("bruh... it's worst ending ever...", 0.3)
            print("\n[HACKED NEUTRAL ENDING]")
            print("The story ends... or not? (UNDERGROUND 2: JUSTICE will be released soon)")
            sleep(5)
            show_credits()
        

    elif pacifist_eligible and kills == 0:
        printa("The world breathes easier.", 0.3)
        printa("You chose compassion. Even Lord Cat lowered his claws.", 0.3)
        printa("'Maybe... we can coexist'", 0.3)
        print("\n[PACIFIST ENDING]")
        print("Peace settles over The Underground.")
        sleep(5)
        show_credits()
        


    elif monsters == 0 and bosses == 0:
        printa("Silence. Only the echo of your steps remains.", 0.3)
        printa("Every creature lies still. You are alone.", 0.3)
        print("\n[GENOCIDE ENDING]")
        print("The Underground is empty. Was it worth it?")
        sleep(5)
        show_credits()

        
    else:
        printa("You survived. But at what cost?", 0.3)
        if kills > 5:
            printa("The walls are stained. You try not to look.", 0.3)
        elif spared > 5:
            printa("Some faces flash in your memory. You hope they're safe.", 0.3)
        else:
            printa("You walk away, unsure if you made the right choices.", 0.3)
        print("\n[NEUTRAL ENDING]")
        print("The story ends... or not?")
        sleep(5)
        show_credits()



def create_character():
    global name, gender, atk_bonus, mp_bonus, appearance, lv, exp, maxHP, hp, maxMP, mp, atk, dfn, weapon, armor, name
    
    cls()
    
    print("=============================================")
    print("         CREATE YOUR CHARACTER")
    print("=============================================")

    sleep(1.5)
    
    name = input("Enter your character's name: ").strip()
    while not name:
        print("Name cannot be empty!")
        name = input("Enter your character's name: ").strip()

    gender = input("Gender (M/F): ").strip().lower()
    while gender not in ['m', 'f']:
        gender = input("Gender (M/F): ").strip().lower()
    
    
    print("Choose class:")
    print("1. Warrior (+ATK, -MP)")
    print("2. Mage (+MP, -ATK)")
    print("3. Default(No changes)")
    class_choice = input("> ")
    if class_choice == "1":
        atk_bonus = 5
        mp_bonus = -20
    elif class_choice == "2":
        atk_bonus = -3
        mp_bonus = 30
    else:
        pass
    
    print("\nChoose appearance:")
    hair = input("Hair color (e.g., brown, red, blue): ").strip()
    eyes = input("Eye color: ").strip()
    build = input("Build (slender/athletic/stocky): ").strip()
    
    if gender == "m":
        appearance = f"A {build} male with {hair} hair and {eyes} eyes."
    elif gender == "f":
        appearance = f"A {build} female with {hair} hair and {eyes} eyes."
    else:
        for i in range(10000):
            printa("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", delay = 0.001)
        showerror(title="Critical Error", message="""Traceback (most recent call last)
File "underground.py", line 711, in <module>
    printa("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

Unknown Error""")
        os._exit(1)
    print("The journey begins...")
    sleep(2)




def nuclear_explosion():




    def generate_frame(radius, char_set):

        lines = [" " * 50 for _ in range(15)]
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                dist_sq = i*i + j*j
                if dist_sq <= radius * radius:
                    y = 7 + i
                    x = 25 + j
                    if 0 <= y < 15 and 0 <= x < 50:
                        char = random.choice(char_set)
                        lines[y] = lines[y][:x] + char + lines[y][x+1:]
        return "\n".join(lines)

    def shake_text(text, intensity=2):

        shifted = ""
        for char in text:
            shift = random.randint(-intensity, intensity)
            shifted += " " * max(0, shift) + char
        return shifted


    cls()
    print("NUCLEAR EXPLOSION!!!")
    sleep(1.2)

    print(shake_text(". . . .", 1))
    sleep(0.4)
    cls()

    print(shake_text("* * *", 1))
    sleep(0.3)
    cls()


    for r in range(1, 10):
        if r < 4:
            chars = "*@#"
        elif r < 7:
            chars = "%%%"
        else:
            chars = ".~"

        frame = generate_frame(r, chars)
        print(f"{frame}")


        delay = 0.15 + (r * 0.03)
        sleep(delay)
        cls()


    for _ in range(4):
        wave = ".".join(["#" * (10 + _*5)])
        print(f"{wave:^50}")
        sleep(0.25)
        cls()
        print(f"{wave:^50}")
        sleep(0.2)
        cls()


    for _ in range(6):
        print(f"{'!' * 60}")
        sleep(0.12)
        cls()
        if _ % 2 == 0:
            print(f"{'!' * 60}")
            sleep(0.1)
            cls()

    print(f"The ground is burning...")
    sleep(1.0)

    for step in range(12):
        line = ""
        for col in range(50):
            if random.random() < (0.4 - step * 0.03):
                line += random.choice(".*~-")
            else:
                line += " "
        print(f"{line}")
        fade_delay = 0.2 + step * 0.05
        sleep(fade_delay)
        cls()


    print("The Underground is now just a crater.")
    sleep(2.5)


def main_menu():
    while True:
        cls()
        print("\n=== MENU ===")
        print("1. New Game")
        print("2. Load Save")
        print("3. About")
        print("4. Quit")
        
        choice = input("> ")
        
        if choice == "1":
            create_character()
            break
        elif choice == "2":
            if load_game(): break
        elif choice == "3":
            show_about()
        elif choice == "4":
            exit()
        else:
            print("Invalid input!")


def battle(enemy):
    global name
    global gender
    global atk_bonus
    global mp_bonus
    global appearance
    global lv
    global exp
    global maxHP
    global hp
    global maxMP
    global mp
    global inventory
    global weapon
    global armor
    global atk
    global atkFin
    global dfn
    global dfnFin
    global monsters
    global bosses
    global kills
    global spared
    global pacifist_eligible
    global gold
    global CRIT_CHANCE
    global CRIT_MULTIPLIER
    
    

    canSpared = False
    dmgMP = 1
    hpMP = 1
    effectDuration = 0
    defend = False
    shieldApplied = False
    enemy.hp = enemy.maxHP

    if enemy.instSpare == True:
        canSpared = True

    
    while True:
        
        updateLV()
        updateHP()
        updateATK()
        updateDFN()
        updateMP()
        
        if enemy.name == "Lord Cat":
            neutral_msg = rnd.choice(neutral_battle_messages)
            printa(neutral_msg)


        if enemy.name == "Lord Cat":
            if monsters == 0 and bosses == 1:
                input("Action(attack, defend, magic, flee, info, item, spare): ")
                cls()
                print("Action(attack, defend, magic, flee, info, item, spare): attack")
                print(f"Damage: {10**40-1}")
                print("Enemy HP: 0/800")
                sleep(0.2)
                printa("Lord Cat: B-b-burn-n in-n t-the-e h-hel-l-l...", 0.15, effect = "whisper")
                print("YOU WON!")
                print(f"You got {enemy.exp} EXP")
                exp += enemy.exp
                kills += 1
                bosses -= 1
                pacifist_eligible = False
                sleep(1)
                break
        bAct = input("Action(attack, defend, magic, flee, info, item, spare, act): ")
        defend = False

        

        
        if bAct == "attack":
            if rnd.random() < CRIT_CHANCE:
                atck = atkFin * hpMP
                crit_damage = int(atck * CRIT_MULTIPLIER)
                blink("CRITICAL HIT!", 8)
                if crit_damage > 10**40-1:
                   print(f"Damage: {10**40-1} (x{CRIT_MULTIPLIER})") 
                else:
                    print(f"Damage: {crit_damage} (x{CRIT_MULTIPLIER})")
                enemy.hp -= crit_damage
            else:
                apw = rnd.randint(50, 200)/100
                atck = int(atkFin * apw * hpMP)
                enemy.hp -= atck
                if atck > 10**40-1:
                    print(f"Damage: {10**40-1}")
                else:
                    print(f"Damage: {atck}")
            if enemy.hp <= 0:
                if enemy.name == "Lord Cat":
                    print("Enemy HP: 0.001/800")
                    printa("Lord Cat: P-p-pleas-s-se d-d-d-don't-t-t k-k-kil-l m-m-me...", effect = "whisper")
                    fAct = input("Action(attack, spare): ")
                    if fAct == "attack":
                        print(f"Damage: {10**40-1}")
                        print("Enemy HP: 0/800")
                        sleep(0.2)
                        printa("Lord Cat: B-b-burn-n in-n t-the-e h-hel-l-l...", 0.15, effect = "whisper")
                        print("YOU WON!")
                        print(f"You got {enemy.exp} EXP")
                        exp += enemy.exp
                        kills += 1
                        bosses -= 1
                        pacifist_eligible = False
                        sleep(1)
                        break
                    elif fAct == "spare":
                        print("Enemy HP: 1/800")
                        printa("Lord Cat: T-t-than-nks-s you-u f-for-r y-your-r-r k-k-kid-dn-nes-s-s...", 0.15, effect = "whisper")
                        break
                    else:
                        print("yet another error message")
                print("YOU WON!")
                print(f"You got {enemy.exp} EXP")
                exp += enemy.exp
                kills += 1
                gold += rnd.randint(25, 70)
                if enemy.boss == False:
                    monsters -= 1
                else:
                    bosses -= 1
                pacifist_eligible = False
                sleep(1)
                break
            else:
                print(f"Enemy HP: {enemy.hp}/{enemy.maxHP}")
        elif bAct == "defend":
            defend = True
            mp = min(mp + 10 + lv * 5, maxMP)
            print(f"You defenced. Your MP increased({mp}/{maxMP}).")
        elif bAct == "magic":
            mgT = input("Select magic(bolt - 70MP, heal - 60MP, fireball - 40MP, shield - 30MP, meteor - 100MP): ")
            if mgT == "bolt":
                  if mp < bolt.cost:
                        print("You don't have enough MP")
                  elif mp >= bolt.cost:
                      mp -= bolt.cost
                      if enemy.boss == True:
                          print("MISS")
                      else:
                          wprint("BOOOOOOOOOOM!", 1)
                          wprint("Enemy turned to dust...", 2)
                          print("YOU WON!")
                          print(f"You got {enemy.exp} EXP.")
                          kills += 1
                          monsters -= 1
                          pacifist_eligible = False 
                          exp += enemy.exp
                          sleep(1)
                          break
            elif mgT == "heal":
                if mp < healer.cost:
                    print("You don't have enough MP")
                elif mp >= healer.cost:
                   mp -= healer.cost
                   hp = maxHP
                   print("Healed all HP")
            elif mgT == "fireball":
                if mp < fireball.cost:
                    print("You don't have enough MP")
                elif mp >= fireball.cost:
                    mp -= fireball.cost
                    enemy.hp -= fireball.atk * lv * hpMP
                    sleep(1.9)
                    print(f"Damage: {fireball.atk * lv * hpMP}")
                    print("BOOOOM!")
                    if enemy.hp <= 0:
                        if enemy.name == "Lord Cat":
                            enemy.hp = 0.001
                        wprint("Enemy turned to dust...", 2)
                        print("YOU WON!")
                        print(f"You got {enemy.exp} EXP.")
                        kills += 1
                        if enemy.boss == False:
                            monsters -= 1
                        else:
                            bosses -= 1
                        pacifist_eligible = False 
                        exp += enemy.exp
                        sleep(1)
                        break
                    print(f"Enemy HP: {enemy.hp}/{enemy.maxHP}")
            elif mgT == "shield":
                if mp < shield.cost:
                    print("You don't have enough MP")
                elif mp >= shield.cost:
                    if shieldApplied == True:
                        print("You already have shield.")
                    else:
                        shieldApplied = True
                        effectDuration = 5
                        mp -= shield.cost
            elif mgT == "meteor":
                if mp < meteor.cost:
                    print("You don't have enough MP")
                elif mp >= meteor.cost:
                    mp -= meteor.cost
                    enemy.hp -= meteor.atk * lv * hpMP
                    sleep(4.7)
                    print(f"Damage: {meteor.atk * lv * hpMP}")
                    print("BOOOOOOOOOOM!")
                    if enemy.hp <= 0:
                        if enemy.name == "Lord Cat":
                            enemy.hp = 0.001
                        wprint("Enemy turned to dust...", 2)
                        print("YOU WON!")
                        print(f"You got {enemy.exp} EXP.")
                        kills += 1
                        if enemy.boss == False:
                            monsters -= 1
                        else:
                            bosses -= 1
                        pacifist_eligible = False 
                        exp += enemy.exp
                        sleep(1)
                        break
                print(f"Enemy HP: {enemy.hp}/{enemy.maxHP}")
        elif bAct == "flee":
            if enemy.boss == False:
                print("Escaped...")
                break
            else:
                print("You try to flee but legs refuse to run.")
        elif bAct == "info":
            print(f"Name: {name}")
            print(f"Gender: {gender.upper()}")
            print(f"Appearance: {appearance}")
            print(f"LV: {lv}")
            print(f"EXP: {exp}")
            print(f"EXP to next level: {get_exp_to_next_level()}")
            print(f"HP: {hp}/{maxHP}")
            print(f"MP: {mp}/{maxMP}")
            print(f"Weapon: {weapon.name}")
            print(f"Armor: {armor.name}")
            print(f"ATK: {atkFin}({atk})")
            print(f"DEF: {dfnFin}({dfn})")
            print(f"GOLD: {gold}")
            print()
            print("ENEMY")
            print(f"Name: {enemy.name}")
            print(f"HP: {enemy.hp}/{enemy.maxHP}")
            print(f"ATK: {enemy.atk}")
        elif bAct == "item":
            print("INVENTORY:")
            print(f"[0] : [{inventory[0].name}]")
            print(f"[1] : [{inventory[1].name}]")
            print(f"[2] : [{inventory[2].name}]")
            print(f"[3] : [{inventory[3].name}]")
            print(f"[4] : [{inventory[4].name}]")
            print(f"[5] : [{inventory[5].name}]")
            print(f"[6] : [{inventory[6].name}]")
            print(f"[7] : [{inventory[7].name}]")
            try:
                itemUse = int(input("What do you want to use?"))
                if inventory[itemUse] == nothing:
                    pass
                else:
                    if inventory[itemUse].type == "nukeTrigger":
                        print("You pressed The Red Button...")
                        sleep(1.5)
                        nuclear_explosion()
                        print("\n[NUKE SECRET ENDING]")
                        print("...")
                        sleep(3)
                        input("Press Enter to quit...")
                        exit()
                    elif inventory[itemUse].type == "weapon":
                        oldWeapon = weapon
                        weapon = inventory[itemUse]
                        inventory[itemUse] = oldWeapon
                    elif inventory[itemUse].type == "armor":
                        oldArmor = armor
                        armor = inventory[itemUse]
                        inventory[itemUse] = oldArmor
                    else:
                        heal(inventory[itemUse].heal, inventory[itemUse].text, inventory[itemUse].name, inventory[itemUse].type)
                        inventory[itemUse] = nothing
            except:
                print("Invalid input!")
        elif bAct == "spare":
            if enemy.name == "Lord Cat":
                wprint("You try to spare...", 1)
                wprint("...but Lord Cat is ignoring you...", 1)
            elif canSpared == True:
                print(f"You decided to spare {enemy.name}.")
                print("The enemy leaves.")
                gold += rnd.randint(25, 70)
                break
            elif enemy.hp > enemy.maxHP * 0.3:
                print(f"{enemy.name} is still too aggressive to be spared!")
            else:
                print(f"You decided to spare {enemy.name}.")
                print("The enemy leaves.")
                gold += rnd.randint(25, 70)
                break
        elif bAct == "act":
            if enemy.name == "Smol Doge":
                talk = input("What do(pet, play, turnaway):")
                if talk == "pet":
                    print("Smol Doge is happy")
                    canSpared = True
                elif talk == "play":
                    print("Smol Doge plays with you. He is tired.")
                    hpMP = 1.6
                    canSpared = True
                elif talk == "turnaway":
                    print("Smol Doge is bored.")
            elif enemy.name == "Just Dog":
                talk = input("What do(call, showfood): ")
                if talk == "call":
                    print("You don't know his name.")
                elif talk == "showfood":
                    print("You show food to Dog. He eats it. He happy.")
                    canSpared = True
            elif enemy.name == "bob":
                talk = input("What do(joke, ignore):")
                if talk == "joke":
                    print("bob is launghes! he is happy.")
                    canSpared = True
                elif talk == "ignore":
                    print("bob is angry. he flees.")
                    sleep(1.2)
                    break
            elif enemy.name == "Leopold":
                talk = input("What do(scold, sing):")
                if talk == "scold":
                    print("Leopold is angry.")
                    dmgMP = 1.5
                elif talk == "sing":
                    print("You are singing. Leopold is happy.")
                    dmgMP = 0.5
                    hpMP = 2
                    canSpared = True
            elif enemy.name == "Smol Spooder" or enemy.name == "Big Spooder" or enemy.name == "Spooder, but faster":
                talk = input("What do(scare, insult, silent, frustrate): ")
                if talk == "scare":
                    print("Spooder isn't scared. He is angry.")
                    dmgMP = 1.8
                elif talk == "insult":
                    print("You are naming he 'dumbest spider ever'")
                    print("He is sad.")
                    canSpared = True
                elif talk == "silent":
                    print("Spooder is bored.")
                    canSpared = True
                elif talk == "frustrate":
                    print("He is frustrated and angry.")
                    dmgMP = 1.7
            elif enemy.name == "Smol Robot":
                talk = input("What do(reboot, ask): ")
                if talk == "reboot":
                    print("Robot is rebooting...")
                    canSpared = True
                elif talk == "ask":
                    printa("SMOL_ROBOT MODEL 078 IS READY TO CLEAN AND FIGHT")
                    printa(f"STATUS: ACTIVE {rnd.randint(10, 100)}% CHARGE")
                    printa("CURRENT TASK: DESTROY TREAT OBJECT ID 0001")
                    printa("TASK PROGRESS: TERMINATING TREAT")
                    printa("OTHER TASKS:")
                    printa("ID 0: CLEAN WAREHOUSE")
                    printa("ID 1: FIX LEFT GUN")
                    printa("...")
                    printa("ID 9354: UPDATE SYSTEM")
                    canSpared = True
            elif enemy.name == "Doge":
                talk = input("What do(dance, pun, insult): ")
                if talk == "dance":
                    chnce = rnd.randint(1, 100)
                    if chnce >= 0 and chnce <= 25:
                        print("You're dancing. The Doge is glad.")
                        canSpared = True
                    else:
                        print("The Doge isn't likes your dance.")
                elif talk == "pun":
                    chnce = rnd.randint(1, 100)
                    if chnce >= 0 and chnce <= 45:
                        print("You're tell bad pun about bones to The Doge. The Doge is launghing.")
                        canSpared = True
                    else:
                        print("The Doge isn't likes your bad puns.")
                        dmgMP = 2
                elif talk == "insult":
                    print("You are naming him 'dirty dumb dog'.")
                    print("He is angry.")
                    dmgMP = 2.3
            elif enemy.name == "TERMINATOR":
                talk = input("What do(hack): ")
                if talk == "hack":
                    print("You trying hack his system")
                    chnce = rnd.randint(1, 100)
                    if chnce >= 0 and chnce <= 15:
                        printa("CRITICAL SYSTEM ERROR: SHUTTING DOWN...")
                        dmgMP = 0
                        canSpared = True
                    else:
                        print("...but no anything happened...")
            elif enemy.name == "Lord Cat":
                talk = input("What do(plead, insult, remind): ")
                if talk == "plead":
                    chnce = rnd.randint(1, 100)
                    if chnce >= 0 and chnce <= 45 and pacifist_eligible == True:
                        print("Lord Cat is attacks not too strong. Lord Cat's ATTACK is LOWERED. Lord Cat's DEFENCE is LOWERED")
                        hpMP = 2
                        dmgMP = 0.5
                    else:
                        print("Lord Cat ignores you...")
                elif talk == "insult":
                    print("You are naming him 'dirty stupid cat'.")
                    print("He is angry.")
                    dmgMP = 2.3
                elif talk == "remind":
                    chnce = rnd.randint(1, 100)
                    if chnce >= 0 and chnce <= 45 and pacifist_eligible == True:
                        print("Lord Cat is reminds something... Lord Cat's ATTACK is LOWERED. Lord Cat's DEFENCE is LOWERED")
                        hpMP = 2
                        dmgMP = 0.5
                    else:
                        print("Lord Cat ignores you...")
            elif enemy.name == "   H U G E    S P O O D E R":
                talk = input("What do(whisper): ")
                if talk == "whisper":
                    chnce = rnd.randint(1, 100)
                    if chnce >= 0 and chnce <= 15:
                        printa("Spooder is interested")
                        dmgMP = 0
                        canSpared = True
                    else:
                        print("...but no anything happened...")

            
                

        if defend == True:
            if shieldApplied == True and effectDuration > 0:
                print("Magical shield is absorbing half of enemy hit!")
                if enemy.atk * dmgMP / 4 > dfnFin:
                    hp -= (enemy.atk - dfnFin) * dmgMP / 4
                    if hp <= 0:
                        gameover()
                        return False
                        break
                    print(f"You got {int((enemy.atk - dfnFin) * dmgMP / 4)} damage. HP: {hp}/{maxHP}")
                else:
                    hp -= 1
                    print(f"You got 1 damage. HP: {hp}/{maxHP}")
                    if hp <= 0:
                        gameover()
                        return False
                        break
                effectDuration -= 1
                if effectDuration == 0:
                    shieldApplied = False
            else:
                print("You blocked half of enemy hit!")
                if enemy.atk * dmgMP / 2 > dfnFin:
                    hp -= (enemy.atk - dfnFin) * dmgMP / 2
                    if hp <= 0:
                        gameover()
                        return False
                        break
                    print(f"You got {int((enemy.atk - dfnFin) * dmgMP / 2)} damage. HP: {hp}/{maxHP}")
                else:
                    hp -= 1
                    print(f"You got 1 damage. HP: {hp}/{maxHP}")
                    if hp <= 0:
                        gameover()
                        return False
                        break


            dmgMP = 1
            
            
        else:
            if shieldApplied == True and effectDuration > 0:
                print("Magical shield is absorbing half of enemy hit!")
                if enemy.atk * dmgMP / 2 > dfnFin:
                    hp -= (enemy.atk - dfnFin) * dmgMP / 2
                    if hp <= 0:
                        gameover()
                        return False
                        break
                    print(f"You got {int((enemy.atk - dfnFin) * dmgMP / 2)} damage. HP: {hp}/{maxHP}")
                else:
                    hp -= 1
                    print(f"You got 1 damage. HP: {hp}/{maxHP}")
                    if hp <= 0:
                        gameover()
                        return False
                        break
                effectDuration -= 1
                if effectDuration == 0:
                    shieldApplied = False
            else:
                if enemy.atk * dmgMP > dfnFin:
                    hp -= int((enemy.atk - dfnFin) * dmgMP)
                    if hp <= 0:
                        gameover()
                        return False
                        break
                    print(f"You got {int(enemy.atk - dfnFin * dmgMP)} damage. HP: {hp}/{maxHP}")
                else:
                    hp -= 1
                    if hp <= 0:
                        gameover()
                        return False
                        break
                    print(f"You got 1 damage. HP: {hp}/{maxHP}")

            
           
            dmgMP = 1
        
            
            
          
print("===========================================")      
print("               UNDERGROUND")
print("===========================================")

sleep(3)

main_menu()


cls()

wprint("Welcome to The Underground", 2)
wprint("Be careful there...", 2)
wprint("You entered to the dark room with dark gray brick walls", 1)

def game_loop():
    global lv
    global exp
    global maxHP
    global hp
    global maxMP
    global mp
    global inventory
    global weapon
    global armor
    global atk
    global atkFin
    global dfn
    global dfnFin
    global room
    global monsters
    global bosses
    global gold
    global name
    global gender
    global atk_bonus
    global mp_bonus
    global appearance


    global kills
    global spared
    global pacifist_eligible
    global dirtyHacker
    
    global CRIT_CHANCE
    global CRIT_MULTIPLIER


    while True:
        updateLV()
        updateHP()
        updateATK()
        updateDFN()
        updateMP()
        
        if room == pianoRoom:
            act = input("Action(info, seek, clear, item, nextroom, open, shop, drop, talk, iteminfo, save, load, play): ")
        else:
            act = input("Action(info, seek, clear, item, nextroom, open, shop, drop, talk, iteminfo, save, load): ")
        if act == "info":
            print(f"Name: {name}")
            print(f"Gender: {gender.upper()}")
            print(f"Appearance: {appearance}")
            print(f"LV: {lv}")
            print(f"EXP: {exp}")
            print(f"EXP to next level: {get_exp_to_next_level()}")
            print(f"HP: {hp}/{maxHP}")
            print(f"MP: {mp}/{maxMP}")
            print(f"Weapon: {weapon.name}")
            print(f"Armor: {armor.name}")
            print(f"ATK: {atkFin}({atk})")
            print(f"DEF: {dfnFin}({dfn})")
            print(f"GOLD: {gold}")
            print()
            print("INVENTORY:")
            print(f"[0] : [{inventory[0].name}]")
            print(f"[1] : [{inventory[1].name}]")
            print(f"[2] : [{inventory[2].name}]")
            print(f"[3] : [{inventory[3].name}]")
            print(f"[4] : [{inventory[4].name}]")
            print(f"[5] : [{inventory[5].name}]")
            print(f"[6] : [{inventory[6].name}]")
            print(f"[7] : [{inventory[7].name}]")       
        elif act == "seek":
            chance = rnd.randint(1,100)
            if chance >= 0 and chance <= 20:
                monster = rnd.choice(room.enemies)
                wprint("...", 1)
                if monsters > 0:
                    wprint(f"{monster.name} {monster.text}", 1)
                    battle(monster)
                else:
                    print("But nobody came...")
            elif chance >= 21 and chance <= 41:
                wprint("...", 1)
                drop = rnd.choice(room.loot)
                print(f"You got {drop.name}!")
                print("INVENTORY:")
                print(f"[0] : [{inventory[0].name}]")
                print(f"[1] : [{inventory[1].name}]")
                print(f"[2] : [{inventory[2].name}]")
                print(f"[3] : [{inventory[3].name}]")
                print(f"[4] : [{inventory[4].name}]")
                print(f"[5] : [{inventory[5].name}]")
                print(f"[6] : [{inventory[6].name}]")
                print(f"[7] : [{inventory[7].name}]")
                try:
                    place = int(input("Where to put it(8 - trash)?"))
                    if place == 8:
                        pass
                    else:
                        inventory[place] = drop
                except:
                    print("Incorrect input!")
            elif chance >= 42 and chance <= 52:
                wprint("...", 1)
                print("You fall into trap...")
                mp = 0
                hp -= 20
                if hp <= 0:
                    gameover()
                print(f"You got 20 damage. HP: {hp}/{maxHP}")
            elif chance >= 53 and chance <= 100:
                wprint("...", 1)
                print("...but you don't find anything.")
            else:
                printa("WHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT!!!", effect = "glitch")
                sleep(0.5)
                cls()
                
        elif act == "clear":
            cls()
        elif act == "item":
            print("INVENTORY:")
            print(f"[0] : [{inventory[0].name}]")
            print(f"[1] : [{inventory[1].name}]")
            print(f"[2] : [{inventory[2].name}]")
            print(f"[3] : [{inventory[3].name}]")
            print(f"[4] : [{inventory[4].name}]")
            print(f"[5] : [{inventory[5].name}]")
            print(f"[6] : [{inventory[6].name}]")
            print(f"[7] : [{inventory[7].name}]")
            
            try:
                itemUse = int(input("What do you want to use?"))
                if inventory[itemUse] == nothing:
                    pass
                else:
                    if inventory[itemUse].type == "nukeTrigger":
                        print("You pressed The Red Button...")
                        sleep(1.5)
                        nuclear_explosion()
                        print("\n[NUKE SECRET ENDING]")
                        print("...")
                        sleep(3)
                        input("Press Enter to quit...")
                        exit()
                    elif inventory[itemUse].type == "weapon":
                        oldWeapon = weapon
                        weapon = inventory[itemUse]
                        inventory[itemUse] = oldWeapon
                    elif inventory[itemUse].type == "armor":
                        oldArmor = armor
                        armor = inventory[itemUse]
                        inventory[itemUse] = oldArmor
                    else:
                        heal(inventory[itemUse].heal, inventory[itemUse].text, inventory[itemUse].name, inventory[itemUse].type)
                        inventory[itemUse] = nothing
            except:
                print("Invalid input!")
        elif act == "nextroom":
            if room.final == False:
                if room.puzzle is not None:
                    print("To proceed, you must solve a puzzle!")
                    print(f"Puzzle: {room.puzzle.question}")
                    
                    if room.puzzle.hint:
                        print(f"Hint: {room.puzzle.hint}")
                    
                    try:
                        user_answer = input("Your answer: ")
                        if room.puzzle.check(user_answer):
                            print("Correct! The path opens.")
                            if room.boss is not None:
                                wprint(f"You see... The {room.boss.name}...", 2)
                                cls()
                            if battle(room.boss) != False:
                                room = room.nextRoom
                            else:
                                game_loop()
                        else:
                            print("Wrong answer! The door remains locked.")
                    except ValueError:
                        print("Invalid input! Try again.")
                else:
                    wprint(f"You go to {room.nextRoom.name}...", 3)
                    if room.boss == None:
                        pass
                    else:
                        wprint(f"You see... The {room.boss.name}...", 2)
                        cls()
                        if battle(room.boss) != False:
                            room = room.nextRoom
                        else:
                            game_loop()
            else:
                final_consequence()
                sleep(2)
                wprint(f"You see The Exit from The Underground...", 3)
                wprint("This fills you with DETERMINATION...", 2)
                wprint(f"You see... The {room.boss.name}...", 2)
                if monsters == 0 and bosses == 1:
                    printa("Lord Cat: There is a beautiful day outside...")
                    sleep(0.7)
                    printa("Lord Cat: Birds are singing...")
                    sleep(0.7)
                    printa("Lord Cat: ...sun is shining.")
                    sleep(0.7)
                    printa("Lord Cat: In that days, kids like you...")
                    sleep(2)
                    printa("Lord Cat: S H O U L D    B E    B U R N    I N    T H E    H E L L!", effect = "whisper")
                    sleep(0.8)
                else:
                    printa("Lord Cat: Oh... hello?!")
                    sleep(0.7)
                    printa("Lord Cat: What's your name?")
                    sleep(1.5)
                    printa(f"Lord Cat: {name}? Good name, {name}.")
                    sleep(0.9)
                    printa("Lord Cat: Nice to meet you, human.")
                    sleep(0.7)
                    printa("Lord Cat: Goodbye.")
                    sleep(2)
                cls()
                if battle(room.boss) != False:
                    pass
                else:
                    game_loop()
                cls()
                wprint("UNDERGROUND", 2)
                wprint("by Alex", 2)
                print()
                show_ending()
                cls()
                input("Press Enter to exit...")
                exit()
        elif act == "open":
            if room.chest is None:
                print("There is no chest here.")
            elif room.chest.opened:
                print("The chest is already empty.")
            else:
                print("You opened the chest!")
                chest = room.chest
                for item in chest.items:
                    print(f"Found: {item.name}")
                    for i in range(len(inventory)):
                        if inventory[i] == nothing:
                            inventory[i] = item
                            print(f"{item.name} added to inventory (slot {i}).")
                            break
                    else:
                        print(f"No space for {item.name}!")
                chest.opened = True
        elif act == "drop":
            print("INVENTORY:")
            for i in range(len(inventory)):
                print(f"[{i}] : [{inventory[i].name}]")
            try:
                slot = int(input("Which item to drop? (Enter slot number): "))
                if slot < 0 or slot >= len(inventory):
                    print("Invalid slot number!")
                elif inventory[slot] == nothing:
                    print("This slot is empty!")
                else:
                    dropped_item = inventory[slot]
                    inventory[slot] = nothing
                    print(f"You dropped {dropped_item.name}.")
            except ValueError:
                print("Please enter a valid number!")
        elif act == "615474520412":
            weapon = debugWP
            inventory[0] = nukeButton
            dirtyHacker = True
        elif act == "g":
            monsters = 0
            pacifist_eligible = False
        elif act == "talk":
            if room.npc is None or len(room.npc) == 0:
                print("There is no one to talk to here.")
            else:
                print("You see:")
                for i, npc in enumerate(room.npc):
                    print(f"[{i}] {npc.name}")
                
                try:
                    choice = int(input("Who do you want to talk to? (enter number): "))
                    if 0 <= choice < len(room.npc):
                        npc = room.npc[choice]
                        print(f"\n{npc.name} says:")
                        for line in npc.dialogue:
                            printa(line, 0.05)
                        
                        if npc.trade:
                            print(f"\n{npc.name} offers to trade:")
                            for i, item in enumerate(npc.items):
                                print(f"[{i}] {item.name} (Heal: {item.heal})")
                            try:
                                trade_choice = int(input("Choose an item to receive (or -1 to cancel): "))
                                if 0 <= trade_choice < len(npc.items):
                                    item = npc.items[trade_choice]
                                    for slot in range(len(inventory)):
                                        if inventory[slot] == nothing:
                                            inventory[slot] = item
                                            print(f"You received {item.name}!")
                                            break
                                    else:
                                        print("Inventory is full!")
                                elif trade_choice != -1:
                                    print("Invalid choice!")
                            except ValueError:
                                print("Please enter a number!")
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Please enter a number!")
        elif act == "shop":
            if room.shop == None:
                print("There isn't any shops.")
            else:
                current_shop = room.shop
                while True:
                    current_shop.show_items()
                    buy_choice = input("Buy item (number) or [b] back: ")
                    
                    if buy_choice == "b":
                        break
                    
                    try:
                        idx = int(buy_choice)
                        if 0 <= idx < len(current_shop.items):
                            item, price = current_shop.items[idx]
                            
                            if gold >= price:
                                for i, inv_item in enumerate(inventory):
                                    if inv_item == nothing:
                                        inventory[i] = item
                                        gold -= price
                                        print(f"Bought {item.name} for {price} gold!")
                                        print(f"Gold left: {gold}")
                                        break
                                else:
                                    print("Inventory is full!")
                            else:
                                print("Not enough gold!")
                        else:
                            print("Invalid item number!")
                    except ValueError:
                        print("Enter a number or 'b'!")
        elif act == "anuke":
            printa("The walls briefly flash with blue light... Build. Defend. Survive.", 0.1)
            print("(You feel a surge of DETERMINATION...)")
            hp = min(hp + 50, maxHP)
            mp = min(mp + 30, maxMP)
        elif act == "play":
            if room == pianoRoom:
                print("You approach the old piano. The keys are dusty but intact.")

                sequence = input("Play notes: ").strip().upper()
                    
                if sequence == "A G F E":
                    printa("The piano emits a soft, melodic chime...", 0.35)
                    printa("Suddenly, the floor shakes!", 0.3)
                    printa("A tiny white dog in a toy race car comes speeding in!", 0.2)
                    printa("BEEP! BEEP! VROOM!", 0.1)
                    sleep(1)
                    printa("CRASH!!!", 1)
                    sleep(0.5)
                            
                    cls()
                    print()
                    print()
                    print("GAME OVER: PUPPY RAMPAGE!")
                    print()
                    print("The dog in the toy car knocked you out!")
                    print("You wake up covered in dog slobber...")
                    print("...and the piano is now on fire.")
                    print()

                            
                    sleep(3)
                    input("Press Enter to accept your fate...")
                    exit()
                else:
                    print("The piano makes a discordant noise. Nothing happens.")
            else:
                print("...")
        elif act == "end":
            room = finalRoom
            dirtyHacker = True
        elif act == "infoitem" or act == "iteminfo":
            print("INVENTORY:")
            for i in range(len(inventory)):
                print(f"[{i}] : [{inventory[i].name}]")
            try:
                slot = int(input("Which item to inspect? (Enter slot number): "))
                if slot < 0 or slot >= len(inventory):
                    print("Invalid slot number!")
                elif inventory[slot] == nothing:
                    print("This slot is empty!")
                else:
                    item = inventory[slot]
                    print(f"\n--- {item.name} ---")
                    print(item.description)
            except ValueError:
                print("Please enter a valid number!")
            
        elif act == "save":
            save_game()
        
        elif act == "load":
            load_game()
        elif act == "AAAAAA":
            for i in range(100):
                printa("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", delay = 0.001)
            showerror(title="Critical Error", message="""Traceback (most recent call last)
File "underground.py", line 1794, in <module>
    printa("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

Unknown Error""")
            os._exit(1)
        elif act == "67":
            for i in range(100):
                printa("676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767", delay = 0.001)
                printa("767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676", delay = 0.001)
            sleep(2)
            print("SixSeven hacked sucessfully.")
            hp = maxHP
            mp = maxMP
            dirtyHacker = True
            


game_loop()
