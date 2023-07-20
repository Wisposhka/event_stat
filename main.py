import tkinter as tk
from tkinter import messagebox as ms
import tkinter.ttk as ttk
import sqlite3
from datetime import datetime
import pandas_t

games_tabl = sqlite3.connect("games_tabl")
games_tabl_C = games_tabl.cursor()
games_tabl_C.execute("""CREATE TABLE IF NOT EXISTS useful(
game_1 TEXT,
game_2 TEXT,
game_3 TEXT,
game_4 TEXT,
game_5 TEXT,
game_6 TEXT,
game_7 TEXT,
game_8 TEXT,
game_9 TEXT,
game_10 TEXT,
game_11 TEXT,
game_12 TEXT,
game_13 INTEGER PRIMARY KEY AUTOINCREMENT
)""")
games_tabl.commit()

df = pandas_t.pandas_test()

root = tk.Tk()
root.title('Статистика ивента')

f1 = tk.Frame(root)
root.geometry('1205x500')
f1.pack()

data_games = ttk.Treeview(f1)
data_games['columns'] = (
    "Дата", "Время", "Результат", "Убийств", "Смертей", "Урон по монику", "Ветка брони", "Ветка оружия", "play style",
    "Команда", "Противники", "Сторона", "id")

data_games.column("#0", width=0)
data_games.column("Дата", width=100)
data_games.column("Время", width=100)
data_games.column("Результат", width=100)
data_games.column("Убийств", width=100)
data_games.column("Смертей", width=100)
data_games.column("Урон по монику", width=100)
data_games.column("Ветка брони", width=100)
data_games.column("Ветка оружия", width=100)
data_games.column("play style", width=100)
data_games.column("Команда", width=100)
data_games.column("Противники", width=100)
data_games.column("Сторона", width=100)
data_games.column("id", width=100)

data_games.heading("#0", text=":)", anchor=tk.CENTER)
data_games.heading("Дата", text="Дата", anchor=tk.CENTER)
data_games.heading("Время", text="Время", anchor=tk.CENTER)
data_games.heading("Результат", text="Результат", anchor=tk.CENTER)
data_games.heading("Убийств", text="Убийств", anchor=tk.CENTER)
data_games.heading("Смертей", text="Смертей", anchor=tk.CENTER)
data_games.heading("Урон по монику", text="Урон по монику", anchor=tk.CENTER)
data_games.heading("Ветка брони", text="Ветка брони", anchor=tk.CENTER)
data_games.heading("Ветка оружия", text="Ветка оружия", anchor=tk.CENTER)
data_games.heading("play style", text="play style", anchor=tk.CENTER)
data_games.heading("Команда", text="Команда", anchor=tk.CENTER)
data_games.heading("Противники", text="Противники", anchor=tk.CENTER)
data_games.heading("Сторона", text="Сторона", anchor=tk.CENTER)
data_games.heading("id", text="id", anchor=tk.CENTER)
data_games.pack(expand=tk.YES, fill=tk.BOTH)

treeview_customer_list = []


def refresh_customer():
    treeview_customer_list.clear()
    data_games.delete(*data_games.get_children())
    for value in games_tabl_C.execute("SELECT * FROM useful"):
        value = list(value)
        treeview_customer_list.append(value)
    count = 0
    for record in treeview_customer_list:
        data_games.insert(parent='', index='end', iid=count, values=(
            record[0], record[1], record[2], record[3],
            record[4], record[5], record[6], record[7],
            record[8], record[9], record[10], record[11],
            record[12]))
        count += 1


refresh_customer()


