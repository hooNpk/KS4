import pandas as pd
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()
#import MySQLdb

from set_dataframe import tidy_df
engine = create_engine("mysql+mysqldb://root:"+"myS@$r55t"+"@localhost/stock_inf_daily", encoding='utf-8')
con = engine.connect()

def write():
  df_hims = tidy_df()
  df_hims.to_sql(name='HIMS', con=engine, if_exists='append')

def main():
  write()

if __name__ == "__main__":
  main()