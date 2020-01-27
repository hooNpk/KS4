#공휴일 걸러내는 모듈
#공공데이터포털 "특일 정보제공 서비스" 사용
#인증키 :VbQNuye6GhNGAQ00jwTa6eGyuFnBY%2B9bmGMYEVXsqBY94ARYroVyHA0WxwOse6em%2FdhcrPZUWBvsoCgl6sDrww%3D%3D

import datetime
import requests
import bs4 as BeautifulSoup

url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?'

def return_dayoff_list(year, month):
  dayoff = []
  queryParams = 'solYear={year_r}&solMonth={month_r}&ServiceKey=VbQNuye6GhNGAQ00jwTa6eGyuFnBY%2B9bmGMYEVXsqBY94ARYroVyHA0WxwOse6em%2FdhcrPZUWBvsoCgl6sDrww%3D%3D'.format(year_r=year, month_r=month)
  r = requests.get(url+queryParams)
  body = r.text
  soup = BeautifulSoup.BeautifulSoup(body, features='lxml')
  soup.prettify()
  #print(soup)
  for date in soup.find_all('locdate'):
    dayoff.append(datetime.datetime.strptime(date.text, '%Y%m%d'))
  return dayoff

def is_dayoff(date):
  time_construct = date.timetuple()
  
  off_list = return_dayoff_list(time_construct.tm_year, time_construct.tm_mon)
  print(off_list)
  if(date in off_list):
    return True
  else:
    return False

def is_weekend(date):
  day = date.weekday()
  if(day==5 or day==6):
    return True
  else:
    return False

#def main():
#  print("공휴일 : "+str(is_dayoff('2020-05-05')))
#  print("주말 : "+str(is_weekend('2020-05-05')))

#if __name__ == "__main__":
#  main()
