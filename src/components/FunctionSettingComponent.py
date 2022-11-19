import tkinter as tk
import tkinter.font as tkFont


class FunctionSettingComponent:
    def __init__(self, root, label_text, x_pos=0, y_pos=0, width=350):
        self.root = root
        ft = tkFont.Font(family='Times', size=10)
        frame = tk.Frame(root)
        frame.grid_columnconfigure(0, weight=5)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        label = tk.Label(frame, font=ft, fg="#333333",
                         anchor="w", text=label_text)
        label.grid(sticky="w", column=0, row=0)

        self.value = tk.StringVar()
        self.value.set('default')
        self.value_custom_start = tk.IntVar()
        self.value_custom_start.set(1)
        self.value_custom_end = tk.IntVar()
        self.value_custom_end.set(1)
        # initial menu text

        r1 = tk.Radiobutton(
            frame, text="Mặc định", variable=self.value, value='default')
        r2 = tk.Radiobutton(
            frame, text="Tùy chỉnh", variable=self.value, value='custom')

        r1.grid(sticky="w", column=1, row=0)
        r2.grid(sticky="w", column=1, row=1)

        start_frame = tk.Frame(frame)
        end_frame = tk.Frame(frame)
        start_col_label = tk.Label(start_frame, font=ft, fg="#333333",
                                   anchor="w", text="từ cột")
        end_col_label = tk.Label(end_frame, font=ft, fg="#333333",
                                 anchor="w", text="đến cột")
        start_col = tk.OptionMenu(
            start_frame,
            self.value_custom_start,
            *[i for i in range(1, 21)])

        end_col = tk.OptionMenu(
            end_frame,
            self.value_custom_end,
            *[i for i in range(1, 21)])
        start_col_label.grid(sticky="w", column=0, row=0)
        start_col.grid(sticky="w", column=1, row=0)
        end_col_label.grid(sticky="w", column=0, row=0)
        end_col.grid(sticky="w", column=1, row=0)

        start_frame.grid(sticky="w", column=2, row=1)
        end_frame.grid(sticky="w", column=3, row=1)

        frame.place(x=x_pos, y=y_pos, anchor="nw", width=width)
        frame.pack_propagate(0)
