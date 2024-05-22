import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
           'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 데이터 불러오기
def load_data(nrows):
   data = pd.read_csv(DATA_URL, nrows=nrows)
   lowercase = lambda x: str(x).lower()
   data.rename(lowercase, axis='columns', inplace=True)
   data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
   return data

# 텍스트 요소 생성. 사용자에게 데이터가 로드 되고 있음을 알린다.
data_load_state = st.text('Loading data...')

# 10000개의 행의 데이터를 로드한다.
data = load_data(10000)

# 데이터가 성공적으로 로드 되었음을 알린다.
data_load_state.text('Loading data...done!')

# 부제목 만들기
st.subheader('Raw data')
st.write(data)

# 데이터 시각화
st.subheader('Pickup by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# 지도 시각화
st.subheader('Pickup locations')
pickup_map = st.map(data)

# 상관관계 히트맵
st.subheader('Feature correlation heatmap')
st.write(sns.heatmap(data.corr(),annot=True))

st.pyplot()