def edit1():
    edit = tk.Toplevel()
    edit.geometry('250x550')
    # tk.Label(edit, text='Дата').pack()
    # edit_E1 = tk.Entry(edit, bd=2, width=20)
    # edit_E1.pack()
    # tk.Label(edit, text='Время').pack()
    # edit_E2 = tk.Entry(edit, bd=2, width=20)
    # edit_E2.pack()
    result = ['Победа', 'Поражение']
    tk.Label(edit, text='Результат').pack()
    edit_E3 = ttk.Combobox(edit, value=result)
    edit_E3.pack()
    tk.Label(edit, text='Убийств').pack()
    edit_E4 = tk.Entry(edit, bd=2, width=20)
    edit_E4.pack()
    tk.Label(edit, text='Смертей').pack()
    edit_E5 = tk.Entry(edit, bd=2, width=20)
    edit_E5.pack()
    tk.Label(edit, text='Урон по монику').pack()
    edit_E6 = tk.Entry(edit, bd=2, width=20)
    edit_E6.pack()
    Armour = ['Пакетик', 'Боевая', 'АО', 'Зверобой']
    tk.Label(edit, text='Ветка брони').pack()
    edit_E7 = ttk.Combobox(edit, value=Armour)
    edit_E7.pack()
    Weapon = ['Печенег', 'Вал', 'Сайга', 'Аек', 'Вектор', 'ФН']
    tk.Label(edit, text='Ветка оружия').pack()
    edit_E8 = ttk.Combobox(edit, value=Weapon)
    edit_E8.pack()
    playstyle = ['Пуш', 'Месилово', 'Спавн килл', 'Хантинг']
    tk.Label(edit, text='play style').pack()
    edit_E9 = ttk.Combobox(edit, value=playstyle)
    edit_E9.pack()
    team = ['Пакеты', 'АОшки', 'Боевые', 'Зверобои']
    tk.Label(edit, text='Команда').pack()
    edit_E10 = ttk.Combobox(edit, value=team)
    edit_E10.pack()
    enemy = ['Пакеты', 'АОшки', 'Боевые', 'Зверобои']
    tk.Label(edit, text='Противники').pack()
    edit_E11 = ttk.Combobox(edit, value=enemy)
    edit_E11.pack()
    side = ['Санитары', 'Блаженные']
    tk.Label(edit, text='Сторона').pack()
    edit_E12 = ttk.Combobox(edit, value=side)
    edit_E12.pack()

    def save():
        date = datetime.now().date()
        time = datetime.now().time()
        data = [str(date), str(time), edit_E3.get(), edit_E4.get(), edit_E5.get(), edit_E6.get(), edit_E7.get(),
                edit_E8.get(), edit_E9.get(), edit_E10.get(), edit_E11.get(), edit_E12.get(), None]
        qr = f"INSERT INTO useful VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        games_tabl_C.execute(qr, data)
        games_tabl.commit()
        refresh_customer()
        edit.destroy()

    tk.Button(edit, text='Сохранить', command=save).pack()


def delete_w():
    x = data_games.selection()[0]
    z = data_games.index(x)
    znach0 = treeview_customer_list[z]
    waring0 = ms.askyesno(title="Windows.exe", message="Вы точно хотите удалить это?")
    if waring0 == True:
        znach0 = znach0[12]
        games_tabl_C.execute(f"DELETE FROM useful WHERE game_13 = '{znach0}'")
        games_tabl.commit()
    refresh_customer()


frame0 = tk.Frame(root, width=1000, height=500)
frame0.pack()

frame1 = tk.Frame(frame0, height=500, width=100, padx=200)
name_label = tk.Label(frame1, text="Статистика")
name_label.pack()

kda = pandas_t.kda
kda_armor = pandas_t.kda_armor
kda_weapon = pandas_t.kda_weapon
kda = kda.astype(str)
kda_armor = kda_armor.astype(str)
kda_weapon = kda_weapon.astype(str)

tk.Label(frame1, text='Твой КД: '+kda).pack()
tk.Label(frame1, text='Лучшая броня: ' + pandas_t.Best_armor + ' ' + 'КД: ' + kda_armor).pack()
tk.Label(frame1, text='Лучшее оружие: ' + pandas_t.Best_weapon + ' ' + 'КД: ' + kda_weapon).pack()

frame1.pack(side=tk.LEFT)

frame2 = tk.Frame(frame0, height=100, width=100, padx=200)
name_label = tk.Label(frame2, text="Кнопачкиии")
name_label.pack()

fbl = tk.Frame(frame2, padx=5)
fbl.pack(side=tk.LEFT)
fbr = tk.Frame(frame2, padx=5)
fbr.pack(side=tk.RIGHT)

button_add = tk.Button(fbl, text='Добавить', command=edit1)
button_add.pack()
buttonf15 = tk.Button(fbl, text='Удалить', command=delete_w)
buttonf15.pack()
tk.Button(fbr, command=pandas_t.show_winrate, text='Винрейт').pack()
tk.Button(fbr, command=pandas_t.show_armor, text='Выбор брони').pack()
tk.Button(fbr, command=pandas_t.show_weapon, text='Выбор оружия').pack()

frame2.pack(side=tk.RIGHT)

root.mainloop()