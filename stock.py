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

while True:
    stock_data = ak.bond_zh_hs_cov_spot()  # 获取最新数据
    stock_data_placeholder.text(stock_data)  # 使用占位符显示最新数据
    refresh_count += 1  # 累计刷新次数加一
    st.write("累计刷新次数:", refresh_count)
    time.sleep(5)  # 每5秒刷新一次数据


