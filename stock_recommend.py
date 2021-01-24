import pandas as pd

kospi_code = pd.read_csv('kospi_list.csv', header=1, encoding='euc-kr',
    names=['standard_code','short_code', '2', 'name',
    '3', '4', '5', '6', '7', '8', 'par', 'share_num'])[['standard_code', 'short_code', 'name', 'par', 'share_num']]
#print(kospi_code.head())
kosdak_code = pd.read_csv('kosdaq_list.csv', header=1, encoding='euc-kr',
    names=['standard_code','short_code', '2', 'name',
    '3', '4', '5', '6', '7', '8', 'par', 'share_num'])[['standard_code', 'short_code', 'name', 'par', 'share_num']]
#print(kosdak_code.head(20))

from bs4 import BeautifulSoup
import requests
import numpy as np

def get_code(stock_name):
    #print("STOCK_NAME :::: ", stock_name)
    code = kosdak_code[kosdak_code['name']==stock_name]['short_code']
    code = code.to_string()
    code = code.split(' ')
    
    # for kospi
    if(code[-1]==')'):
        code = kospi_code[kospi_code['name']==stock_name]['short_code']
        code = code.to_string()
        code = code.split(' ')
    
    #print(code)   
    return (code[-1])

def get_url(stock_name, case): #어느 용도로 쓰느냐에 따라 url을 다르기 리턴해줘야할 필요가 있음
    code = get_code(stock_name)
    #종목 분석 url
    url = ''
    if(case=='brief'):
        url = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={code_num}'.format(code_num=code)
    elif(case =='main'):
        url = 'https://finance.naver.com/item/main.nhn?code={code_num}'.format(code_num=code)
    return(url)

def str_tidy(elem):
    elem = elem.replace(',', '')
    elem = elem.replace('\n', '')
    elem = elem.replace('\t', '')
    elem = elem.replace('\r', '')
    elem = elem.replace('%', '')
    elem = elem.replace('원', '')
    elem = elem.replace('주', '')
    elem = elem.replace(' ', '')
    return elem

def fundamental_df(stock_name):
    url = get_url(stock_name, 'brief')
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    soup.prettify()
    base_table = soup.find('div', {'id' : 'pArea'})
    
    #Base Information
    base_info = base_table.find_all('table')[0].find_all('dt', {'class' : 'line-left'})
    sector = base_info[1].get_text()
    field = base_info[2].get_text()

    print("sector :: {0} ##  field :: {1}".format(sector, field))

    # @@ For breif information on a stock
    brief_table = base_table.find('table', {'id' : 'cTB11'})
    trs = brief_table.find_all('td')
    high_low_52, share, foreign_share = str_tidy(trs[1].get_text()), str_tidy(trs[6].get_text()), str_tidy(trs[7].get_text())
    high_low_52 = high_low_52.split('/')
    high_52 = high_low_52[0]
    low_52 = high_low_52[1]
    share = share.split('/')
    all_stock_num = share[0]
    floating_share = share[1]
    
    print('52weeks high : {0} ## 52weeks low : {1} ## all stock num : {2} ## floating share : {3} ## foreign_share : {4}'.format(
        high_52,low_52, all_stock_num, floating_share, foreign_share))

    #FINANCIAL STATEMENTS
    url = get_url(stock_name, 'main')
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    finance_info = soup.select('div.section.cop_analysis div.sub_section')[0]

    th_data = [item.get_text().strip() for item in finance_info.select('thead th')]
    annual_date = th_data[3:7]
    quarter_date = th_data[7:13]

    finance_index = [item.get_text().strip() for item in finance_info.select('th.h_th2')][3:]
    finance_data = [item.get_text().strip() for item in finance_info.select('td')]
    finance_data = np.array(finance_data)
    finance_data.resize(len(finance_index), 10)

    finance_date = annual_date + quarter_date
    finance = pd.DataFrame(data=finance_data[0:, 0:], index=finance_index, columns=finance_date)
    print(finance)   
    
    
def compose_data_df(url):
    page = 1
    pg_url = '{url}'.format(url=url)
    
    #GET HTML Document
    r = requests.get(pg_url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc)
    soup.prettify()
    print(soup)
    day_price = soup.find('table', summary='외국인 기관 순매매 거래량에 관한표이며 날짜별로 정보를 제공합니다.')
    trs = day_price.find_all('tr')
    
    #data별 리스트
    date = []
    price = []
    diff = []
    diff_per = []
    volume = []
    gigwan = []
    foreign = []
    
    for i in range(3, len(trs)):
        tds = trs[i].find_all('td')
        if(i%8==0 or i%8==1 or i%8==2):
            #비어있는 td 들 빼주는 코드.
           continue
        date.append(tds[0].text)
        price.append(tds[1].text)
        diff.append(tds[2].text)
        diff_per.append(tds[3].text)
        volume.append(tds[4].text)
        gigwan.append(tds[5].text)
        foreign.append(tds[6].text)
    
    date = pd.Series(np.array(date))
    price = pd.Series(np.array(price))
    diff = pd.Series(np.array(diff))
    diff_per = pd.Series(np.array(diff_per))
    volume = pd.Series(np.array(volume))
    gigwan = pd.Series(np.array(gigwan))
    foreign = pd.Series(np.array(foreign))
    
    #Data Tidying
    date = pd.to_datetime(date, errors='coerce')
    price = price.apply(str_tidy)
    price = pd.to_numeric(price, errors='coerce')
    diff = diff.apply(str_tidy)
    diff = pd.to_numeric(diff, errors='coerce')
    diff_per = diff_per.apply(str_tidy)
    diff_per = pd.to_numeric(diff_per, errors='coerce', downcast='float')
    volume = volume.apply(str_tidy)
    volume = pd.to_numeric(volume, errors='coerce')
    gigwan = gigwan.apply(str_tidy)
    gigwan = pd.to_numeric(gigwan, errors='coerce', downcast='float')
    foreign = foreign.apply(str_tidy)
    foreign = pd.to_numeric(foreign, errors='coerce', downcast='float')
    
    df = pd.DataFrame({"date":date, "price":price, "diff":diff, "diff_per":diff_per, "volume":volume, "gigwan":gigwan,
                      "foreign":foreign})
    return df


df = fundamental_df('쎄트렉아이')