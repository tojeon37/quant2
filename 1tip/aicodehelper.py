
# aicodehelper 단축키
# https://www.youtube.com/watch?v=SQPLPPb_LuE

# Ctrl+Alt+Shift+z 주석달기
# Ctrl+Alt+Shift+r 리팩토링
# Ctrl+Alt+Shift+c 코드리뷰
# Ctrl+Alt+Shift+g 자연어명령->코드
# Ctrl+Alt+Shift+m 개발 이외 일반적인 질문

# 필요한 라이브러리 import
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# 네이버 금융에서 삼성전자의 1년간 시가, 고가, 저가, 종가 데이터 가져와서 그려줘  Ctrl+Alt+Shift+g

# requests 라이브러리를 이용하여 url에서 html 코드를 가져온다.
url = "https://finance.naver.com/item/sise_day.nhn?code=005930"
html = requests.get(url).text

# BeautifulSoup 라이브러리를 이용하여 html 코드를 파싱한다.
soup = BeautifulSoup(html, "html.parser")

# html 코드에서 첫번째로 발견되는 table 태그를 찾아서 가져온다.
table = soup.find_all("table")[0]

# pandas 라이브러리를 이용하여 table 태그 안에 있는 데이터를 가져온다.
df = pd.read_html(str(table))[0]

# 결측치가 있는 행을 제거한다.
df = df.dropna()

# 데이터를 전처리한다.
# 역순으로 정렬하고, 인덱스를 재설정한다.
df = df.iloc[::-1]
df = df.reset_index(drop=True)

# 컬럼명을 변경하고, 날짜 데이터를 datetime 형식으로 변환한다.
df = df.rename(columns={"날짜": "date", "시가": "open", "고가": "high", "저가": "low", "종가": "close"})
df["date"] = pd.to_datetime(df["date"])

# 그래프를 그린다.
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["high"], label="고가")
plt.plot(df["date"], df["low"], label="저가")
plt.plot(df["date"], df["close"], label="종가")
plt.legend()
plt.title("삼성전자 1년간 시가고가저가종가")
plt.xlabel("날짜")
plt.ylabel("주가")
plt.show()