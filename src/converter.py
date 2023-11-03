import pandas as pd
import numpy as np
from tkinter import N, messagebox
import traceback
import copy
from config import conf
import os


def genDataRow(in_data, settings):
    name = in_data[settings["sheet_level"]-1]
    sheet_conf = conf["ui"]["settings"]["sheet"]
    data = {}
    data["Type"] = "Manual"
    data["Status"] = "Done"
    data["Test Step #"] = 1
    if settings["test_case_type"] == 3:
        data["Name"] = in_data[-3]
        data["Test Step Description"] = in_data[-2]
        data["Test Step Expected Result"] = in_data[-1]

        if settings["function"]["type"] == "default":
            data["Chức năng"] = "/".join(in_data[settings["sheet_level"]-1:-3])
        else:
            data["Chức năng"] = "/".join(in_data[settings["function"]
                                         ["start"]:settings["function"]["end"]])
    elif settings["test_case_type"] == 2:
        data["Name"] = in_data[-2]
        data["Test Step Expected Result"] = in_data[-1]
        if settings["function"]["type"] == "default":
            data["Chức năng"] = "/".join(in_data[settings["sheet_level"]-1:-2])
        else:
            data["Chức năng"] = "/".join(in_data[settings["function"]
                                         ["start"]:settings["function"]["end"]])

    if name.lower() == sheet_conf["logic"]["name"].lower() or sheet_conf["logic"]["name"].lower() in data["Chức năng"].lower():
        data["Mức độ ưu tiên"] = settings["sheets"]["logic"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["logic"]["importance"]
        data["Loại testcase"] = settings["sheets"]["logic"]["testType"]
    elif name.lower() == sheet_conf["screen"]["name"].lower() or sheet_conf["screen"]["name"].lower() in data["Chức năng"].lower():
        data["Mức độ ưu tiên"] = settings["sheets"]["screen"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["screen"]["importance"]
        data["Loại testcase"] = settings["sheets"]["screen"]["testType"]
    elif name.lower() == sheet_conf["authorization"]["name"].lower() or sheet_conf["authorization"]["name"].lower() in data["Chức năng"].lower():
        data["Mức độ ưu tiên"] = settings["sheets"]["authorization"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["authorization"]["importance"]
        data["Loại testcase"] = settings["sheets"]["authorization"]["testType"]
    elif name.lower() == sheet_conf["precondition"]["name"].lower() or sheet_conf["precondition"]["name"].lower() in data["Chức năng"].lower():
        data["Mức độ ưu tiên"] = settings["sheets"]["precondition"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["precondition"]["importance"]
        data["Loại testcase"] = settings["sheets"]["precondition"]["testType"]
    elif name.lower() == sheet_conf["affection"]["name"].lower() or sheet_conf["affection"]["name"].lower() in data["Chức năng"].lower():
        data["Mức độ ưu tiên"] = settings["sheets"]["affection"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["affection"]["importance"]
        data["Loại testcase"] = settings["sheets"]["affection"]["testType"]
    elif name.lower() == sheet_conf["outlier"]["name"].lower() or sheet_conf["outlier"]["name"].lower() in data["Chức năng"].lower():
        data["Mức độ ưu tiên"] = settings["sheets"]["outlier"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["outlier"]["importance"]
        data["Loại testcase"] = settings["sheets"]["outlier"]["testType"]
    else:
        data["Mức độ ưu tiên"] = settings["sheets"]["other"]["priority"]
        data["Kịch bản trọng yếu"] = settings["sheets"]["other"]["importance"]
        data["Loại testcase"] = settings["sheets"]["other"]["testType"]
    return data


def processSheet(rows, settings):
    df = pd.DataFrame(columns=["Name", "Id", "Attachments", "Status", "Type", "Test Step #", "Tiền điều kiện", "Test Step Description",
                                       "Test Step Expected Result", "Chức năng", "Mức độ ưu tiên", "Smoke test", "Kịch bản trọng yếu", "Loại testcase", "Testcase SIT/UAT"])

    for row in rows:
        df = pd.concat(
            [df, pd.DataFrame.from_records([genDataRow(row, settings)])])

    return df


def processFile(rows, file_name, settings):
    entries = []
    sheets = []
    sheet_names = {}
    for i in range(len(rows)):
        entries.append(rows[i])
        if i == len(rows)-1 or rows[i][settings["sheet_level"]-1] != rows[i + 1][settings["sheet_level"]-1]:
            # Check same sheet name then create new name
            name = rows[i][settings["sheet_level"]-1][:30]
            if name in sheet_names.keys():
                name = "{}-{}".format(name, sheet_names[name])
            sheet_names[name] = sheet_names.get(name, 0) + 1

            df = processSheet(copy.deepcopy(entries), settings)
            sheets.append(
                {"name": name, "df": df})
            entries = []

    # Print to file
    writer = pd.ExcelWriter(os.path.join(
        settings['out_path'], '{}.xlsx'.format(file_name)), engine='xlsxwriter')
    for sheet in sheets:
        testcase_name_list = sheet["df"]["Name"].to_list()
        chuc_nang_list = sheet["df"]["Chức năng"].to_list()
        for i in range(len(testcase_name_list)):
            suffix = 1
            for j in range(i+1, len(testcase_name_list)):
                if testcase_name_list[i] == testcase_name_list[j] and chuc_nang_list[i] == chuc_nang_list[j]:
                    testcase_name_list[j] = "{}-{}".format(
                        testcase_name_list[j], suffix)
                    suffix = suffix + 1

        sheet["df"]["Name"] = testcase_name_list
        sheet['df'].to_excel(writer, sheet_name=sheet['name'], index=False)
    writer.save()
    writer.close()


def convert(settings):
    try:
        df = pd.read_excel(settings["in_path"], header=None)
        if len(df.columns) < 3:
            messagebox.showerror(
                "Validation error", "Số cột của file nhỏ hơn 3 (tên testcase, các bước thực hiện, kết quả mong muốn)")
            return False

        if len(df.columns) <= settings["sheet_level"]:
            messagebox.showerror(
                "Validation error", "Số level của file nhỏ hơn sheet level config")
            return False
        entries = []

        validIndexes = pd.DataFrame(df.T).apply(pd.Series.last_valid_index)
        file_names = {}
        prev_row = None
        for (_, row), last_index in zip(df.iterrows(), validIndexes):
            cur_row = row.to_list()[:last_index + 1]
            if prev_row:
                # Check if file level not nan
                if isinstance(cur_row[settings["file_level"]-1], str):
                    name = prev_row[settings["file_level"]-1]
                    if name in file_names.keys():
                        name = "{}-{}".format(name, file_names[name])
                    file_names[name] = file_names.get(name, 0) + 1

                    processFile(copy.deepcopy(entries), name, settings)
                    entries = []

                for i in range(last_index):
                    if not isinstance(cur_row[i], str):
                        cur_row[i] = prev_row[i]

            cur_row = cur_row[:last_index + 1]
            prev_row = cur_row
            entries.append(cur_row)

        if prev_row and len(entries) > 0:
            name = prev_row[settings["file_level"]-1]
            if name in file_names.keys():
                name = "{}-{}".format(name, file_names[name])

            file_names[name] = file_names.get(name, 0) + 1
            processFile(copy.deepcopy(entries),
                        name, settings)

        for file_name in file_names:
            df_excel = pd.ExcelFile(os.path.join(
                settings['out_path'], '{}.xlsx'.format(file_name)))
            sheet_names = df_excel.sheet_names  # Lấy danh sách tất cả các sheet

            for sheet_name in sheet_names:
                df_sheet = df_excel.parse(sheet_name)

                csv_file_name = '{}_{}.csv'.format(file_name, sheet_name)
                csv_file_path = os.path.join(
                    settings['out_path'], csv_file_name)

                df_sheet.to_csv(csv_file_path, index=False)

    except Exception as e:
        messagebox.showerror("Error", "Kiểm tra fileupload: \n"
                             "1-Đã save as đủ 2 lần chưa? \n"
                             "2-Có dòng nào bị thiếu bước không? \n"
                                      + "{}\nStack trace:\n{}".format(
                                          str(e), traceback.format_exc()))
        return False
    return True


if __name__ == "__main__":
    settings = {'in_path': 'E:/projects/mb-mindmap-converter/data/test-success.xlsx', 'out_path': 'E:/projects/mb-mindmap-converter/data', 'file_level': 2,
                'sheet_level': 3, 'sheets': {'logic': 1, 'screen': 3, 'authorization': 2, 'precondition': 2, 'affection': 3, 'outlier': 4, 'other': 3}}
    convert(settings)
