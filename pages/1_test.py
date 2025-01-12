import streamlit as st

# タイトル
st.title('簡単なStreamlitアプリ')

# テキスト入力
name = st.text_input('あなたの名前を入力してください')

# ボタン
if st.button('送信'):
    st.write(f'こんにちは、{name}さん！')

# スライダー
age = st.slider('あなたの年齢を選択してください', 0, 100, 25)
st.write(f'あなたの年齢は {age} 歳です。')

# チェックボックス
hobby = st.checkbox('趣味がありますか？')
if hobby:
    st.write('趣味があるんですね！')

# セレクトボックス
option = st.selectbox(
    '好きなプログラミング言語を選んでください',
    ('Python', 'JavaScript', 'Java', 'C++', 'その他')
)
st.write(f'あなたの好きなプログラミング言語は {option} です。')