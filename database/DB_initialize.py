import pandas as pd
from stock_inf_manage import stock_code_list
from set_dataframe import tidy_df

from db_connect import write

def write_all_df():
  code_list = stock_code_list()
  for code_element in code_list:
    df_temp = tidy_df(code_element)
    #write(db_name, dataframe, stock_code)
    write('stock_inf_daily', df_temp, code_element)

def main():
  write_all_df()

if __name__=="__main__":
  main()