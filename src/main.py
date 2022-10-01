import tkinter as tk
import tkinter.font as tkFont
from components.ChooseFolderComponent import ChooseFolderComponent
from components.SettingComponent import SettingComponent


class App:
    def __init__(self, root):
        # setting title
        root.title("Mindmap converter")
        # setting window size
        width = 500
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ft = tkFont.Font(family='Times', size=10)

        # Upload file
        upload_path_component = ChooseFolderComponent(
            root, label_text="Upload file", button_text="Choose file", y_pos=40)

        # Download file destination
        output_path_component = ChooseFolderComponent(
            root, label_text="Output folder", button_text="Choose", y_pos=90)

        # -------------------Settings--------------------
        setting_frame = tk.Frame(root)

        setting_label = tk.Label(setting_frame, anchor="w", font=ft)
        setting_label["text"] = "Cấu hình"
        setting_label.place(x=20, y=0, anchor="nw")

        file_setting = SettingComponent(
            root=setting_frame,
            label_text="Cấu hình file - level",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=30)

        sheet_setting = SettingComponent(
            root=setting_frame,
            label_text="Cấu hình sheet - level",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=60)
        setting_frame.place(x=0, y=150, anchor="nw", width=width, height=110)
        setting_frame.pack_propagate(0)

        # ----------------Sheet Settings-----------------
        sheet_setting_frame = tk.Frame(root)

        sheet_setting_label = tk.Label(
            sheet_setting_frame, anchor="w", font=ft)
        sheet_setting_label["text"] = "Cấu hình mức độ ưu tiên cho sheet"
        sheet_setting_label.place(x=20, y=0, anchor="nw")

        logic_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra luồng xử lý",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=30)

        screen_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra màn hình",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=60)

        sheet_authorization_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra phân quyền",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=90)
        sheet_precondition_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra tiền điều kiện",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=120)
        sheet_influence_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra ảnh hưởng",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=150)
        sheet_outlier_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra màn hình",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=180)
        sheet_other_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet khác",
            default_idx=0,
            options=[1, 2, 3, 4],
            x_pos=120, y_pos=210)
        sheet_setting_frame.place(
            x=0, y=270, anchor="nw", width=width, height=240)
        sheet_setting_frame.pack_propagate(0)

        # --------------------Start----------------------

        start_button = tk.Button(root,
                                 font=ft,
                                 bg="#f0f0f0",
                                 fg="#000000",
                                 justify="center")
        start_button["text"] = "Start"
        start_button.place(x=215, y=560, width=70, height=30)
        start_button["command"] = None


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
