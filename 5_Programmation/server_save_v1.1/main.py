#main.py | Robin Forestier | 2021 / 2022

from flask import Flask, g, render_template, request, session, url_for, redirect
import time
import datetime
import threading
import csv
import os
import logging

import RPi.GPIO as GPIO

logging.basicConfig(filename="log.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG) 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO 0 to 11 in output mode at 0
for i in range(12):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.session_cookie_name = 'MyBeautifulCookies'

authorize_ip = ["localhost", "127.0.0.1", "172.16.32.133"]

buttonSts_p1 = ["/static/img/img_off.png"] * 8
buttonSts_p2 = ["/static/img/img_off.png"] * 8
color = ["#333333"] * 8
warning = ""

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='elo', password='elo'))
users.append(User(id=2, username='admin', password='admin'))
users.append(User(id=3, username='local', password='local'))

def gpio_modif():

    for i in range(8):
        if buttonSts_p1[i] == "/static/img/img_off.png":
            #OFF
            GPIO.output(i, 0)
        else:
            #ON
            GPIO.output(i, 1)
            #time.sleep(1)     #security time for fuses

def getTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)

    return current_time

@app.before_request
def before_request():
    g.user = None

    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    if 'user_id' in session :
        #logging.debug("reconnect " + str(ip))
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

    else :
        for i in authorize_ip:
            if ip == i:
                if 'user_id' in session:
                    #logging.debug("reconect as local " + str(ip))
                    user = [x for x in users if x.id == session['user_id']][0]
                    g.user = user
                
                else :
                    logging.info("creat local user" + str(ip))
                    session.pop('user_id', None)
                    session['user_id'] = 3
                    return redirect(url_for('page1'))

@app.route("/", methods=['POST', 'GET'])
def login():
    current_time = getTime()

    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        try:
            user = [x for x in users if x.username == username][0]
            try:
                if user and user.password == password:
                    session['user_id'] = user.id
                    logging.info("New login username : " + username + " ip : ", str(ip))
                    return redirect(url_for('page1'))
            except:
                logging.warning("bad password : " + username + " ip : " + str(ip))
                return redirect(url_for('login'))
        except:
            logging.warning("bad username : " + username + " ip : " + str(ip))
            return redirect(url_for('login'))

    return render_template("login.html", time=current_time, warning=warning)

@app.route("/page1", methods = ['POST', 'GET'])
def page1():
    current_time = getTime()

    if not g.user:
        return redirect(url_for('login'))

    if all(elem == "/static/img/img_on.png" for elem in buttonSts_p1):
        buttonSts_p2[0] = "/static/img/img_on.png"
    else:
        buttonSts_p2[0] = "/static/img/img_off.png"

    if request.method == 'POST':
        if request.form['button_p1'] == '1':
            if buttonSts_p1[0] == "/static/img/img_on.png":
                buttonSts_p1[0] = "/static/img/img_off.png"
                color[0] = "#333333"
            else:
                buttonSts_p1[0] = "/static/img/img_on.png"
                color[0] = "#FFFFFF"
        elif request.form['button_p1'] == '2':
            if buttonSts_p1[1] == "/static/img/img_on.png":
                buttonSts_p1[1] = "/static/img/img_off.png"
                color[1] = "#333333"
            else:
                buttonSts_p1[1] = "/static/img/img_on.png"
                color[1] = "#FFFFFF"
        elif request.form['button_p1'] == '3':
            if buttonSts_p1[2] == "/static/img/img_on.png":
                buttonSts_p1[2] = "/static/img/img_off.png"
                color[2] = "#333333"
            else:
                buttonSts_p1[2] = "/static/img/img_on.png"
                color[2] = "#FFFFFF"
        elif request.form['button_p1'] == '4':
            if buttonSts_p1[3] == "/static/img/img_on.png":
                buttonSts_p1[3] = "/static/img/img_off.png"
                color[3] = "#333333"
            else:
                buttonSts_p1[3] = "/static/img/img_on.png"
                color[3] = "#FFFFFF"
        elif request.form['button_p1'] == '5':
            if buttonSts_p1[4] == "/static/img/img_on.png":
                buttonSts_p1[4] = "/static/img/img_off.png"
                color[4] = "#333333"
            else:
                buttonSts_p1[4] = "/static/img/img_on.png"
                color[4] = "#FFFFFF"
        elif request.form['button_p1'] == '6':
            if buttonSts_p1[5] == "/static/img/img_on.png":
                buttonSts_p1[5] = "/static/img/img_off.png"
                color[5] = "#333333"
            else:
                buttonSts_p1[5] = "/static/img/img_on.png"
                color[5] = "#FFFFFF"
        elif request.form['button_p1'] == '7':
            if buttonSts_p1[6] == "/static/img/img_on.png":
                buttonSts_p1[6] = "/static/img/img_off.png"
                color[6] = "#333333"
            else:
                buttonSts_p1[6] = "/static/img/img_on.png"
                color[6] = "#FFFFFF"
        elif request.form['button_p1'] == '8':
            if buttonSts_p1[7] == "/static/img/img_on.png":
                buttonSts_p1[7] = "/static/img/img_off.png"
                color[7] = "#333333"
            else:
                buttonSts_p1[7] = "/static/img/img_on.png"
                color[7] = "#FFFFFF"
        elif request.form['button_p1'] == 'page_2':
            return redirect(url_for('page2'))
        else:
            pass

        gpio_modif()

    return render_template('page1.html', button=buttonSts_p1, color=color, time=current_time, warning=warning)

