import pandas as pd
from stock_code_manage import stock_code_list
from set_dataframe import tidy_df

from db_connect import write

def write_all_df():
  code_list = stock_code_list()
  print(code_list)
  for code_element in code_list:
    df_temp = tidy_df(code_element)
    write(df_temp, code_element)
  
  #########
  #df_main = df_main.pivot(index='code', columns='date')
  #df_followed = tidy_df(220630)
  #df_followed = df_followed.pivot(index='code', columns='date')
  #df_main = merge_df(df_main, df_followed)
  #print(df_main)

def main():
  write_all_df()

if __name__ =="__main__":
  main()