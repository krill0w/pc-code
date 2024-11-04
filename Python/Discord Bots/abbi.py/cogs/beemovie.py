import nextcord
from nextcord.ext import commands


class BeeMovieCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='beeMovie', aliases=['bM', 'barry', 'beemovie'])
	async def do_bee_movie(self, ctx, line: str):
		f = open(r'D:\pc-code\Python\202X Python\abbi.py\cogs\beemovie.txt', 'r')
		content = f.readlines()
		count = 0
		if line == 'all':
			for lines in content:
				count += 1
				await ctx.send(lines.strip())
		elif line == 'stop':
			await ctx.send("Stopping...")
			return ""
		elif line not in ['all', 'stop']:
			line = int(line)
			output = ''.join(content[line])
			await ctx.send(output)


def setup(bot):
	bot.add_cog(BeeMovieCog(bot))
