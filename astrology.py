from aiogram.utils import executor
from creation import dp

async def on_startup(_):
    print('Bot is online')


from handlers import client,other

client.register_handlers_client(dp)

executor.start_polling(dp, on_startup=on_startup)