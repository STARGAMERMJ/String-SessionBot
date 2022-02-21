from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Welcome {}

If you don't trust this bot, 
1) Don't read this message
2) Block bot or delete chat

This Bot Works To Help You Get Session String Via Bot, Recommendation If You Want To Retrieve String Use Another Account, So As Not To Delay
 
**Thank you**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("• Start Generating Session •", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("• Start Generating Session •", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("• Start Generating Session •", callback_data="generate")],
        [InlineKeyboardButton("🐱 Developer 🐱", url="https://t.me/tzypis")],
        [
            InlineKeyboardButton("Menu Bantuan ❔", callback_data="help"),
            InlineKeyboardButton("🤖 About 🤖", callback_data="about")
        ],
        [InlineKeyboardButton("• Info Project •", url="https://t.me/ApisProject")],
    ]

    # Help Message
    HELP = """
👇🏻 **Perintah yang tersedia** 👇🏻

/about - Tentang Bot ini
/help - Pesan ini
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan proses
/restart - Membatalkan proses
"""

    # About Message
    ABOUT = """
**Tentang Bot ini** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon String Session

Grup Support : [Userbot Telegram](https://t.me/UserbotTelegramSupport)

Kerangka : [Pyrogram](docs.pyrogram.org)

Bahasa : [Python](www.python.org)

Developer : @tzypis
    """
