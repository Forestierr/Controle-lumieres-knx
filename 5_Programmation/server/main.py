"""
main.py | Robin Forestier | 2021 / 2022

Goal : Create a user interface to controle the light of the ELO's workshop.

Explanation :   I use Flask for create a Web server.
                A shield is plug on the Raspberry Pi (server) with optocoupleur to ABB module with the GPIO.

┌─────────────────────────────────┐
│ Raspberry Pi 3B+                │ ┌───────────────────────┐
│                            ┌──┐ │ │ Shield Octo           │
│                            │  │ │ │                       │
│          GPIO 2  |         │  │ │ │ X1 / DRV3 |           │
│          GPIO 3  |         │  │ │ │ X1 / DRV4 |           │
│          GPIO 4  |         │  │ │ │ X2 / DRV1 |           │
│                  |         │  │ │ │           |           │
│          GPIO 10 |         │  │ │ │ X3 / DRV3 |           │
│          GPIO 9  |         │  │ │ │ X3 / DRV2 |           │
│          GPIO 11 | GPIO 8  │  │ │ │ X3 / DRV4 | X3 / DRV1 │
│                  | GPIO 7  │  │ │ │           | X2 / DRV4 │
│          GPIO 0  | GPIO 1  │  │ │ │ X1 / DRV1 | X1 / DRV2 │
│          GPIO 5  |         │  │ │ │ X2 / DRV2 |           │
│          GPIO 6  |         │  │ │ │ X2 / DRV3 |           │
│                            │  │ │ └───────────────────────┘
│                            │  │ │
│                            └──┘ │
│                     ┌───────┐   │
│  ┌────┐   ┌────┐    │       │   │
│  │    │   │    │    │       │   │
└──┴────┴───┴────┴────┴───────┴───┘

.. Liens::
    GitLab : http://172.16.32.230/Forestier/controle-des-lumieres-knx \n
    XWiki : https://xwiki.serverelo.org/xwiki/bin/view/Centre%20de%20Formation%20ELO/Projets/Controle%20des%20lumières%20KNX/
"""

from flask import Flask, render_template, request, session, url_for, redirect, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import time
import datetime
import threading
import csv
import os
import logging
from werkzeug.exceptions import HTTPException

rpi = False
"""
rpi is used to know if the programm is running on a Raspberry Pi or not. \n
rpi = True --> run on Raspberry Pi. \n
esle : False
"""
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # GPIO 0 to 11 in output mode at 0
    for i in range(12):
        GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

    #it's a raspberry pi
    rpi = True
except :
    rpi = False

#Creating log file (log.log)
logging.basicConfig(filename="log.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

#Creating flask app
app = Flask(__name__)

#Config
app.config.update(
    SECRET_KEY = 'somesecretkeythatonlyishouldknow',
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3",
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SESSION_TYPE = 'sqlalchemy',
    SESSION_COOKIE_NAME = 'MyBeautifulCookies',
    SESSION_COOKIE_SAMESITE = 'Strict',
)

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db
sess = Session(app)

#creat the database
db.create_all()

authorize_ip = ["localhost", "127.0.0.1", "172.16.32.133"]
"""Ip of the server (for the local user) use to skip authentication."""

buttonSts_p1 = ["off"] * 8
"""value of all the page1 buttons"""
buttonSts_p2 = ["on"] * 8
"""value of all the page2 buttons"""
color = ["#333333"] * 8
"""color of the 8 neon"""
warning = ""
"""warning from the app to the server"""

#Path to config file "/config.csv"
if rpi:
    path_to_csv = "/home/pi/controle-des-lumieres-knx/5_Programmation/server/config.csv"
else:
    path_to_csv = "C:/Users/FIX-4/Desktop/server_v2/config.csv"

class User:
    """
    User : creat different user for the login.
    """
    def __init__(self, id, username, password):
        """
        Parameters
        ----------
        id : int
            A basic id for eache login.
        username : str
            The username for the login.
        password : str
            The password of the login.
        """
        self.id = id
        self.username = username
        self.password = password

users = []

"""
user :
    elo - basic user / can only modifie light
    admin - all acces (settings acces)
    local - only used for the raspberry why the tuchscreen (server) / can't acces to settings / don't have to login.
"""
users.append(User(id=1, username='elo', password='elo'))
users.append(User(id=2, username='admin', password='admin'))
users.append(User(id=3, username='local', password='local'))

def gpio_modif():
    """
    modif all the GPIO by looking into buttonSts_p1[]

    Parameters
    ----------
    ...
    """
    if rpi:
        for i in range(8):
            if buttonSts_p1[i] == "off":
                #OFF
                GPIO.output(i, 0)
            else:
                #ON
                GPIO.output(i, 1)
                #time.sleep(1)     #security time for fuses
    else:
        pass


def getTime():
    """
    Get time on format : HH:MM

    Parameters
    ----------
    ...

    Returns
    ----------
    current_time : str
        The current time in format HH:MM
    """
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)

    return current_time

