import streamlit as st

# タイトルを設定
st.title('Streamlit Columnsのデモ')

# セクション1: 基本的な2列レイアウト
st.header('1. 基本的な2列レイアウト')
col1, col2 = st.columns(2)  # 等幅の2列を作成

with col1:
    st.subheader('左列')
    st.write('これは基本的な2列レイアウトの左側です')
    st.number_input('数値を入力', value=0)

with col2:
    st.subheader('右列')
    st.write('これは基本的な2列レイアウトの右側です')
    st.button('クリックしてください')

# セクション2: カスタム幅の列
st.header('2. カスタム幅の列')
col3, col4 = st.columns([5, 1])  # 3:1の比率で列を作成

with col3:
    st.subheader('広い列 (3)')
    st.line_chart({'data': [1, 2, 3, 4, 5]})

with col4:
    st.subheader('狭い列 (1)')
    st.write('データ値:')
    st.write('1\n2\n3\n4\n5')

# セクション3: 3列レイアウト
st.header('3. 3列レイアウト')
col5, col6, col7 = st.columns([2, 1, 1])  # 2:1:1の比率で列を作成

with col5:
    st.subheader('入力セクション')
    user_name = st.text_input('お名前を入力してください')

with col6:
    st.subheader('選択セクション')
    color = st.selectbox('色を選択', ['赤', '青', '緑', '黄'])

with col7:
    st.subheader('表示セクション')
    if user_name:
        st.write(f'こんにちは、{user_name}さん！')
    if color:
        st.write(f'選択された色: {color}')
