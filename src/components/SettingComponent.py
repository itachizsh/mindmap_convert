import tkinter as tk
import tkinter.font as tkFont


class SettingComponent:
    def __init__(self, root, label_text,  default_values, options, x_pos=0, y_pos=0, width=350):
        self.root = root
        ft = tkFont.Font(family='Times', size=10)
        frame = tk.Frame(root)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        label = tk.Label(frame, width=25)
        label["font"] = ft
        label["fg"] = "#333333"
        label["anchor"] = "w"
        label["text"] = label_text
        label.grid(sticky="w", column=0, row=0)

        # Importance
        self.value_importance = tk.StringVar()
        self.value_importance.set(default_values["importance"])
        dropdown_importance = tk.OptionMenu(
            frame,
            self.value_importance,
            *options["importance"])
        dropdown_importance.config(width=15)
        dropdown_importance.grid(sticky="e", column=1, row=0)
        # Test type
        self.value_test_type = tk.StringVar()
        self.value_test_type.set(default_values["testType"])
        dropdown_test_type = tk.OptionMenu(
            frame,
            self.value_test_type,
            *options["testType"])
        dropdown_test_type.config(width=15)
        dropdown_test_type.grid(sticky="e", column=2, row=0)

        # Priority
        self.value_priority = tk.StringVar()
        self.value_priority.set(default_values["priority"])
        dropdown_priority = tk.OptionMenu(
            frame,
            self.value_priority,
            *options["priority"])
        dropdown_priority.config(width=15)
        dropdown_priority.grid(sticky="e", column=3, row=0)

        frame.place(x=x_pos, y=y_pos, anchor="nw", width=width)
        frame.pack_propagate(0)
