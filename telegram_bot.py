# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai
import json

# Параметры для конфига системы
api_ai_token = "9f442ba7276d40d1aa64a32a156af507"
telegram_token = "524706088:AAGq3De-XCF-vb3-Z5NvScaoULoMAlosYO4"

# Создаем основные объекты для работы с телеграмом
updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher


# Обработка первой команды на старт работы с ботом
def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я помогу тебе выбрать мероприятие, на которое стоит сходить')


# Обработка текстовых сообщений от пользователя
def text_message(bot, update_from_telegram):

    # Получаем результаты классификации и выделения сущностей из api ai
    user_message_text = update_from_telegram.message.text
    result_of_classification = get_classification_and_entities(api_ai_token, user_message_text)

    # Если удалось обработать сообщение, то формируем ответ пользователю, иначе отвечаем заглушкой
    if result_of_classification:
        bot.send_message(chat_id=update_from_telegram.message.chat_id, text='Ответ заглушечкой')
    else:
        bot.send_message(chat_id=update_from_telegram.message.chat_id, text='Шестеренки за болты забежали, попробуйте еще раз')


def get_classification_and_entities(api_ai_token, user_message_text):
    """
    Функция возвращает результата классификации реплики пользователя и выделенные сущности
    :param api_ai_token: токен для доступа к интерфейсу api ai
    :param user_message_text: текст сообщения пользователя
    :return: словарь с тематикой обращения и выделенными сущностями
    """
    result = {}
    request_to_apiai = apiai.ApiAI(api_ai_token).text_request()  # Токен API к Dialogflow
    request_to_apiai.lang = 'ru'  # На каком языке будет послан запрос
    request_to_apiai.session_id = "idSessionOfDialog"  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request_to_apiai.query = user_message_text  # Готовим к передаче в apiai текст сообщения пользователя

    # Непосредственно выполняем запрос к apiai
    try:
        response_json_from_apiai = json.loads(request_to_apiai.getresponse().read().decode('utf-8'))
    except Exception as e:
        print("ошибка ", str(e))

    # Получаем результат классификации сообщения пользователя
    result['intent_name'] = response_json_from_apiai['result']['metadata']['intentName']

    # Параметры для интента поиска мероприятий
    if result['intent_name'] == 'Find events':
        result['date_period'] = response_json_from_apiai['result']['parameters']['date-period']
        result['with_who'] = response_json_from_apiai['result']['parameters']['With-who']
        result['date'] = response_json_from_apiai['result']['parameters']['date']
        result['free_or_not'] = response_json_from_apiai['result']['parameters']['Free-or-not']
        result['time_period'] = response_json_from_apiai['result']['parameters']['time-period']

    return result


# Создаем обработчики событий для телеграма
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)
# Добавляем обработчики событий для телеграма в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Запускаем бесконечный цикл получения и обработки новых сообщений из телеграма
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
