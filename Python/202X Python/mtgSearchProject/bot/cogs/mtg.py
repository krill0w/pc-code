import nextcord
from nextcord.ext import commands
import mtgSearchBackend as BE

class MTGCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #nameSearch command
  @commands.command(name='nameSearch', aliases=['nS'])
  async def do_nameSearch(self, ctx, *, searchTerm : str):
    output = '\n'.join(BE.searchByName(searchTerm))
    await ctx.send(output)

  #moreInfo command
  @commands.command(name='moreInfo', aliases=['mI'])
  async def do_moreInfo(self, ctx, *, searchTerm : str):

    embed = nextcord.Embed(title=BE.moreInfoName(searchTerm),
                          description=BE.moreInfoFlavour(searchTerm),
                          url='https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=' + BE.getMultiverseID(searchTerm))
    embed.set_image(url=BE.moreInfoImage(searchTerm))

    await ctx.send(content=' ', embed=embed)


  @commands.command(name='printTest', aliases=['pT'])
  async def do_printTest(self, ctx):
    print('command run')
    await ctx.send(BE.printCardTest())
    print('command done')



def setup(bot):
  bot.add_cog(MTGCog(bot))