from bs4 import BeautifulSoup
import requests

from tidy_code import tidy_code_kosdak, tidy_code_kospi

kosdak_code = tidy_code_kosdak()
kospi_code = tidy_code_kospi()

def get_code(stock_name):
  code = kosdak_code['code'][stock_name]
  return code

def get_url(stock_code):
  url = 'http://finance.naver.com/item/frgn.nhn?code={code_num}'.format(code_num=stock_code)
  return url

def list_making_for_column():
  stock_name = '힘스'
  stock_code = get_code(stock_name)
  url = get_url(stock_code)

  date, price, diff, diff_per, volume, gigwan, foreign = [], [], [], [], [], [], []

  for page in range(1, 6):
    pg_url = '{url}&page={page_num}'.format(url=url, page_num=page)
    #GET HTML Document
    r = requests.get(pg_url)
    if(r):
      html_doc = r.text
      soup = BeautifulSoup(html_doc, features='lxml')
      soup.prettify()
      day_price = soup.find('table', summary='외국인 기관 순매매 거래량에 관한표이며 날짜별로 정보를 제공합니다.')
      trs = day_price.find_all('tr')

      for i in range(3, len(trs)):
        tds = trs[i].find_all('td')
        if(i%8==0 or i%8==1 or i%8==2):
          #비어있는 td를 빼주는 코드
          continue
        date.append(tds[0].text)
        price.append(tds[1].text)
        diff.append(tds[2].text)
        diff_per.append(tds[3].text)
        volume.append(tds[4].text)
        gigwan.append(tds[5].text)
        foreign.append(tds[6].text)

  return (date, price, diff, diff_per, volume, gigwan, foreign)