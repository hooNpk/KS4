import pandas as pd

from db_connect import write, read_table
#write(db_name, df_name, stock_code)
#read_table(db_name, table_name)
from stock_inf_manage import stock_code_list


def avg_line(stock_code):
  org_table = read_table('stock_inf_daily', 'k'+stock_code)
  
  avg_price = org_table.loc[:,'date':'code']
  
  fivedays_avg = org_table.loc[:, 'price']
  fivedays_avg = fivedays_avg.rolling(5).mean()
  avg_price['fivedays_avg'] = fivedays_avg

  twentyfivedays_avg = org_table.loc[:, 'price'].rolling(25).mean()
  avg_price['twentyfivedays_avg'] = twentyfivedays_avg
  print(avg_price)
  return avg_price


def main():
  code_list = stock_code_list()
  for elem in code_list:
    write('avg_stock_inf', avg_line(elem), elem)

if __name__ == "__main__":
  main()