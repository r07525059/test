import pandas as pd
import csv


def read():
    
    with open('DATA/南下.csv',"r") as csvfile:

        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        li = []
        # 以迴圈輸出每一列
        for row in rows:
            # print(row)
            li.append(row)

    return li


    # pd.read_csv('DATA/南下.csv')

if __name__ == "__main__":
    read()