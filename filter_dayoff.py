#공휴일 걸러내는 모듈
#공공데이터포털 "특일 정보제공 서비스" 사용
#인증키 :VbQNuye6GhNGAQ00jwTa6eGyuFnBY%2B9bmGMYEVXsqBY94ARYroVyHA0WxwOse6em%2FdhcrPZUWBvsoCgl6sDrww%3D%3D

from urllib.parse import urlencode, quote_plus
import requests
import pandas as pd
import bs4 as BeautifulSoup

url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?'
def return_dayoff_list(year, month):

  dayoff = []
  
  queryParams = 'solYear={year_r}&solMonth={month_r}&ServiceKey=VbQNuye6GhNGAQ00jwTa6eGyuFnBY%2B9bmGMYEVXsqBY94ARYroVyHA0WxwOse6em%2FdhcrPZUWBvsoCgl6sDrww%3D%3D'.format(year_r=year, month_r=month)
  r = requests.get(url+queryParams)
  body = r.text
  soup = BeautifulSoup.BeautifulSoup(body, features='lxml')
  soup.prettify()

  for date in soup.find_all('locdate'):
    dayoff.append(pd.to_datetime(date.text))
  return dayoff

def is_weekend(date):


def main():
  a = return_dayoff_list('2020', '04')

if __name__ == "__main__":
  main()
