import dotos

import nextcord
from nextcord.ext import commands


# logging for the bot
import logging
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="nextcord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = nextcord.Intents.default()
intents.message_content = True


def get_prefix(bot, message):
    prefixes = ['mtg!', 'm!']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)


load_extensions = ['cogs.mtg']

bot = commands.Bot(command_prefix=get_prefix, intents=intents)


if __name__ == '__main__':
    for extension in load_extensions:
        bot.load_extension(extension)
        print(extension, 'commands have been loaded successfully')


@bot.event
async def on_ready():
    print(f"\n\nLogging in as: {bot.user.name} - {bot.user.id}\nVersion: {nextcord.__version__}\n")
    game = nextcord.Game("w"
                         "ith my code")
    await bot.change_presence(status=nextcord.Status.do_not_disturb, activity=game)
    print("Successfully logged in and booted...!")

bot.run(dotos.token, reconnect=True)