from ast import Try
from datetime import datetime
from re import T
from tkinter import PhotoImage
import telebot
import time
from telebot import types
from flask import Flask, request
import os



API_KEY = '5710613073:AAGXeCjp48xycIxKGllcXUYISZ-ncFXmGy0' 
APP_URL = f'https://green-canyon-bot.herokuapp.com/'
bot = telebot.TeleBot(API_KEY)
server = Flask(__name__)



@bot.message_handler(['start', '⬅️Главная_страница'])
def start(message):
    markupButtons = types.ReplyKeyboardMarkup(one_time_keyboard=False, row_width=3)
    item1 = types.KeyboardButton('/Номера🚪')
    item2 = types.KeyboardButton('/Тарифы🏷️')
    item3 = types.KeyboardButton('/Удобства_и_услуги')
    item4 = types.KeyboardButton('/Меню🍔')
    item5 = types.KeyboardButton('/Виды_Green_Canyon🏔️')
    item6 = types.KeyboardButton('/Мероприятия🎤')
    item7 = types.KeyboardButton('/Местоположение📍')
    markupButtons.add(item7, item1, item2, item3, item4, item5, item6)
    msg = bot.reply_to(message, 'hello, choose one:', reply_markup=markupButtons)

@bot.message_handler(['Местоположение📍'])
def location(message):
     bot.reply_to(message, 'https://www.google.com/maps/place/Green+Canyon/@41.5841401,70.0906515,16.22z/data=!4m8!3m7!1s0x38af6d773da04853:0xbc7ef48a43a381a5!5m2!4m1!1i2!8m2!3d41.5847837!4d70.0905612')

@bot.message_handler(['Номера🚪'])
def rooms(message):
     markupButtons = types.ReplyKeyboardMarkup(one_time_keyboard=False, row_width=2)
     item1 = types.KeyboardButton('/Стандарты🚪')
     item2 = types.KeyboardButton('/Полу-люксы🚪')
     item3 = types.KeyboardButton('/Люксы🚪')
     item4 = types.KeyboardButton('/Семейные🚪')
     item5 = types.KeyboardButton('/⬅️Главная_страница')
     markupButtons.add(item1, item2, item3, item4, item5)
     msg = bot.reply_to(message, 'Номера:', reply_markup=markupButtons)

@bot.message_handler(['Стандарты🚪'])
def standart(message):
     markupButtons = types.ReplyKeyboardMarkup(one_time_keyboard=False, row_width=3)
     item1 = types.KeyboardButton('/№3')
     item2 = types.KeyboardButton('/№6')
     item3 = types.KeyboardButton('/№9')
     item4 = types.KeyboardButton('/№11')
     item5 = types.KeyboardButton('/№15')
     item6 = types.KeyboardButton('/⬅️Главная_страница')
     markupButtons.add(item1, item2, item3, item4, item5, item6)
     msg = bot.reply_to(message, 'Номера:', reply_markup=markupButtons)

@bot.message_handler(['Полу-люксы🚪'])
def semi_suits(message):
     markupButtons = types.ReplyKeyboardMarkup(one_time_keyboard=False, row_width=1)
     item1 = types.KeyboardButton('/№14')
     item2 = types.KeyboardButton('/№16')
     item3 = types.KeyboardButton('/№17')
     item4 = types.KeyboardButton('/⬅️Главная_страница')
     markupButtons.add(item1, item2, item3, item4)
     msg = bot.reply_to(message, 'Номера:', reply_markup=markupButtons)

@bot.message_handler(['Люксы🚪'])
def suits(message):
     markupButtons = types.ReplyKeyboardMarkup(one_time_keyboard=False, row_width=4)
     item1 = types.KeyboardButton('/№1')
     item2 = types.KeyboardButton('/№2')
     item3 = types.KeyboardButton('/№4')
     item4 = types.KeyboardButton('/№5')
     item5 = types.KeyboardButton('/№7')
     item6 = types.KeyboardButton('/№8')
     item7 = types.KeyboardButton('/№10')
     item8 = types.KeyboardButton('/⬅️Главная_страница')
     markupButtons.add(item1, item2, item3, item4, item5, item6, item7, item8)
     msg = bot.reply_to(message, 'Номера:', reply_markup=markupButtons)


