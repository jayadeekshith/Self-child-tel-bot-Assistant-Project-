#pip install pyTelegramBotAPI
#pip install selenium
#pip install pywhatkit
#search botfather in telegram
#click on start
#send /start in botfather
#send newbot
#set a name of ypur bot
#set a user name for it
#search username in telegram u will see ypur bot click start
#the telegram bot created now the code part
import telebot
import webbrowser
import pywhatkit as kt
bot =telebot.TeleBot("1793603050:AAHJHzymqf6YyOnJhM-ITqeyXF7MU2s8OLI") #this is your http api availabe in telegram
##browsing

#google
@bot.message_handler(commands=['google'])
def send_welcome(message):
    bot.reply_to(message,webbrowser.open('http://google.com'))

#youtube
@bot.message_handler(commands=['youtube'])
def send_welcome(message):
    bot.reply_to(message,webbrowser.open('https://www.youtube.com/'))

#github
@bot.message_handler(commands=['github'])
def send_welcome(message):
    bot.reply_to(message,webbrowser.open('https://github.com/'))

#instagram
@bot.message_handler(commands=['instagram'])
def send_welcome(message):
    bot.reply_to(message,kt.search('https://www.instagram.com/'))

#github
@bot.message_handler(commands=['facebook'])
def send_welcome(message):
    bot.reply_to(message,webbrowser.open('https://facebook.com/'))

#whatsapp_timer
@bot.message_handler(commands=['send_whatsapp_timer'])
def send_welcome(message):
    bot.reply_to(message,kt.sendwhatmsg("+919999999999","hello",10,54))

#playsongs
@bot.message_handler(commands=['play_songs'])
def send_welcome(message):
    bot.reply_to(message,kt.search("https://gaana.com/playlist/dunuambrose-indiagana"))

    
#shutdown
@bot.message_handler(commands=['turnoff'])
def send_welcome(message):
    bot.reply_to(message,kt.shutdown(10))


#enter your input search
@bot.message_handler(commands=["search"])
def send_welcome(message):
    a=input("Enter your search : ")
    bot.reply_to(message,kt.search(a))

#covid_updates
@bot.message_handler(commands=['covid_updates'])
def send_welcome(message):
    bot.reply_to(message,kt.search('https://www.worldometers.info/coronavirus/?fbclid=IwAR35ZFiRZJ8tyBCwazX2N-k7yJjZOLDQiZSA_MsJAfdK74s8f2a_Dgx4iVk'))


bot.polling()
