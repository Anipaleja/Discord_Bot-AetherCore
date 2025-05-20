import discord
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ydl_opts = {'format': 'bestaudio', 'noplaylist': 'True'}

    @commands.command()
    async def play(self, ctx, *, url):
        channel = ctx.author.voice.channel
        if not ctx.voice_client:
            await channel.connect()
        vc = ctx.voice_client

        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
        vc.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))
        await ctx.send(f'Now playing: {info["title"]}')
