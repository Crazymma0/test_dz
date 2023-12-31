from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# async def start_kb():
#     quiz_button = KeyboardButton("/quiz")
#     mark_up = ReplyKeyboardMarkup(one_time_keyboard=True,
#                                   resize_keyboard=True)
#
#     mark_up.add(quiz_button)
#     return mark_up


async def quiz_1_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Следующая Викторина",
        callback_data="button_call_1"
    )
    markup.row(
        button_call_1
    )
    return markup


async def quiz_2_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Male",
        callback_data="answer_male"
    )
    button_call_2 = InlineKeyboardButton(
        "Female",
        callback_data="answer_female"
    )
    markup.row(
        button_call_1,
        button_call_2
    )
    return markup


async def admin_select_user_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list = InlineKeyboardButton(
        "Список пользователей",
        callback_data="admin_user_list"
    )

    markup.row(
        admin_user_list
    )
    return markup


async def new_start_kb():
    markup = InlineKeyboardMarkup()
    random_profiles_button = InlineKeyboardButton(
        "Анкеты для просмотра",
        callback_data="random_profiles"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )
    reference_button = InlineKeyboardButton(
        "Реферальная программа",
        callback_data="reference_menu"
    )
    parsing_button = InlineKeyboardButton(
        "Последние новости",
        callback_data="news_parsing"
    )
    markup.add(
        random_profiles_button
    ).add(
        my_profile_button

    ).add(
        reference_button
    ).add(
        parsing_button
    )
    return markup


async def like_dislike_profiles_keyboard(form_telegram_id):
    markup = InlineKeyboardMarkup(row_width=2)
    like_button = InlineKeyboardButton(
        "👍🏻",
        callback_data=f"like_{form_telegram_id}"
    )
    dislike_button = InlineKeyboardButton(
        "👎🏻",
        callback_data="random_profiles"
    )
    markup.row(
        like_button,
        dislike_button
    )
    return markup


async def my_profile_detail_keyboard(telegram_id):
    markup = InlineKeyboardMarkup(row_width=2)
    update_button = InlineKeyboardButton(
        "Изменить Анкету 💡",
        callback_data="signup"
    )
    delete_button = InlineKeyboardButton(
        "Удалить Анкету ❌",
        callback_data=f"delete_form"
    )
    markup.row(
        update_button,
        delete_button
    )
    return markup


async def my_profile_create_form_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    update_button = InlineKeyboardButton(
        "Registration 💡",
        callback_data="signup"
    )
    pass_button = InlineKeyboardButton(
        "Pass ❓",
        callback_data="pass_creation"
    )
    markup.row(
        update_button,
        pass_button
    )
    return markup


async def save_news_keyboard(url):
    markup = InlineKeyboardMarkup()
    print(url)
    save_button = InlineKeyboardButton(
        "Save 💡",
        callback_data=f"save_"
    )
    markup.row(
        save_button,
    )
    return markup