import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
import re
import keyboards as nav
import database.db_hendlers as db
from database.db_hendlers import cursor
from config import TOKEN
dp = Dispatcher()
router = Router()
bot = Bot(token=TOKEN)
global isAdmin
global isGirl
#Функция старта бота
@router.message(Command("start", "menu", "help"))
async def start_message(message: types.Message, command: types.BotCommand):
    user_id = message.from_user.id
    user = db.get_user(cursor, user_id)
    #Если юзер не задан в нашей таблице, то он становится None
    if user is None:
        referrer_id = command.args
        referred_user_id = message.chat.id
        if referrer_id is not None:
            ref_text = f'''
                Пользователь с ID {referred_user_id} перешел по вашей реферральной ссылке!
            '''
            cursor.execute("UPDATE users SET count_ref = count_ref + 1 WHERE user_id = ?", (referrer_id, ))
            await Bot.send_message(chat_id=referrer_id, text=ref_text, self=bot)
        else:
            referrer_id = 0
        cursor.execute("INSERT INTO 'users' (user_id, who_ref) VALUES (?, ?)", (user_id, referrer_id,))
        #Добавляем id пользователя в таблицу 'users' при первом запуске, вторая строчка овтечает за сохранение базы данных(важно, потому что при перезапуске тогда стирается)
        db.conn.commit()
        await message.answer(
            'Привет, мы первый бот',
            reply_markup=nav.main_menu()
        )
        isAdmin = False
        isGirl = False
    else:
        worker = db.get_worker(cursor, message.from_user.id)
        admin = db.get_admin(cursor, message.from_user.id)
        #Заглядываем в таблицу 'users' и проверяем стоит ли у пользователя значение 1
        #Заглядываем в таблицу и проверяем стоит ли у пользователя статус 2
        #Если да, выдаем соответсвующую панель
        if worker is not None:
            await message.answer(
                'Привет, сыночек',
                reply_markup=nav.main_worker_menu()
            )
            isGirl = True
            isAdmin = False
        elif admin is not None:
            await message.answer(
                'привет, папа',
                reply_markup=nav.main_admin_menu()
            )
            isAdmin = True
            isGirl = False
        else:
            await message.answer(
                "Привет, мы первый бот",
                reply_markup=nav.main_menu()
        #Задаем боту стартовое сообщение и назначаем ему меню из файла keyboards.py.
            )
            isAdmin = False
            isGirl = False


