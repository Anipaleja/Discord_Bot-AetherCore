from discord.ext import commands
from collections import Counter

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_counts = Counter()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            self.message_counts[message.author.id] += 1

    @commands.command()
    async def top(self, ctx):
        sorted_users = self.message_counts.most_common(5)
        leaderboard = '\n'.join([f"<@{uid}>: {count}" for uid, count in sorted_users])
        await ctx.send(f"Top active users:\n{leaderboard}")
