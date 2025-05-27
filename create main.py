import streamlit as st
import folium
from streamlit_folium import st_folium

# 서초구 중심 좌표
seocho_center = [37.4836, 127.0326]

# 민트초코 관련 장소 (예시)
mint_choco_places = [
    {"name": "민트초코 카페 서초점", "location": [37.4919, 127.0145]},
    {"name": "민트초코 덕후들의 성지", "location": [37.4872, 127.0308]},
    {"name": "Minty 서초", "location": [37.4789, 127.0403]},
]

# 제목
st.title("서초구 민트초코 지도")

# 지도 생성
m = folium.Map(location=seocho_center, zoom_start=13)

# 마커 추가
for place in mint_choco_places:
    folium.Marker(
        location=place["location"],
        popup=place["name"],
        icon=folium.Icon(color="green", icon="info-sign"),
    ).add_to(m)

# Folium 지도를 Streamlit에 출력
st_folium(m, width=700, height=500)

