import discord
from discord.ext import commands
from moderation import Moderation
from musicplayer import MusicPlayer

client = commands.Bot(command_prefix='/')
moderation = Moderation()
music_player = MusicPlayer()

@client.event
async def on_ready():
    print('Bot is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await moderation.delete_blacklisted(message)
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def hello(ctx):
    embed = discord.Embed(title="Hello!", description="Nice to meet you!", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
async def blacklist(ctx, word):
    moderation.blacklist.append(word)
    await ctx.send(f'`{word}` has been added to the blacklist.')

@client.command()
async def unblacklist(ctx, word):
    try:
        moderation.blacklist.remove(word)
        await ctx.send(f'`{word}` has been removed from the blacklist.')
    except ValueError:
        await ctx.send(f'`{word}` is not in the blacklist.')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await moderation.ban(ctx, member, reason)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await moderation.kick(ctx, member, reason)

@client.command()
async def timeout(ctx, member: discord.Member, duration, *, reason=None):
    await moderation.timeout(ctx, member, duration, reason)

@client.command()
async def play(ctx, uri):
    await music_player.play(uri)

@client.command()
async def stop(ctx):
    await music_player.stop()

@client.command()
async def loop(ctx):
    await music_player.loop()

@client.command()
async def volume(ctx, vol):
    await music_player.volume(vol)

@client.command()
async def lineup(ctx, uri):
    await music_player.lineup(uri)

client.run('YOUR_DISCORD_BOT_TOKEN')
