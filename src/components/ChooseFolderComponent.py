import tkinter as tk
import tkinter.font as tkFont


class ChooseFolderComponent:
    def __init__(self, root, label_text, button_text, x_pos=20, y_pos=0, height=30, path=""):

        self.root = root
        self.path = path

        ft = tkFont.Font(family='Times', size=10)

        label = tk.Label(root)
        label["font"] = ft
        label["fg"] = "#333333"
        label["anchor"] = "w"
        label["text"] = label_text
        label.place(x=x_pos, y=y_pos, width=80, height=height)

        path_label = tk.Label(root, borderwidth=2, relief="groove")
        path_label["font"] = ft
        path_label["fg"] = "#333333"
        path_label["bg"] = "#ffffff"
        path_label["anchor"] = "w"
        path_label["text"] = path
        path_label.place(x=x_pos + 100, y=y_pos, width=250, height=height)

        button = tk.Button(root)
        button["bg"] = "#f0f0f0"
        button["font"] = ft
        button["fg"] = "#000000"
        button["justify"] = "center"
        button["text"] = button_text
        button.place(x=x_pos + 380, y=y_pos, width=70, height=height)
        button["command"] = None