@app.errorhandler(HTTPException)
def handle_exception(e):
    """handle_exception : all http error are show on the 404.html page"""
    e = str(e) #404 not ...  :  The request URL ...
    code = e.split(":") #404 Not Found

    return render_template('404.html', error=code[1], title=code[0]), code[0][0:3]

@app.route("/login", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def login():
    """
    login page

    Receive from POST : username / password
    We first check if username existe and after password.
    If it's a bad username or pass we flash the error.

    Parameters
    ----------
    ...

    Returns
    ----------
    login.html : str
        Page login in html and (css).
    time : str
        The current time.
    warning : str
        The différent warning.
    """
    current_time = getTime()
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    #check for autorized ip
    for i in authorize_ip:
        if ip == i:
            logging.info("creat local user" + str(ip))
            session['user_id'] = 3
            return redirect(url_for('page1'))

    #if already login
    if session.get("user_id") is not None:
        return redirect(url_for('page1'))

    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        try:
            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                logging.info("New login username : " + username + " ip : " + str(ip))
                #Login accepted
                return redirect(url_for('page1'))
            elif user.password != password:
                #bad password / log it / and flash the error
                logging.warning("bad password : " + username + " ip : " + str(ip))
                flash("Bad password")

            return redirect(url_for('login'))

        except:
            #bad username / log it / and flash the error
            logging.warning("bad username : " + username + " ip : " + str(ip))
            flash("Bad username")
            return redirect(url_for('login'))

    return render_template("login.html", time=current_time, warning=warning)

@app.route("/page1", methods = ['POST', 'GET'])
def page1():
    """
    page1

    The page1 show on the left a map of the lights and on the right 9 buttons.

    Parameters
    ----------
    ...

    Returns
    ----------
    page1.html : str
        Page page1 in html and (css).
    button : list
        List of the state of the buttons.
    color : list
        List of neon colors on the map.
    time : str
        The current time.
    warning : str
        The différent warning.
    """
    current_time = getTime()

    # check the id for the session and redirect to loggin.
    if session.get("user_id") == None:
        return redirect(url_for('login'))

    if all(elem == "on" for elem in buttonSts_p1):
        buttonSts_p2[0] = "on"
    else:
        buttonSts_p2[0] = "off"

    if request.method == 'POST':
        if request.form['button_p1'] == '1':
            if buttonSts_p1[0] == "on":
                buttonSts_p1[0] = "off"
                color[0] = "#333333"
            else:
                buttonSts_p1[0] = "on"
                color[0] = "#FFFFFF"
        elif request.form['button_p1'] == '2':
            if buttonSts_p1[1] == "on":
                buttonSts_p1[1] = "off"
                color[1] = "#333333"
            else:
                buttonSts_p1[1] = "on"
                color[1] = "#FFFFFF"
        elif request.form['button_p1'] == '3':
            if buttonSts_p1[2] == "on":
                buttonSts_p1[2] = "off"
                color[2] = "#333333"
            else:
                buttonSts_p1[2] = "on"
                color[2] = "#FFFFFF"
        elif request.form['button_p1'] == '4':
            if buttonSts_p1[3] == "on":
                buttonSts_p1[3] = "off"
                color[3] = "#333333"
            else:
                buttonSts_p1[3] = "on"
                color[3] = "#FFFFFF"
        elif request.form['button_p1'] == '5':
            if buttonSts_p1[4] == "on":
                buttonSts_p1[4] = "off"
                color[4] = "#333333"
            else:
                buttonSts_p1[4] = "on"
                color[4] = "#FFFFFF"
        elif request.form['button_p1'] == '6':
            if buttonSts_p1[5] == "on":
                buttonSts_p1[5] = "off"
                color[5] = "#333333"
            else:
                buttonSts_p1[5] = "on"
                color[5] = "#FFFFFF"
        elif request.form['button_p1'] == '7':
            if buttonSts_p1[6] == "on":
                buttonSts_p1[6] = "off"
                color[6] = "#333333"
            else:
                buttonSts_p1[6] = "on"
                color[6] = "#FFFFFF"
        elif request.form['button_p1'] == '8':
            if buttonSts_p1[7] == "on":
                buttonSts_p1[7] = "off"
                color[7] = "#333333"
            else:
                buttonSts_p1[7] = "on"
                color[7] = "#FFFFFF"
        elif request.form['button_p1'] == 'page_2':
            return redirect(url_for('page2'))
        else:
            pass

        gpio_modif()

    return render_template('page1.html', button=buttonSts_p1, color=color, time=current_time, warning=warning)

@app.route("/page2", methods = ['POST', 'GET'])
def page2():
    """
    page2

    The page2 show on the left a map of the lights and on the right 9 buttons.

    Parameters
    ----------
    ...

    Returns
    ----------
    page2.html : str
        Page page1 in html and (css).
    button : list
        List of the state of the buttons.
    color : list
        List of neon colors on the map.
    time : str
        The current time.
    warning : str
        The différent warning.
    """
    current_time = getTime()

    #check the id for the session and redirect to loggin.
    if session.get("user_id") == None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if request.form['button_p1'] == '1':
            buttonSts_p2[0] = "on"
            for i in range(8):
                buttonSts_p1[i] = "on"
                color[i] = "#FFFFFF"
        elif request.form['button_p1'] == '2':
            buttonSts_p2[1] = "off"
            for i in range(8):
                buttonSts_p1[i] = "off"
                buttonSts_p2[i] = "off"
                color[i] = "#333333"
        elif request.form['button_p1'] == '3':
            buttonSts_p2[0] = "off"
            buttonSts_p2[1] = "off"

            for i in range(0, 8, 2):
                color[i] = "#FFFFFF"
                color[i + 1] = "#333333"

                buttonSts_p1[i] = "on"
                buttonSts_p1[i + 1] = "off"
        elif request.form['button_p1'] == '4':
            buttonSts_p2[0] = "off"
            buttonSts_p2[1] = "off"

            for i in range(0, 8):
                if i < 3:
                    color[i] = "#FFFFFF"
                    buttonSts_p1[i] = "on"
                else :
                    color[i] = "#333333"
                    buttonSts_p1[i] = "off"
        elif request.form['button_p1'] == '5':
            buttonSts_p2[0] = "off"
            buttonSts_p2[1] = "off"

            for i in range(0, 8):
                if i > 3 and i != 7:
                    color[i] = "#FFFFFF"
                    buttonSts_p1[i] = "on"
                else:
                    color[i] = "#333333"
                    buttonSts_p1[i] = "off"

        elif request.form['button_p1'] == 'page_1':
            return redirect(url_for('page1'))
        else:
            pass

        gpio_modif()


    return render_template('page2.html', button=buttonSts_p2, color=color, time=current_time, warning=warning)

@app.route("/settings", methods = ['POST', 'GET'])
def settings():
    """
    settings

    The settings page can only be acces via admin login.

    Parameters
    ----------
    ...

    Returns
    ----------
    settings.html : str
        Page page1 in html and (css).
    time : str
        The current time.
    warning : str
        The différent warning.
    """

    """
    Get the id for the session.
    If == None --> go to login.
    If == 3 (local) --> go to page 1.
    If == 1 (elo) --> remove the id / error 418.
    """
    id = session.get("user_id")

    if id is None:
        return redirect(url_for('login'))
    elif id == 3:
        return redirect(url_for('page1'))
    elif id == 1:
        session.pop("user_id")
        abort(418) # 🍵

    current_time = getTime()

    # Check all settings via a form
    # Settings :
    #           Auto on  -> turn on at a certain time
    #           Auto off -> turn off at a certain time
    if request.method == 'POST':
        check1 = request.form.get('Auto on')
        time1 = request.form.get('time Auto on')
        check2 = request.form.get('Auto off')
        time2 = request.form.get('time Auto off')

        file = open(path_to_csv, "w", newline='')
        header = ['name','state','param1']
        csvf = csv.DictWriter(file, fieldnames=header)

        csvf.writeheader()
        csvf.writerow({'name': 'Auto on', 'state': check1, 'param1': time1})
        csvf.writerow({'name': 'Auto off', 'state': check2, 'param1': time2})

        file.close()

        return redirect(url_for('page1'))

    with open(path_to_csv, "r") as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)

    f.close()

    return render_template('settings.html', time=current_time, settings=rows, warning=warning)

