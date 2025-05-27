import streamlit as st
import requests
from datetime import datetime

# secrets.toml에서 API 키 불러오기
API_KEY = "DEMO_KEY"

# 오늘 날짜를 YYYY-MM-DD 형식으로 가져오기
today = datetime.now().strftime("%Y-%m-%d")

# NASA APOD API endpoint
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={today}"

# API 요청
response = requests.get(url)
data = response.json()

# 제목과 설명 출력
st.title("🌌 NASA 오늘의 우주 사진")
st.subheader(data.get("title", "제목 없음"))

# 미디어 타입에 따라 사진 또는 영상 출력
if data.get("media_type") == "image":
    st.image(data.get("url"), use_column_width=True)
elif data.get("media_type") == "video":
    st.video(data.get("url"))
else:
    st.warning("지원하지 않는 미디어 형식입니다.")

# 설명 출력
st.markdown(f"**설명:** {data.get('explanation', '설명이 없습니다.')}")

# 날짜 출력
st.markdown(f"📅 날짜: {data.get('date', today)}")
