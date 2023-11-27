import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\vspy\TEST2\주식.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active

codes = [
    '005930', #삼성전자
    '000660', # SK 하이닉스
    '035720' #카카오
]
row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(price)
    ws[f'B{row}'] = int(price)
    row = row+1
wb.save(fpath)