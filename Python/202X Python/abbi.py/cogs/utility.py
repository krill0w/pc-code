import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
import time


class UtilityCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='ping', aliases=['pong', 'pding'])
  async def do_ping(self, ctx):
    t = await ctx.send('pong!')
    ms = (t.created_at - ctx.message.created_at).total_seconds() * 1000
    await t.edit(f'pong! took {ms}ms')

def setup(bot):
  bot.add_cog(UtilityCog(bot))