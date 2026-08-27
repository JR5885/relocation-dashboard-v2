import os
import requests
import json

# 你的 Google 試算表公開 CSV 匯出網址
GSHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQUem3z16ko71Gyz_80gTFiw7C_O9UkoBcJP8nAWabx1ikg23ujAUlEwyVTr4s-rguZ1DKbuDVkZB8c/pub?output=csv"

def sync_data():
    print("正在從 Google 試算表抓取最新資料...")
    response = requests.get(GSHEET_CSV_URL)
    if response.status_code == 200:
        csv_content = response.text
        
        # 將抓下來的資料存成 data.csv 供前端讀取，或直接寫入檔案
        with open("data.csv", "w", encoding="utf-8") as f:
            f.write(csv_content)
            
        print("資料同步成功！")
    else:
        print("抓取失敗，狀態碼：", response.status_code)
        exit(1)

if __name__ == "__main__":
    sync_data()