import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import mcrcon


load_dotenv()

client = discord.Client()
bot = commands.Bot(command_prefix="mc ")
bot.remove_command("help")

@bot.event
async def on_ready():
  print("We have logged in as {0.user}".format(bot))


@bot.command(pass_context = True)
async def help(ctx):
  embed = discord.Embed(title = "Help",
    colour = discord.Colour.green()
  )

  embed.add_field(name="name",value= "desc",inline=False)
  embed.set_thumbnail(url= "https://ibb.co/Hh5GwNr")
  embed.set_footer(text = "Made with ❤️ by dextero")

  await ctx.channel.send(embed = embed)

@bot.command()
async def hi(ctx):
  await ctx.channel.send("Hello!")
  return

@bot.command()
async def exec(ctx,*,cmd):


  if cmd == None:
    await ctx.send("Invalid command")
  else:
    mcr = mcrcon.MCRcon(os.getenv('host'),os.getenv('pass'))
    mcr.connect()
    print(os.getenv('host'))
    resp = mcr.command(cmd) 
    await ctx.send(resp)
    mcr.disconnect()

    
@client.event
async def on_message(message):
  if message.author == client.user:
    return


bot.run(os.getenv('TOKEN'))