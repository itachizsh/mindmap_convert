import tkinter as tk
import tkinter.font as tkFont


class SettingComponent:
    def __init__(self, root, label_text,  default_value, options, x_pos=0, y_pos=0, width=350):
        self.root = root
        ft = tkFont.Font(family='Times', size=10)
        frame = tk.Frame(root)
        frame.grid_columnconfigure(0, weight=4)
        frame.grid_columnconfigure(1, weight=1)

        label = tk.Label(frame)
        label["font"] = ft
        label["fg"] = "#333333"
        label["anchor"] = "w"
        label["text"] = label_text
        label.grid(sticky="w", column=0, row=0)

        self.chosen_value = tk.StringVar()
        # initial menu text
        self.chosen_value.set(default_value)
        dropdown = tk.OptionMenu(
            frame,
            self.chosen_value,
            *options)
        dropdown.config(width=5)
        dropdown.grid(sticky="e", column=1, row=0)
        frame.place(x=x_pos, y=y_pos, anchor="nw", width=width)
        frame.pack_propagate(0)
