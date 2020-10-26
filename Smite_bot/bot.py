# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
has_god = False
prev_god = ""
@bot.command(name='rgod', help='Responds with a random god')
async def get_randgod(ctx):
    global has_god
    global prev_god
    has_god = True
    msg = '{0.author.mention}, your random god is '.format(ctx.message)
    smite_gods = [
        "Achilles",
        "Agni",
        "Ah muzen cab",
        "Ah puch",
        "Amaterasu",
        "Anhur", "Anubis", "Ao kuang", "Aphrodite", "Apollo", "Arachne", "Ares", "Artemis", "Artio", "Athena", "Awilix",
       "Bacchus", "Bakasura", "Baron samedi", "bastet", "bellona", "Cabrakan", "Camazotz", "Cerberus", "Cernunnos", "Chaac", "Chang e", "Chernobog", "Chiron", "Chronos", "Cu chulainn",
       "Cupid", "Da ji", "Discordia", "Erlang shen", "Fafnir", "Fenrir", "Freya", "Ganesha", "Geb", "Guan yu", "Hachiman", "Hades", "He bo", "Hel", "Heimdallr", "Hera", "Hercules",
       "Horus", "Hou yi", "Hun batz", "Isis", "Izanami", "Janus", "Jing wei", "Jormungandr", "Kali", "Khepri", "King Arthur", "Kukulkan", "Kumbhakarna", "Kuzenbo", "Loki", "Medusa",
       "Mercury", "Merlin", "Ne zha", "Neith", "Nemesis", "Nike", "nox", "Nu wa", "Odin", "Olorun", "Osiris", "Pele", "Persephone", "Poseidon", "Ra", "Raijin", "Rama", "Ratatoskr",
       "Ravana", "Scylla", "Serqet", "Set", "Skadi", "Sobek", "Sol", "Sun wukong", "Susano", "Sylvanus", "Terra", "Thanatos", "The Morrigan", "Thor", "Thoth", "Tyr", "Ullr", "Vamana",
       "Vulcan", "Xbalanque", "Xing tian", "Yemoja", "Ymir", "Zeus", "Zhong kui"
    ]
    prev_god = str(random.choice(smite_gods))
    response = msg + prev_god + '\n'
    await ctx.send(response)



