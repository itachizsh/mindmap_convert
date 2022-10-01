import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from components.ChooseFolderComponent import ChooseFolderComponent
from components.SettingComponent import SettingComponent
from converter import convert
from config import conf


class App:
    def __init__(self, root):
        setting_conf = conf["ui"]["settings"]
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
        self.upload_path = ChooseFolderComponent(
            root, component_type="excel", label_text="Upload file", button_text="Choose", y_pos=40)

        # Download file destination
        self.output_path = ChooseFolderComponent(
            root, component_type="folder", label_text="Output folder", button_text="Choose", y_pos=90)

        # -------------------Settings--------------------
        setting_frame = tk.Frame(root)

        setting_label = tk.Label(setting_frame, anchor="w", font=ft)
        setting_label["text"] = "Cấu hình"
        setting_label.place(x=20, y=0, anchor="nw")

        self.file_setting = SettingComponent(
            root=setting_frame,
            label_text="Cấu hình file - level",
            default_value=setting_conf["file"]["defaultValue"],
            options=setting_conf["file"]["values"],
            x_pos=120, y_pos=30)

        self.sheet_setting = SettingComponent(
            root=setting_frame,
            label_text="Cấu hình sheet - level",
            default_value=setting_conf["sheet"]["defaultValue"],
            options=setting_conf["sheet"]["values"],
            x_pos=120, y_pos=60)
        setting_frame.place(x=0, y=150, anchor="nw", width=width, height=110)
        setting_frame.pack_propagate(0)

        # ----------------Sheet Settings-----------------
        sheet_setting_frame = tk.Frame(root)

        sheet_setting_label = tk.Label(
            sheet_setting_frame, anchor="w", font=ft)
        sheet_setting_label["text"] = "Cấu hình mức độ ưu tiên cho sheet"
        sheet_setting_label.place(x=20, y=0, anchor="nw")

        self.sheet_logic_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra luồng xử lý",
            default_value=setting_conf["sheet"]["logic"]["defaultValue"],
            options=setting_conf["sheet"]["logic"]["values"],
            x_pos=120, y_pos=30)

        self.sheet_screen_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra màn hình",
            default_value=setting_conf["sheet"]["screen"]["defaultValue"],
            options=setting_conf["sheet"]["screen"]["values"],
            x_pos=120, y_pos=60)

        self.sheet_authorization_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra phân quyền",
            default_value=setting_conf["sheet"]["authorization"]["defaultValue"],
            options=setting_conf["sheet"]["authorization"]["values"],
            x_pos=120, y_pos=90)
        self.sheet_precondition_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra tiền điều kiện",
            default_value=setting_conf["sheet"]["precondition"]["defaultValue"],
            options=setting_conf["sheet"]["precondition"]["values"],
            x_pos=120, y_pos=120)
        self.sheet_affection_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra ảnh hưởng",
            default_value=setting_conf["sheet"]["affection"]["defaultValue"],
            options=setting_conf["sheet"]["affection"]["values"],
            x_pos=120, y_pos=150)
        self.sheet_outlier_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra ngoại lệ",
            default_value=setting_conf["sheet"]["outlier"]["defaultValue"],
            options=setting_conf["sheet"]["outlier"]["values"],
            x_pos=120, y_pos=180)
        self.sheet_other_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet khác",
            default_value=setting_conf["sheet"]["other"]["defaultValue"],
            options=setting_conf["sheet"]["other"]["values"],
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
        start_button["command"] = self.onStartClick

    def onStartClick(self):
        settings = self.getSettings()
        if self.validateSettings(settings):
            convert(settings)

    def validateSettings(self, settings):
        # Check in file
        if len(settings["in_path"]) == 0:
            messagebox.showerror("Validation error",
                                 "Hãy chọn đường dẫn file upload")
            return False
        # Check out file
        if len(settings["out_path"]) == 0:
            messagebox.showerror("Validation error",
                                 "Hãy chọn đường dẫn output folder")
            return False
        # Check file level < sheet level
        if settings["file_level"] >= settings["sheet_level"]:
            messagebox.showerror(
                "Validation error", "Cấu hình file level phải nhỏ hơn sheet level")
            return False
        return True

    def getSettings(self):
        settings = {}
        settings["in_path"] = self.upload_path.path
        settings["out_path"] = self.output_path.path
        settings["file_level"] = int(self.file_setting.value.get())
        settings["sheet_level"] = int(self.sheet_setting.value.get())
        settings["sheets"] = {}
        settings["sheets"]["logic"] = int(self.sheet_logic_setting.value.get())
        settings["sheets"]["screen"] = int(
            self.sheet_screen_setting.value.get())
        settings["sheets"]["authorization"] = int(
            self.sheet_authorization_setting.value.get())
        settings["sheets"]["precondition"] = int(
            self.sheet_precondition_setting.value.get())
        settings["sheets"]["affection"] = int(
            self.sheet_affection_setting.value.get())
        settings["sheets"]["outlier"] = int(
            self.sheet_outlier_setting.value.get())
        settings["sheets"]["other"] = int(self.sheet_other_setting.value.get())
        return settings


if __name__ == "__main__":
    root = tk.Tk()

    app = App(root)
    root.mainloop()
