# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:15:34 2023

@author: yp
"""
import streamlit as st
import time
import akshare as ak


#@st.cache_data
# 获取股票实时行情数据
def get_stock_data():
    data = ak.bond_zh_hs_cov_spot()
    return data

st.title('可转债实时行情')

# 在页面上显示实时数据
while True:
    stock_data = get_stock_data()
    st.write(stock_data)
    time.sleep(5)  # 每5秒刷新一次数据




















