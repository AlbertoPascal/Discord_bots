# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import configparser
import os.path
from datetime import datetime

random.seed(datetime.now())

config = configparser.ConfigParser()
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

config = configparser.ConfigParser()


if os.path.isfile('pet.data'):
    print ("File exists")
else:
    print ("File does not exist. Creating")
    myfile = open("pet.data", "w")
    myfile.close()
bot = commands.Bot(command_prefix="!")
@bot.command(name="adopt", help="Adopt a new doggy!")
async def get_a_doggy(ctx, petname):
    response = "ok"
    config.read('test.data')
    print("Im trying to adopt " + str(petname))
    print(ctx.author.id)
    if not config.has_section(str(ctx.author.id)):
       print("entré aquí")
       config.add_section(str(ctx.author.id))
       print("Added user section")
       with open('test.data', 'w') as savefile:
           config.write(savefile)
    if config.has_option(str(ctx.author.id), 'pet.' + str(petname) + '.growth'):
        response = "You cannot adopt two pets with the same name! That would be mean!"
    else:
        config.read('test.data')
        random.seed(datetime.now())
        rand_doggy_num = random.randint(0,100)
        rand_doggy = '1'
        if (rand_doggy_num <=20):
            rand_doggy = '1'
        elif(rand_doggy_num >20 and rand_doggy_num <=40):
            rand_doggy = '2'
        elif (rand_doggy_num >40 and rand_doggy_num <=60):
            rand_doggy = '3'
        elif (rand_doggy_num >60 and rand_doggy_num <=80):
            rand_doggy = '4'
        else:
            rand_doggy = '5'
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.growth', 'puppy')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.sleepdays' , '1')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.hunger' , 'not hungry')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.hunger_meter' , '100')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.mood' , 'excited')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.energy' , '100')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.img' , 'dog' + str(rand_doggy) + '.jpg')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.img_play' , 'dog' + str(rand_doggy) + '_play.gif')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.img_play2' , 'dog' + str(rand_doggy) + '_play2.gif')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.img_sleep' , 'dog' + str(rand_doggy) + '_sleep.gif')
        config.set(str(ctx.author.id), 'pet.' + str(petname) + '.img_sleep2' , 'dog' + str(rand_doggy) + '_sleep2.gif')
        with open('test.data', 'w') as savefile:
               config.write(savefile)
        msg = "{0.author.mention}... ".format(ctx.message)
        response = "You have just adopted a new doggy. Say hi to " +str(petname) + "!\n"
        await ctx.send(msg + response)