@app.route("/page2", methods = ['POST', 'GET'])
def page2():
    current_time = getTime()

    if not g.user:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if request.form['button_p1'] == '1':
            buttonSts_p2[0] = "/static/img/img_on.png"
            for i in range(8):
                buttonSts_p1[i] = "/static/img/img_on.png"
                color[i] = "#FFFFFF"
        elif request.form['button_p1'] == '2':
            buttonSts_p2[1] = "/static/img/img_off.png"
            for i in range(8):
                buttonSts_p1[i] = "/static/img/img_off.png"
                buttonSts_p2[i] = "/static/img/img_off.png"
                color[i] = "#333333"
        elif request.form['button_p1'] == '3':
            buttonSts_p2[0] = "/static/img/img_off.png"
            buttonSts_p2[1] = "/static/img/img_off.png"

            for i in range(0, 8, 2):
                color[i] = "#FFFFFF"
                color[i + 1] = "#333333"

                buttonSts_p1[i] = "/static/img/img_on.png"
                buttonSts_p1[i + 1] = "/static/img/img_off.png"
        elif request.form['button_p1'] == '4':
            buttonSts_p2[0] = "/static/img/img_off.png"
            buttonSts_p2[1] = "/static/img/img_off.png"

            for i in range(0, 8):
                if i < 3:
                    color[i] = "#FFFFFF"
                    buttonSts_p1[i] = "/static/img/img_on.png"
                else :
                    color[i] = "#333333"
                    buttonSts_p1[i] = "/static/img/img_off.png"
        elif request.form['button_p1'] == '5':
            buttonSts_p2[0] = "/static/img/img_off.png"
            buttonSts_p2[1] = "/static/img/img_off.png"

            for i in range(0, 8):
                if i > 3 and i != 7:
                    color[i] = "#FFFFFF"
                    buttonSts_p1[i] = "/static/img/img_on.png"
                else:
                    color[i] = "#333333"
                    buttonSts_p1[i] = "/static/img/img_off.png"

        elif request.form['button_p1'] == 'page_1':
            return redirect(url_for('page1'))
        else:
            pass

        gpio_modif()


    return render_template('page2.html', button=buttonSts_p2, color=color, time=current_time, warning=warning)

@app.route("/settings", methods = ['POST', 'GET'])
def settings(setting=None):
    if g.user.id == 3:
        return redirect(url_for('page1'))

    if not g.user.username == "admin":
        return redirect(url_for('login'))

    current_time = getTime()

    if request.method == 'POST':
        check1 = request.form.get('Auto on')
        time1 = request.form.get('time Auto on')
        check2 = request.form.get('Auto off')
        time2 = request.form.get('time Auto off')

        file = open('/home/pi/controle-des-lumieres-knx/5_Programmation/INT_SERV/config.csv', "w", newline='')
        header = ['name','state','param1']
        csvf = csv.DictWriter(file, fieldnames=header)

        csvf.writeheader()
        csvf.writerow({'name': 'Auto on', 'state': check1, 'param1': time1})
        csvf.writerow({'name': 'Auto off', 'state': check2, 'param1': time2})

        file.close()

        return redirect(url_for('page1'))

    with open('/home/pi/controle-des-lumieres-knx/5_Programmation/INT_SERV/config.csv', "r") as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)

    f.close()

    return render_template('settings.html', time=current_time, settings=rows, warning=warning)

@app.before_first_request
def activate_job():
    def run_job():
        logging.debug("starting while loop")
        while True:
            t = getTime()

            with open('/home/pi/controle-des-lumieres-knx/5_Programmation/INT_SERV/config.csv', "r") as f:
                csvreader = csv.reader(f)
                header = next(csvreader)
                rows = []
                for row in csvreader:
                    rows.append(row)
            f.close()

            day = datetime.datetime.today().weekday()
            #0 monday / 6 sunday

            #ALL ON and ALL OFF
            if rows[0][1] == 'on' and t == rows[0][2] and day < 5:
                logging.info("All light ON Automaticly")
                buttonSts_p2[0] = "/static/img/img_on.png"
                for i in range(8):
                    buttonSts_p1[i] = "/static/img/img_on.png"
                    color[i] = "#FFFFFF"
                gpio_modif()

            if rows[1][1] == 'on' and t == rows[1][2] and day < 5:
                logging.info("All light ON Automaticly")
                buttonSts_p2[1] = "/static/img/img_off.png"
                for i in range(8):
                    buttonSts_p1[i] = "/static/img/img_off.png"
                    buttonSts_p2[i] = "/static/img/img_off.png"
                    color[i] = "#333333"
                gpio_modif()

            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as ftemp:
                global warning
                temp = int(ftemp.read()) / 1000
                if temp > 60:
                    logging.warning("Temp = " + str(int(temp)) + "°")
                    warning = "Temp = " + str(int(temp)) + "°"
                else:
                    warning = ""

            time.sleep(60)

    thread = threading.Thread(target=run_job)
    thread.start()

if __name__ == "__main__":
    logging.info("Strating server")
    app.run(host='0.0.0.0', port=80, debug=False)
    GPIO.cleanup()

