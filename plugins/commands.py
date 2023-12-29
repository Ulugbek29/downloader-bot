from pyrogram import filters, Client as Mbot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import DUMP_GROUP

subscribed_users = set()


@Mbot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    channel_username = "FilmPrimiere"  
    
    try:
        chat_member = await client.get_chat_member(channel_username, message.from_user.id)
        
        if chat_member.status in ["member", "administrator", "creator"]:
            if message.from_user.id not in subscribed_users:
                subscribed_users.add(message.from_user.id)
                await message.reply("Спасибо")
        else:
            await message.reply(f"🔥 Приветствуем, {message.from_user.mention()}! Добро пожаловать в нашего уникального бота!\n\nТеперь вы можете легко скачивать контент из популярных социальных сетей:\n\n• Instagram — сохраняйте истории, посты и IGTV в любом формате!\n• TikTok — загружайте видео без водяных знаков в любом формате!\n• Facebook — скачивайте посты в любом формате!\n• Twitter — сохраняйте посты и видео в любом формате!\n\n<b>🚀 Просто отправьте ссылку, чтобы начать загрузку медиа.</b>\n\n<b>👨‍💻 Вопросы? Обращайтесь к администратору:</b> @yusufbekovv24") 

    except Exception as e:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Подписаться✅", url=f"https://t.me/{channel_username}")
                ]
            ]
        )
        await message.reply("Пожалуйста, подпишитесь на наши каналы ниже,\n затем вы можете использовать бота.🎉", reply_markup=keyboard)
        
@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("Добро пожаловать!\n🌟 Наш удобный бот создан специально для вас. Просто отправьте сюда свой ролик из социальных сетей и делитесь ссылками без лишних усилий:)")
