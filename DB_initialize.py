import pandas as pd
from stock_code_manage import stock_code_list
from set_dataframe import tidy_df

def set_all_df():
  code_list = stock_code_list()
  df_list=[]
  for code_element in code_list:
    df_temp = tidy_df(code_element)
    df_temp.dropna(inplace=True)#이부분 tidy_df로 옮기자
    df_temp = df_temp.pivot(index='code', columns='date')
    print(df_temp.head())
    df_list.append(df_temp)
  df_main = pd.concat(df_list)
  return df_main
  #########
  #df_main = df_main.pivot(index='code', columns='date')
  #df_followed = tidy_df(220630)
  #df_followed = df_followed.pivot(index='code', columns='date')
  #df_main = merge_df(df_main, df_followed)
  #print(df_main)