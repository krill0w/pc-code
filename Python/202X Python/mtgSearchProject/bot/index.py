#bot modules
import nextcord
from nextcord.ext import commands

#utility modules
import sys, traceback

#personal modules
import dontopenthisonstream as dotos


def get_prefix(bot, message):
  prefixes = ['mtg!', 'm!']
  if not message.guild:
    return '?'

  return commands.when_mentioned_or(*prefixes)(bot, message)


loadup_extentions = ['cogs.mtg']

bot = commands.Bot(command_prefix=get_prefix, description='A simple MTG Search Bot')

if __name__ == '__main__':
  for extention in loadup_extentions:
    bot.load_extension(extention)
    print(extention, 'commands have been loaded successfully')


@bot.event
async def on_ready():
  print('\n\nLogged in as: {} - {}\nVersion: {}\n'.format(bot.user.name, bot.user.id, nextcord.__version__))
  game = nextcord.Game("with my code")
  await bot.change_presence(status=nextcord.Status.do_not_disturb, activity=game)
  print('Successfully logged in and booted...!')

bot.run(dotos.token, reconnect=True)
