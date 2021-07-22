import functions
import part_main
import numpy as np
import pandas as pd
form = input("輸入檔案名稱")
date_num = eval(input("輸入天數"))
keyword = input("輸入關鍵字")
temp_read = pd.read_excel(form)
data = functions.cut(temp_read, date_num)#切成只有名子科目跟所有日期
b = data["科目"].unique()
a = data.columns
all_date = a[2:]    #儲存所有時間段
final = []
for co in b: 
    #an = []
    #an.append(co) 
    an = (part_main.main(data, co, keyword))
    #print(an)
    final.append(an)


df = pd.DataFrame(final)
df.columns = (all_date)
df.index = (b)
df.to_excel('Result.xlsx')
df
