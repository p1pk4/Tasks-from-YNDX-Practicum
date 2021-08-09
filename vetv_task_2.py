#Научите Анфису печатать фразу 'У вас нет сообщений', если количество сообщений равно нулю.
for messages_count in range(6):
    if messages_count > 0:
        print('Новых сообщений: ' + str(messages_count))
    else:
        print('У вас нет сообщений')
