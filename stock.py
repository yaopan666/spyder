# -*- coding: utf-8 -*-
import streamlit as st
import time
import akshare as ak
#streamlit run C:\Users\Administrator\Desktop\new\stock.py


st.title('可转债实时行情')

# 创建一个空白的占位符
stock_data_placeholder = st.empty()


# 累计刷新次数
refresh_count = 0
refresh_count_placeholder = st.empty()  # 创建一个用于显示刷新次数的占位符

while True:
    stock_data = ak.bond_zh_hs_cov_spot()  # 获取最新数据
    stock_data['trade'] = pd.to_numeric(stock_data['trade'], errors='coerce')
    stock_data_placeholder.dataframe(stock_data)  # 使用占位符以DataFrame形式显示最新数据
    refresh_count += 1  # 累计刷新次数加一
    refresh_count_placeholder.text("累计刷新次数: {}".format(refresh_count))  # 更新累计刷新次数的显示
    time.sleep(5)  # 每5秒刷新一次数据
