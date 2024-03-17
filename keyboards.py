import configparser
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import  InlineKeyboardBuilder
from aiogram import types

#Задаем список переменных, что бы легче потом было на них ссылаться
forms_girl = "💝 Анкеты"
fast_order = "✨Быстрая услуга"
referalls = "Рефералы"
m_balance = "👛Кошелёк"
people_top = "Топ людей"
awful_people = "🤥Жалобы"
send_form = "🥰Подать заявку"
info_desk = "👾Информация"
main_back_text = 'Главное меню'

#Список переменных для быстрых услуг
hire_voice_button = InlineKeyboardButton(text='Голосовые', callback_data='voice_hired')
hire_videovoice_button = InlineKeyboardButton(text='Видеокружки', callback_data='videovoice_hired')
hire_photo_button = InlineKeyboardButton(text='Фото', callback_data='photo_hired')
hire_video_button = InlineKeyboardButton(text='Видео', callback_data='video_hired')
hire_nude_photo_button = InlineKeyboardButton(text='Фото 18+', callback_data='nude_photo_hired')
hire_nude_video_button = InlineKeyboardButton(text='Видео 18+', callback_data='nude_video_hired')
hire_videocall_button = InlineKeyboardButton(text='Видео-звонки', callback_data='videocall_hired')
hire_videocall_nude_button = InlineKeyboardButton(text='Видео-звонки 18+', callback_data='videocall_nude_hired')

#Список переменных для авторизированных пользователей
worker_button = InlineKeyboardButton(text='Меню работника', callback_data='worker_pressed')
admin_button = InlineKeyboardButton(text='Меню Админа', callback_data='admin_pressed')

#да или нет
yes_button = InlineKeyboardButton(text='Подтверждаю', callback_data='yes_press')
no_button = InlineKeyboardButton(text='Передумал', callback_data='no_press')

#Список переменных для заказа
fifteen_sec_button_voice = InlineKeyboardButton(text='До 15 секунд', callback_data='sec_fifteen_voice_pressed')
fourty_sec_button_voice = InlineKeyboardButton(text='До 40 секунд', callback_data='sec_fourty_voice_pressed')
one_min_button_voice = InlineKeyboardButton(text='До 1 минуты', callback_data='sec_sixty_voice_pressed')
back_to_buy_menu = InlineKeyboardButton(text='Вернуться в меню', callback_data='forder1')
fifteen_sec_button_video = InlineKeyboardButton(text='До 15 секунд', callback_data='sec_fifteen_video_pressed')
fourty_sec_button_video = InlineKeyboardButton(text='До 40 секунд', callback_data='sec_fourty_video_pressed')
one_min_button_video = InlineKeyboardButton(text='До 1 минуты', callback_data='sec_sixty_video_pressed')
fifteen_sec_button_voicevideo = InlineKeyboardButton(text='До 15 секунд', callback_data='sec_fifteen_voicevideo_pressed')
fourty_sec_button_voicevideo = InlineKeyboardButton(text='До 40 секунд', callback_data='sec_fourty_voicevideo_pressed')
one_min_button_voicevideo = InlineKeyboardButton(text='До 1 минуты', callback_data='sec_sixty_voicevideo_pressed')


#Переменные в виде готовых кнопок меню, InlineKeyboardButton отвечает за кнопки под сообщениями, в text мы задаем текст переменной 
#В callback_data содержится данные, которые получает бот при нажатии на них.
forgl = InlineKeyboardButton(text=forms_girl, callback_data='forgl1')
forder = InlineKeyboardButton(text=fast_order, callback_data='forder1')
referal = InlineKeyboardButton(text=referalls, callback_data='referal1')
mbalance = InlineKeyboardButton(text=m_balance, callback_data='mbalance1')
peoplet = InlineKeyboardButton(text=people_top, callback_data='peoplet1')
apeople = InlineKeyboardButton(text=awful_people, callback_data='apeopl1')
sform = InlineKeyboardButton(text=send_form, callback_data='sform1')
idesk = InlineKeyboardButton(text=info_desk, callback_data='idesk1')
main_back_inline = InlineKeyboardButton(text=main_back_text, callback_data='main_back')

#Главное меню покупателя, присутвует разделение по строчкам с помощью квадратных скобок.
def main_menu():
    buttons = [
        [forgl,forder],[referal,mbalance],[peoplet,apeople,],[sform,idesk]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
    #В теории, здесь можно придать любые названия переменным, самое главное останется то, что записано в def, но я рекомендую пока писать так

#Меню информации - его просто проще всего сделать
def main_back_button():
    #Я не уверен стоит ли делать buttons, когда кнопка только 1
    buttons = [[main_back_inline]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def fasthire_menu():
    buttons = [
        [
            hire_voice_button,
            hire_videovoice_button
        ],
        [
            hire_photo_button,
            hire_video_button
        ],
        [
            hire_nude_photo_button,
            hire_nude_video_button
        ],
        [
            hire_videocall_button,
            hire_videocall_nude_button
        ],
        [
            main_back_inline
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def main_worker_menu():
    buttons = [
        [
            forgl,
            forder
        ],
        [
            referal,
            mbalance
        ],
        [
            peoplet,
            apeople
        ],
        [
            sform,
            idesk
        ],
        [
            worker_button
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def main_admin_menu():
    buttons = [
        [
            forgl,
            forder
        ],
        [
            referal,
            mbalance
        ],
        [
            peoplet,
            apeople
        ],
        [
            sform,
            idesk
        ],
        [
            admin_button
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def choose_voice_duration():
    buttons = [
        [
            fifteen_sec_button_voice,
            fourty_sec_button_voice
        ],
        [
            one_min_button_voice,
            back_to_buy_menu
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def choose_video_duration():
    buttons = [
        [
            fifteen_sec_button_video,
            fourty_sec_button_video
        ],
        [
            one_min_button_video,
            back_to_buy_menu
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def choose_videovoice_duration():
    buttons = [
        [
            fifteen_sec_button_voicevideo,
            fourty_sec_button_voicevideo
        ],
        [
            one_min_button_voicevideo,
            back_to_buy_menu
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

#def choose_media_format():
#    buttons = [[media_with_face_button, media_without_face_button], [back_to_buy_menu]]
#    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
#    return keyboard

def back_from_description():
    buttons = [
        [main_back_inline]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def unsucces_payment():
    buttons = [
        [mbalance, forder]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

#не используется)
def yes_or_no_menu():
    buttons = [
        [yes_button, no_button]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard