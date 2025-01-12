import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt



@st.cache_data
def load_data():
    return pd.read_csv('toshokan.csv')

#wide表示
st.set_page_config(layout="wide")

#toshokan.csvをheaderありで読み込む

df = load_data()

#dfのyearの最小値と最大値を取得
min_year = df['year'].min()
max_year = df['year'].max()

#スライダーを表示
start_year, end_year = st.slider('年度', min_value=min_year, max_value=max_year, value=(min_year, max_year))

#yearでフィルタリング
df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
#年度ごとの件数を集計
df_grouped = df.groupby('year').size().reset_index(name='count')
#線グラフを表示
st.line_chart( df_grouped.set_index('year') )
#1.categoryごとの件数を集計
#2.年を検索できるようにして、その年のデータを表で表示
#3.年ごとではなく、月ごとに集計して、棒グラフで表示
