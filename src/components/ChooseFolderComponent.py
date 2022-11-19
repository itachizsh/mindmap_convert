import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, askdirectory


class ChooseFolderComponent:
    def __init__(self, root, component_type, label_text, button_text, x_pos=20, y_pos=0, height=30, path=""):
        self.type = component_type
        self.root = root
        self.path = path

        ft = tkFont.Font(family='Times', size=10)
        ft_header = tkFont.Font(family='Times', size=10, weight='bold')

        label = tk.Label(root)
        label["font"] = ft_header
        label["fg"] = "#333333"
        label["anchor"] = "w"
        label["text"] = label_text
        label.place(x=x_pos, y=y_pos, width=80, height=height)

        self.path_label = tk.Label(root, borderwidth=2, relief="groove")
        self.path_label["font"] = ft
        self.path_label["fg"] = "#333333"
        self.path_label["bg"] = "#ffffff"
        self.path_label["anchor"] = "w"
        self.path_label["text"] = path
        self.path_label.place(x=x_pos + 100, y=y_pos, width=450, height=height)

        button = tk.Button(root)
        button["bg"] = "#f0f0f0"
        button["font"] = ft
        button["fg"] = "#000000"
        button["justify"] = "center"
        button["text"] = button_text
        button.place(x=x_pos + 560, y=y_pos, width=70, height=height)
        button["command"] = self.onButtonClick

    def onButtonClick(self):
        if self.type == "excel":
            self.path = askopenfilename(
                filetypes=[("Excel files", ".xlsx .xls")])
        else:
            self.path = askdirectory()
        self.path_label.config(text=self.path)
