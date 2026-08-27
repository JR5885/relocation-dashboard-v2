import os
import requests
import csv
import json

# 你的 Google 試算表公開 CSV 匯出網址
GSHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQUem3z16ko71Gyz_80gTFiw7C_O9UkoBcJP8nAWabx1ikg23ujAUlEwyVTr4s-rguZ1DKbuDVkZB8c/pub?output=csv"

def sync_data():
    print("正在從 Google 試算表同步資料...")
    response = requests.get(GSHEET_CSV_URL)
    if response.status_code == 200:
        csv_content = response.text
        
        # 直接把清洗並對應好欄位的資料存成 data.json，讓網頁 100% 穩定讀取
        lines = csv_content.splitlines()
        reader = csv.DictReader(lines)
        
        data_list = []
        for row in reader:
            # 支援你試算表現有的欄位名稱對應
            item = {
                "EmployeeID": row.get("EmployeeID", ""),
                "EmployeeName": row.get("EmployeeName", ""),
                "Region": row.get("Region", "").strip(),
                "Status": row.get("Status", "").strip(),
                "BudgetAllocated": row.get("BudgetAlloc", row.get("BudgetAllocated", "0")),
                "BudgetSpent": row.get("BudgetSpen", row.get("BudgetSpent", "0")),
                "TargetArrivalDate": row.get("TargetArriva", row.get("TargetArrivalDate", ""))
            }
            if item["EmployeeID"]:
                data_list.endswith = data_list.append(item) # standard append
                
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=2)
            
        print("資料轉換與同步成功！")
    else:
        print("抓取失敗，狀態碼：", response.status_code)
        exit(1)

if __name__ == "__main__":
    sync_data()
