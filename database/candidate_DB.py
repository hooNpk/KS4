from decide_candidate import is_candidate
import psycopg2

conn_string = "host='localhost' dbname='postgres' user='postgres' password='secret'"
conn  = psycopg2.connect(conn_string)
cur = conn.cursor()
