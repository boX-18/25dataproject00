import yfinance as yf
import plotly.graph_objects as go

# 글로벌 시총 10위 기업 티커 리스트
tickers = ["AAPL", "MSFT", "2222.SR", "GOOGL", "AMZN", "TSLA", "NVDA", "BRK-B", "META", "TSM"]

# 데이터 다운로드 (최근 6개월 종가)
data = {}
for ticker in tickers:
    df = yf.download(ticker, period="6mo", progress=False)
    data[ticker] = df['Close']

# 날짜 공통으로 맞추기 (가장 짧은 날짜 기준)
common_dates = set.intersection(*(set(d.index) for d in data.values()))
common_dates = sorted(common_dates)

# 각 기업 종가 정렬 및 준비
close_prices = {t: data[t].loc[common_dates] for t in tickers}

# Plotly Figure 생성
fig = go.Figure()

# 라인 플롯 추가
for t in tickers:
    fig.add_trace(go.Scatter(
        x=common_dates,
        y=close_prices[t],
        mode='lines',
        name=t
    ))

# — 버섯 갓 (붉은색 큰 타원)
fig.add_shape(type="ellipse",
              xref="paper", yref="paper",
              x0=0.08, y0=0.68, x1=0.32, y1=0.9,
              fillcolor="red", line_color="red")

# 버섯 갓 아래 둥근 곡선(흰색 테두리 느낌)
fig.add_shape(type="path",
              path="M0.08,0.79 Q0.20,0.72 0.32,0.79 L0.32,0.68 L0.08,0.68 Z",
              xref="paper", yref="paper",
              fillcolor="white", line_color="white")

# — 버섯 흰 점들 (크기와 위치 다양하게)
white_dots = [
    (0.14, 0.84, 0.035),
    (0.22, 0.83, 0.04),
    (0.27, 0.87, 0.03),
    (0.18, 0.88, 0.025),
    (0.25, 0.81, 0.03)
]
for (x, y, r) in white_dots:
    fig.add_shape(type="circle",
                  xref="paper", yref="paper",
                  x0=x - r, y0=y - r, x1=x + r, y1=y + r,
                  fillcolor="white", line_color="white")

# — 버섯 대 (베이지색, 둥근 사각형)
fig.add_shape(type="rect",
              xref="paper", yref="paper",
              x0=0.19, y0=0.5, x1=0.23, y1=0.68,
              fillcolor="#F5DEB3", line_color="#F5DEB3",
              layer="below")

fig.add_shape(type="circle",  # 대 위쪽 둥근 마무리
              xref="paper", yref="paper",
              x0=0.19, y0=0.66, x1=0.23, y1=0.70,
              fillcolor="#F5DEB3", line_color="#F5DEB3",
              layer="below")

fig.add_shape(type="circle",  # 대 아래쪽 둥근 마무리
              xref="paper", yref="paper",
              x0=0.19, y0=0.49, x1=0.23, y1=0.53,
              fillcolor="#F5DEB3", line_color="#F5DEB3",
              layer="below")

# 레이아웃 세팅
fig.update_layout(
    title="글로벌 시총 10위 기업 주가 (정교한 마리오 버섯 모양 데코 포함)",
    xaxis_title="날짜",
    yaxis_title="종가 (USD)",
    legend_title="기업",
    width=900,
    height=600,
    margin=dict(t=50, b=50, l=50, r=50)
)

fig.show()
