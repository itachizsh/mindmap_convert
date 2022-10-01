conf = {
    "ui": {
        "settings": {
            "file": {
                "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "defaultValue": 1
            },
            "sheet": {
                "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "defaultValue": 2,
                "logic": {
                    "values": [1 ,2, 3, 4],
                    "defaultValue": 1,
                    "name": "Kiểm tra luồng xử lý"
                },
                "screen": {
                    "values": [1 ,2, 3, 4],
                    "defaultValue": 3,
                    "name": "Kiểm tra màn hình"
                },
                "authorization": {
                    "values": [1 ,2, 3, 4],
                    "defaultValue": 2,
                    "name": "Kiểm tra phân quyền"
                },
                "precondition": {
                    "values": [1 ,2, 3, 4],
                    "defaultValue": 2,
                    "name": "Kiểm tra tiền điều kiện"
                },
                "affection": {
                    "values": [1 ,2, 3, 4],
                    "defaultValue": 3,
                    "name": "Kiểm tra ảnh hưởng"
                },
                "outlier": {
                    "values": [1 ,2, 3, 4],
                    "defaultValue": 4,
                    "name": "Kiểm tra ngoại lệ"
                },
                "other": {
                   "values": [1 ,2, 3, 4],
                    "defaultValue": 3
                }
            }
        }
    }
}