@bot.command(name='rbuild', help = 'This option will generate a random build for the given god. Compound names need to be between "')
async def get_rand_build(ctx, god):
    global has_god
    global prev_god
    
   # if has_god:
    #    god = prev_god
    #has_god = False
    print("My god was " + str(has_god))
    msg = '{0.author.mention}, your random god is '.format(ctx.message)
    smite_gods_phys = [
           "Achilles",
            "Ah Muzen Cab",
            "Amaterasu",
            "Anhur",
            "Apollo",
            "Arachne",
            "Artemis",
            "Awilix",
            "Bakasura",
            "Bastet",
            "Bellona",
            "Camazotz",
            "Cernunnos",
            "Chaac",
            "Chernobog",
            "Chiron",
            "Cu Chulainn",
            "Cupid",
            "Da Ji",
            "Erlang Shen",
            "Fenrir",
            "Guan Yu",
            "Hachiman",
            "Heimdallr",
            "Hercules",
            "Horus",
            "Hou Yi",
            "Hun Batz",
            "Izanami",
            "Jing Wei",
            "Kali",
            "King Arthur",
            "Loki",
            "Medusa",
            "Mercury",
            "Ne Zha",
            "Neith",
            "Nemesis",
            "Nike",
            "Odin",
            "Osiris",
            "Pele",
            "Rama",
            "Ratatoskr",
            "Ravana",
            "Serqet",
            "Set",
            "Skadi",
            "Sun Wukong",
            "Susano",
            "Thanatos",
            "Thor",
            "Tyr",
            "Ullr",
            "Vamana",
            "Xbalanque"
    ]
    smite_gods_magic = [  
            "Agni",
            "Ah Puch",
            "Anubis",
            "Ao Kuang",
            "Aphrodite",
            "Ares",
            "Artio",
            "Athena",
            "Bacchus",
            "Baron Samedi",
            "Cabrakan",
            "Cerberus",
            "Chang'e",
            "Chronos",
            "Discordia",
            "Fafnir",
            "Freya",
            "Ganesha",
            "Geb",
            "Hades",
            "He Bo",
            "Hel",
            "Hera",
            "Isis",
            "Janus",
            "Jormungandr",
            "Khepri",
            "Kukulkan",
            "Kumbhakarna",
            "Kuzenbo",
            "Merlin",
            "Nox",
            "Nu Wa",
            "Olorun",
            "Persephone",
            "Poseidon",
            "Ra",
            "Raijin",
            "Scylla",
            "Sobek",
            "Sol",
            "Sylvanus",
            "Terra",
            "The Morrigan",
            "Thoth",
            "Vulcan",
            "Xing Tian",
            "Yemoja",
            "Ymir",
            "Zeus",
            "Zhong Kui"
        
    ]
    response = ""
    phys_shoes = ["Ninja tabi", "Reinforced Greaves", "Warrior Tabi", "Talaria Boots"]
    phys_items=["Fail-not", "Berserkers Shield", "Gladiators Shield", "Winged Blade", "Relic Dagger", "Shield of Regrowth",
       "Emperor's Armor", "Witchblade", "Contagion", "Odysseus Bow", "Sovereignty", "Oni Hunters Garb", "Heartward Amulet", "Spectral Armor", "Runic Shield", "Ancile", "Hydras Lament",
       "Magis Cloak", "Talisman of Energy", "Genjis Guard", "Hide of the Nemean Lion", "Atalantas Bow", "Blackthorn Hammer", "Shoguns Kusari", "Silverbranch Bow", "Golden Blade",
       "Toxic Blade", "Mail of Renewal", "Pestilence", "Stone of Gaia", "Bulwark of Hope", "Devourers Gauntlet", "Frostbound Hammer", "Breastplate of Valor", "Midgardian Mail",
       "Soul Eater", "Titans Bane", "Brawlers Beat Stick", "The Executioner", "Jotunns Wrath", "Gauntlet of Thebes", "Shifters Shield", "Rage", "Runeforged Hammer",
       "Pridwen", "The Crusher", "Hide of the Urchin", "Ichaival", "Bumbas Mask", "Rangas Mask", "Masamune", "Spirit Robe", "Wind Demon", "Poisoned Star", "Stone Cutting Sword",
       "Hastened Katana", "Asi", "Trascendence", "Arondight", "Void Shield", "Malice", "Mystical Mail", "Qins Sais", "Bloodforge", "Mantle of Discord", "Deathbringer", "Heartseeker"]
    magic_shoes = ["Shoes of the Magi", "Shoes of Focus", "Reinforced Shoes", "Traveler Shoes"]
    magic_items=["Pythagorems Piece", "Bancrofts Talon", "Typhon Fang", "Soul Gem", "Demonic Grip",
               "Telkhines Ring", "Shamans Ring", "Hastened Ring", "Obsidian Shard", "Divine Ruin", "Spear of the Magus", "Spear of Desolation", "Gem of Isolation", "Warlocks Staff",
               "Ethereal Staff", "Rod of Asclepius", "Book of Thoth", "Polynomicon", "Soul Reaver", "Rod of Tahuti", "Chronos Pendant", "Celestial Legion Helm", "Lotus Crown",
               "Jade Emperors Crown", "Void Stone", "Stone of Fal", "Staff of Myrddin", "Pestilence", "Heartward Amulet", "Lonos Mask", "Stone of Binding",
               "Sages Stone", "Dynasty Plate Helm", "Book of the Dead", "Doom Orb"]
    actives=["Cursed Ankh", "Aegis Amulet", "Heavenly Wings", "Blink Rune", "Purification Beads", "Teleport Glyph", "Meditation Cloak", "Magic Shell", "Shield of Thorns", "Sundering Spear", "Phantom Veil", "Bracer of Undoing", "Horrific Emblem", "Belt of Frenzy"]
    
    msg="No god selected"
    print("My name given was " + god.lower())
    for godname in smite_gods_magic:
        if god.lower() == godname.lower():
            msg = "magical"
    for godname in smite_gods_phys:
        if god.lower() == godname.lower():
            msg = "physical"
    if msg == "No god selected":
        msg = "God not found. Please make sure it is written correctly."
        response = msg
    else:
        print("The god " + god + " is " + msg + '\n')
        for i in range (0,6):
            if msg == "magical":
                if response == "":
                    response = response +random.choice(magic_shoes)
                else:
                    rand = random.choice(magic_items)
                    print("my random item was " + rand + "and I have " + response + '\n')
                    while rand in response:
                        rand = random.choice(magic_items)
                    response = response + " , " + rand
            else:
                if response == "":
                    response = response +random.choice(phys_shoes)
                else:
                    rand = random.choice(phys_items)
                    print("my random item was " + rand + "and I have " + response + '\n')
                    while rand in response:
                        rand =random.choice(phys_items)
                    response = response + " , " + rand
        print("finished getting the items. Now getting actives....\n")
        for i in range (0,2):
            rand = random.choice(actives)
            while rand in response:
                rand = random.choice(actives)
            if i == 0:
                response = response + "\n Actives: \n " + rand
            else:
                response = response + " , " + rand
        response = '{0.author.mention}, your random build for '.format(ctx.message) + str(god) + ' is : \n' + response + '\n'
    await ctx.send(response)


