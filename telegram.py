from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext  # type: ignore

# Словарь с числами и их возможными следующими числами
numbers_dict = {
    "0": ["18", "23", "00", "5", "24", "13"],
    "1": ["13", "2", "00", "28", "21", "27"],
    "2": ["28", "35", "14", "27", "23", "3"],
    "3": ["30", "34", "15", "12", "27", "6"],
    "4": ["6", "8", "7", "11", "24", "35"],
    "5": ["30", "18", "24", "5", "25", "3"],
    "6": ["17", "18", "32", "9", "26", "16"],
    "7": ["11", "20", "10", "16", "12", "14"],
    "8": ["22", "11", "33", "15", "29", "34"],
    "9": ["27", "30", "6", "14", "26", "30"],
    "10": ["13", "15", "20", "30", "5", "25"],
    "11": ["22", "20", "7", "4", "35", "33"],
    "12": ["13", "00", "27", "16", "19", "3"],
    "13": ["27", "10", "36", "1", "25", "31"],
    "14": ["9", "16", "18", "34", "3", "12"],
    "15": ["35", "1", "00", "8", "22", "24"],
    "16": ["32", "14", "9", "7", "18", "19"],
    "17": ["32", "22", "5", "20", "6", "23"],
    "18": ["5", "17", "19", "36", "00", "1"],
    "19": ["34", "22", "23", "1", "00", "21"],
    "20": ["10", "22", "24", "33", "7", "30"],
    "21": ["22", "18", "20", "32", "12", "1"],
    "22": ["33", "11", "23", "31", "17", "6"],
    "23": ["32", "35", "33", "30", "9", "36"],
    "24": ["36", "35", "13", "22", "29", "4"],
    "25": ["5", "30", "32", "10", "36", "27"],
    "26": ["9", "35", "30", "4", "14", "35"],
    "27": ["2", "21", "7", "1", "10", "00"],
    "28": ["9", "8", "35", "1", "22", "2"],
    "29": ["12", "25", "14", "24", "22", "30"],
    "30": ["28", "35", "14", "27", "23", "3"],
    "31": ["23", "5", "20", "32", "27", "3"],
    "32": ["33", "28", "36", "22", "29", "13"],
    "33": ["21", "17", "5", "20", "1", "0"],
    "34": ["17", "15", "22", "19", "35", "14"],
    "35": ["4", "26", "31", "9", "26", "12"],
    "36": ["1", "24", "18", "13", "25", "10"],
    "00": ["19", "29", "32", "27", "8", "35"]
}

# Обработчик команды /start


async def start(update: Update, context: CallbackContext):
    # Создаем клавиатуру с числами
    keyboard = [
        [InlineKeyboardButton("0", callback_data="0")],
        [InlineKeyboardButton("00", callback_data="00")],
        *[[InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1 + j * 6, 7 + j * 6)] for j in range(6)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text("Выберите число:", reply_markup=reply_markup)

# Обработчик нажатия на кнопку


async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    user_choice = query.data

    # Проверяем, есть ли выбранное число в словаре
    if user_choice in numbers_dict:
        next_numbers = numbers_dict[user_choice]
        await query.edit_message_text(f"Следующие числа: {', '.join(next_numbers)}")
    else:
        await query.edit_message_text("Ошибка: число не найдено.")

    # Снова показываем клавиатуру для выбора следующего числа
    keyboard = [
        [InlineKeyboardButton("0", callback_data="0")],
        [InlineKeyboardButton("00", callback_data="00")],
        *[[InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1 + j * 6, 7 + j * 6)] for j in range(6)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Выберите число:", reply_markup=reply_markup)

# Основная функция для запуска бота


def main():
    # Укажите ваш токен
    token = "7877763853:AAH6Pr5Dtkr2GJ2fNwQbu5lEVYLQdCbjGhA"

    # Создаем приложение и добавляем обработчики
    application = Application.builder().token(token).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик нажатия на кнопку
    application.add_handler(CallbackQueryHandler(button_click))

    # Запускаем бота
    application.run_polling()


if __name__ == "__main__":
    main()
