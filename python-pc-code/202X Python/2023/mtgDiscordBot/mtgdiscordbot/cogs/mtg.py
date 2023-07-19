import nextcord
from nextcord.ext import commands
import mtgSearchBackend as BE

class MTGCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nameSearch", aliases=["nS"])
    async def do_nameSearch(self, ctx, *, searchTerm : str):
        await ctx.send("\n".join(BE.searchByName(searchTerm)))

def setup(bot):
    bot.add_cog(MTGCog(bot))
