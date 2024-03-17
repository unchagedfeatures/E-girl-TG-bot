#code
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
words = ["привет", "пока", "гугл"]

# Define your handler
@dp.message()
async def handle_messages(message: types.Message):
    print(type(message.text))
    # Check if the message contains an ID or login
    if str(message.from_user.id) in str(message.text) or str(message.from_user.username) in str(message.text):
        # Replace the message with a new one
        await message.answer("Please do not share your ID or login.")
    else:
        # Do something else if the message doesn't contain ID or login
        await message.answer("Your message was received.")

async def main():
    try:
        await dp.start_polling(bot)  
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
