import re
import discord

class Moderation:
    def __init__(self):
        self.blacklist = ['badword1', 'badword2']
    async def delete_blacklisted(self, message):
        for word in self.blacklist:
            if re.search(word, message.content, re.IGNORECASE):
                await message.delete()
                break

    async def ban(self, ctx, member: discord.Member, reason=None):
        if reason:
            await member.ban(reason=reason)
            await ctx.send(f'{member} has been banned. Reason: {reason}')
        else:
            await member.ban()
            await ctx.send(f'{member} has been banned.')

    async def kick(self, ctx, member: discord.Member, reason=None):
        if reason:
            await member.kick(reason=reason)
            await ctx.send(f'{member} has been kicked. Reason: {reason}')
        else:
            await member.kick()
            await ctx.send(f'{member} has been kicked.')

    async def timeout(self, ctx, member: discord.Member, duration, reason=None):
        try:
            duration = int(duration)
        except ValueError:
            await ctx.send('Invalid duration. Must be an integer.')
            return

        if reason:
            await member.add_roles('YOUR_TIMEOUT_ROLE_HERE')
            await ctx.send(f'{member} has been timed out for {duration} seconds. Reason: {reason}')
            await asyncio.sleep(duration)
            await member.remove_roles('YOUR_TIMEOUT_ROLE_HERE')
            await ctx.send(f'{member} has been un-timed out.')
        else:
            await member.add_roles('YOUR_TIMEOUT_ROLE_HERE')
            await ctx.send(f'{member} has been timed out for {duration} seconds.')
            await asyncio.sleep(duration)
            await member.remove_roles('YOUR_TIMEOUT_ROLE_HERE')
            await ctx.send(f'{member} has been un-timed out.')
