import tkinter as tk       # <-- avoid star imports
from tkinter import font
from PIL import ImageTk, Image
import RPi.GPIO as GPIO
import time

is_on = [1,1,1,1,1,1,1,1]

class AlertPanel(tk.Frame):   # <-- is a tk.Frame, and can be manipulated as such

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.myFont = font.Font(family='Helvetica', size=15, weight='bold')
        self.config(bg="#000000")

        off = Image.open("img_off.png")
        off = off.resize((130, 93), Image.ANTIALIAS)
        self.img_off = ImageTk.PhotoImage(off)

        on = Image.open("img_on.png")
        on = on.resize((130, 93), Image.ANTIALIAS)
        self.img_on = ImageTk.PhotoImage(on)

        img_plus = Image.open("img_plus.png")
        img_plus = img_plus.resize((130, 93), Image.ANTIALIAS)
        self.img_plus = ImageTk.PhotoImage(img_plus)

        self.alert_actions = tuple(
            [self.alert_bt_0, self.alert_bt_1, self.alert_bt_2, self.alert_bt_3, self.alert_bt_4, self.alert_bt_5,
             self.alert_bt_6, self.alert_bt_7, self.quit])
        self.alert_buttons = []
        self.make_alert_buttons()
        self.pack(expand=True)


    def make_alert_buttons(self):
        btn_idx = 0

        for row in range(1, 4):
            for col in range(3):
                action = self.alert_actions[btn_idx]
                img = self.img_off
                b_text = f" {btn_idx + 1} \n\nOFF"
                if row == 3 and col == 1:
                    b_text = f" P \n\nOFF"
                if row == 3 and col == 2:
                    img = self.img_plus
                    b_text = ""
                b = tk.Button(self, image = img, text=b_text, fg="#FFFFFF", bg="#000000",highlightthickness=0,activebackground="#000000", activeforeground="#FFFFFF",font=self.myFont, compound="center", borderwidth=0, relief=tk.FLAT, command=action)
                b.image = self.img_off
                b.grid(row=row, column=col, padx=5, pady = 10)
                self.alert_buttons.append(b)
                btn_idx += 1
        self.alert_buttons = tuple(self.alert_buttons)

    def alert_bt_0(self):
        global is_on
        btn_idx = 0

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_1(self):
        global is_on
        btn_idx = 1

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_2(self):
        global is_on
        btn_idx = 2

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_3(self):
        global is_on
        btn_idx = 3

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_4(self):
        global is_on
        btn_idx = 4

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_5(self):
        global is_on
        btn_idx = 5

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_6(self):
        global is_on
        btn_idx = 6

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def alert_bt_7(self):
        global is_on
        btn_idx = 7

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" P \n\nON", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#FFFFFF")
            GPIO.output(btn_idx, 1)
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" P \n\nOFF", compound="center")
            canevas.itemconfig(draw[btn_idx], fill="#333333")
            GPIO.output(btn_idx, 0)
            is_on[btn_idx] = 1

    def quit(self):
        GPIO.cleanup()
        root.destroy()

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        
    clock.after(200, tick)

GPIO.setmode(GPIO.BCM)

#GPIO 3 to 13 in output
for i in range(12):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

time1 =''

root = tk.Tk()
root.title("Light Control")
root.geometry("800x480")
root.resizable(False, False)
root.config(bg='#000000')
root.wm_attributes('-fullscreen', 'true')  # <-- untested

frame1 = tk.Frame(root)

img_logo = Image.open("logo.png")
img_logo_resize = img_logo.resize((32, 32), Image.ANTIALIAS)
img_logo_resize = ImageTk.PhotoImage(img_logo_resize)

img_logo_label = tk.Label(frame1, image=img_logo_resize, bg="#333333")

clock = tk.Label(frame1, font=("Helvetica", 18, "bold"), bg="#333333", fg="#FFFFFF", anchor="w")

logo_lbl = tk.Label(frame1, text="ELO Light Control", font=("Helvetica", 18, "bold"), bg="#333333", fg="#FFFFFF", anchor="w")
logo_lbl.pack(side = tk.LEFT, fill=tk.BOTH,expand=1, padx=10)
clock.pack(side=tk.LEFT, padx=5)
img_logo_label.pack(side=tk.LEFT, padx=5)

frame1.pack(fill=tk.BOTH)
frame1.config(bg="#333333")

#CREAT PLAN

plan = Image.open("plan_vide.png")
plan_resize = plan.resize((314, 400), Image.ANTIALIAS)
plan = ImageTk.PhotoImage(plan_resize)

canevas = tk.Canvas(root, bg="#000000", width=300, height=390, borderwidth=0, relief=tk.FLAT)
canevas.pack(side=tk.LEFT, padx=5, pady=15)

canevas.create_image(0, 0, image=plan, anchor=tk.NW)
draw = []
draw.append(canevas.create_rectangle(30, 30, 40, 340, fill="#333333"))
draw.append(canevas.create_rectangle(73, 30, 83, 340, fill="#333333"))
draw.append(canevas.create_rectangle(113, 65, 123, 340, fill="#333333"))
draw.append(canevas.create_rectangle(163, 65, 173, 340, fill="#333333"))
draw.append(canevas.create_rectangle(213, 65, 223, 270, fill="#333333"))
draw.append(canevas.create_rectangle(250, 30, 260, 270, fill="#333333"))
draw.append(canevas.create_rectangle(290, 30, 300, 270, fill="#333333"))
draw.append(canevas.create_rectangle(123, 30, 213, 40, fill="#333333"))

#canevas.itemconfig(l2, fill="#00FF00")
app1 = AlertPanel(root)

tick()

root.mainloop()
