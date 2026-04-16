import pandas as pd
import numpy as np

china_divisions = [
    "北京市", "天津市", "上海市", "重庆市",                     # 直辖市
    "河北省", "山西省", "内蒙古自治区",                       # 华北地区
    "辽宁省", "吉林省", "黑龙江省",                           # 东北地区
    "江苏省", "浙江省", "安徽省", "福建省", "江西省", "山东省", # 华东地区
    "河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省", # 中南地区
    "四川省", "贵州省", "云南省", "西藏自治区",               # 西南地区
    "陕西省", "甘肃省", "青海省", "宁夏回族自治区", "新疆维吾尔自治区", # 西北地区
]
dfs = [pd.read_excel(file+".xlsx",skiprows=1,index_col=0) for file in china_divisions]
for i in range(len(china_divisions)):
    df=dfs[i]

    

    #print(df.isnull().sum())

    #要有空格
    #print(df.loc['  第一产业增加值'])

    #print(df.index)#检查索引
    
    print("列名列表：",df.columns.tolist())
    print("行索引：",df.index)
    print("前三行数据：")
    print(df.head(3))
    
   


