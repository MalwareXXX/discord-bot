import discord
from discord.ext import commands
from moderation import Moderation
from musicplayer import MusicPlayer

client = commands.Bot(command_prefix='/')
moderation = Moderation()
music_player = MusicPlayer()

log_channel_id = 1234567890  # Replace with the ID of the log channel
log_channel = None

@client.event
async def on_ready():
    global log_channel
    print('Bot is online')
    log_channel = client.get_channel(log_channel_id)
    if not log_channel:
        print(f"Couldn't find log channel with ID {log_channel_id}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await moderation.delete_blacklisted(message)
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def hello(ctx):
    embed = discord.Embed(title="Hello!", description="Nice to meet you!", color=discord.Color.blue())
    await ctx.send(embed=embed)
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def blacklist(ctx, word):
    moderation.blacklist.append(word)
    await ctx.send(f'`{word}` has been added to the blacklist.')
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def unblacklist(ctx, word):
    try:
        moderation.blacklist.remove(word)
        await ctx.send(f'`{word}` has been removed from the blacklist.')
        await log_command_usage(ctx.message.author, ctx.command.name)
    except ValueError:
        await ctx.send(f'`{word}` is not in the blacklist.')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await moderation.ban(ctx, member, reason)
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await moderation.kick(ctx, member, reason)
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def timeout(ctx, member: discord.Member, duration, *, reason=None):
    await moderation.timeout(ctx, member, duration, reason)
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def play(ctx, uri):
    await music_player.play(uri)
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def stop(ctx):
    await music_player.stop()
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def loop(ctx):
    await music_player.loop()
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def volume(ctx, vol):
    await music_player.volume(vol)
    await log_command_usage(ctx.message.author, ctx.command.name)

@client.command()
async def lineup(ctx, uri):
    await music_player.lineup(uri)
    await log_command_usage(ctx.message.author, ctx.command.name)

async def log_command_usage(user, command_name):
    embed = discord.Embed(title=f"Command used: {command_name}", color=discord.Color.green())
    embed.add_field(name="User", value=user.mention, inline=True)
    embed.add_field(name="Command", value=command_name, inline=True)
    await log_channel.send(embed=embed)

client.run('YOUR_DISCORD_BOT_TOKEN')
