from bs4 import BeautifulSoup
from get_fund_from_naver import str_tidy
from time import sleep, time
from progressbar import ProgressBar
import requests

def get_url(stock_code):
  url = 'http://finance.naver.com/item/frgn.nhn?code={code_num}'.format(code_num=stock_code)
  return url

def list_making_for_column(stock_code):
  #stock_name = '힘스'
  #stock_code = get_code(stock_name)
  url = get_url(stock_code)
  MAXPAGE = 50

  code, date, price, diff, diff_per, volume, gigwan, foreign = [], [], [], [], [], [], [], []

  bar = ProgressBar()
  for page in bar(range(1, MAXPAGE)):
    pg_url = '{url}&page={page_num}'.format(url=url, page_num=page)
    r = requests.get(pg_url, headers = {'User-Agent' : 'Mozilla/5.0'})
    if(r):
      html_doc = r.text
      soup = BeautifulSoup(html_doc, features='lxml')
      soup.prettify()
      day_price = soup.find('table', summary='외국인 기관 순매매 거래량에 관한표이며 날짜별로 정보를 제공합니다.')
      trs = day_price.find_all('tr')

      for i in range(3, len(trs)):
        tds = trs[i].find_all('td')
        if 0 <= i%8 < 3:
          #비어있는 td를 빼주는 코드
          continue
        
        date.append(tds[0].text)
        code.append(stock_code)
        price.append(tds[1].text)
        if '상승' in str(tds[2]):
          diff.append('+')
        elif '하락' in str(tds[2]):
          diff.append('-')
        else:
          diff.append('')
        diff[-1] += str_tidy(tds[2].text)
        diff_per.append(tds[3].text.replace('\t', '').replace('\n', '').replace('%', ''))
        volume.append(str_tidy(tds[4].text))
        gigwan.append(tds[5].text)
        foreign.append(tds[6].text)
    else:
      print('page None : ', page)
    sleep(0.1)

  return (code, date, price, diff, diff_per, volume, gigwan, foreign)

print('now crawling')
tik = time()
#print(*list_making_for_column('005930'), sep='\n\n')
list_making_for_column('005930')
tok = time()
print(tok - tik, 's spended', sep='')
