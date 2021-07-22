import functions
import numpy as np
import pandas as pd


def main(data, cour, keyword):
    condition = (data["科目"] == cour)
    a = data[condition]
    data_array = np.array(a)
    n = len(data_array[0, :])  # column
    m = len(data_array[:, 0])  # row
    data_array = functions.add_rightanddown(data_array, m, n)  # 在右邊跟下面加上空的一行
    functions.tranfer(data_array, keyword, m, n)  # 將關鍵字轉為1,0
    functions.able_person_in_time(data_array, m, n)  # 計算該時段可以的人數並記錄在最下行
    an = functions.the_final(data_array, m, n)  # 計算出最後班表並存至an
    return an
