import pandas as pd
from db_connect import read_table
# read_table(db_name, table_name)
from datetime import date, timedelta
from filter_dayoff import is_dayoff, is_weekend

def get_code_data(stock_code):
  #db_name1 : 'avg_stock_inf'  db_name2 : 'stock_inf_daily'
  today = date.today()
  start = get_date_8days_ago(today)
  stock_avg_inf = read_table('avg_stock_inf', 'k'+str(stock_code), start, today)
  stock_daily_inf = read_table('stock_inf_daily', 'k'+str(stock_code), start, today)
  return (stock_avg_inf, stock_daily_inf)

def get_date_8days_ago(start):
  i=0
  date = start
  while(i<8):
    off = is_dayoff(date) or is_weekend(date)
    if(not(off)):
      i=i+1
    date = date+timedelta(days=-1)
  return date

def is_qualified():
  #check two things
  #whether stock price line and twenty-price line crossed in 3 days - 3일 이내에 크로스 발생했는지
  #doesn't ocurred cross again in 8 days - 8일 이내에 크로스가 발생했었는데 한 번 더 발생한 건 아닌지 확인
  daily_inf, avg_inf = get_code_data('084850')

  cur_price = daily_inf['price']
  twenty_days_avg = avg_inf['twentydays_avg']
  print(cur_price)
  print(twenty_days_avg)

def main():
  is_qualified()

if __name__ == '__main__':
  main()