from get_data_from_web import list_making_for_column
import psycopg2 as pg2

conn = pg2.connect(database='postgres', user='postgres', password='secret', host='127.0.0.1')
cur = conn.cursor()

cur.execute('SELECT code FROM candidates;')
codes = cur.fetchall()

for i in range(2):
    cur.execute('CREATE TABLE test%d(code varchar(10), date varchar(50) PRIMARY KEY, price integer, diff varchar(50), diff_per varchar(10), volume integer, gigwan varchar(50), foreigner varchar(50));' % i)
    columns = list_making_for_column(*codes[i])
    for row in zip(*columns):
        cur.execute('INSERT INTO test%d VALUES (%s);' % (i, ', '.join(row)))
    cur.execute('COMMIT;')

cur.close()