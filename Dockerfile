# 使用輕量級的 Python 環境
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 將需求檔複製並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有專案檔案
COPY . .

# 開放 5000 port
EXPOSE 5000

# 啟動程式
CMD ["python", "app.py"]
