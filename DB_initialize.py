import pandas as pd
from tidy_stock_code import tidy_code_kosdak, tidy_code_kospi
from set_dataframe import tidy_df

kosdak_code = tidy_code_kosdak()
kospi_code = tidy_code_kospi()

#여기가 메인이고 여기서 지금까지 짠 코드 총괄
def get_code(stock_name):
  code = kosdak_code['code'][stock_name]
  if code:
    return code
  else:
    code = kospi_code['code'][stock_name]
    return code

def merge_df(main, followed):
  return main.append(followed)

def kosdak_code_list():
  print(kosdak_code.head())

def main():
  #df_main = tidy_df(238490)
  #df_main = df_main.pivot(index='code', columns='date')
  #df_followed = tidy_df(220630)
  #df_followed = df_followed.pivot(index='code', columns='date')
  #df_main = merge_df(df_main, df_followed)
  #print(df_main)
  kosdak_code_list()

if(__name__ == "__main__"):
  main()