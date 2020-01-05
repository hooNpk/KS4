import pandas as pd
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()

def write(db_name, df_to_db, stock_code):
  engine = create_engine("mysql+mysqldb://root:"+"myS@$r55t"+"@localhost/{db_name}".format(db_name=db_name), encoding='utf-8')
  con = engine.connect()
  df_to_db.to_sql(name='k'+str(stock_code), con=engine, if_exists='replace')
  print('complete writing!')
  con.close()

def read_table(db_name, table_name, start_date=None, end_date=None):
  conn = pymysql.connect(host='localhost', user='root', password='myS@$r55t', db=db_name, charset='utf8')
  curs = conn.cursor()

  if(start_date):
    sql = 'SELECT * FROM {table_name} WHERE DATE(date) BETWEEN \'{start}\' AND \'{end}\''.format(table_name=table_name, start=start_date, end=end_date)
  else:
    sql = 'SELECT * FROM {table_name}'.format(table_name=table_name)

  curs.execute(sql)
  rows = curs.fetchall()
  df = pd.DataFrame(rows)
  columns = curs.description
  columns = {columns[index][0] : column for index, column in enumerate(rows[0])}.keys()
  df.columns = columns
  
  conn.close()
  return df