import nest_asyncio
import asyncio
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
import logging

from dotenv import load_dotenv
import os

# Загружаем .env
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Получаем токен
TOKEN = os.getenv("BOT_TOKEN")

# Проверяем загрузку токена
if TOKEN is None:
    print("❌ Ошибка: Токен не загружен! Проверь .env")
else:
    print(f"✅ TOKEN загружен: {TOKEN[:10]}...")


# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция для старта
async def start(update: Update, context):
    # Клавиатура с кнопками
    reply_keyboard = [
        ['✅ЛУЧШИЕ ПРОЕКТЫ', '🎁БОНУСЫ'],
        ['💸ТАКТИКИ 1WIN', '🏆ТОП СТРИМЕРЫ'],
        ['⚡️ВАУЧЕРЫ', '🆘ПОДДЕРЖКА']
    ]
    
    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        "👋Привет! Выберите одну из кнопок:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    )

# Обработка текстовых кнопок
async def inline_buttons(update: Update, context):
    text = update.message.text

    # --- ЛУЧШИЕ ПРОЕКТЫ ---
    if text == "✅ЛУЧШИЕ ПРОЕКТЫ":
        await update.message.reply_text(
            "📊 Вот список лучших и проверенных проектов:\n\n"
            "💎 FLAGMAN — [Ссылка](https://flagman-way-six.com/c186266d0)\n"
            "👾 IRWIN — [Ссылка](https://rwn-irrs10.com/c8283aa0e)\n"
            "🏆 ARKADA — [Ссылка](https://grid-cyberlane.com/s2641aa71)\n"
            "⚡️ GIZBO — [Ссылка](https://gizbo-way-eight.com/c4da3d5d8)\n"
            "⭐️ LEX — [Ссылка](https://lex-blrs10.com/c451caa1e)\n"
            "❤️ 1GO — [Ссылка](https://1go-irrs01.com/c1bfc9db8)\n"
            "💙 1WIN — [Ссылка](https://1wcneg.com/casino/list/4?p=fnfz)\n"
            "💴 CASHER — [Ссылка](https://aff.casher.ink/?alias=b79492)\n"
            "🐍 VEGA — [Ссылка](https://vega.bet/?rf=cm4gasdu600cf7csc3x957ff2)",
            parse_mode="Markdown"
        )

    # --- БОНУСЫ ---
    elif text == "🎁БОНУСЫ":
        bonus_keyboard = [
            [InlineKeyboardButton("💎 FLAGMAN", callback_data="bonus_flagman")],
            [InlineKeyboardButton("👾 IRWIN", callback_data="bonus_irwin")],
            [InlineKeyboardButton("🏆 ARKADA", callback_data="bonus_arkada")],
            [InlineKeyboardButton("⚡️ GIZBO", callback_data="bonus_gizbo")],
            [InlineKeyboardButton("⭐️ LEX", callback_data="bonus_lex")],
            [InlineKeyboardButton("❤️ 1GO", callback_data="bonus_1go")],
            [InlineKeyboardButton("💙 1WIN", callback_data="bonus_1win")],
            [InlineKeyboardButton("💴 CASHER", callback_data="bonus_casher")],
            [InlineKeyboardButton("🐍 VEGA", callback_data="bonus_vega")]
        ]
        
        await update.message.reply_text(
            "🎁 Выбери проект, чтобы узнать о бонусах!\u26A0\uFE0F Чтобы бонусы работали, важно зарегистрироваться по данным ссылкам и верифицировать аккаунт!",
            reply_markup=InlineKeyboardMarkup(bonus_keyboard)
        )

    # --- ВАУЧЕРЫ ---
    elif text == "⚡️ВАУЧЕРЫ":
        vouchers_keyboard = [
            [InlineKeyboardButton("📩 Подписаться на рассылку", callback_data="subscribe")],
            [InlineKeyboardButton("🚫 Отписаться от рассылки", callback_data="unsubscribe")]
        ]

        await update.message.reply_text(
            "💌 Управляй своей подпиской на рассылку ваучеров:",
            reply_markup=InlineKeyboardMarkup(vouchers_keyboard)
        )

    # --- ТАКТИКИ 1WIN ---
    elif text == "💸ТАКТИКИ 1WIN":
        keyboard = [
            [InlineKeyboardButton("🎯 LUCKY JET", callback_data="tactic_lucky_jet")],
            [InlineKeyboardButton("💣 MINES", callback_data="tactic_mines")],
            [InlineKeyboardButton("🚀 ROCKET QUEEN", callback_data="tactic_rocket_queen")],
        ]

        await update.message.reply_text(
            "🎯 Выбери игру, для которой нужна тактика:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # --- ТОП СТРИМЕРЫ ---
    elif text == "🏆ТОП СТРИМЕРЫ":
        await update.message.reply_text(
            "🎥 *ТОП-6 стримеров, которые приносят удачу:*\n\n"
            "🔥 1. *WINIK* — мастер крупных заносов\n"
            "🎮 2. *Evelone* — гарантированное веселье\n"
            "⚡️ 3. *Плохой Парень* — делает ставки на максимум\n"
            "💸 4. *Mellstroy* — разбирает казино в пух и прах\n"
            "🎲 5. *LuckyStrike* — профессионал в слотах\n"
            "🎯 6. *TurboRoll* — знает все секреты больших заносов\n\n"
            "📲 Следи за их успехами и перенимай опыт!",
            parse_mode="Markdown"
        )

    # --- ПОДДЕРЖКА ---
    elif text == "🆘ПОДДЕРЖКА":
        await update.message.reply_text(
            "🆘 *Нужна помощь?*\n\n"
            "📧 Напиши в наш Telegram: [@win_manager](https://t.me/win_manager)\n\n"
            "Мы всегда рядом, чтобы помочь тебе! 💙",
            parse_mode="Markdown"
        )

# Обработка нажатий на кнопки бонусов
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    # Описания бонусов
    project_bonuses = {
        "bonus_flagman": "🥇 Почему FLAGMAN — выбор лидеров? 🥇\n"
                         "🔹 Моментальная регистрация — ты в игре за секунды.\n"
                         "🔹 225% + до 500 FS — Welcome Pack для уверенного старта.\n"
                         "🔹 Кешбэк до 20% — возврат каждую неделю.\n"
                         "🔹 10000+ игр — от легендарных хитов до свежих новинок.\n"
                         "🔹 Турниры и лотереи — ещё больше шансов на крупный выигрыш.\n"
                         "🔹 Лутбоксы с призами — копи коины и открывай награды.\n"
                         "🔹 Бездеп до 50 000 ₽ в подарок на День Рождения.\n\n"
                         "📣 Забирай 50FS по промо: WINIK в слотах The Dog House, Cleocatra, Gates of Olympus\n"
                         "👉 [Регистрируйся здесь](https://flagman-way-six.com/c186266d0)",

        "bonus_irwin": "⬇️ Почему IRWIN — ваш идеальный выбор с первого клика ⬇️\n"
                       "🟣 Простой старт — регистрируйся в 1 клик и начинай выигрывать.\n"
                       "🟣 Кэшбек до 20% каждую неделю.\n"
                       "🟣 Более 6500 игр — от классических слотов до новинок.\n"
                       "🟣 До 50 000 рублей в подарок на день рождения.\n"
                       "📌 Промокод WINIK даёт 50FS при регистрации!\n"
                       "👉 [Регистрируйся здесь](https://rwn-irrs10.com/c8283aa0e)",

        "bonus_arkada": "🌀 Регистрируйся в новом Arkada Casino и получай бездепозитные 100 FS!\n"
                        "🎁 Вводи промокод WINIK при регистрации\n"
                        "👉 [Arkada — играй по-новому!](https://grid-cyberlane.com/s2641aa71)",

        "bonus_gizbo": "🔥САМЫЙ МОЩНЫЙ ПРОЕКТ🔥\n"
                       "Встречайте, идеальное казино GIZBO\n"
                       "🟣 Высокий RTP и большие ставки\n"
                       "🟣 Приветственный пакет 225% + до 600FS\n"
                       "🟣 Лутбоксы и мгновенные выплаты\n"
                       "📌 Промокод WINIK даёт 50FS при регистрации!\n"
                       "👉 [Регистрируйся здесь](https://gizbo-way-eight.com/c4da3d5d8)",

        "bonus_lex": "Ищешь идеальное казино?\n"
                     "LEX — это то, что ты искал.\n"
                     "1️⃣ Быстрые выводы и пополнения\n"
                     "2️⃣ Высокий RTP\n"
                     "📌 Промокод WINIK даёт 50FS при регистрации!\n"
                     "👉 [Регистрируйся здесь](https://lex-blrs10.com/c451caa1e)",

        "bonus_1go": "🏁 На старт, внимание — 1GO!\n"
                     "1GO Casino — игровой портал врывается на драйве!\n"
                     "🔥 Легенды гейм-индустрии, быстрая регистрация.\n"
                     "📌 Промокод WINIK даёт 50FS при регистрации!\n"
                     "📲 [Регистрируйся здесь](https://1go-irrs01.com/c1bfc9db8)",

        "bonus_1win": "🏆 Самый популярный проект с амбассадорами:\n"
                      "Mellstroy, Асхаб Тамаев, Evelon и другие.\n"
                      "🔹 Бонус 500% на первый депозит до 200 000 рублей и 70FS по промокоду WINIK\n"
                      "👉 [Регистрируйся здесь](https://1wcneg.com/casino/list/4?p=fnfz)",

        "bonus_casher": "Casher — криптовалютное казино с огромным выбором игр.\n"
                        "🎰 1900+ игр от ведущих провайдеров.\n"
                        "👉 [Регистрируйся здесь](https://aff.casher.ink/?alias=b79492)",

        "bonus_vega": "🐍 VEGA — казино с высокими шансами на победу!\n"
                      "✅ Высокий RTP и ежедневный рейкбэк.\n"
                      "👉 [Ссылка на регистрацию](https://vega.bet/?rf=cm4gasdu600cf7csc3x957ff2)"
    }

    # Отправляем соответствующее описание бонуса
    if query.data in project_bonuses:
        await query.edit_message_text(
            text=project_bonuses[query.data],
            parse_mode="Markdown",
            disable_web_page_preview=False
        )

# Обработка нажатий на кнопки тактик
async def tactic_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    tactics_info = {
        "tactic_lucky_jet": """⚡️ *Стратегии LUCKY JET*  
✔ Тактика x1.1 — минимальный риск, стабильный доход.  
✔ Стратегия Мартингейл — удваиваем ставку после проигрыша.  
✔ Система Даламбера — уменьшаем ставку при выигрыше, увеличиваем при проигрыше.  
✔ Тактика двух ставок — одна на x1.5, вторая вручную на x2+.  

🔗 [Играть в Lucky Jet](https://1wcneg.com/casino/list/4?p=fnfz)""",

        "tactic_mines": """💣 *Стратегии для MINES*  
✔ Мартингейл — удвоение ставки после проигрыша.  
✔ Flat — фиксированная ставка 7% от банка.  
✔ Grind — увеличиваем процент ставки при проигрыше.  
✔ 20 бомб — высокие риски, но и большие выигрыши.  

🔗 [Играть в Mines](https://1wcneg.com/casino/list/4?p=fnfz)""",

        "tactic_rocket_queen": """🚀 *Тактики для ROCKET QUEEN*  
✔ Минимальные коэффициенты — x1.2-1.5 для стабильности.  
✔ Две ставки: авто-вывод на x1.1 и ручная на x2.  
✔ Стратегия догона — удваивание при проигрыше.  

🔗 [Играть в Rocket Queen](https://1wcneg.com/casino/list/4?p=fnfz)"""
    }

    if query.data in tactics_info:
        keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="back_to_tactics")]]
        await query.edit_message_text(
            text=tactics_info[query.data],
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
            disable_web_page_preview=True
        )