@bot.message_handler(['№1'])
def room1(message):
    chatId = message.chat.id
    a = open(r'Rooms\room #1\a.jpg', 'rb')
    a1 = open(r'Rooms\room #1\a1.jpg', 'rb')
    a2 = open(r'Rooms\room #1\a2.jpg', 'rb')
    a3 = open(r'Rooms\room #1\a3.jpg', 'rb')
    a4 = open(r'Rooms\room #1\a4.jpg', 'rb')
    a5 = open(r'Rooms\room #1\a5.jpg', 'rb')
    a6 = open(r'Rooms\room #1\a6.jpg', 'rb')
    a7 = open(r'Rooms\room #1\a7.jpg', 'rb')
    a8 = open(r'Rooms\room #1\a8.jpg', 'rb')
    bot.send_photo(chatId, a)
    bot.send_photo(chatId, a1)
    bot.send_photo(chatId, a2)
    bot.send_photo(chatId, a3)
    bot.send_photo(chatId, a4)
    bot.send_photo(chatId, a5)
    bot.send_photo(chatId, a6)
    bot.send_photo(chatId, a7)
    bot.send_photo(chatId, a8)

@bot.message_handler(['№2'])
def room2(message):
    chatId = message.chat.id
    b = open(r'Rooms\room #2\b.jpg', 'rb')
    b1 = open(r'Rooms\room #2\b1.jpg', 'rb')
    b2 = open(r'Rooms\room #2\b2.jpg', 'rb')
    b3 = open(r'Rooms\room #2\b3.jpg', 'rb')
    b4 = open(r'Rooms\room #2\b4.jpg', 'rb')
    b5 = open(r'Rooms\room #2\b5.jpg', 'rb')
    b6 = open(r'Rooms\room #2\b6.jpg', 'rb')
    b7 = open(r'Rooms\room #2\b7.jpg', 'rb')
    b8 = open(r'Rooms\room #2\b8.jpg', 'rb')
    b9 = open(r'Rooms\room #2\b9.jpg', 'rb')
    bot.send_photo(chatId, b)
    bot.send_photo(chatId, b1)
    bot.send_photo(chatId, b2)
    bot.send_photo(chatId, b3)
    bot.send_photo(chatId, b4)
    bot.send_photo(chatId, b5)
    bot.send_photo(chatId, b6)
    bot.send_photo(chatId, b7)
    bot.send_photo(chatId, b8)
    bot.send_photo(chatId, b9)

@bot.message_handler(['№3'])
def room3(message):
    chatId = message.chat.id
    c = open(r'Rooms\room #3\c.jpg', 'rb')
    c1 = open(r'Rooms\room #3\c1.jpg', 'rb')
    c2 = open(r'Rooms\room #3\c2.jpg', 'rb')
    c3 = open(r'Rooms\room #3\c3.jpg', 'rb')
    c4 = open(r'Rooms\room #3\c4.jpg', 'rb')
    c5 = open(r'Rooms\room #3\c5.jpg', 'rb')
    bot.send_photo(chatId, c)
    bot.send_photo(chatId, c1)
    bot.send_photo(chatId, c2)
    bot.send_photo(chatId, c3)
    bot.send_photo(chatId, c4)
    bot.send_photo(chatId, c5)

