import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from components.ChooseFolderComponent import ChooseFolderComponent
from components.SettingComponent import SettingComponent
from components.LevelSettingComponent import LevelSettingComponent
from components.TestCaseTypeComponent import TestCaseTypeComponent
from components.FunctionSettingComponent import FunctionSettingComponent
from converter import convert
from config import conf


class App:
    def __init__(self, root):
        setting_conf = conf["ui"]["settings"]
        # setting title
        root.title("Mindmap converter")
        # setting window size
        width = 700
        height = 700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ft = tkFont.Font(family='Times', size=10)
        ft_header = tkFont.Font(family='Times', size=10, weight='bold')

        # Upload file
        self.upload_path = ChooseFolderComponent(
            root, component_type="excel", label_text="Upload file", button_text="Chọn", y_pos=40)

        # Download file destination
        self.output_path = ChooseFolderComponent(
            root, component_type="folder", label_text="Output folder", button_text="Chọn", y_pos=90)

        # -------------------Settings--------------------
        setting_frame = tk.Frame(root)

        setting_label = tk.Label(setting_frame, anchor="w", font=ft_header)
        setting_label["text"] = "Cấu hình"
        setting_label.place(x=20, y=0, anchor="nw")

        self.file_setting = LevelSettingComponent(
            root=setting_frame,
            label_text="File - chọn cột thứ",
            default_value=setting_conf["file"]["defaultValue"],
            options=setting_conf["file"]["values"],
            x_pos=120, y_pos=30, width=200)

        self.sheet_setting = LevelSettingComponent(
            root=setting_frame,
            label_text="Sheet - chọn cột thứ",
            default_value=setting_conf["sheet"]["defaultValue"],
            options=setting_conf["sheet"]["values"],
            x_pos=120, y_pos=60, width=200)
        self.type_setting = TestCaseTypeComponent(
            root=setting_frame,
            label_text="Chọn test case gồm",
            default_value=setting_conf["type"]["defaultValue"],
            x_pos=120, y_pos=100, width=455)
        self.function_setting = FunctionSettingComponent(
            root=setting_frame,
            label_text="Cột chức năng",
            x_pos=120, y_pos=150, width=410)

        setting_frame.place(x=0, y=140, anchor="nw", width=width, height=240)
        setting_frame.pack_propagate(0)

        # ----------------Sheet Settings-----------------
        sheet_setting_frame = tk.Frame(root)

        sheet_setting_label = tk.Label(
            sheet_setting_frame, anchor="w", font=ft_header)
        sheet_setting_label["text"] = "Cấu hình testcase theo sheet"
        sheet_setting_label.place(x=20, y=0, anchor="nw")

        self.genSheetHeader(sheet_setting_frame, x_pos=45, y_pos=30, width=600)

        # ------------Data--------------
        self.sheet_logic_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra luồng xử lý",
            default_values=setting_conf["sheet"]["logic"]["defaultValues"],
            options=setting_conf["sheet"]["logic"]["values"],
            x_pos=45, y_pos=60, width=600)

        self.sheet_screen_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra màn hình",
            default_values=setting_conf["sheet"]["screen"]["defaultValues"],
            options=setting_conf["sheet"]["screen"]["values"],
            x_pos=45, y_pos=90, width=600)
        self.sheet_authorization_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra phân quyền",
            default_values=setting_conf["sheet"]["authorization"]["defaultValues"],
            options=setting_conf["sheet"]["authorization"]["values"],
            x_pos=45, y_pos=120, width=600)
        self.sheet_precondition_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra tiền điều kiện",
            default_values=setting_conf["sheet"]["precondition"]["defaultValues"],
            options=setting_conf["sheet"]["precondition"]["values"],
            x_pos=45, y_pos=150, width=600)
        self.sheet_affection_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra ảnh hưởng",
            default_values=setting_conf["sheet"]["affection"]["defaultValues"],
            options=setting_conf["sheet"]["affection"]["values"],
            x_pos=45, y_pos=180, width=600)
        self.sheet_outlier_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet kiểm tra ngoại lệ",
            default_values=setting_conf["sheet"]["outlier"]["defaultValues"],
            options=setting_conf["sheet"]["outlier"]["values"],
            x_pos=45, y_pos=210, width=600)
        self.sheet_other_setting = SettingComponent(
            root=sheet_setting_frame,
            label_text="Sheet khác",
            default_values=setting_conf["sheet"]["other"]["defaultValues"],
            options=setting_conf["sheet"]["other"]["values"],
            x_pos=45, y_pos=240, width=600)
        sheet_setting_frame.place(
            x=0, y=360, anchor="nw", width=width, height=270)
        sheet_setting_frame.pack_propagate(0)

        # --------------------Start----------------------

        start_button = tk.Button(root,
                                 font=ft,
                                 bg="#f0f0f0",
                                 fg="#000000",
                                 justify="center")
        start_button["text"] = "Start"
        start_button.place(x=315, y=650, width=70, height=30)
        start_button["command"] = self.onStartClick

    def genSheetHeader(self, root, x_pos=0, y_pos=0, width=350):
        frame = tk.Frame(root)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        label = tk.Label(frame, font='Times 10 bold', width=22)
        label["fg"] = "#333333"
        label["anchor"] = "w"
        label["text"] = "Sheet"
        label.grid(sticky="w", column=0, row=0)

        label = tk.Label(frame, font='Times 10 bold', width=15)
        label["fg"] = "#333333"
        label["anchor"] = "center"
        label["text"] = "Kịch bản trọng yếu"
        label.grid(sticky="we", column=1, row=0)

        label = tk.Label(frame, font='Times 10 bold', width=15)
        label["fg"] = "#333333"
        label["anchor"] = "center"
        label["text"] = "Loại test case"
        label.grid(sticky="we", column=2, row=0)

        label = tk.Label(frame, font='Times 10 bold', width=15)
        label["fg"] = "#333333"
        label["anchor"] = "center"
        label["text"] = "Mức độ ưu tiên"
        label.grid(sticky="we", column=3, row=0)

        frame.place(x=x_pos, y=y_pos, anchor="nw", width=width)
        frame.pack_propagate(0)

    def onStartClick(self):
        settings = self.getSettings()
        if self.validateSettings(settings):
            status = convert(settings)
            if status:
                messagebox.showinfo("Hoàn thành", "Hoàn thành")

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
        # Check file level <= sheet level
        if settings["file_level"] > settings["sheet_level"]:
            messagebox.showerror(
                "Validation error", "Cấu hình cột file level phải nhỏ hơn hoặc bằng cột sheet")
            return False

        # Check function rows custom
        if not self.validateFunctionSettings(settings):
            return False

        return True

    def validateFunctionSettings(self, settings):
        if settings["function"]["type"] == 'default':
            return True

        if settings["function"]["start"] < settings["sheet_level"]:
            messagebox.showerror(
                "Validation error", "Cấu hình cột bắt đầu chức năng phải lớn hơn hoặc bằng cột sheet")
            return False

        if settings["function"]["start"] > settings["function"]["end"]:
            messagebox.showerror(
                "Validation error", "Cấu hình cột bắt đầu chức năng phải lớn hơn hoặc bằng cột kết thúc chức năng")
            return False
        return True

    def getSettings(self):
        settings = {}
        settings["in_path"] = self.upload_path.path
        settings["out_path"] = self.output_path.path
        settings["file_level"] = int(self.file_setting.value.get())
        settings["sheet_level"] = int(self.sheet_setting.value.get())
        settings["test_case_type"] = int(self.type_setting.value.get())
        settings["function"] = {}
        settings["function"]["type"] = self.function_setting.value.get()
        settings["function"]["start"] = self.function_setting.value_custom_start.get()
        settings["function"]["end"] = self.function_setting.value_custom_end.get()
        settings["sheets"] = {}

        settings["sheets"]["logic"] = {
            "importance": self.sheet_logic_setting.value_importance.get(),
            "testType": self.sheet_logic_setting.value_test_type.get(),
            "priority": int(self.sheet_logic_setting.value_priority.get())
        }

        settings["sheets"]["screen"] = {
            "importance": self.sheet_screen_setting.value_importance.get(),
            "testType": self.sheet_screen_setting.value_test_type.get(),
            "priority": int(self.sheet_screen_setting.value_priority.get())
        }

        settings["sheets"]["authorization"] = {
            "importance": self.sheet_authorization_setting.value_importance.get(),
            "testType": self.sheet_authorization_setting.value_test_type.get(),
            "priority": int(self.sheet_authorization_setting.value_priority.get())
        }

        settings["sheets"]["precondition"] = {
            "importance": self.sheet_precondition_setting.value_importance.get(),
            "testType": self.sheet_precondition_setting.value_test_type.get(),
            "priority": int(self.sheet_precondition_setting.value_priority.get())
        }
        settings["sheets"]["affection"] = {
            "importance": self.sheet_affection_setting.value_importance.get(),
            "testType": self.sheet_affection_setting.value_test_type.get(),
            "priority": int(self.sheet_affection_setting.value_priority.get())
        }
        settings["sheets"]["outlier"] = {
            "importance": self.sheet_outlier_setting.value_importance.get(),
            "testType": self.sheet_outlier_setting.value_test_type.get(),
            "priority": int(self.sheet_outlier_setting.value_priority.get())
        }
        settings["sheets"]["other"] = {
            "importance": self.sheet_other_setting.value_importance.get(),
            "testType": self.sheet_other_setting.value_test_type.get(),
            "priority": int(self.sheet_other_setting.value_priority.get())
        }
        return settings


if __name__ == "__main__":
    root = tk.Tk()

    app = App(root)
    root.mainloop()