@router.message(Command("new_girl"))
#Функция выдачи роли "Девушка"
async def getgirl(
        message: types.Message,
        command: types.BotCommand
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    admin = db.get_admin(cursor, message.from_user.id)
    if admin is not None:
        if command.args is None:
            await message.answer(
                "Ошибка: id не указано"
            )
            return
        else:

            number_pattern = r'\b\d+\b'
            ids = re.findall(number_pattern, command.args)
            if ids:
                new_girl_id = int(ids[0])
            else:
                await message.answer('Убедитесь в правильности написанного id')
                return
            #Проверка на админа и работника
            check_worker = db.get_worker(cursor, new_girl_id)
            check_admin = db.get_admin(cursor, new_girl_id)
            if check_worker is not None:
                await message.answer('Такой пользователь уже зарегестрирован')
            elif check_admin is not None:
                await message.answer('Я не думаю, что стоит это делать.')
            elif new_girl_id == message.from_user.id:
                await message.answer(
                    'Нет, нет, ты уже админ, так нельзя'
                )
            else:
                try:
                    user = db.get_user(cursor, new_girl_id)
                    if user is None:
                        await message.answer(f'Пользователь {new_girl_id} не является нашим пользователем.')
                    else:
                        cursor.execute("UPDATE users SET status=? WHERE user_id=?;", (1, new_girl_id,))
                        await message.answer(f'Пользователь {new_girl_id} была добавлена.')
                        db.conn.commit()
                except:
                    await message.answer('Произошла ошибка')
    else:
        await message.answer(
            'Нет доступа.'
        )

@router.message(Command("del_girl"))
#Функция удаления роли "Девушка"
async def delgirl(
        message: types.Message,
        command: types.BotCommand
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    admin = db.get_admin(cursor, message.from_user.id)
    if admin is not None:
        if command.args is None:
            await message.answer(
                "Ошибка: id не указано"
            )
            return
        else:

            number_pattern = r'\b\d+\b'
            ids = re.findall(number_pattern, command.args)
            if ids:
                new_girl_id = int(ids[0])
            else:
                await message.answer('Убедитесь в правильности написанного id')
                return
            #Проверка на админа и работника
            check_worker = db.get_worker(cursor, new_girl_id)
            check_admin = db.get_admin(cursor, new_girl_id)
            if check_worker is None:
                await message.answer('Этот пользователь не является нашим работником.')
            elif check_admin is not None:
                await message.answer('Я не думаю, что стоит это делать.')
            elif new_girl_id == message.from_user.id:
                await message.answer(
                    'Нет, нет, ты админ, так нельзя'
                )
            else:
                try:
                    user = db.get_user(cursor, new_girl_id)
                    if user is None:
                        await message.answer(f'Пользователь {new_girl_id} не является нашим пользователем.')
                    else:
                        cursor.execute("UPDATE users SET status=? WHERE user_id=?;", (0, new_girl_id,))
                        await message.answer(f'Пользователь {new_girl_id} была удалена из работников')
                        db.conn.commit()
                except:
                    await message.answer('Произошла ошибка')
    else:
        await message.answer(
            'Нет доступа.'
        )

@router.message(Command("add_balance"))
#Функция добавления баланса пользователю Админами
async def addbalance(
        message: types.Message,
        command: types.BotCommand
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    admin = db.get_admin(cursor, message.from_user.id)
    if admin is not None:
        if command.args is None:
            await message.answer(
                "Ошибка: неправильный формат команды. Пример:\n"
                "/add_balance <id> <amount>"
            )
            return
        args = command.args.split()
        if len(args) != 2:
            await message.answer(
                "Ошибка: неправильный формат команды. Пример:\n"
                "/add_balance <id> <amount>"
            )
            return
        recieve_id, newmoney = args
        if not recieve_id.isdigit() or not newmoney.isdigit():
            await message.answer(
                "Ошибка: аргументы должны быть целыми числами"
            )
            return
        user = db.get_user(cursor, recieve_id)
        if user is None:
            await message.answer(f'Пользователь {recieve_id} не является нашим пользователем.')
        else:
            cursor.execute("UPDATE users SET money = money + ? WHERE user_id = ?", (newmoney, recieve_id,))
            db.conn.commit
            result = db.get_balance(cursor, recieve_id)
            new_balance = result[0]
            await message.answer(
                "Баланс добавлен!\n"
                f"Получатель: {recieve_id}\n"
                f"Сколько добавлено: {newmoney} RUB\n"
                f"Новый баланс: {new_balance} RUB"
                )
            db.conn.commit()
    else:
        await message.answer(
            'Нет доступа.'
        )

@router.message(Command("min_balance"))
#Функция отнятия баланса пользователю Админами
async def minbalance(
        message: types.Message,
        command: types.BotCommand
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    admin = db.get_admin(cursor, message.from_user.id)
    if admin is not None:
        if command.args is None:
            await message.answer(
                "Ошибка: неправильный формат команды. Пример:\n"
                "/min_balance <id> <amount>"
            )
            return
        args = command.args.split()
        if len(args) != 2:
            await message.answer(
                "Ошибка: неправильный формат команды. Пример:\n"
                "/min_balance <id> <amount>"
            )
            return
        recieve_id, newmoney = args
        if not recieve_id.isdigit() or not newmoney.isdigit():
            await message.answer(
                "Ошибка: аргументы должны быть целыми числами"
            )
            return
        user = db.get_user(cursor, recieve_id)
        if user is None:
            await message.answer(f'Пользователь {recieve_id} не является нашим пользователем.')
        else:
            cursor.execute("UPDATE users SET money = money - ? WHERE user_id = ?", (newmoney, recieve_id,))
            db.conn.commit
            result = db.get_balance(cursor, recieve_id)
            new_balance = result[0]
            await message.answer(
                "Баланс изменён!\n"
                f"Получатель: {recieve_id}\n"
                f"Сколько удалено: {newmoney} RUB\n"
                f"Новый баланс: {new_balance} RUB"
                )
            db.conn.commit()
    else:
        await message.answer(
            'Нет доступа.'
        )