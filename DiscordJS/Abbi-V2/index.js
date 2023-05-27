const { Client, Collection } = require("discord.js");
const { token } = require("./botconfig.json");
const bot = new Client();

["aliases", "commands"].forEach(x => bot[x] = new Collection());
["console", "command", "event", "dms"].forEach(x => require(`./handlers/${x}`)(bot));

bot.on('message', (message) => {
    if(message.content == '@everyone') {
        message.reply('Shut The Fuck Up');
    }
});

bot.login(token);