from aiogram import Dispatcher, types, F, Router
import keyboards as nav
import database.db_hendlers as db
from database.db_hendlers import cursor
import information.messages as mesg
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup

dp = Dispatcher()
router = Router()

class Form(StatesGroup):
    description = State()
class Meeting(StatesGroup):
    meeting_link = State()

@router.callback_query(F.data == 'main_back')
async def start_message_back(callback: types.CallbackQuery):
    worker = db.get_worker(cursor, callback.from_user.id)
    admin = db.get_admin(cursor, callback.from_user.id)
    if worker is not None:
        await callback.message.edit_text(
            'привет, сыночек',
            reply_markup=nav.main_worker_menu()
        )
    elif admin is not None:
        await callback.message.edit_text(
            'привет, папа',
            reply_markup=nav.main_admin_menu()
        )
    else:
        await callback.message.edit_text(
        "Привет, мы первый бот",
        reply_markup=nav.main_menu()
    )

@router.callback_query(F.data == 'sform1')
async def new_girl(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Напишите о себе что-то!',
        reply_markup=nav.main_back_button()
    )

@router.callback_query(F.data == 'forgl1')
async def form_girl(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Анкеты',
        reply_markup=nav.main_back_button()
)
#
#Быстрые услуги
#
@router.callback_query(F.data == 'forder1')
async def order_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Быстрые услуги',
        reply_markup=nav.fasthire_menu()
    )
#
#Рефералы
#
@router.callback_query(F.data == 'referal1')
async def ref_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Ваши реффералы',
        reply_markup=nav.main_back_button()
    )
#
#Кошелек
#
@router.callback_query(F.data == 'mbalance1')
async def balance_menu(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    result = db.get_balance(cursor, user_id)
    money_value = result[0]
    await callback.message.edit_text(
        f'Ваш ID: {user_id}\nУ вас на счету {money_value} RUB. Хотите пополнить? ',
        reply_markup=nav.main_back_button()
    )
#
#Топ людей
#
@router.callback_query(F.data == 'peoplet1')
async def top_people_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Топ людей',
        reply_markup=nav.main_back_button()
    )
#
#Жалобы
#
@router.callback_query(F.data == 'apeopl1')
async def awful_people_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Жалобы:',
        reply_markup=nav.main_back_button()
    )
#
#Информация
#
@router.callback_query(F.data == 'idesk1')
async def inform_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Информация о проекте \nОчень важная, тут много что сказано и о том как сказано нужно говорить побольше',
        reply_markup=nav.main_back_button()
    )
#
#Голосовые
#
@router.callback_query(F.data == 'voice_hired')
async def hiring_voice_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=mesg.hire_voice_txt,
        reply_markup=nav.choose_voice_duration()
    )
#
#Видеокружки
#
@router.callback_query(F.data == 'videovoice_hired')
async def hiring_voice_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=mesg.hire_voice_txt,
        reply_markup=nav.choose_videovoice_duration()
    )
#
#Кнопка админа
#
@router.callback_query(F.data == 'admin_pressed')
async def give_worker(callback: types.CallbackQuery):
    await callback.message.edit_text(
        mesg.admin_panel_faq,
        reply_markup=nav.main_back_button()
    )
#
#Реакция на кнопку "Главное меню"
#
@router.callback_query(F.data == 'main_back')
async def start_message_back(callback: types.CallbackQuery):
    worker = db.get_worker(cursor, callback.from_user.id)
    admin = db.get_admin(cursor, callback.from_user.id)
    if worker is not None:
        await callback.message.edit_text(
            'привет, сыночек',
            reply_markup=nav.main_worker_menu()
        )
    elif admin is not None:
        await callback.message.edit_text(
            'привет, папа',
            reply_markup=nav.main_admin_menu()
        )
    else:
        await callback.message.edit_text(
        "Привет, мы первый бот",
        reply_markup=nav.main_menu()
    )
#
#Видео заказано
#
@router.callback_query(F.data == 'video_hired')
async def hiring_video_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=mesg.hire_voice_txt,
        reply_markup=nav.choose_video_duration()
    )
#
#Заказ времени
#
@router.callback_query(lambda query: query.data.startswith('sec'))
async def write_voice_description(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(what_ordered=callback.data)
    await callback.message.answer('Напишите что бы Вы хотели видеть',
                                  reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.description)
#
#Заказ видео-звонка
#
@router.callback_query(lambda query: query.data.startswith('videocall'))
async def write_voice_description(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(what_ordered=callback.data)
    await callback.message.answer('Укажите ссылку и соц сеть',
                                  reply_markup=ReplyKeyboardRemove())
    await state.set_state(Meeting.meeting_link)