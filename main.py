import discord
from discord.ext.commands import Bot
 
client = Bot("prefix here")
 
@client.event
async def on_ready():
    print("Logged in as")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------")
    await client.change_presence(game=discord.Game(name='Streaming on YouTube'))
 
@client.command()
async def ping():
    embed = discord.Embed(description = "Pong/Server is working", color = discord.Color.red())
 
    await client.say(embed = embed)
 
@client.command()
async def invite():
    embed = discord.Embed(description = "[Invite me](https://discordapp.com/oauth2/authorize?client_id=331823215330590720&scope=bot&permissions=2146958591)", color = discord.Color.red())
 
    await client.say(embed = embed)
 
@client.command()
async def eightball():
    import random
 
    choices = ["I believe so,", "Why not", "Pretty sure not,", "I agree", "I disagree", "Of course"]
 
    await client.say(random.choice(choices))
 
@client.command()
async def coinflip():
    import random
 
    choices = ["Heads", "Tails"]
 
    await client.say(random.choice(choices))
 
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
    return await client.say(embed = embed)
 
 
client.run("token here")
