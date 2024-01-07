# -*- coding: utf-8 -*-
import streamlit as st
import time
import akshare as ak

st.title('可转债实时行情')

# 获取股票实时行情数据
def get_stock_data():
    data = ak.bond_zh_hs_cov_spot()
    return data

# 累计刷新次数
refresh_count = 0

while True:
    stock_data = get_stock_data()  # 获取最新数据
    st.write(stock_data)  # 显示数据框
    refresh_count += 1  # 累计刷新次数加一
    st.write("累计刷新次数:", refresh_count)
    time.sleep(5)  # 每5秒刷新一次数据
