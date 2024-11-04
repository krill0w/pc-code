import nextcord
from nextcord.ext import commands


class SimpleCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='hello', aliases=['hi', 'hai', 'hallo', 'hey'])
	async def do_hello(self, ctx):
		await ctx.send('hai!')

	@commands.command(name='saysorrytocallumrightnowisweartogod')
	async def do_sorry_callum(self, ctx):
		await ctx.send(
			'I am so very sorry Callum Ellis "Big Man" Disney for causing you copious amounts of grief in your very short time in the PP Clan. I well and truly repent for my actions and wholeheartedly promise to never cause you such pain and anguish ever in my life. Love bmil <3')


def setup(bot):
	bot.add_cog(SimpleCog(bot))
