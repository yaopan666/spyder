# -*- coding: utf-8 -*-
import streamlit as st
import time
import akshare as ak
import pandas as pd
#streamlit run C:\Users\Administrator\Desktop\new\etf.py


from functools import lru_cache
import pandas as pd
import requests


class etf_data:
    def __init__(self):
        pass

    @lru_cache()
    def fund_etf_spot_em(self) -> pd.DataFrame:
        url = "https://88.push2.eastmoney.com/api/qt/clist/get"
        params = {
            "pn": "1",
            "pz": "5000",
            "po": "1",
            "np": "1",
            "ut": "bd1d9ddb04089700cf9c27f6f7426281",
            "fltt": "2",
            "invt": "2",
            "wbp2u": "|0|0|0|web",
            "fid": "f3",
            "fs": "b:MK0021,b:MK0022,b:MK0023,b:MK0024",
            "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152",
            "_": "1672806290972",
        }
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["data"]["diff"])
        temp_df.rename(
            columns={
                "f12": "代码",
                "f14": "名称",
                "f2": "最新价",
                "f4": "涨跌额",
                "f3": "涨跌幅",
                "f5": "成交量",
                "f6": "成交额",
                "f17": "开盘价",
                "f15": "最高价",
                "f16": "最低价",
                "f18": "昨收",
                "f8": "换手率",
                "f21": "流通市值",
                "f20": "总市值",
            },
            inplace=True,
        )
        temp_df = temp_df[
            [
                "代码",
                "名称",
                "最新价",
                "涨跌额",
                "涨跌幅",
                "成交量",
                "成交额",
                "开盘价",
                "最高价",
                "最低价",
                "昨收",
                "换手率",
                "流通市值",
                "总市值",
            ]
        ]
        temp_df["最新价"] = pd.to_numeric(temp_df["最新价"], errors="coerce")
        temp_df["涨跌额"] = pd.to_numeric(temp_df["涨跌额"], errors="coerce")
        temp_df["涨跌幅"] = pd.to_numeric(temp_df["涨跌幅"], errors="coerce")
        temp_df["成交量"] = pd.to_numeric(temp_df["成交量"], errors="coerce")
        temp_df["成交额"] = pd.to_numeric(temp_df["成交额"], errors="coerce")
        temp_df["开盘价"] = pd.to_numeric(temp_df["开盘价"], errors="coerce")
        temp_df["最高价"] = pd.to_numeric(temp_df["最高价"], errors="coerce")
        temp_df["最低价"] = pd.to_numeric(temp_df["最低价"], errors="coerce")
        temp_df["昨收"] = pd.to_numeric(temp_df["昨收"], errors="coerce")
        temp_df["换手率"] = pd.to_numeric(temp_df["换手率"], errors="coerce")
        temp_df["流通市值"] = pd.to_numeric(temp_df["流通市值"], errors="coerce")
        temp_df["总市值"] = pd.to_numeric(temp_df["总市值"], errors="coerce")
        return temp_df




st.title('ETF实时行情')

# 创建一个空白的占位符
stock_data_placeholder = st.empty()

# 累计刷新次数
refresh_count = 0
refresh_count_placeholder = st.empty()  # 创建一个用于显示刷新次数的占位符

while True:
    models=etf_data()
    stock_data = models.fund_etf_spot_em()
    #ak.bond_zh_hs_cov_spot()  # 获取最新数据
    
    # 将"trade"列更改为数字格式
    #stock_data['trade'] = pd.to_numeric(stock_data['trade'], errors='coerce')
    
    stock_data_placeholder.dataframe(stock_data)  # 使用占位符以DataFrame形式显示最新数据
    refresh_count += 1  # 累计刷新次数加一
    refresh_count_placeholder.text("累计刷新次数: {}".format(refresh_count))  # 更新累计刷新次数的显示
    time.sleep(5)  # 每5秒刷新一次数据
    










