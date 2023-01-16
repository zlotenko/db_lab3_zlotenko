import psycopg2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from textwrap import wrap

username = 'postgres'
password = 'alohomora26'
database = 'russian Equipment Losses'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW ModelLosses AS
SELECT model, losses_total
FROM equip_new
'''
query_2 = '''
CREATE VIEW TypeLosses AS
SELECT equip_type, SUM(losses_total)
FROM equip_new
GROUP BY equip_type

'''

query_3 = '''
CREATE VIEW TypeCaptured AS
SELECT equip_type, SUM(captured)
FROM equip_new
GROUP BY equip_type
'''
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("Database opened successfully")
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS ModelLosses')

    cur.execute(query_1)
    cur.execute('SELECT * FROM ModelLosses')
    equipment = []
    equip_losses = []
    for row in cur:
        equipment.append(row[0])
        equip_losses.append(row[1])

    cur.execute('DROP VIEW IF EXISTS TypeLosses')
    cur.execute(query_2)
    cur.execute('SELECT * FROM TypeLosses')
    types = []
    type_losses = []
    for row in cur:
        types.append(row[0])
        type_losses.append(row[1])

    cur.execute('DROP VIEW IF EXISTS TypeCaptured')
    cur.execute(query_3)
    cur.execute('SELECT * FROM TypeCaptured')
    types_with_captures = []
    type_captures = []
    for row in cur:
        if row[1]:
            types_with_captures.append(row[0])
            type_captures.append(row[1])

fig, (pie_ax) = plt.subplots(1, 1)


bar1_ax.set_title('Загальні втрати кожної моделі')
bar1_ax.set_xlabel('Модель')
bar1_ax.set_ylabel('Загальні втрати')
bar1_ax.bar(equipment, equip_losses)
fig.autofmt_xdate(rotation=45)


pie_ax.pie(type_losses, labels=types)
pie_ax.set_title('Загальні втрати по типам техніки')


bar2_ax.set_title('Захоплено техніки кожного типу')
bar2_ax.set_xlabel('Тип техніки')
bar2_ax.set_ylabel('Захоплено')
bar2_ax.bar(types_with_captures, type_captures)
fig.autofmt_xdate(rotation=45)

plt.get_current_fig_manager().resize(1900, 900)
plt.subplots_adjust(left=0.04,
                    bottom=0.321,
                    right=0.993,
                    top=0.967,
                    wspace=0.76,
                    hspace=0.195)

plt.show()