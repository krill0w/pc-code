module.exports = (bot) => {
let prompt = process.openStdin()
prompt.addListener("data", res => {
    let x = res.toString().trim().split(/ +/g)
        bot.channels.get("519920731904016384").send(x.join(" "));
    });
}