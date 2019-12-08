import pandas as pd
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()

from DB_initialize import set_all_df
engine = create_engine("mysql+mysqldb://root:"+"myS@$r55t"+"@localhost/stock_inf_daily", encoding='utf-8')
con = engine.connect()

def write():
  df_hims = set_all_df()
  df_hims.to_sql(name='things_daily', con=engine, if_exists='append')

def main():
  write()

if(__name__=='__main__'):
  main()