@bot.message_handler(['№4'])
def room4(message):
    chatId = message.chat.id
    d = open(r'Rooms\room #4\d.jpg', 'rb')
    d1  = open(r'Rooms\room #4\d1.jpg', 'rb')
    d2  = open(r'Rooms\room #4\d2.jpg', 'rb')
    d3  = open(r'Rooms\room #4\d3.jpg', 'rb')
    d4  = open(r'Rooms\room #4\d4.jpg', 'rb')
    d5  = open(r'Rooms\room #4\d5.jpg', 'rb')
    d6  = open(r'Rooms\room #4\d6.jpg', 'rb')
    d7  = open(r'Rooms\room #4\d7.jpg', 'rb')
    d8  = open(r'Rooms\room #4\d8.jpg', 'rb')
    bot.send_photo(chatId, d)
    bot.send_photo(chatId, d1)
    bot.send_photo(chatId, d2)
    bot.send_photo(chatId, d3)
    bot.send_photo(chatId, d4)
    bot.send_photo(chatId, d5)
    bot.send_photo(chatId, d6)
    bot.send_photo(chatId, d7)
    bot.send_photo(chatId, d8)

@bot.message_handler(['№5'])
def room5(message):
    chatId = message.chat.id
    e = open(r'Rooms\room #5\e.jpg', 'rb')
    e1 = open(r'Rooms\room #5\e1.jpg', 'rb')
    e2 = open(r'Rooms\room #5\e2.jpg', 'rb')
    e3 = open(r'Rooms\room #5\e3.jpg', 'rb')
    e4 = open(r'Rooms\room #5\e4.jpg', 'rb')
    e5 = open(r'Rooms\room #5\e5.jpg', 'rb')
    e6 = open(r'Rooms\room #5\e6.jpg', 'rb')
    e7 = open(r'Rooms\room #5\e7.jpg', 'rb')
    e8 = open(r'Rooms\room #5\e8.jpg', 'rb')
    bot.send_photo(chatId, e)
    bot.send_photo(chatId, e1)
    bot.send_photo(chatId, e2)
    bot.send_photo(chatId, e3)
    bot.send_photo(chatId, e4)
    bot.send_photo(chatId, e5)
    bot.send_photo(chatId, e6)
    bot.send_photo(chatId, e7)
    bot.send_photo(chatId, e8)

@bot.message_handler(['№6'])
def room6(message):
    chatId = message.chat.id
    f = open(r'Rooms\room #6\f.jpg', 'rb')
    f1 = open(r'Rooms\room #6\f1.jpg', 'rb')
    f2 = open(r'Rooms\room #6\f2.jpg', 'rb')
    f3 = open(r'Rooms\room #6\f3.jpg', 'rb')
    f4 = open(r'Rooms\room #6\f4.jpg', 'rb')
    f5 = open(r'Rooms\room #6\f5.jpg', 'rb')
    bot.send_photo(chatId, f)
    bot.send_photo(chatId, f1)
    bot.send_photo(chatId, f2)
    bot.send_photo(chatId, f3)
    bot.send_photo(chatId, f4)
    bot.send_photo(chatId, f5)

@bot.message_handler(['№7'])
def room7(message):
    chatId = message.chat.id
    g = open(r'Rooms\room #7\g.jpg', 'rb')
    g1 = open(r'Rooms\room #7\g1.jpg', 'rb')
    g2 = open(r'Rooms\room #7\g2.jpg', 'rb')
    g3 = open(r'Rooms\room #7\g3.jpg', 'rb')
    g4 = open(r'Rooms\room #7\g4.jpg', 'rb')
    g5 = open(r'Rooms\room #7\g5.jpg', 'rb')
    g6 = open(r'Rooms\room #7\g6.jpg', 'rb')
    g7 = open(r'Rooms\room #7\g7.jpg', 'rb')
    g8 = open(r'Rooms\room #7\g8.jpg', 'rb')
    g9 = open(r'Rooms\room #7\g9.jpg', 'rb')
    bot.send_photo(chatId, g)
    bot.send_photo(chatId, g1)
    bot.send_photo(chatId, g2)
    bot.send_photo(chatId, g3)
    bot.send_photo(chatId, g4)
    bot.send_photo(chatId, g5)
    bot.send_photo(chatId, g6)
    bot.send_photo(chatId, g7)
    bot.send_photo(chatId, g8)
    bot.send_photo(chatId, g9)

