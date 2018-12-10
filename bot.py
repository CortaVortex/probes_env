# какой бот (пробы и ошибки)
bot = telebot.TeleBot ( " 721177798:AAH9pelo668_CftdnQXf2GhsGoRW8bNSRRg " )

# предполагаемое приветствие
@ bot.message_handler ( commands = [ ' start ' , ' info ' ])
 def  send_welcome ( message ):
	bot.reply_to (сообщение « Привет. Я - бот-цензор. Я могу быть очень злым, если так решили админы чата, так что советую следовать правилам: (ссылка) (команда) - нажимай, если хочешь узнать, что я умею. » )

# проверка-повторюшка
@ bot.message_handler ( func = lambda  m : True )
 def  echo_all ( message ):
	bot.reply_to (message, message.text)

# запуск бота?
bot.polling ()
