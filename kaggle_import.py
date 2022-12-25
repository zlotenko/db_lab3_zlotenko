import csv
import psycopg2

username = 'postgres'
password = 'alohomora26'
database = 'russian Equipment Losses'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'russian_losses.csv'

query_0 = '''
CREATE TABLE equip_new
(
    equip_id integer,
    equip_type character(200),
    model character(200),
    submodel character(200),
    country character(200),
    CONSTRAINT pk_equip_new PRIMARY KEY (equip_id)
)
'''


query_1 = '''
DELETE FROM equip_new
'''

query_2 = '''
INSERT INTO equip_new (equip_id, equip_type, country, model, submodel) VALUES (%s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    cur.execute(query_0)
    cur.execute(query_1)
    with open(INPUT_CSV_FILE, 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            values = (idx, row['equipment'], row['model'], row['sub_model'], row['manufacturer'])
            cur.execute(query_2, values)

    conn.commit()