@bot.command(name="play", help = "This will throw a ball for one of your adopted doggies")
async def get_ball(ctx, dogname):
    config.read('test.data')
    response = ""
    msg = "{0.author.mention}, ".format(ctx.message)
    if not config.has_section(str(ctx.author.id)):
        response = "You have not adopted a dog yet!! Try adopting one with !adopt name!"
    elif config.has_option(str(ctx.author.id),"pet." + dogname + ".growth"):
        #we can play fetch with dog. 
        energybar = config.get(str(ctx.author.id), 'pet.' + dogname + '.energy')
        hungermeter = config.get(str(ctx.author.id), 'pet.' + dogname + '.hunger_meter')
        dog_age = config.get(str(ctx.author.id), 'pet.' + dogname + '.growth')
        if (dog_age == 'puppy' and int(energybar) >= 20):
            config.set(str(ctx.author.id),'pet.' + str(dogname) + '.mood', 'happy')
            config.set(str(ctx.author.id), 'pet.' + str(dogname) + '.energy', str(int(energybar )-20))
            #enough energy to play and become happy
        elif (dog_age == 'young' and int(energybar) >= 25):
            config.set(str(ctx.author.id),'pet.' + str(dogname) + '.mood', 'happy')
            config.set(str(ctx.author.id), 'pet.' + str(dogname) + '.energy', str(int(energybar )-25))
           
        elif (dog_age == 'adult' and int(energybar) >= 33.34) :
            config.set(str(ctx.author.id),'pet.' + str(dogname) + '.mood', 'happy')
            config.set(str(ctx.author.id), 'pet.' + str(dogname) + '.energy', str(int(energybar )-33.33))
        energybar = config.get(str(ctx.author.id), 'pet.' + dogname + '.energy')
        if int(energybar) <=0:
            if config.get(str(ctx.author.id),'pet.' + str(dogname) + '.mood') != 'tired' and config.get(str(ctx.author.id),'pet.' + str(dogname) + '.hunger') !='very hungry':
                #al azar decido si le da hambre o sueño   
                random.seed(datetime.now())
                num = random.randint(1,100)
                if (num<50):
                    config.set(str(ctx.author.id),'pet.' + str(dogname) + '.mood', 'tired')
                    response = dogname + " is too tired to play and needs to sleep! Try with !sleep name"
                else:
                    config.set(str(ctx.author.id),'pet.' + str(dogname) + '.hunger', 'very hungry')
                    response = dogname + " is too hungry to play and needs some food! Try with !feed name"
            elif config.get(str(ctx.author.id),'pet.' + str(dogname) + '.mood') == 'tired':
                #do sth
                response = dogname + " is too tired to play and needs to sleep! Try with !sleep name"
            elif config.get(str(ctx.author.id),'pet.' + str(dogname) + '.hunger') =='very hungry':
                response = dogname + " is too hungry to play and needs some food! Try with !feed name"
       
        elif config.get(str(ctx.author.id),'pet.' + str(dogname) + '.mood') == 'tired':
            #I have energy because I ate but I am still tired and need to rest. 
            response = dogname + " is too tired to play and needs to sleep! Try with !sleep name"
        elif config.get(str(ctx.author.id),'pet.' + str(dogname) + '.hunger') == 'very hungry':
            #I have energy because I ate but I am still tired and need to rest. 
            response = dogname + " is too hungry to play and needs to eat! Try with !feed name"
        else:
            rand_play=''
            random.seed(datetime.now())
            rand_play_num = random.randint(0,100)
            if rand_play_num < 50:
                rand_play=''
            else:
                rand_play = '2'
            print('My random number was ' ,rand_play)
            dog_img = config.get(str(ctx.author.id), 'pet.' + dogname + '.img_play' + str(rand_play))
            response = "You throw a ball for " + dogname + ". " + dogname + " is now wigging its tail in happiness!"
            await ctx.send('', file = discord.File('images/' + dog_img))
        with open('test.data', 'w') as savefile:
            config.write(savefile)
    else:
        response = "You have no dog named " + dogname + ". Why don't you play with "
    
    await ctx.send(msg + response)
    
    
@bot.command(name="feed", help="This command will give some tasty food to your pet and restore some of its energy!")    
async def get_some_food(ctx, dogname):
    config.read('test.data')
    msg = "{0.author.mention}, ".format(ctx.message)
    if config.has_section(str(ctx.author.id)):
        if config.has_option(str(ctx.author.id), 'pet.' + dogname + '.img'):
            #I can feed my dog. 
            config.set(str(ctx.author.id),'pet.' + dogname + '.energy', '100')
            config.set(str(ctx.author.id), 'pet.' + dogname + '.hunger', 'full')
            with open('test.data', 'w') as savefile:
                config.write(savefile)    
            await ctx.send(msg + dogname + " ate all the food! and is full of energy once again and excited to play! WOOF WOOF")
        else:
             await ctx.send(msg + "Woops! You have no dog named " + dogname)
    else:
        await ctx.send(msg + "You haven't adopted a dog yet! Try with !adopt")
