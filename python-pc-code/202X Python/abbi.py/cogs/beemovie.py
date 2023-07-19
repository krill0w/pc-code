import nextcord
from nextcord.ext import commands

class BeeMovieCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='beeMovie', aliases=['bM', 'barry'])
  async def do_beeMovie(self, ctx, line : str):
    f = open(r'E:\Creativeness Productions\Coding\2020 Python\abbi.py\cogs\beemovie.txt', 'r')
    content = f.readlines()
    count = 0
    if line == 'all':
      for lines in content:
        count += 1
        await ctx.send(lines.strip())
    elif line != 'all':
      line = int(line)
      output = ''.join(content[line])
      await ctx.send(output)

def setup(bot):
  bot.add_cog(BeeMovieCog(bot))