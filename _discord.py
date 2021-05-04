import os
import discord
import random
from replit import db


client = discord.Client()

######################### UPDATE em r_palavras_acrescentadas #####################################
def uptade_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len (encouragements) > index:
        del encouragements [index]
        db["encouragements"] = encouragements
################################################################################################
######################## UPDATE em palavras_acrescentadas #####################################
def uptade_encouragements2(encouraging_message2):
    if "encouragements2" in db.keys():
        encouragements2 = db["encouragements2"]
        encouragements2.append(encouraging_message2)
        db["encouragements2"] = encouragements2
    else:
        db["encouragements2"] = [encouraging_message2]

def delete_encouragements2(index2):
    encouragements2 = db["encouragements2"]
    if len (encouragements2) > index2:
        del encouragements2 [index2]
        db["encouragements2"] = encouragements2
################################################################################################3

@client.event
async def on_ready():
    #print("We have logged in as {0.user}".format(client))
    print(f"Connected succesfully as {client.user}")

palavras_acrescentadas = ["jogo","mano"]
r_palavras_acrescentadas = ["bacana","ha ha ha"]

diferente = ["quero uivar","Tô com fome", "que canseira", "relaxa carinha","acho que tô com pulga"]
r_diferente = ["quero uivar","Tô com fome", "que canseira", "relaxa carinha","acho que tô com pulga"]

palavrax = ["oi ", "ola "]
r_palavrax = ["olá amigo como vc está hoje?"," tô perdido aqui","au au au","eu sou o cão coragem"]

cumprimentosx = ["bem","bom","legal"]
r_cumprimentosx = ["vc disse bem uhuu que bacana","vc disse bom, que legal carinha", "vc escreveu legal e eu concordo com vc!!"]

gx = ["bom dia","boa noite", "boa tarde"]
r_gx = ["para vc também", "bom para todos", "bom mesmo uhu"]

if "responding" not in db.keys():
    db["responding"] = True

@client.event
async def on_message(message):
    if message.author == client.user:
        return
############## acrescenta palavra na lista r_palavras_acrescentadas #######
    
    if db["responding"]:
        options = r_palavras_acrescentadas
        if "encouragements" in db.keys():
            options.extend(db["encouragements"]) #adiciona lista em outra lista
            #options = options + db["encouragements"]
            
        if any(word in message.content for word in palavras_acrescentadas):
            await message.channel.send(random.choice(options))
        
    if message.content.startswith("$new "):
        encouraging_message = message.content.split("$new ",1)[1]
        uptade_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if message.content.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(message.content.split("$del",1)[1])
            delete_encouragements(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)
############################################################################
    if message.content.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if message.content.startswith("$responding"):
        value = message.content.split("$responding ",1)[1]

        if  value.lower() == "true":
            db["responding"] = True
            await message.channel.send("cao coragem ligado!")
        else:
            db["responding"] = False
            await message.channel.send("cao coragem desligado")

 #############################################################################
 ############## acrescenta palavra na lista palavras_acrescentadas #######
    options2 = palavras_acrescentadas
    if "encouragements2" in db.keys():
        options2.extend(db["encouragements2"]) #adiciona lista em outra lista
        #options = options + db["encouragements"]
        
    if any(word in message.content for word in r_palavras_acrescentadas):
        await message.channel.send(random.choice(options2))
        
    if message.content.startswith("$new_palavras "):
        encouraging_message2 = message.content.split("$new_palavras ",1)[1]
        uptade_encouragements2(encouraging_message2)
        await message.channel.send("New encouraging message added.")

    if message.content.startswith("$del_palavras"):
        encouragements2 = []
        if "encouragements2" in db.keys():
            index2 = int(message.content.split("$del_palavras",1)[1])
            delete_encouragements2(index2)
            encouragements2 = db["encouragements2"]
        await message.channel.send(encouragements2)
 #############################################################################       

    if message.content == "duliano":
        await message.channel.send("escreva no particular para o seu amigo")
        dm = await message.author.create_dm()  # Creates a dm channel with the user
        await dm.send("o que você quer falar com duliano?")  # Sends the user the message

    if any (palavra in message.content for palavra in diferente):
        await message.channel.send(random.choice(r_diferente))

    if any (palavra in message.content + (" ") for palavra in palavrax):
        await message.channel.send(random.choice(r_palavrax))

    if any (palavra in message.content != "bom" for palavra in gx):
        await message.channel.send(random.choice(r_gx))

    if any (palavra in message.content != "bom dia" for palavra in cumprimentosx):
        await message.channel.send(random.choice(r_cumprimentosx))

    '''else:
        await message.author.send("Ainda não aprendi essa palavra \nMe ensina?")'''

client.run(os.getenv("REC"))
my_secret = os.environ['REC']