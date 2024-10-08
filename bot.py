import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router, BaseMiddleware
from aiogram.filters.command import Command
from aiogram.filters import Command, StateFilter
import re
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

#Импорты из наших папок
from config import TOKEN
from database.db_hendlers import cursor
import database.db_hendlers as db
import keyboards as nav
import information.messages as mesg
import information.prices as prices
import hendlers.commands as cmd
import hendlers.button_clicks as buttonclick

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()
router = Router()
global BadUser
global IsAdmin
global IsGirl

class Form(StatesGroup):
    description = State()
class Orders(StatesGroup):
    order_type = State()
class Meeting(StatesGroup):
    meeting_link = State()

@dp.message(StateFilter(Meeting.meeting_link), F.text)
async def edit_description(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(meeting_link=callback.text)
    user_data = await state.get_data()
    meeting_link = user_data.get('meeting_link')
    user_id = callback.from_user.id
    what_order = user_data.get('what_ordered')
    result = db.get_balance(cursor, user_id)
    money_value = result[0]
    if what_order in prices.price_map:
        price = prices.price_map[what_order]
        if money_value >= price:
            cursor.execute("UPDATE users SET money = money - ? WHERE user_id = ?",  (price, user_id))
            result = db.get_balance(cursor, user_id)
            money_value = result[0]
            cursor.execute("INSERT INTO 'orders' (who_pays_id, what_ordered, meeting_link) VALUES (?, ?, ?)", (user_id, what_order, meeting_link))
            cursor.execute("UPDATE users SET count_orders= count_orders + 1 WHERE user_id=?;", (user_id, ))
            await callback.answer(f'Цена за это составит {price} RUB.\nНа Вашем балансе {money_value} RUB. \nУслуга оплачена.', reply_markup=nav.back_from_description())
        else:
            await callback.answer(f'На Вашем счету недостаточно средств. \n Цена за это составит {price} RUB.\n На Вашем балансе {money_value} RUB. \n', reply_markup=nav.unsucces_payment())
    else:
        await callback.answer(f'Случилась техническая ошибка.', reply_markup=nav.back_from_description)
        db.conn.commit()
    await state.clear()
    db.conn.commit()


@dp.message(StateFilter(Form.description), F.text)
async def edit_description(callback: types.CallbackQuery, state: FSMContext):
    if str(callback.from_user.username) in callback.text:
        BadUser = True
    else:
        BadUser = False
    await state.update_data(description=callback.text)
    user_data = await state.get_data()
    description = user_data.get('description')
    await callback.answer(f'Твой текст: {description}', reply_markup=ReplyKeyboardRemove())
    user_id = callback.from_user.id
    what_order = user_data.get('what_ordered')
    result = db.get_balance(cursor, user_id)
    money_value = result[0]
    if what_order in prices.price_map:
        price = prices.price_map[what_order]
        if money_value >= price:
            cursor.execute("UPDATE users SET money = money - ? WHERE user_id = ?",  (price, user_id))
            result = db.get_balance(cursor, user_id)
            money_value = result[0]
            if BadUser == False:
                cursor.execute("INSERT INTO 'orders' (who_pays_id, what_ordered, order_description) VALUES (?, ?, ?)", (user_id, what_order, description))
                cursor.execute("UPDATE users SET count_orders= count_orders + 1 WHERE user_id=?;", (user_id, ))
                await callback.answer(f'Цена за это составит {price} RUB.\nНа Вашем балансе {money_value} RUB. \nУслуга оплачена.', reply_markup=nav.back_from_description())
            else:
                cursor.execute("UPDATE users SET violations= violations + 1 WHERE user_id=?;", (user_id, ))
                cursor.execute("UPDATE users SET count_orders= count_orders + 1 WHERE user_id=?;", (user_id, ))
                await callback.answer(f'Цена за это составит {price} RUB.\nНа Вашем балансе {money_value} RUB. \nУслуга оплачена.\nВ Вашем сообщении замечено нарушение, если Вы считаете, что это ошибка, обратитесь к Администрации.', reply_markup=nav.back_from_description())
            db.conn.commit()
        else:
            await callback.answer(f'На Вашем счету недостаточно средств. \n Цена за это составит {price} RUB.\n На Вашем балансе {money_value} RUB. \n', reply_markup=nav.unsucces_payment())
            db.conn.commit()
    else:
        await callback.answer(f'Случилась техническая ошибка.', reply_markup=nav.back_from_description)
        db.conn.commit()
    await state.clear()
    db.conn.commit()




# Запуск процесса поллинга новых апдейтов
async def main():
    try:
        dp.include_routers(buttonclick.router, cmd.router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
#Просто важная штука, я не уверен, за что она отвечает
if __name__ == "__main__":
    asyncio.run(main())