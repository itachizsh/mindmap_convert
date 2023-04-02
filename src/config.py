conf = {
    "ui": {
        "settings": {
            "file": {
                "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                "defaultValue": 1
            },
            "sheet": {
                "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                "defaultValue": 2,
                "logic": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 1
                    },
                    "name": "Kiểm tra luồng xử lý"
                },
                "screen": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 3
                    },
                    "name": "Kiểm tra màn hình"
                },
                "authorization": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 2
                    },
                    "name": "Kiểm tra phân quyền"
                },
                "precondition": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 2
                    },
                    "name": "Kiểm tra tiền điều kiện"
                },
                "affection": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 3
                    },
                    "name": "Kiểm tra ảnh hưởng"
                },
                "outlier": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 4
                    },
                    "name": "Kiểm tra ngoại lệ"
                },
                "other": {
                    "values": {
                        "importance": ["", "Yes", "No"],
                        "testType": ["", "Xuôi", "Ngược"],
                        "priority": [1, 2, 3, 4]
                    },
                    "defaultValues": {
                        "importance": "",
                        "testType": "",
                        "priority": 3
                    },
                }
            },
            "type":{
                "values": [2, 3],
                "defaultValue": 3
            }
        }
    }
}
