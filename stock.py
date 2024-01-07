import streamlit as st
import time
import akshare as ak

# 获取可转债实时行情数据
def get_stock_data():
    data = ak.bond_zh_hs_cov_spot()
    return data

st.title('股票实时行情')

# 显示实时数据的函数
@st.cache
def show_stock_data(stock_data):
    st.write(stock_data)

# 实时更新数据并展示
while True:
    stock_data = get_stock_data()
    show_stock_data(stock_data)
    time.sleep(5)  # 每5秒刷新一次数据