# Кнопка "Назад" в тактиках
async def back_to_tactics(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🎯 LUCKY JET", callback_data="tactic_lucky_jet")],
        [InlineKeyboardButton("💣 MINES", callback_data="tactic_mines")],
        [InlineKeyboardButton("🚀 ROCKET QUEEN", callback_data="tactic_rocket_queen")],
    ]

    await query.edit_message_text(
        text="🎯 Выбери игру, для которой нужна тактика:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Обработка подписки и отписки
async def subscription_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "subscribe":
        message = "✅ Вы успешно подписались на рассылку!"
    elif query.data == "unsubscribe":
        message = "❌ Вы успешно отписались от рассылки!"

    await query.edit_message_text(message)

# Обработчик ошибок
async def error(update, context):
    logging.error(f"Ошибка: {context.error}")

# Настройка обработчиков
def setup_handlers(application):
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, inline_buttons))
    application.add_handler(CallbackQueryHandler(tactic_callback, pattern="^tactic_.*$"))
    application.add_handler(CallbackQueryHandler(back_to_tactics, pattern="^back_to_tactics$"))
    application.add_handler(CallbackQueryHandler(button_callback, pattern="^bonus_.*$"))
    application.add_handler(CallbackQueryHandler(subscription_callback, pattern="^(subscribe|unsubscribe)$"))
    application.add_error_handler(error)

# Основная функция
async def main():
    application = Application.builder().token(TOKEN).build()
    setup_handlers(application)
    await application.run_polling()

# Запуск бота
if __name__ == '__main__':
    import asyncio

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())