@bot.message_handler(['№8'])
def room8(message):
    chatId = message.chat.id
    h = open(r'Rooms\room #8\h.jpg', 'rb')
    h1 = open(r'Rooms\room #8\h1.jpg', 'rb')
    h2 = open(r'Rooms\room #8\h2.jpg', 'rb')
    h3 = open(r'Rooms\room #8\h3.jpg', 'rb')
    h4 = open(r'Rooms\room #8\h4.jpg', 'rb')
    h5 = open(r'Rooms\room #8\h5.jpg', 'rb')
    h6 = open(r'Rooms\room #8\h6.jpg', 'rb')
    h7 = open(r'Rooms\room #8\h7.jpg', 'rb')
    bot.send_photo(chatId, h)
    bot.send_photo(chatId, h1)
    bot.send_photo(chatId, h2)
    bot.send_photo(chatId, h3)
    bot.send_photo(chatId, h4)
    bot.send_photo(chatId, h5)
    bot.send_photo(chatId, h6)
    bot.send_photo(chatId, h7)

@bot.message_handler(['№9'])
def room9(message):
    chatId = message.chat.id
    i = open(r'Rooms\room #9\i.jpg', 'rb')
    i1 = open(r'Rooms\room #9\i1.jpg', 'rb')
    i2 = open(r'Rooms\room #9\i2.jpg', 'rb')
    i3 = open(r'Rooms\room #9\i3.jpg', 'rb')
    i4 = open(r'Rooms\room #9\i4.jpg', 'rb')
    i5 = open(r'Rooms\room #9\i5.jpg', 'rb')
    bot.send_photo(chatId, i)
    bot.send_photo(chatId, i1)
    bot.send_photo(chatId, i2)
    bot.send_photo(chatId, i3)
    bot.send_photo(chatId, i4)
    bot.send_photo(chatId, i5)


@bot.message_handler(['№10'])
def room10(message):
    chatId = message.chat.id
    j = open(r'Rooms\room #10\j.jpg', 'rb')
    j1 = open(r'Rooms\room #10\j1.jpg', 'rb')
    j2 = open(r'Rooms\room #10\j2.jpg', 'rb')
    j3 = open(r'Rooms\room #10\j3.jpg', 'rb')
    j4 = open(r'Rooms\room #10\j4.jpg', 'rb')
    j5 = open(r'Rooms\room #10\j5.jpg', 'rb')
    j6 = open(r'Rooms\room #10\j6.jpg', 'rb')
    j7 = open(r'Rooms\room #10\j7.jpg', 'rb')
    j8 = open(r'Rooms\room #10\j8.jpg', 'rb')
    j9 = open(r'Rooms\room #10\j9.jpg', 'rb')
    bot.send_photo(chatId, j)
    bot.send_photo(chatId, j1)
    bot.send_photo(chatId, j2)
    bot.send_photo(chatId, j3)
    bot.send_photo(chatId, j4)
    bot.send_photo(chatId, j5)
    bot.send_photo(chatId, j6)
    bot.send_photo(chatId, j7)
    bot.send_photo(chatId, j8)
    bot.send_photo(chatId, j9)

@bot.message_handler(['№11'])
def room11(message):
    chatId = message.chat.id
    k = open(r'Rooms\room #11\k.jpg', 'rb')
    k1 = open(r'Rooms\room #11\k1.jpg', 'rb')
    k2 = open(r'Rooms\room #11\k2.jpg', 'rb')
    k3 = open(r'Rooms\room #11\k3.jpg', 'rb')
    k4 = open(r'Rooms\room #11\k4.jpg', 'rb')
    k5 = open(r'Rooms\room #11\k5.jpg', 'rb')
    bot.send_photo(chatId, k)
    bot.send_photo(chatId, k1)
    bot.send_photo(chatId, k2)
    bot.send_photo(chatId, k3)
    bot.send_photo(chatId, k4)
    bot.send_photo(chatId, k5)

