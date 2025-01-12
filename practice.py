import streamlit as st
import random



num = st.number_input('generate count', min_value=0)
if st.button('random generate'):
    for i in range(num):
        random_number = random.randint(0, 100)
        st.write(random_number)
