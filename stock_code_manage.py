import pandas as pd
from set_dataframe import str_tidy

def tidy_code_kospi():
  kospi_code = pd.read_excel('kospi_list.xlsx', dtype='object')[['회사명', '종목코드']]
  kospi_code.columns = ['corporate_name', 'code']
  return kospi_code

def tidy_code_kosdak():
  kosdak_code = pd.read_excel('kosdak_list.xlsx', dtype='object')[['회사명', '종목코드']]
  kosdak_code.columns = ['corporate_name', 'code']
  return kosdak_code

kospi_code = tidy_code_kospi()
kosdak_code = tidy_code_kosdak()

def stock_code_list():
  #stock_code_list = pd.concat([kosdak_code['code'], kospi_code['code']], ignore_index=True)
  #return stock_code_list.to_list()
  stock_code_list = kosdak_code.iloc[3:13, 1]
  stock_code_list.apply(str_tidy)
  return stock_code_list.to_list()
  #return ['103840', '317530', '300080', '305090', '278280', '238490', '263800', '265520', '220630', '177350']

def get_code(stock_name):
  code = kosdak_code['code'][stock_name]
  if code:
    return code
  else:
    code = kospi_code['code'][stock_name]
    return code