@bot.command(name = 'ritem', help = 'This option generates a single random item. M is for magical and P for physical' )
async def get_rand_item(ctx, opt):

    phys_items=["Ninja tabi", "Reinforced Greaves", "Warrior Tabi", "Talaria Boots","Fail-not", "Berserkers Shield", "Gladiators Shield", "Winged Blade", "Relic Dagger", "Shield of Regrowth",
       "Emperor's Armor", "Witchblade", "Contagion", "Odysseus Bow", "Sovereignty", "Oni Hunters Garb", "Heartward Amulet", "Spectral Armor", "Runic Shield", "Ancile", "Hydras Lament",
       "Magis Cloak", "Talisman of Energy", "Genjis Guard", "Hide of the Nemean Lion", "Atalantas Bow", "Blackthorn Hammer", "Shoguns Kusari", "Silverbranch Bow", "Golden Blade",
       "Toxic Blade", "Mail of Renewal", "Pestilence", "Stone of Gaia", "Bulwark of Hope", "Devourers Gauntlet", "Frostbound Hammer", "Breastplate of Valor", "Midgardian Mail",
       "Soul Eater", "Titans Bane", "Brawlers Beat Stick", "The Executioner", "Jotunns Wrath", "Gauntlet of Thebes", "Shifters Shield", "Rage", "Runeforged Hammer",
       "Pridwen", "The Crusher", "Hide of the Urchin", "Ichaival", "Bumbas Mask", "Rangas Mask", "Masamune", "Spirit Robe", "Wind Demon", "Poisoned Star", "Stone Cutting Sword",
       "Hastened Katana", "Asi", "Trascendence", "Arondight", "Void Shield", "Malice", "Mystical Mail", "Qins Sais", "Bloodforge", "Mantle of Discord", "Deathbringer", "Heartseeker"]
    magic_items=["Shoes of the Magi", "Shoes of Focus", "Reinforced Shoes", "Traveler Shoes","Pythagorems Piece", "Bancrofts Talon", "Typhon Fang", "Soul Gem", "Demonic Grip",
               "Telkhines Ring", "Shamans Ring", "Hastened Ring", "Obsidian Shard", "Divine Ruin", "Spear of the Magus", "Spear of Desolation", "Gem of Isolation", "Warlocks Staff",
               "Ethereal Staff", "Rod of Asclepius", "Book of Thoth", "Polynomicon", "Soul Reaver", "Rod of Tahuti", "Chronos Pendant", "Celestial Legion Helm", "Lotus Crown",
               "Jade Emperors Crown", "Void Stone", "Stone of Fal", "Staff of Myrddin", "Pestilence", "Heartward Amulet", "Lonos Mask", "Stone of Binding",
               "Sages Stone", "Dynasty Plate Helm", "Book of the Dead", "Doom Orb"]
    rand_item = ""
    response = '{0.author.mention}, '.format(ctx.message) + " your random item is "
    if opt.lower() == 'm':
        rand_item = random.choice(magic_items)
        response = response + rand_item + '\n'
    elif opt.lower() == 'p':
        rand_item = random.choice(phys_items)
        response = response + rand_item + '\n'
    elif opt.lower() != 'm'  and opt.lower() != 'p':
        rand_item = "Please try again typing !ritem m for a magical item or !ritem p for a physical item"
        response = rand_item
        
    await ctx.send(response)
    
