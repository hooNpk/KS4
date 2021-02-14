from decide_candidate import is_candidate
from get_fund_from_naver import return_fundamental
import pandas as pd
import psycopg2


conn_string = "host='localhost' dbname='postgres' user='postgres' password='secret'"
conn  = psycopg2.connect(conn_string)
cur = conn.cursor()

#cur.execute("CREATE TABLE candidates (code VARCHAR(10), sector VARCHAR(20), field VARCHAR(20), high_52weeks INT, low_52weeks INT, all_share INT, floating_share FLOAT, foreign_share FLOAT, y3_sale BIGINT, y3_profit BIGINT, y3_profit_ratio FLOAT, y3_debt_ratio FLOAT, y3_quick_ratio FLOAT, y3_per FLOAT, y2_sale BIGINT, y2_profit BIGINT, y2_profit_ratio FLOAT, y2_debt_ratio FLOAT, y2_quick_ratio FLOAT, y2_per FLOAT, y1_sale BIGINT, y1_profit BIGINT, y1_profit_ratio FLOAT, y1_debt_ratio FLOAT, y1_quick_ratio FLOAT, y1_per FLOAT, q4_sale BIGINT, q4_profit BIGINT, q4_profit_ratio FLOAT, q4_debt_ratio FLOAT, q4_quick_ratio FLOAT, q4_per FLOAT, q3_sale BIGINT, q3_profit BIGINT, q3_profit_ratio FLOAT, q3_debt_ratio FLOAT, q3_quick_ratio FLOAT, q3_per FLOAT, q2_sale BIGINT, q2_profit BIGINT, q2_profit_ratio FLOAT, q2_debt_ratio FLOAT, q2_quick_ratio FLOAT, q2_per FLOAT, q1_sale BIGINT, q1_profit BIGINT, q1_profit_ratio FLOAT, q1_debt_ratio FLOAT, q1_quick_ratio FLOAT, q1_per FLOAT, allo INT, allo_ratio FLOAT, PRIMARY KEY (code));")
#cur.execute("SELECT * FROM CANDIDATES;")

def iterate_all():
    #fund = return_fundamental()
    kospi = pd.read_csv('kospi_list.csv', header=1, encoding='euc-kr',
        names=['standard_code','short_code', '2', 'name',
        '3', '4', '5', '6', '7', '8', 'par', 'share_num'])[['standard_code', 'short_code', 'name', 'par', 'share_num']]
    kosdak = pd.read_csv('kosdaq_list.csv', header=1, encoding='euc-kr',
        names=['standard_code','short_code', '2', 'name',
        '3', '4', '5', '6', '7', '8', 'par', 'share_num'])[['standard_code', 'short_code', 'name', 'par', 'share_num']]

    kospi_code = kospi['short_code']
    
    for stock in kospi_code:
        info = return_fundamental(stock)
        if(info):
            if(is_candidate(info)):
                print("{0} is appropriate".format(stock))
                print(info)
                cur.execute("INSERT INTO candidates (code, sector, field, high_52weeks, low_52weeks, all_share, floating_share, foreign_share, y3_sale, y3_profit, y3_profit_ratio, y3_debt_ratio, y3_quick_ratio, y3_per, y2_sale, y2_profit, y2_profit_ratio, y2_debt_ratio, y2_quick_ratio, y2_per, y1_sale, y1_profit, y1_profit_ratio, y1_debt_ratio, y1_quick_ratio, y1_per, q4_sale, q4_profit, q4_profit_ratio, q4_debt_ratio, q4_quick_ratio, q4_per, q3_sale, q3_profit, q3_profit_ratio, q3_debt_ratio, q3_quick_ratio, q3_per, q2_sale, q2_profit, q2_profit_ratio, q2_debt_ratio, q2_quick_ratio, q2_per, q1_sale, q1_profit, q1_profit_ratio, q1_debt_ratio, q1_quick_ratio, q1_per, allo, allo_ratio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8][0], info[8][1], info[8][2], info[8][3], info[8][4], info[8][5], info[9][0], info[9][1], info[9][2], info[9][3], info[9][4], info[9][5], info[10][0], info[10][1], info[10][2], info[10][3], info[10][4], info[10][5], info[11][0], info[11][1], info[11][2], info[11][3], info[11][4], info[11][5], info[12][0], info[12][1], info[12][2], info[12][3], info[12][4], info[12][5],info[13][0], info[13][1], info[13][2], info[13][3], info[13][4], info[13][5], info[14][0], info[14][1], info[14][2], info[14][3], info[14][4], info[14][5], info[15], info[16]))
iterate_all()
