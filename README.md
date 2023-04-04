# Mindmap converter

Tạo môi trường python

```
conda create --name mindmap-converter python=3.8
conda activate mindmap-converter
```

Cài đặt dependencies

```
pip install -r requirements.txt
```

Để chạy project:

```
python src/main.py
```

Build thành file exe, sau khi build sẽ ở thư mục `/dist`

```
pyinstaller.exe --onefile --icon=src/resources/Convert.ico --name MindmapConverter_v3.0 src/main.py
```
