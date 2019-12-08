import pandas as pd

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
  stock_code_list = pd.concat([kosdak_code['code'], kospi_code['code']], ignore_index=True)
  return stock_code_list.to_list()

def get_code(stock_name):
  code = kosdak_code['code'][stock_name]
  if code:
    return code
  else:
    code = kospi_code['code'][stock_name]
    return code