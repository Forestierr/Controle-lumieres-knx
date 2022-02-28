import tkinter as tk       # <-- avoid star imports
from tkinter import font
from PIL import ImageTk, Image

is_on = [1,1,1,1,1,1,1,1]

class AlertPanel(tk.Frame):   # <-- is a tk.Frame, and can be manipulated as such

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.myFont = font.Font(family='Lucida Console', size=15, weight='bold')
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

        self.alert_actions = tuple([self.alert_bt_0, self.alert_bt_1, self.alert_bt_2, self.alert_bt_3, self.alert_bt_4, self.alert_bt_5, self.alert_bt_6, self.alert_bt_7, self.quit])
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
                if row == 3 and col == 2:
                    img = self.img_plus
                    b_text = ""
                b = tk.Button(self, image = img, text=b_text, fg="#FFFFFF", bg="#000000", font=self.myFont, compound="center", borderwidth=0, relief=tk.FLAT, command=action)
                b.image = self.img_off
                b.grid(row=row, column=col, padx=10, pady = 10)
                self.alert_buttons.append(b)
                btn_idx += 1
        self.alert_buttons = tuple(self.alert_buttons)

    def alert_bt_0(self):
        print("Alert Button 1 Pressed")
        global is_on
        btn_idx = 0

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_1(self):
        print("Alert Button 2 Pressed")
        global is_on
        btn_idx = 1

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_2(self):
        print("Alert Button 3 Pressed")
        global is_on
        btn_idx = 2

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_3(self):
        print("Alert Button 4 Pressed")
        global is_on
        btn_idx = 3

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_4(self):
        print("Alert Button 5 Pressed")
        global is_on
        btn_idx = 4

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_5(self):
        print("Alert Button 6 Pressed")
        global is_on
        btn_idx = 5

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_6(self):
        print("Alert Button 7 Pressed")
        global is_on
        btn_idx = 6

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def alert_bt_7(self):
        print("Alert Button 8 Pressed")
        global is_on
        btn_idx = 7

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(image=self.img_on, text=f" {btn_idx + 1} \n\nON", compound="center")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(image=self.img_off, text=f" {btn_idx + 1} \n\nOFF", compound="center")
            is_on[btn_idx] = 1

    def quit(self):
        root.destroy()



root = tk.Tk()
root.title("Light Control")
root.geometry("800x480")
root.resizable(False, False)
root.config(bg='#000000')
#root.wm_attributes('-fullscreen', 'true')  # <-- untested

frame1 = tk.Frame(root)

img_logo = Image.open("logo.png")
img_logo_resize = img_logo.resize((32, 32), Image.ANTIALIAS)
img_logo_resize = ImageTk.PhotoImage(img_logo_resize)

img_logo_label = tk.Label(frame1, image=img_logo_resize, bg="#333333")

logo_lbl = tk.Label(frame1, text="ELO Light Control", font=("Helvetica", 18, "bold"), bg="#333333", fg="#FFFFFF", anchor="w")
logo_lbl.pack(side = tk.LEFT, fill=tk.BOTH,expand=1)
img_logo_label.pack(side=tk.LEFT)

frame1.pack(fill=tk.BOTH)

plan = Image.open("plan.png")
plan_resize = plan.resize((314, 400), Image.ANTIALIAS)
plan = ImageTk.PhotoImage(plan_resize)

lbl_plan = tk.Label(root, image = plan)
lbl_plan.image = plan

lbl_plan.pack(side=tk.LEFT, padx=5, pady=15)

app1 = AlertPanel(root)

root.mainloop()