@bot.command(name='rgodnbuild', help = 'This option will generate both a random god and its random build')
async def get_rand_build(ctx):
    global has_god
    global prev_god
    msg2 = '{0.author.mention}, your random god is '.format(ctx.message)
    smite_gods = [
        "Achilles",
        "Agni",
        "Ah muzen cab",
        "Ah puch",
        "Amaterasu",
        "Anhur", "Anubis", "Ao kuang", "Aphrodite", "Apollo", "Arachne", "Ares", "Artemis", "Artio", "Athena", "Awilix",
       "Bacchus", "Bakasura", "Baron samedi", "bastet", "bellona", "Cabrakan", "Camazotz", "Cerberus", "Cernunnos", "Chaac", "Chang e", "Chernobog", "Chiron", "Chronos", "Cu chulainn",
       "Cupid", "Da ji", "Discordia", "Erlang shen", "Fafnir", "Fenrir", "Freya", "Ganesha", "Geb", "Guan yu", "Hachiman", "Hades", "He bo", "Hel", "Heimdallr", "Hera", "Hercules",
       "Horus", "Hou yi", "Hun batz", "Isis", "Izanami", "Janus", "Jing wei", "Jormungandr", "Kali", "Khepri", "King Arthur", "Kukulkan", "Kumbhakarna", "Kuzenbo", "Loki", "Medusa",
       "Mercury", "Merlin", "Ne zha", "Neith", "Nemesis", "Nike", "nox", "Nu wa", "Odin", "Olorun", "Osiris", "Pele", "Persephone", "Poseidon", "Ra", "Raijin", "Rama", "Ratatoskr",
       "Ravana", "Scylla", "Serqet", "Set", "Skadi", "Sobek", "Sol", "Sun wukong", "Susano", "Sylvanus", "Terra", "Thanatos", "The Morrigan", "Thor", "Thoth", "Tyr", "Ullr", "Vamana",
       "Vulcan", "Xbalanque", "Xing tian", "Yemoja", "Ymir", "Zeus", "Zhong kui"
    ]
    god = str(random.choice(smite_gods))
    msg2 = msg2 + god + '\n'
   # if has_god:
    #    god = prev_god
    #has_god = False
    #print("My god was " + str(has_god))
    #msg = '{0.author.mention}, your random god is '.format(ctx.message)
    smite_gods_phys = [
           "Achilles",
            "Ah Muzen Cab",
            "Amaterasu",
            "Anhur",
            "Apollo",
            "Arachne",
            "Artemis",
            "Awilix",
            "Bakasura",
            "Bastet",
            "Bellona",
            "Camazotz",
            "Cernunnos",
            "Chaac",
            "Chernobog",
            "Chiron",
            "Cu Chulainn",
            "Cupid",
            "Da Ji",
            "Erlang Shen",
            "Fenrir",
            "Guan Yu",
            "Hachiman",
            "Heimdallr",
            "Hercules",
            "Horus",
            "Hou Yi",
            "Hun Batz",
            "Izanami",
            "Jing Wei",
            "Kali",
            "King Arthur",
            "Loki",
            "Medusa",
            "Mercury",
            "Ne Zha",
            "Neith",
            "Nemesis",
            "Nike",
            "Odin",
            "Osiris",
            "Pele",
            "Rama",
            "Ratatoskr",
            "Ravana",
            "Serqet",
            "Set",
            "Skadi",
            "Sun Wukong",
            "Susano",
            "Thanatos",
            "Thor",
            "Tyr",
            "Ullr",
            "Vamana",
            "Xbalanque"
    ]
    smite_gods_magic = [  
            "Agni",
            "Ah Puch",
            "Anubis",
            "Ao Kuang",
            "Aphrodite",
            "Ares",
            "Artio",
            "Athena",
            "Bacchus",
            "Baron Samedi",
            "Cabrakan",
            "Cerberus",
            "Chang'e",
            "Chronos",
            "Discordia",
            "Fafnir",
            "Freya",
            "Ganesha",
            "Geb",
            "Hades",
            "He Bo",
            "Hel",
            "Hera",
            "Isis",
            "Janus",
            "Jormungandr",
            "Khepri",
            "Kukulkan",
            "Kumbhakarna",
            "Kuzenbo",
            "Merlin",
            "Nox",
            "Nu Wa",
            "Olorun",
            "Persephone",
            "Poseidon",
            "Ra",
            "Raijin",
            "Scylla",
            "Sobek",
            "Sol",
            "Sylvanus",
            "Terra",
            "The Morrigan",
            "Thoth",
            "Vulcan",
            "Xing Tian",
            "Yemoja",
            "Ymir",
            "Zeus",
            "Zhong Kui"
        
    ]
    response = ""
    phys_shoes = ["Ninja tabi", "Reinforced Greaves", "Warrior Tabi", "Talaria Boots"]
    phys_items=["Fail-not", "Berserkers Shield", "Gladiators Shield", "Winged Blade", "Relic Dagger", "Shield of Regrowth",
       "Emperor's Armor", "Witchblade", "Contagion", "Odysseus Bow", "Sovereignty", "Oni Hunters Garb", "Heartward Amulet", "Spectral Armor", "Runic Shield", "Ancile", "Hydras Lament",
       "Magis Cloak", "Talisman of Energy", "Genjis Guard", "Hide of the Nemean Lion", "Atalantas Bow", "Blackthorn Hammer", "Shoguns Kusari", "Silverbranch Bow", "Golden Blade",
       "Toxic Blade", "Mail of Renewal", "Pestilence", "Stone of Gaia", "Bulwark of Hope", "Devourers Gauntlet", "Frostbound Hammer", "Breastplate of Valor", "Midgardian Mail",
       "Soul Eater", "Titans Bane", "Brawlers Beat Stick", "The Executioner", "Jotunns Wrath", "Gauntlet of Thebes", "Shifters Shield", "Rage", "Runeforged Hammer",
       "Pridwen", "The Crusher", "Hide of the Urchin", "Ichaival", "Bumbas Mask", "Rangas Mask", "Masamune", "Spirit Robe", "Wind Demon", "Poisoned Star", "Stone Cutting Sword",
       "Hastened Katana", "Asi", "Trascendence", "Arondight", "Void Shield", "Malice", "Mystical Mail", "Qins Sais", "Bloodforge", "Mantle of Discord", "Deathbringer", "Heartseeker"]
    magic_shoes = ["Shoes of the Magi", "Shoes of Focus", "Reinforced Shoes", "Traveler Shoes"]
    magic_items=["Pythagorems Piece", "Bancrofts Talon", "Typhon Fang", "Soul Gem", "Demonic Grip",
               "Telkhines Ring", "Shamans Ring", "Hastened Ring", "Obsidian Shard", "Divine Ruin", "Spear of the Magus", "Spear of Desolation", "Gem of Isolation", "Warlocks Staff",
               "Ethereal Staff", "Rod of Asclepius", "Book of Thoth", "Polynomicon", "Soul Reaver", "Rod of Tahuti", "Chronos Pendant", "Celestial Legion Helm", "Lotus Crown",
               "Jade Emperors Crown", "Void Stone", "Stone of Fal", "Staff of Myrddin", "Pestilence", "Heartward Amulet", "Lonos Mask", "Stone of Binding",
               "Sages Stone", "Dynasty Plate Helm", "Book of the Dead", "Doom Orb"]
    actives=["Cursed Ankh", "Aegis Amulet", "Heavenly Wings", "Blink Rune", "Purification Beads", "Teleport Glyph", "Meditation Cloak", "Magic Shell", "Shield of Thorns", "Sundering Spear", "Phantom Veil", "Bracer of Undoing", "Horrific Emblem", "Belt of Frenzy"]
    
    msg="No god selected"
    #print("My name given was " + god.lower())
    for godname in smite_gods_magic:
        if god.lower() == godname.lower():
            msg = "magical"
    for godname in smite_gods_phys:
        if god.lower() == godname.lower():
            msg = "physical"
    if msg == "No god selected":
        msg = "God not found. Please make sure it is written correctly."
        response = msg
    else:
        print("The god " + god + " is " + msg + '\n')
        for i in range (0,6):
            if msg == "magical":
                if response == "":
                    response = response +random.choice(magic_shoes)
                else:
                    rand = random.choice(magic_items)
                    print("my random item was " + rand + "and I have " + response + '\n')
                    while rand in response:
                        rand = random.choice(magic_items)
                    response = response + " , " + rand
            else:
                if response == "":
                    response = response +random.choice(phys_shoes)
                else:
                    rand = random.choice(phys_items)
                    print("my random item was " + rand + "and I have " + response + '\n')
                    while rand in response:
                        rand =random.choice(phys_items)
                    response = response + " , " + rand
        print("finished getting the items. Now getting actives....\n")
        for i in range (0,2):
            rand = random.choice(actives)
            while rand in response:
                rand = random.choice(actives)
            if i == 0:
                response = response + "\n Actives: \n " + rand
            else:
                response = response + " , " + rand
        response = msg2 + " and your random build for " + str(god) + ' is : \n' + response + '\n'
    await ctx.send(response)
bot.run(token)