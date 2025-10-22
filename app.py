import streamlit as st
import pandas as pd
import numpy as mp

st.title("my first stramlit app")

st.write("here is our first attempt at using data to create a table")
st.write(pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
}))