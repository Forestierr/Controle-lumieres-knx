#interface_test.py | Robin Forestier | 29.11.2021
import tkinter as tk       # <-- avoid star imports
from tkinter import font
from PIL import ImageTk, Image

is_on = [1,1,1,1,1,1,1,1]

class AlertPanel(tk.Frame):   # <-- is a tk.Frame, and can be manipulated as such

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        self.myFont = font.Font(family='Helvetica', size=30, weight='bold')

        self.alert_actions = tuple([self.alert_bt_0, self.alert_bt_1, self.alert_bt_2, self.alert_bt_3, self.alert_bt_4, self.alert_bt_5, self.alert_bt_6, self.alert_bt_7, self.quit])
        self.alert_buttons = []
        self.make_alert_buttons()
        self.pack(fill=tk.BOTH, expand=True)   # <-- because self is a tk.Frame

    def make_alert_buttons(self):
        btn_idx = 0

        lbl_logo = tk.Label(self, text="ELO Light Control", font=('Helvetica', 20), height=2, width=15)
        lbl_logo.grid(row = 0, columnspan  = 3, sticky = tk.NW)

        for row in range(1, 4):
            for col in range(3):
                action = self.alert_actions[btn_idx]
                b_text = f"{btn_idx + 1} \n OFF"
                if row == 3 and col == 2:
                    b_text = "QUIT"
                b = tk.Button(self,
                              text = b_text,
                              font=self.myFont,
                              command=action,
                              height=2, width=9)
                b.grid(row=row, column=col, padx=20, pady = 10)
                self.alert_buttons.append(b)
                btn_idx += 1
        self.alert_buttons = tuple(self.alert_buttons)

    def alert_bt_0(self):
        print("Alert Button 1 Pressed")
        global is_on
        btn_idx = 0

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_1(self):
        print("Alert Button 2 Pressed")
        global is_on
        btn_idx = 1

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_2(self):
        print("Alert Button 3 Pressed")
        global is_on
        btn_idx = 2

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_3(self):
        print("Alert Button 4 Pressed")
        global is_on
        btn_idx = 3

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_4(self):
        print("Alert Button 5 Pressed")
        global is_on
        btn_idx = 4

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_5(self):
        print("Alert Button 6 Pressed")
        global is_on
        btn_idx = 5

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_6(self):
        print("Alert Button 7 Pressed")
        global is_on
        btn_idx = 6

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def alert_bt_7(self):
        print("Alert Button 8 Pressed")
        global is_on
        btn_idx = 7

        # Determine is on or off
        if is_on[btn_idx] == 1:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \nON")
            is_on[btn_idx] = 0
        else:
            self.alert_buttons[btn_idx].config(text=f"{btn_idx + 1} \n OFF")
            is_on[btn_idx] = 1

    def quit(self):
        self.master.destroy()



root = tk.Tk()
root.title("Light Control")
root.geometry("800x480")
root['bg'] = '#181818'
root.wm_attributes('-fullscreen', 'true')  # <-- untested
app1 = AlertPanel(root)

root.mainloop()