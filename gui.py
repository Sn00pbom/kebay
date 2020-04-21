import tkinter as tk
from copy import deepcopy

class ArgPopup(tk.Frame):
    def __init__(self, args, master=None):
        super().__init__(master)
        self.master = master
        self.args = args
        self.pack()
        self.entries = {}
        self.create_widgets()

    def create_widgets(self):
        i = 0
        for name, val in self.args.items():
            # load defaults into text boxes
            lbl_name, entry_val = tk.Label(self, text=name), tk.Entry(self)
            entry_val.insert(0, str(val))
            self.entries[name] = entry_val
            lbl_name.grid(row=i, column=0)
            entry_val.grid(row=i, column=1)
            i += 1

        btn_confirm = tk.Button(self, text='Confirm', command=self.confirm)
        btn_confirm.grid(row=i, column=1)

    def confirm(self):
        # move entry data into args dict
        for k, v in self.entries.items():
            self.args[k] = v.get()
        self.master.destroy()


class MainFrame(tk.Frame):
    def __init__(self, modules, args_sets, master=None):
        super().__init__(master)
        self.mod_names = list(modules.keys())
        self.modules = modules
        self.args_sets = args_sets
        self.cartridges = []
        self.master = master
        self.pack()
        self.vals = {}
        self.create_widgets()

    def create_widgets(self):
        self.opt_var = tk.StringVar()
        self.opt_var.set("")
        option = tk.OptionMenu(self.master, self.opt_var, *self.mod_names)
        option.pack()
        btn = tk.Button(self.master, text='Add', command=self.new_window)
        btn.pack()
        exebtn = tk.Button(self.master, text='Execute Jobs', command=self.execute_cartridges)
        exebtn.pack()

    def new_window(self):
        if self.opt_var.get() == '':
            return

        kmod = self.opt_var.get()
        args = deepcopy(self.args_sets[kmod])
        self.cartridges.append((kmod, args))
        self.nwin = tk.Toplevel(self.master)
        self.app = ArgPopup(args, self.nwin)

    def execute_cartridges(self):
        for kmod, args in self.cartridges:
            mod = self.modules[kmod]
            print(mod.run(*args.values()))


def start(modules, args_sets):
    root = tk.Tk()
    app = MainFrame(modules, args_sets, master=root)
    app.mainloop()