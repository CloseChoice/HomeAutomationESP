import matplotlib.pyplot as plt
import pandas as pd
import sqlite3


connection = sqlite3.connect('database/temperature_humidity.db')

def plot_table_from_starttime(tablename, connection, start_time=None, outputname=None):
    sql = f'select * from {tablename}'
    if start_time:
        sql = sql + f' where receive_time > "{start_time}"'
    df = pd.read_sql(sql, con=connection)
    df['receive_time'] = pd.to_datetime(df['receive_time'])
    df.plot(x='receive_time',
            y=tablename.replace('fct_', ''),
            rot=90,
            )
    if outputname:
        plt.savefig(outputname)

plot_table_from_starttime('fct_temperature', connection, start_time='2020-01-01', outputname='test2.png')
