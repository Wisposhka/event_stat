import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def pandas_test():
    cnx = sqlite3.connect('games_tabl')
    df = pd.read_sql_query("SELECT * FROM useful", cnx)
    return df


df = pandas_test()
df['game_4'] = df['game_4'].astype(int)
df['game_5'] = df['game_5'].astype(int)
df['game_6'] = df['game_6'].astype(int)
kda = (round(df['game_4'].sum() / df['game_5'].sum(), 2))
uron = (round(df['game_6'].sum()/ df['game_6'].count(), 1))

# Улучшить по возможности
armor1 = df.game_7.loc[(df['game_7'] == 'Боевая') & (df['game_3'] == 'Победа')].count() - df.game_7.loc[
    (df['game_7'] == 'Боевая') & (df['game_3'] == 'Поражение')].count()
armor2 = df.game_7.loc[(df['game_7'] == 'Пакетик') & (df['game_3'] == 'Победа')].count() - df.game_7.loc[
    (df['game_7'] == 'Пакетик') & (df['game_3'] == 'Поражение')].count()
armor3 = df.game_7.loc[(df['game_7'] == 'АО') & (df['game_3'] == 'Победа')].count() - df.game_7.loc[
    (df['game_7'] == 'АО') & (df['game_3'] == 'Поражение')].count()
armor4 = df.game_7.loc[(df['game_7'] == 'Зверобой') & (df['game_3'] == 'Победа')].count() - df.game_7.loc[
    (df['game_7'] == 'Зверобой') & (df['game_3'] == 'Поражение')].count()

Best_armor = ''

if armor1 > armor2 and armor1 > armor3 and armor1 > armor4:  # Улучшить по возможности
    Best_armor = 'Боевая'
else:
    if armor2 > armor3 and armor2 > armor4:
        Best_armor = 'Пакетик'
    else:
        if armor3 > armor4:
            Best_armor = 'АО'
        else:
            Best_armor = 'Зверобой'

kda_armor = round(df.game_4.loc[df['game_7'] == Best_armor].sum() / df.game_5.loc[df['game_7'] == Best_armor].sum(), 2)
# print(kda_armor)

# Улучшить по возможности
weapon1 = df.game_8.loc[(df['game_8'] == 'Печенег') & (df['game_3'] == 'Победа')].count() - df.game_8.loc[
    (df['game_8'] == 'Печенег') & (df['game_3'] == 'Поражение')].count()
weapon2 = df.game_8.loc[(df['game_8'] == 'Вал') & (df['game_3'] == 'Победа')].count() - df.game_8.loc[
    (df['game_8'] == 'Вал') & (df['game_3'] == 'Поражение')].count()
weapon3 = df.game_8.loc[(df['game_8'] == 'Сайга') & (df['game_3'] == 'Победа')].count() - df.game_8.loc[
    (df['game_8'] == 'Сайга') & (df['game_3'] == 'Поражение')].count()
weapon4 = df.game_8.loc[(df['game_8'] == 'Аек') & (df['game_3'] == 'Победа')].count() - df.game_8.loc[
    (df['game_8'] == 'Аек') & (df['game_3'] == 'Поражение')].count()
weapon5 = df.game_8.loc[(df['game_8'] == 'Вектор') & (df['game_3'] == 'Победа')].count() - df.game_8.loc[
    (df['game_8'] == 'Вектор') & (df['game_3'] == 'Поражение')].count()
weapon6 = df.game_8.loc[(df['game_8'] == 'ФН') & (df['game_3'] == 'Победа')].count() - df.game_8.loc[
    (df['game_8'] == 'ФН') & (df['game_3'] == 'Поражение')].count()
# print(weapon1, weapon2, weapon3, weapon4, weapon5, weapon6)
Best_weapon = ' '

if weapon1 > weapon2 and weapon1 > weapon3 and weapon1 > weapon4 and weapon1 > weapon5 and weapon1 > weapon6:  # Улучшить по возможности
    Best_weapon = 'Печенег'
else:
    if weapon2 > weapon3 and weapon2 > weapon4 and weapon2 > weapon5 and weapon2 > weapon6:
        Best_weapon = 'Вал'
    else:
        if weapon3 > weapon4 and weapon3 > weapon5 and weapon3 > weapon6:
            Best_weapon = 'Сайга'
        else:
            if weapon4 > weapon5 and weapon4 > weapon6:
                Best_weapon = 'Аек'
            else:
                if weapon5 > weapon6:
                    Best_weapon = 'Вектор'
                else:
                    Best_weapon = 'ФН'

