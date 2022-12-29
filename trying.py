import streamlit as st
import pandas as pd

st.title("NYOBA GES")

df = pd.read_csv(r'trying-github.csv')

l=df['A'][1]
st.write(l)

k=l*2
st.write(k)
