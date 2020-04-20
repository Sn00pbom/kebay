import tkinter as tk

class ArgPopup(tk.Frame):
    def __init__(self, args, master=None):
        super().__init__(master)
        self.master = master
        self.args = args
        self.pack()
        self.vals = {}
        self.create_widgets()

    def create_widgets(self):
        for i, a in enumerate(self.args):
            t = str(a)
            lbl, entry = tk.Label(self, text=t), tk.Entry(self)
            self.vals[t] = (lbl, entry)
            lbl.grid(row=i, column=0)
            entry.grid(row=i, column=1)

        btn_confirm = tk.Button(self, text='Confirm')
        btn_confirm.grid(row=len(self.args), column=1)


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.vals = {}
        self.create_widgets()

    def create_widgets(self):
        btn = tk.Button(self.master, text='popup', command=self.new_window)
        btn.pack()

    def new_window(self):
        args = {
            'arg1': 5,
            'arg2': 50,
            'arg3': 15,
            'arg4': 255,
        }
        self.nwin = tk.Toplevel(self.master)
        self.app = ArgPopup(args, self.nwin)

def start():
    root = tk.Tk()
    app = MainFrame(master=root)
    app.mainloop()