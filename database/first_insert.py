from get_data_from_web import list_making_for_column
import psycopg2 as pg2

conn = pg2.connect(database='postgres', user='postgres', password='secret', host='127.0.0.1')
cur = conn.cursor()

cur.execute('SELECT code FROM candidates;')
codes = cur.fetchall()

for i in range(2):
    print('CREATE TABLE test%d(code varchar(10), date varchar(50) PRIMARY KEY, price integer, diff integer, diff_per integer, volume integer, gigwan integer, foreigner integer);' % i)
    cur.execute('CREATE TABLE test%d(code varchar(10), date varchar(50) PRIMARY KEY, price integer, diff integer, diff_per integer, volume integer, gigwan integer, foreigner integer);' % i)
    columns = list_making_for_column(*codes[i])
    print(columns)
    for row in zip(*columns):
        cur.execute('INSERT INTO test%d VALUES (%s);' % (i, ', '.join(row)))
    cur.execute('COMMIT;')

cur.close()