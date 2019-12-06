import pandas as pd

def tidy_code_kospi():
  kospi_code = pd.read_excel('kospi_list.xlsx')[['회사명', '종목코드']]
  kospi_code.columns = ['corporate_name', 'code']
  kospi_code.set_index('corporate_name', inplace=True)
  return kospi_code

def tidy_code_kosdak():
  kosdak_code = pd.read_excel('kosdak_list.xlsx')[['회사명', '종목코드']]
  kosdak_code.columns = ['corporate_name', 'code']
  kosdak_code.set_index('corporate_name', inplace=True)
  return kosdak_code