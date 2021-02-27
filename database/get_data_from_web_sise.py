from bs4 import BeautifulSoup
from get_fund_from_naver import str_tidy
from progressbar import ProgressBar
from time import sleep, time
import requests

def get_sise_url(code):
  url = 'https://finance.naver.com/item/sise_day.nhn?code={code_num}'.format(code_num=code)
  return url

def high_low_price(stock_code):
  url = get_sise_url(stock_code)
  MAXPAGE = 50

  high_price, low_price = [], []
  bar = ProgressBar()
  for page in bar(range(1, MAXPAGE)):
    pg_url = '{url}&page={page_num}'.format(url=url, page_num=page)
    r = requests.get(pg_url, headers={'User-Agent' : 'Mozilla/5.0'})
    if(r):
      html_doc = r.text
      soup = BeautifulSoup(html_doc, features='lxml')
      soup.prettify()
      highlow_price = soup.find('table', cellspacing='0')
      trs = highlow_price.find_all('tr')

      for i in range(2, len(trs)):
        tds = trs[i].find_all('td')
        if(i%8==0 or i%8==1 or i%8==7):
          continue
        high_price.append(tds[4].text)
        low_price.append(tds[5].text)
    sleep(0.1)
  return (high_price, low_price)

print('now crawling')
tik = time()
#print(*high_low_price('005930'), sep='\n\n')
high_low_price('005930')
tok = time()
print(tok - tik, 's spended', sep='')