@app.before_first_request
def activate_job():
    """
    activate_job

    Fonction to run job on backround of the web server (with thread)

    Parameters
    ----------
    ...

    Returns
    ----------
    ...
    """
    def run_job():
        """
        run_job

        Run background job (run every minute).
        Auto - on/off
        Check temperature of the Raspberry Pi

        Parameters
        ----------
        ...

        Returns
        ----------
        ...
        """

        logging.debug("starting while loop")
        while True:
            t = getTime()

            with open(path_to_csv, "r") as f:
                csvreader = csv.reader(f)
                header = next(csvreader)
                rows = []
                for row in csvreader:
                    rows.append(row)
            f.close()

            """
            if day is on monday to friday (0 to 4 // 0 is monday)
            check for auto all on / off.
            """
            day = datetime.datetime.today().weekday()
            if rows[0][1] == 'on' and t == rows[0][2] and day < 5:
                logging.info("All light ON Automaticly")
                buttonSts_p2[0] = "on"
                for i in range(8):
                    buttonSts_p1[i] = "on"
                    color[i] = "#FFFFFF"
                gpio_modif()

            if rows[1][1] == 'on' and t == rows[1][2] and day < 5:
                logging.info("All light ON Automaticly")
                buttonSts_p2[1] = "off"
                for i in range(8):
                    buttonSts_p1[i] = "off"
                    buttonSts_p2[i] = "off"
                    color[i] = "#333333"
                gpio_modif()

            #Check temperature warning
            if rpi:
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
    logging.info(" *** Strating server *** ")
    app.run(host='0.0.0.0', port=80, debug=False)
    GPIO.cleanup()
