from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Создать ссылку 🔗",
        callback_data="reference_link_creation"
    )
    balance_button = InlineKeyboardButton(
        "Баланс 💵",
        callback_data="user_balance"
    )
    markup.add(
        link_button
    ).add(
        balance_button
    )
    return markup