@bot.message_handler(['№12'])
def room12(message):
    chatId = message.chat.id
    l = open(r'Rooms\room #12\l.jpg', 'rb')
    l1 = open(r'Rooms\room #12\l1.jpg', 'rb')
    l2 = open(r'Rooms\room #12\l2.jpg', 'rb')
    l3 = open(r'Rooms\room #12\l3.jpg', 'rb')
    l4 = open(r'Rooms\room #12\l4.jpg', 'rb')
    l5 = open(r'Rooms\room #12\l5.jpg', 'rb')
    l6 = open(r'Rooms\room #12\l6.jpg', 'rb')
    l7 = open(r'Rooms\room #12\l7.jpg', 'rb')
    bot.send_photo(chatId, l)
    bot.send_photo(chatId, l1)
    bot.send_photo(chatId, l2)
    bot.send_photo(chatId, l3)
    bot.send_photo(chatId, l4)
    bot.send_photo(chatId, l5)
    bot.send_photo(chatId, l6)
    bot.send_photo(chatId, l7)



@bot.message_handler(['№13'])
def room13(message):
    chatId = message.chat.id
    m = open(r'Rooms\room #13\m.jpg', 'rb')
    m1 = open(r'Rooms\room #13\m1.jpg', 'rb')
    m2 = open(r'Rooms\room #13\m2.jpg', 'rb')
    m3 = open(r'Rooms\room #13\m3.jpg', 'rb')
    m4 = open(r'Rooms\room #13\m4.jpg', 'rb')
    m5 = open(r'Rooms\room #13\m5.jpg', 'rb')
    m6 = open(r'Rooms\room #13\m6.jpg', 'rb')
    m7 = open(r'Rooms\room #13\m7.jpg', 'rb')
    m8 = open(r'Rooms\room #13\m8.jpg', 'rb')
    m9 = open(r'Rooms\room #13\m9.jpg', 'rb')
    bot.send_photo(chatId, m)
    bot.send_photo(chatId, m1)
    bot.send_photo(chatId, m2)
    bot.send_photo(chatId, m3)
    bot.send_photo(chatId, m4)
    bot.send_photo(chatId, m5)
    bot.send_photo(chatId, m6)
    bot.send_photo(chatId, m7)
    bot.send_photo(chatId, m8)
    bot.send_photo(chatId, m9)

@bot.message_handler(['№14'])
def room14(message):
    chatId = message.chat.id
    n = open(r'Rooms\room #14\n.jpg', 'rb')
    n1 = open(r'Rooms\room #14\n1.jpg', 'rb')
    n2 = open(r'Rooms\room #14\n2.jpg', 'rb')
    n3 = open(r'Rooms\room #14\n3.jpg', 'rb')
    n4 = open(r'Rooms\room #14\n4.jpg', 'rb')
    n5 = open(r'Rooms\room #14\n5.jpg', 'rb')
    bot.send_photo(chatId, n)
    bot.send_photo(chatId, n1)
    bot.send_photo(chatId, n2)
    bot.send_photo(chatId, n3)
    bot.send_photo(chatId, n4)
    bot.send_photo(chatId, n5)

@bot.message_handler(['№15'])
def room15(message):
    chatId = message.chat.id
    o = open(r'Rooms\room #15\o.jpg', 'rb')
    o1 = open(r'Rooms\room #15\o1.jpg', 'rb')
    o2 = open(r'Rooms\room #15\o2.jpg', 'rb')
    o3 = open(r'Rooms\room #15\o3.jpg', 'rb')
    o4 = open(r'Rooms\room #15\o4.jpg', 'rb')
    o5 = open(r'Rooms\room #15\o5.jpg', 'rb')
    bot.send_photo(chatId, o)
    bot.send_photo(chatId, o1)
    bot.send_photo(chatId, o2)
    bot.send_photo(chatId, o3)
    bot.send_photo(chatId, o4)
    bot.send_photo(chatId, o5)

