from bs4 import BeautifulSoup
import requests

def get_sise_url(code):
  url = 'https://finance.naver.com/item/sise_day.nhn?code={code_num}'.format(code_num=code)
  return url

def high_low_price(stock_code):
  #stock_name='힘스'
  #stock_code = get_code(stock_name)
  url = get_sise_url(stock_code)

  high_price, low_price = [], []
  for page in range(1, 3):#11이였음
    pg_url = '{url}&page={page_num}'.format(url=url, page_num=page)
    r = requests.get(pg_url)
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
  return (high_price, low_price)