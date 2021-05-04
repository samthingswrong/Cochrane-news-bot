import mysql
import re

import asyncio
from aiogram import Bot, Dispatcher, executor, types

import keyboards as kb
import parser as prs
from config import API_TOKEN, commands


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

db = mysql.Database("new_users.db")
news_parser = prs.NewsParser()


# Check for new post and send it to subscribers
async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)

        new_post = news_parser.get_new_post_key()
        if new_post != news_parser.get_last_post_key():
            post = news_parser.get_content()[0]
            kb.inline_button_link.url = post['article_link']
            subscriptions = db.get_users()
            for s in subscriptions:
                await bot.send_photo(s[0],
                                     post['img_link'],
                                     caption=post['short_description'].upper() + '\n' + post['publish_date'] + '\n',
                                     disable_notification=True,
                                     reply_markup=kb.inline_kb_link
                                     )
            news_parser.update_last_post_key(new_post)


@dp.message_handler(commands=['sub'])
async def subscribe(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    db.update_subscription(message.from_user.id, 1)
    await message.answer('You are subscribed. Wait for new events! 🤓')


@dp.message_handler(commands=['unsub'])
async def unsubscribe(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    db.update_subscription(message.from_user.id, 0)
    await message.answer('You are unsubscribed 😭')


@dp.message_handler(commands=['start'])
async def say_hi(message: types.Message):
    db.add_user(message.from_user.id, 0)
    await bot.send_message(message.from_user.id, 'Hello!', reply_markup=kb.greet_kb)


# Send latest News and Events
@dp.message_handler(commands=['news'])
async def send_news(message: types.Message):
    content = news_parser.get_content()
    for news in content:
        kb.inline_button_link.url = news['article_link']
        await bot.send_photo(message.from_user.id,
                             news['img_link'],
                             caption=news['short_description'].upper() + '\n' + news['publish_date'] + '\n',
                             disable_notification=True,
                             reply_markup=kb.inline_kb_link
                             )


# Send latest [1-8] News and Events
@dp.message_handler(commands=['top_news'])
async def send_top_news(message: types.Message):
    content = news_parser.get_content()
    numb = int(re.findall(r'\d', message.text)[0])
    for i in range(numb):
        news = content[i]
        kb.inline_button_link.url = news['article_link']
        await bot.send_photo(message.from_user.id,
                             news['img_link'],
                             caption=news['short_description'].upper() + '\n' + news['publish_date'] + '\n',
                             disable_notification=True,
                             reply_markup=kb.inline_kb_link
                             )


# Send latest [1-10] evidence
@dp.message_handler(commands=['top_evidence'])
async def send_top_evidence(message: types.Message):
    content = news_parser.get_evidence()
    numb = int(re.findall(r'\d\d?', message.text)[0])
    for i in range(numb):
        news = content[i]
        kb.inline_button_link.url = news['article_link']
        await bot.send_message(message.from_user.id,
                               text=news['short_description'].upper(),
                               disable_notification=True,
                               reply_markup=kb.inline_kb_link
                               )


# Open command list
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    msg = ''
    for command in commands:
        msg += command + '\n'
    await message.answer(msg)


# Report error or wrong command
@dp.message_handler()
async def unknown(message: types.Message):
    await message.answer("Type /help to open command list!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(1))
    executor.start_polling(dp, skip_updates=True)
