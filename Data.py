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
        [InlineKeyboardButton("🐱 Developer 🐱", url="https://t.me/STARGAMERMJ")],
        [
            InlineKeyboardButton("Help Menu ❔", callback_data="help"),
            InlineKeyboardButton("🤖 About 🤖", callback_data="about")
        ],
        [InlineKeyboardButton("• Info Project •", url="https://t.me/scripthelperbots")],
    ]

    # Help Message
    HELP = """
👇🏻 **Available commands** 👇🏻

/about - About this Bot
/help - This message
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancel process
/restart - Cancel process
"""

    # About Message
    ABOUT = """
**About this Bot** 

A telegram bot to retrieve String Session pyrograms and telethons

Grup Support : [Userbot Telegram](https://t.me/scripthelper360)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @STARGAMERMJ
    """
