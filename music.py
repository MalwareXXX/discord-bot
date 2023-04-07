class MusicPlayer:
    def __init__(self, sp):
        self.sp = sp
        self.queue = []
        self.is_playing = False
        self.current_song = None
        self.volume = 0.5
        self.loop = False

    async def play(self, ctx, query):
        # Use Spotify API to search for song and get its URI
        uri = self.sp.search(q=query, type='track')['tracks']['items'][0]['uri']
        # Play the song using the URI
        # ...

    async def stop(self, ctx):
        # Stop the current song
        # ...

    async def toggle_loop(self, ctx):
        # Toggle the loop flag
        # ...

    async def set_volume(self, ctx, value):
        # Set the volume to the specified value (0-1)
        # ...

    async def queue_songs(self, ctx, queries):
        # Add the specified songs to the song queue
        # ...
