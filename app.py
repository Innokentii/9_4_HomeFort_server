from flask import Flask, render_template, request, jsonify, Response
import sqlite3 as SQL
from flask_cors import CORS
import telebot

# Функция запуска сайта
app = Flask(__name__)
CORS(app)
def create_app():
    return app

#===============================================================#
#                Работа_с_базой_данных_SQLite3                  #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# База данных комнат;
conn = SQL.connect('customers.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        room_id TEXT,
        date TEXT,
        time TEXT,
        name TEXT)
''')
conn.commit()
conn.close()

# База данных описания рекламы "Hostel HOME FORT";
conn = SQL.connect('advertisement.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS advertisements (
        id TEXT,
        advert TEXT
        )
''')
conn.commit()
conn.close()

# База данных id групп и пользователей;
conn = SQL.connect('id_group.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS id_nums (
        id TEXT,
        id_num INT,
        on_off TEXT      
        )
''')
conn.commit()
conn.close()

#===============================================================#
#                       Работа с Ботам                          #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# Запрос "GET" для запуска бота;
arrow_id = [6165294691, 1766368801, -1001978383126, -4113046905, 1654209558]
@app.route('/get_bot_start', methods=['GET'])
def get_bot_start_f():
    conn = SQL.connect('advertisement.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM advertisements")
    rows_tel_bot = cursor.fetchall()
    conn.commit()
    conn.close()
    print(rows_tel_bot[0][1])
    global arrow_id
    for id in arrow_id:
        bot = telebot.TeleBot('6324320483:AAEIwgbVGkhx3w9-rPfh2yGonnATKkuPm_U')
        bot.send_message(id, rows_tel_bot[0][1])
        bot.send_message(id, "Разошли это сообщение по твоим группам пожалуйста🙏 это нужно для рекламы хостела 'HOME FORT'. Буду очень благодарен🤝")
        bot.stop_polling()

    return jsonify(rows_tel_bot[0][1])

#===============================================================#
#                      Функции и классы                         #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# Запрос "GET";
@app.route('/get_costomers', methods=['GET'])
def get_costomers_f():
    conn = SQL.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return jsonify(rows)

# Запрос "POST";
@app.route('/post_save', methods=['POST'])
def post_save_f():
    post_request = request.get_json(force=True)
    post_request = post_request['save_obj']
    print(post_request)
    conn = SQL.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET date = ?, time = ?, name = ? WHERE room_id = ?", (post_request[1], post_request[2], post_request[3], str(post_request[0])))
    conn.commit()
    conn.close()
    return post_request

# Запрос "GET";
@app.route('/get_costomers_bot', methods=['GET'])
def get_costomers_bot_f():
    conn = SQL.connect('advertisement.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM advertisements")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return jsonify(rows[0][1])

# Запрос "POST";
@app.route('/post_save_bot', methods=['POST'])
def post_save_bot_f():
    post_request = request.get_json(force=True)
    post_request = post_request['save_obj']
    print(post_request)
    conn = SQL.connect('advertisement.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE advertisements SET advert = ? WHERE id = ?", (post_request, 1))
    conn.commit()
    conn.close()
    return post_request

#===============================================================#
#                    Работа со страницами                       #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# Рендер тела сайта (запуск сайта);
@app.route('/')
@app.route('/main')
def main_f():
    render_template('main.html')
    return render_template('block_1.html')

# Рендер страницы "block_1";
@app.route("/block_1")
def _block_1_f():
    return render_template("block_1.html")

# Рендер страницы "block_2";
@app.route("/block_2")
def _block_2_f():
    return render_template("block_2.html")

# Рендер страницы "block_3";
@app.route("/block_3")
def _block_3_f():
    return render_template("block_3.html")
