# modules
import nextcord
from nextcord.ext import commands
import logging
import dotos

# prefix commands intent
intents = nextcord.Intents.default()
intents.message_content = True

# logging
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='bmil.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s |  %(message)s'))
logger.addHandler(handler)


# define prefix and prevent action on mentions
def get_prefix(bot, message):
	prefixes = ['b!', 'bmil!']
	if not message.guild:
		return '?'
	return commands.when_mentioned_or(*prefixes)(bot, message)


loadup_extensions = ['cogs.simple', 'cogs.utility']

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

if __name__ == '__main__':
	for extension in loadup_extensions:
		bot.load_extension(extension)
		ext = extension.strip('cogs.')
		print(extension, 'commands have been loaded successfully')


@bot.event
async def on_ready():
	print(f'\nLogged in as {bot.user.name} - {bot.user.id}\nVersion: {nextcord.__version__}')
	game = nextcord.Game('with your balls')
	await bot.change_presence(status=nextcord.Status.online, activity=game)
	print('Successfully logged in and booted..!')


bot.run(dotos.TOKEN, reconnect=True)
