#공휴일 걸러내는 모듈
#공공데이터포털 "특일 정보제공 서비스" 사용
#인증키 : VbQNuye6GhNGAQ00jwTa6eGyuFnBY%2B9bmGMYEVXsqBY94ARYroVyHA0WxwOse6em%2FdhcrPZUWBvsoCgl6sDrww%3D%3D

from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen

url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo'
def return_dayoff_list(year, month):
  queryParams = '?'+'ServiceKey=VbQNuye6GhNGAQ00jwTa6eGyuFnBY%2B9bmGMYEVXsqBY94ARYroVyHA0WxwOse6em%2FdhcrPZUWBvsoCgl6sDrww%3D%3D&solYear={year_r}&quote_plus={month_r}'.format(year_r=year, month_r=month)
  
  request = Request(url+queryParams)
  request.get_method = lambda:'GET'
  response_body = urlopen(request).read()
  print(response_body)

def main():
  return_dayoff_list('2018', '05')

if __name__ == "__main__":
  main()
