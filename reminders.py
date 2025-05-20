from discord.ext import commands, tasks
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        self.scheduler.start()

    @commands.command()
    async def remind(self, ctx, minutes: int, *, msg):
        remind_time = datetime.now() + timedelta(minutes=minutes)
        self.scheduler.add_job(self.send_reminder, 'date', run_date=remind_time, args=[ctx.channel.id, msg])
        await ctx.send(f"Reminder set for {minutes} minutes from now.")

    async def send_reminder(self, channel_id, msg):
        channel = self.bot.get_channel(channel_id)
        await channel.send(f"⏰ Reminder: {msg}")
