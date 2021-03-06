import os
import discord
from discord.ext import commands

PREFIX = os.environ["PREFIX"]
TOKEN = os.environ["TOKEN"]

STREAM = {
	"name": None,
	"details": None,
	"url": None
}

client = discord.Client()

@client.event
async def on_ready():
		print('Bot successfully started.')

@client.event
async def on_message(message):
		if message.author == client.user:
				if message.content.startswith(PREFIX):
					cmd = "".join(message.content.split(" ")[0:1]).replace(PREFIX, '')
					args = message.content.split(" ")[1:]
					channel = message.channel
					if cmd == "me": 
						if len(args) == 0:
							message.delete()
							await channel.send("Ce selfbot créer par Nigary est disponible gratuitement par : https://github.com/Nigary/Selfbot")
					if cmd == "msg":
						if len(args) == 0:
							message.deleted()
							await channel.send("Voici quelques crétions originales : \n ·**·.¸(¯`·.¸*.Ton Pseudo.*¸.·´¯)¸.·**·. \n •.¸.•*´¨`*•.♥ Ton Pseudo ♥.•*´¨`*•.¸.• \n • «.¸¸.¤°´¯`• Ton Pseudo• ´¯`°¤.¸¸.»• \n •.¸.•*♥ Ton Pseudo ♥*• .¸.• \n (¯`·._) Ton Pseudo (¯`·._) \n •—(•÷[ Ton Pseudo ]÷•)—• \n *¯':.-> °º*Ton Pseudo*º° <-.:'¯* \n >------» Ton Pseudo «------< \n ¯`·..·¯`·..->• Ton Pseudo •<-..·`¯`·..·`¯ \n °·..·°¯°·..-> Ton Pseudo <-..·°¯°·..·° \n (-_-)(^_^)(-_-)Ton Pseudo(-_-)(^_^)(-_-) \n (^_^) -->Ton Pseudo<-- (^_^)°¯°~☆~·*·~๑ \n ☆๑-~·*''n »-(¯`v´¯)-» Ton Pseudo »-(¯`v´¯)-» \n ▁ ▂ ▃ ▄ ▅ ▆ ▇ Ton Pseudo █ ▇ ▆ ▅ ▄ ▂ ▁ \n •*¤*•.¸.•*♥ Ton Pseudo ♥*.¸.•*¤*• \n (¯`·._) ( Ton Pseudo ) (¯`·._) \n .°•. °•. °•. °•. Ton Pseudo .•° .•° .•° .•°. \n ------» ( Ton Pseudo ) «------ \n .·¯(_.·¯(_.·¯(_ Ton Pseudo _)¯`·._)¯`·._)¯`·. \n ★·.·´¯`·.·★Ton Pseudo★·.·´¯`·.·★ \n ..♩.¸¸♬´¯`♬.¸¸¤Ton Pseudo¤¸¸.♬´¯`♬¸¸.♩..")
					if cmd == "aide": 
						if len(args) == 0:
							message.delete()
							await channel.send("{PREFIX}aide : ce message  \n {PREFIX}me : le lien pour le selfbot \n {PREFIX}streaname : chnager le nom de votre stream \n {PREFIX}streamurl : changez le lien Twitch \n  {PREFIX}streaminfo : Toutes les infos sur votre stream-selfbot \n {PREFIX}streamstart : démarrer votre selfbot")
						else:
							await channel.send("Usage: .aide")
					if cmd == "streamname":
						if len(args) >= 1:
							STREAM['name'] = ' '.join(args)
							await channel.send("Streamname a était changé.")
						else:
							await channel.send("Usage: .streamname <name>")
					if cmd == "streamgame":
						if len(args) >= 1:
							newgame = ' '.join(args)
							if newgame == "none":
								STREAM['details'] = None
							else:
								STREAM['details'] = newgame
							await channel.send("Streamgame a était changé.")
						else:
							await channel.send("Usage: .streamgame <name>")
					if cmd == "streamurl":
						if len(args) >= 1:
							STREAM['url'] = ' '.join(args)
							await channel.send("Streamurl a était changé.")
						else:
							await channel.send("Usage: .streamurl <url>")
					if cmd == "streaminfo":
						if len(args) == 0:
							msg = "Stream Infos:\n"
							msg += "Streamname: " + str(STREAM["name"]) + "\n"
							msg += "Streamgame: " + str(STREAM["details"]) + "\n"
							msg += "Streamurl: " + str(STREAM["url"]) + "\n"
							await channel.send(msg)
						else:
							await channel.send("Usage: .streaminfo")
					if cmd == "streamstart":
						if len(args) == 0:
							if STREAM["name"] != None:
								if STREAM["url"] != None:
									streaming = discord.Streaming(name=STREAM["name"], url=STREAM["url"], details=STREAM["details"])
									await client.change_presence(activity=streaming)
									await channel.send("Le Stream vient de commencer")
									return
							await channel.send("You have to define a ``streamname`` et ``streamurl``!")
						else:
							await channel.send("Usage: .streamstart")
					if cmd == "streamstop":
						if len(args) == 0:
							await client.change_presence(activity=None)
							await channel.send("Le stream vient de s'arreter")
							return
						else:
							await channel.send("Usage: .streamstop"
client.run(TOKEN, bot=False)
