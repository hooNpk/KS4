import pandas as pd
from db_connect import read_table
# read_table(db_name, table_name)
from datetime import date, timedelta

def get_code_data(stock_code):
  #db_name1 : 'avg_stock_inf'  db_name2 : 'stock_inf_daily'
  today = date.today()
  start = today+timedelta(days=-4)
  stock_avg_inf = read_table('avg_stock_inf', 'k'+str(stock_code), start, today)
  print(stock_avg_inf)


def is_crossed_ocurred(avg_inf):
  today = date.today()
  five_days_avg = avg_inf['fivedays_avg']
  twenty_days_avg = avg_inf['twentydays_avg']
  diff = twenty_days_avg - five_days_avg

def main():
  get_code_data('084850')

if __name__ == '__main__':
  main()