@bot.message_handler(['№16'])
def room16(message):
    chatId = message.chat.id
    p = open(r'Rooms\room #16\p.jpg', 'rb')
    p1 = open(r'Rooms\room #16\p1.jpg', 'rb')
    p2 = open(r'Rooms\room #16\p2.jpg', 'rb')
    p3 = open(r'Rooms\room #16\p3.jpg', 'rb')
    p4 = open(r'Rooms\room #16\p4.jpg', 'rb')
    p5 = open(r'Rooms\room #16\p5.jpg', 'rb')
    bot.send_photo(chatId, p)
    bot.send_photo(chatId, p1)
    bot.send_photo(chatId, p2)
    bot.send_photo(chatId, p3)
    bot.send_photo(chatId, p4)
    bot.send_photo(chatId, p5)

@bot.message_handler(['№17'])
def room17(message):
    chatId = message.chat.id
    q = open(r'Rooms\room #17\q.jpg', 'rb')
    q1 = open(r'Rooms\room #17\q1.jpg', 'rb')
    q2 = open(r'Rooms\room #17\q2.jpg', 'rb')
    q3 = open(r'Rooms\room #17\q3.jpg', 'rb')
    q4 = open(r'Rooms\room #17\q4.jpg', 'rb')
    q5 = open(r'Rooms\room #17\q5.jpg', 'rb')
    bot.send_photo(chatId, q)
    bot.send_photo(chatId, q1)
    bot.send_photo(chatId, q2)
    bot.send_photo(chatId, q3)
    bot.send_photo(chatId, q4)
    bot.send_photo(chatId, q5)

@bot.message_handler(['Удобства_и_услуги'])
def facilities(message):
     chatId = message.chat.id
     u = open(r'facilities\pools\pool.jpg', 'rb')
     u1 = open(r'facilities\pools\pool2.jpg', 'rb')
     u2 = open(r'facilities\pools\pool3.jpg', 'rb')
     u3 = open(r'facilities\pools\pool4.jpg', 'rb')
     u4 = open(r'facilities\pools\pool5.jpg', 'rb')    
     bot.send_photo(chatId, u)
     bot.send_photo(chatId, u1)
     bot.send_photo(chatId, u2)
     bot.send_photo(chatId, u3)
     bot.send_photo(chatId, u4)
     v = open(r'facilities\sauna&hammam\sauna.jpg', 'rb')
     bot.send_photo(chatId, v)
     w = open(r'facilities\sauna&hammam\hammam.jpg', 'rb')
     bot.send_photo(chatId, w)
     x = open(r'facilities\playgrounds\play1.jpg', 'rb')
     x1 = open(r'facilities\playgrounds\play2.jpg', 'rb')
     x3 = open(r'facilities\playgrounds\play4.jpg', 'rb')
     bot.send_photo(chatId, x)
     bot.send_photo(chatId, x1)
     bot.send_photo(chatId, x3)
     x2 = open(r'facilities\playgrounds\play3.jpg', 'rb')
     bot.send_photo(chatId, x2)
     y = open(r'facilities\topchan\topchan.jpg', 'rb')
     bot.send_photo(chatId, y)


@bot.message_handler(['Тарифы🏷️'])
def tarifs(message):
     chatId = message.chat.id
     z = open(r'tarif\tarif.jpg', 'rb')
     bot.send_photo(chatId, z)

@bot.message_handler(['Семейные🚪'])
def family_rooms(message):
     markupButtons = types.ReplyKeyboardMarkup(one_time_keyboard=False, row_width=1)
     item1 = types.KeyboardButton('/№12')
     item2 = types.KeyboardButton('/№13')
     item3 = types.KeyboardButton('/⬅️Главная_страница')
     markupButtons.add(item1, item2, item3)
     msg = bot.reply_to(message, 'Номера:', reply_markup=markupButtons)

