import tweepy
import discord

class TweetEmbed:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, discord_client):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        self.discord_client = discord_client

    def embed_tweet(self, tweet_id, discord_channel):
        tweet = self.api.get_status(tweet_id, tweet_mode='extended')
        embed = discord.Embed(
            title=f"Tweet by @{tweet.user.screen_name}",
            description=tweet.full_text,
            url=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        )
        embed.set_thumbnail(url=tweet.user.profile_image_url_https)
        embed.set_footer(text=f"Tweeted on {tweet.created_at}")
        self.discord_client.send_message(discord_channel, embed=embed)
