import tkinter as tk
import tkinter.font as tkFont


class TestCaseTypeComponent:
    def __init__(self, root, label_text,  default_value, x_pos=0, y_pos=0, width=350):
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

        self.value = tk.StringVar()
        # initial menu text

        r1 = tk.Radiobutton(
            frame, text="2 bước [Tên TC - Kết quả ]", variable=self.value, value=2)
        r1.grid(sticky="w", column=1, row=0)

        r2 = tk.Radiobutton(
            frame, text="3 bước [Tên TC - Các bước thực hiện - Kết quả]", variable=self.value, value=3)
        r2.grid(sticky="w", column=1, row=1)

        self.value.set(default_value)
        frame.place(x=x_pos, y=y_pos, anchor="nw", width=width)
        frame.pack_propagate(0)
