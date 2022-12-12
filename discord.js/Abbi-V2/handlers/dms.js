module.exports = (bot) => {
  bot.on("message", async message => {
    if (message.channel.type === 'dm'){
      console.log(`${message.author.username} said: ${message.content}`);
    }
  });
}