import pandas as pd

from db_connect import write, read_table
#write(db_name, df_name, stock_code)
#read_table(db_name, table_name)


def avg_line():
  org_table = read_table('stock_inf_daily', 'k084850')
  
  avg_price = org_table.loc[:,'date':'code']
  
  fivedays_avg = org_table.loc[:, 'price']
  fivedays_avg = fivedays_avg.rolling(5).mean()
  avg_price['fivedays_avg'] = fivedays_avg

  twentydays_avg = org_table.loc[:, 'price'].rolling(20).mean()
  avg_price['twentydays_avg'] = twentydays_avg
  print(avg_price)
  return avg_price


def main():
  avg_line()

if __name__ == "__main__":
  main()