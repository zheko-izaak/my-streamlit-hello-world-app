import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 My Hello World App')

with st.sidebar:
    st.header('About App')
    st.write('This is my first app!')

# st.write('Hello world!')

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

st.markdown('This is created using st.markdown.')

st.subheader('st.columns')
col1, col2 = st.columns(2)

with col1:
    x = st.slider('Choose an x value:', 1, 10)

with col2:    
    st.write('The value of :red[***x***] is', x)

st.subheader('st.area_chart')
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.area_chart(chart_data)
