import pandas as pd
import numpy as np

out_df = pd.DataFrame(columns=["Name", "Id", "Attachments", "Status", "Type", "Test Step #", "Test Step Description",
                      "Test Step Expected Result", "Chức năng", "Mức độ ưu tiên", "Smoke test", "Kịch bản trọng yếu", "Loại testcase", "Testcase SIT/UAT"])

df = pd.read_excel("data\Sổ phụ 24h.xlsx", header=None)
df.to_excel("data/out.xlsx")


def genDataRow(in_data):
    data = {}
    data["Type"] = "Manual"
    data["Mức độ ưu tiên"] = 3
    data["Name"] = in_data[-3]
    data["Test Step Description"] = in_data[-2]
    data["Test Step Expected Result"] = in_data[-1]
    data["Chức năng"] = "/".join(in_data[:-3])
    return data


validIndexes = pd.DataFrame(df.T).apply(pd.Series.last_valid_index)
prev_row = None
for (idx, row), last_index in zip(df.iterrows(), validIndexes):
    cur_row = row.to_list()[:last_index + 1]
    # print(cur_row)
    if prev_row:
        for i in range(last_index):
            if not isinstance(cur_row[i], str):
                cur_row[i] = prev_row[i]

    if len(cur_row) <= 3:
        cur_row.insert(0, "")
    cur_row = cur_row[:last_index + 1]
    out_df = pd.concat(
        [out_df, pd.DataFrame.from_records([genDataRow(cur_row)])])
    prev_row = cur_row

out_df.to_excel("data/mindmap_out.xlsx", index=False)
