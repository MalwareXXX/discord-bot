import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from music import MusicPlayer

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

@client.command()
async def setprefix(ctx, prefix):
    client.command_prefix = prefix
    await ctx.send(f'Prefix set to: {prefix}')

def main():
    SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
    SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
    client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Initialize music player object
    player = MusicPlayer(sp)

    # Add music-related commands to bot
    @client.command()
    async def play(ctx, query):
        await player.play(ctx, query)

    @client.command()
    async def stop(ctx):
        await player.stop(ctx)

    @client.command()
    async def loop(ctx):
        await player.toggle_loop(ctx)

    @client.command()
    async def volume(ctx, value):
        await player.set_volume(ctx, value)

    @client.command()
    async def lineup(ctx, *queries):
        await player.queue_songs(ctx, queries)

    client.run('YOUR_BOT_TOKEN_HERE')

if __name__ == '__main__':
    main()
