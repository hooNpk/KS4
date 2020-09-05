let cron = require('node-cron');

const TelegramBot = require('node-telegram-bot-api');
const Token = '1222541501:AAE4NchzefyiuYj_SW4ihDZIEbbZ5S4_H6s';
const bot = new TelegramBot(Token, {polling:true});
const CHAT_ID = '1006200994';

cron.schedule('37 13 * * *', function(){
    botMessage();
}).start();

function botMessage(){
    const text = '이것은 로컬에서 보낸 메시지';
    bot.sendMessage(CHAT_ID, text).then(function(data){
        console.log('success sending text');
    }).catch(err=>{console.log(err);});
}