@bot.command(name="sleep", help="This command will give some tasty food to your pet and restore some of its energy!")    
async def get_some_food(ctx, dogname):
    config.read('test.data')
    msg = "{0.author.mention}, ".format(ctx.message)
    if config.has_section(str(ctx.author.id)):
        if config.has_option(str(ctx.author.id), 'pet.' + dogname + '.img'):
            #I can feed my dog. 
            rand_play=''
            random.seed(datetime.now())
            rand_play_num = random.randint(0,100)
            if rand_play_num < 50:
                rand_play=''
            else:
                rand_play = '2'
            dog_img = config.get(str(ctx.author.id), 'pet.' + dogname + '.img_sleep' + str(rand_play))
            config.set(str(ctx.author.id),'pet.' + dogname + '.energy', '100')
            config.set(str(ctx.author.id), 'pet.' + dogname + '.mood', 'relaxed')
            with open('test.data', 'w') as savefile:
                config.write(savefile)    
            await ctx.send(msg + dogname + " took a relaxing nap and is now full of energy and excited to play again! WOOF WOOF", file = discord.File('images/' + dog_img))
        else:
             await ctx.send(msg + "Woops! You have no dog named " + dogname)
    else:
        await ctx.send(msg + "You haven't adopted a dog yet! Try with !adopt")
@bot.command(name="hi", help="Makes your dog answer to you!")
async def get_dog_hi(ctx, dogname):
    msg = "{0.author.mention}, ".format(ctx.message)
    response = msg + dogname + " says: WOOF WOOF!!\n"
    config.read('test.data')
    print("going to feed")
    if config.has_section(str(ctx.author.id)):
        if config.has_option(str(ctx.author.id), 'pet.' + dogname + '.img'):
            #we have an existing pet like this. 
            dog_img = config.get(str(ctx.author.id), 'pet.' + dogname + '.img')
            await ctx.send(response, file = discord.File('images/' + dog_img))
        else:
            
            await ctx.send(msg + "Woops! You have no dog named " + dogname)
    else:   
        await ctx.send(msg + "You have not adopted any dogs yet! Try adopting one with !adopt name")
    #area=ctx.message.channel
    #await bot.send_file(area, r"D:\Documents\Miri_discord_bot\images\dog1.jpg",filename="Hello",content=response)        
@bot.command(name="comp", help="Responds with a randomly built compliment for my awesome girlfriend, Miranda Flores!")
async def get_compliment(ctx):
   #ctx.author.id
    msg = "{0.author.mention}, Pascal Camaleón says:  ".format(ctx.message)
    phrases = [
            
            "You are my one and only!"
            "I love being in love with you.",
            "Thank you for looking after me.",
            "Thank you for always being there for me.",
            "I love the unique way you giggle.",
            "I can't get enough of you.",
            "I admire your strength, determination and patience!",
            "I don't know what I'd do without you.",
            "You are truly gorgeous.",
            "You mean the world to me.",
            "I love doing life with you.",
            "Being with you trumps all other plans.",
            "When I hold you in my arms, I feel so lucky.",
            "I'm thankful that I can spend my days with the best woman on earth! How lucky I am!",
            "I love being with you so much, I wish time could stand still when we're together.",
            "Seeing you smile is the best part of my day.",
            "There is no one else like you. You are the best",
            "I'm always here for you.",
            "I cannot stop looking at you. You're beautiful!",
            "You make me feel special.",
            "I am the luckiest man for getting to have you by my side.",
            "You brighten up the room every time you laugh.",
            "You have the key to my heart! (And that will never change, no matter what)",
            "They say falling in love is great... but I'm sure that being in love with you is even better!",
            "Adventures with you are my favorite.",
            "You make the world so much more beautiful.",
            "I'm in awe of what a wonderful girlfriend you are.",
            "You inspire me to be a better man.",
            "You are my lucky charm.",
            "I appreciate that you are always here for me. I want to be there for you too!",
            "If you let me, I would hold you forever.",
            "When I'm with you, I feel like I found what I was looking for.",
            "There aren't enough stars in the sky to show you how much you brighten up my day.",
            "I could stare into your eyes forever.",
            "Your presence brings the best out of me.",
            "My cheeks hurt from smiling so much around you.",
            "You have the sweetest smile I've ever seen! I can't help but smile too whenever I see it!.",
            "I still feel butterflies around you.",

            
    ]
    rand_phrase = phrases[random.randint(0,len(phrases))]
    response = msg + rand_phrase + "♥\n"
    await ctx.send(response)

bot.run(token)