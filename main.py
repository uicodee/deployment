import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp, CommandSettings, Command

import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text='Salom, men test uchun yaratilgan botman!'
    )


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message) -> None:
    await message.answer(
        text='Mana sizga qo\'llanma'
    )


@dp.message_handler(CommandSettings())
async def cmd_settings(message: types.Message) -> None:
    await message.answer(
        text='Sozlamalar'
    )


@dp.message_handler(Command('random'))
async def cmd_random(message: types.Message) -> None:
    await message.answer(
        text='Tasodifiy son {r}'.format(r=str(random.randint(0, 1000)))
    )


if __name__ == '__main__':
    executor.start_polling(dp)