kda_weapon = round(df.game_4.loc[df['game_8'] == Best_weapon].sum() / df.game_5.loc[df['game_8'] == Best_weapon].sum(), 2)


def show_winrate():
    df = pandas_test()
    win = (df.game_3.loc[df['game_3'] == 'Победа'].count())
    lose = (df.game_3.loc[df['game_3'] == 'Поражение'].count())
    data = {'Category': ['Победа', 'Поражение'],
            'Value': [win, lose]}
    for_circle = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.pie(for_circle['Value'], labels=for_circle['Category'], startangle=90, counterclock=False, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Винрейт')
    plt.show()


def show_armor():
    df = pandas_test()
    a1 = (df.game_7.loc[df['game_7'] == 'Пакетик'].count())
    a2 = (df.game_7.loc[df['game_7'] == 'Боевая'].count())
    a3 = (df.game_7.loc[df['game_7'] == 'АО'].count())
    a4 = (df.game_7.loc[df['game_7'] == 'Зверобой'].count())
    data = {'Category': ['Пакетик', 'Боевая', 'АО', 'Зверобой'],
            'Value': [a1, a2, a3, a4]}
    for_circle = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.pie(for_circle['Value'], labels=for_circle['Category'], startangle=50, counterclock=False, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Выбор брони')
    plt.show()


def show_weapon():
    df = pandas_test()
    w1 = (df.game_8.loc[df['game_8'] == 'Печенег'].count())
    w2 = (df.game_8.loc[df['game_8'] == 'Вал'].count())
    w3 = (df.game_8.loc[df['game_8'] == 'Сайга'].count())
    w4 = (df.game_8.loc[df['game_8'] == 'Аек'].count())
    w5 = (df.game_8.loc[df['game_8'] == 'Вектор'].count())
    w6 = (df.game_8.loc[df['game_8'] == 'ФН'].count())
    data = {'Category': ['Печенег', 'Вал', 'Сайга', 'Аек', 'Вектор', 'ФН'],
            'Value': [w1, w2, w3, w4, w5, w6]}
    for_circle = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.pie(for_circle['Value'], labels=for_circle['Category'], startangle=50, counterclock=False, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Выбор оружия')
    plt.show()


def show_team():
    df = pandas_test()
    t1 = (df.game_10.loc[df['game_10'] == 'АОшки'].count())
    t2 = (df.game_10.loc[df['game_10'] == 'Пакеты'].count())
    t3 = (df.game_10.loc[df['game_10'] == 'Боевые'].count())
    t4 = (df.game_10.loc[df['game_10'] == 'Зверобои'].count())
    t5 = (df.game_10.loc[df['game_10'] == 'Баланс'].count())

    data = {'Category': ['АОшки', 'Пакеты', 'Боевые', 'Зверобои', 'Баланс'],
            'Value': [t1, t2, t3, t4, t5]}
    for_circle = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.pie(for_circle['Value'], labels=for_circle['Category'], startangle=50, counterclock=False, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Что выбирает твоя командка')
    plt.show()


def show_enemy():
    df = pandas_test()
    e1 = (df.game_11.loc[df['game_11'] == 'АОшки'].count())
    e2 = (df.game_11.loc[df['game_11'] == 'Пакеты'].count())
    e3 = (df.game_11.loc[df['game_11'] == 'Боевые'].count())
    e4 = (df.game_11.loc[df['game_11'] == 'Зверобои'].count())
    e5 = (df.game_11.loc[df['game_11'] == 'Баланс'].count())

    data = {'Category': ['АОшки', 'Пакеты', 'Боевые', 'Зверобои', 'Баланс'],
            'Value': [e1, e2, e3, e4, e5]}
    for_circle = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.pie(for_circle['Value'], labels=for_circle['Category'], startangle=50, counterclock=False, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Выбор противников')
    plt.show()

def show_side():
    df = pandas_test()
    s1 = (df.game_12.loc[df['game_12'] == 'Санитары'].count())
    s2 = (df.game_12.loc[df['game_12'] == 'Блаженные'].count())

    data = {'Category': ['Санитары', 'Блаженные'],
            'Value': [s1, s2]}
    for_circle = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.pie(for_circle['Value'], labels=for_circle['Category'], startangle=50, counterclock=False, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Сторона')
    plt.show()