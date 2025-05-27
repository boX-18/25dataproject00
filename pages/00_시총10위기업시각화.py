import yfinance as yf
import plotly.graph_objs as go

# 글로벌 시총 10위 기업 티커 (2025년 기준 예시)
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "BRK-B", "NVDA", "META", "TSM", "V"]

data = []
for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")  # 최근 1개월 데이터
    data.append(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name=ticker))

fig = go.Figure(data=data)
fig.update_layout(title="글로벌 시총 10위 기업 주식 종가 (최근 1개월)", xaxis_title="날짜", yaxis_title="종가(USD)")
fig.show()
