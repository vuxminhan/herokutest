import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
from PIL import Image
import plotly.graph_objects as go
brush = alt.selection_interval( bind='scales')

st.set_page_config(page_title='Impression Results')
st.header('Impression Results 2022')
st.subheader('')

# excel_file = 'Extension Impression.csv'
df = pd.read_csv('Extension Impression1.csv', encoding='latin-1')
# df = df.fillna(0)
df = df.astype({"Extension install": int}, errors='raise')
df = df.astype({"Extension uninstall": int}, errors='raise')
# df.dtypes
print(df)
# st.dataframe(df)
# st.line_chart(df)
# test = df.astype(str)
df = df.melt('Ngày', var_name='name', value_name='value')
df['Ngày'] = df['Ngày'].apply(pd.to_datetime)
df = df.sort_values(by='Ngày')
#
#
# print(type(df['Ngày'][0]))
st.write(df)
zoom = alt.selection_interval(
    bind='scales',
    on="[mousedown[!event.shiftKey], mouseup] > mousemove",
    translate="[mousedown[!event.shiftKey], mouseup] > mousemove!",
)

selection = alt.selection_interval(
    on="[mousedown[event.shiftKey], mouseup] > mousemove",
    translate="[mousedown[event.shiftKey], mouseup] > mousemove!",
)
chart = alt.Chart(df).mark_line().encode(
  x=alt.X('Ngày:T',  axis=alt.Axis(labelOverlap="greedy",grid=False)),
  y=alt.Y('value:Q',impute=alt.ImputeParams(value=None)),
  color=alt.Color("name:N")
).properties(title="Hello World 2").add_selection(zoom, selection)


chart

