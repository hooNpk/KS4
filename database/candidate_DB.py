from decide_candidate import is_candidate
import psycopg2

conn_string = "host='localhost' dbname='postgres' user='postgres' password='secret'"
conn  = psycopg2.connect(conn_string)
cur = conn.cursor()

#cur.execute("CREATE TABLE candidates (code VARCHAR(10), sector VARCHAR(20), field VARCHAR(20), high_52weeks INT, low_52weeks INT, all_share INT, floating_share FLOAT, foreign_share FLOAT, y3_sale BIGINT, y3_profit BIGINT, y3_profit_ratio FLOAT, y3_debt_ratio FLOAT, y3_quick_ratio FLOAT, y3_per FLOAT, y2_sale BIGINT, y2_profit BIGINT, y2_profit_ratio FLOAT, y2_debt_ratio FLOAT, y2_quick_ratio FLOAT, y2_per FLOAT, y1_sale BIGINT, y1_profit BIGINT, y1_profit_ratio FLOAT, y1_debt_ratio FLOAT, y1_quick_ratio FLOAT, y1_per FLOAT, q4_sale BIGINT, q4_profit BIGINT, q4_profit_ratio FLOAT, q4_debt_ratio FLOAT, q4_quick_ratio FLOAT, q4_per FLOAT, q3_sale BIGINT, q3_profit BIGINT, q3_profit_ratio FLOAT, q3_debt_ratio FLOAT, q3_quick_ratio FLOAT, q3_per FLOAT, q2_sale BIGINT, q2_profit BIGINT, q2_profit_ratio FLOAT, q2_debt_ratio FLOAT, q2_quick_ratio FLOAT, q2_per FLOAT, q1_sale BIGINT, q1_profit BIGINT, q1_profit_ratio FLOAT, q1_debt_ratio FLOAT, q1_quick_ratio FLOAT, q1_per FLOAT, allo INT, allo_ratio FLOAT, PRIMARY KEY (code));")

cur.execute("SELECT * FROM CANDIDATES;")
