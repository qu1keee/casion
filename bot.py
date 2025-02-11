import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7877763853:AAH6Pr5Dtkr2GJ2fNwQbu5lEVYLQdCbjGhA"

data = {
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

bot = Bot(token=TOKEN)
dp = Dispatcher()

def generate_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=str(i)) for i in range(j, j+6) if i <= 36] 
            for j in range(0, 37, 6)
        ] + [[KeyboardButton(text="00")]],
        resize_keyboard=True
    )
    return keyboard


@dp.message(lambda message: message.text in data)
async def send_numbers(message: types.Message):
    chosen_number = message.text
    response_numbers = ", ".join(data[chosen_number])
    await message.answer(f"Ваши числа: {response_numbers}", reply_markup=generate_keyboard())

@dp.message()
async def unknown_message(message: types.Message):
    await message.answer("Выберите число с клавиатуры", reply_markup=generate_keyboard())

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