@bot.message_handler(['Меню🍔'])
def menu(message):
     chatId = message.chat.id
     xy = open(r'menu\me1.jpg', 'rb')
     xy1 = open(r'menu\me2.jpg', 'rb')
     xy2 = open(r'menu\me3.jpg', 'rb')
     xy3 = open(r'menu\me4.jpg', 'rb')
     xy4 = open(r'menu\me5.jpg', 'rb')
     xy5 = open(r'menu\me6.jpg', 'rb')
     xy6 = open(r'menu\me7.jpg', 'rb')
     xy7 = open(r'menu\me8.jpg', 'rb')
     bot.send_photo(chatId, xy)
     bot.send_photo(chatId, xy1)
     bot.send_photo(chatId, xy2)
     bot.send_photo(chatId, xy3)
     bot.send_photo(chatId, xy4)
     bot.send_photo(chatId, xy5)
     bot.send_photo(chatId, xy6)
     bot.send_photo(chatId, xy7)

@bot.message_handler(['Мероприятия🎤'])
def events(message):
    chatId = message.chat.id
    ev1 = open(r'events\ev1.jpg', 'rb')
    ev2 = open(r'events\ev2.jpg', 'rb')
    ev3 = open(r'events\ev3.jpg', 'rb')
    ev4 = open(r'events\ev4.jpg', 'rb')
    ev5 = open(r'events\ev5.jpg', 'rb')
    ev6 = open(r'events\ev6.jpg', 'rb')
    ev7 = open(r'events\ev7.jpg', 'rb')
    ev8 = open(r'events\ev8.jpg', 'rb')
    ev9 = open(r'events\ev9.jpg', 'rb')
    bot.send_photo(chatId, ev1)
    bot.send_photo(chatId, ev2)
    bot.send_photo(chatId, ev3)
    bot.send_photo(chatId, ev4)
    bot.send_photo(chatId, ev5)
    bot.send_photo(chatId, ev6)
    bot.send_photo(chatId, ev7)
    bot.send_photo(chatId, ev8)
    bot.send_photo(chatId, ev9)

@bot.message_handler(['Виды_Green_Canyon🏔️'])
def views(message):
     chatId = message.chat.id
     ve = open(r'views\ve1.jpg', 'rb')
     ve1 = open(r'views\ve2.jpg', 'rb')
     ve2 = open(r'views\ve3.jpg', 'rb')
     ve3 = open(r'views\ve4.jpg', 'rb')
     ve4 = open(r'views\ve5.jpg', 'rb')
     ve5 = open(r'views\ve6.jpg', 'rb')
     ve6 = open(r'views\ve7.jpg', 'rb')
     ve7 = open(r'views\ve8.jpg', 'rb')
     ve8 = open(r'views\ve9.jpg', 'rb')
     ve9 = open(r'views\ve10.jpg', 'rb')
     ve10 = open(r'views\ve11.jpg', 'rb')
     ve11 = open(r'views\ve12.jpg', 'rb')
     ve12 = open(r'views\ve13.jpg', 'rb')
     ve13 = open(r'views\ve14.jpg', 'rb')
     ve14 = open(r'views\ve15.jpg', 'rb')
     bot.send_photo(chatId, ve)
     bot.send_photo(chatId, ve1)
     bot.send_photo(chatId, ve2)
     bot.send_photo(chatId, ve3)
     bot.send_photo(chatId, ve4)
     bot.send_photo(chatId, ve5)
     bot.send_photo(chatId, ve6)
     bot.send_photo(chatId, ve7)
     bot.send_photo(chatId, ve8)
     bot.send_photo(chatId, ve9)
     bot.send_photo(chatId, ve10)
     bot.send_photo(chatId, ve11)
     bot.send_photo(chatId, ve12)
     bot.send_photo(chatId, ve13)
     bot.send_photo(chatId, ve14)


@server.route('/' + API_KEY, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
