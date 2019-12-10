import pandas as pd
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()

engine = create_engine("mysql+mysqldb://root:"+"myS@$r55t"+"@localhost/stock_inf_daily", encoding='utf-8')
con = engine.connect()

def write(df_to_db, stock_code):
  df_to_db.to_sql(name='k'+str(stock_code), con=engine, if_exists='replace')