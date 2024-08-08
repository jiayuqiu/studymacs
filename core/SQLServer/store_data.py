import pandas as pd
from sqlalchemy import create_engine
from alive_progress import alive_bar

import json
from glob import glob
import traceback
import time


MS_INFO = {
    'host': '192.168.152.133',
    'port': 1433,
    'user': 'sa',
    'password': '5cHC*J6x2B',
    'database': 'MacsDB'
}

engine = create_engine(
    f"mssql+pymssql://{MS_INFO['user']}:{MS_INFO['password']}@{MS_INFO['host']}:{MS_INFO['port']}/{MS_INFO['database']}"
)

with open(r"C:\Users\qiu\IdeaProjects\studymacs\core\utils\columns_map.json") as fp:
    column_dict = json.load(fp)

print(column_dict)


def time_str2int(dt_str):
    time_array = time.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    time_unix = int(time.mktime(time_array))
    return time_unix


class DataStore(object):
    def __init__(self, engine):
        self.engine = engine

    def store(self, df_list, table_name, ):
        conn = self.engine.connect()
        trans = conn.begin()
        insert_row_cnt = 0

        for _, df in enumerate(df_list):
            try:
                df.to_sql(
                    name=table_name,
                    if_exists='append',
                    index=False,
                    con=conn,
                    schema="VehicleLoad"
                )
                trans.commit()
                insert_row_cnt += df.shape[0]
            except:
                trans.rollback()
                traceback.print_exc()
        conn.close()
        return insert_row_cnt

    def run(self,):
        file_list = glob(r"F:\Virtual Servers\shares\基于单车整理后数据_7.16-7.31\*\*\*.csv")
        n = len(file_list)
        with alive_bar(n, force_tty=True) as bar:
            for _, f in enumerate(file_list):
                df_ = pd.read_csv(f)

                matched_col_dict = {}
                for col in df_.columns:
                    if "-" in col:
                        desc, pid = col.split("-")
                    else:
                        desc = col
                        pid = col

                    if desc in column_dict.keys():
                        matched_col_dict[col] = pid

                df_ = df_.loc[:, list(matched_col_dict.keys())]
                df_.rename(columns=matched_col_dict, inplace=True)
                df_.rename(columns=column_dict, inplace=True)
                df_.loc[:, 'clt_timestamp'] = df_['clt_timestamp'].map(lambda ts: time_str2int(ts))
                insert_row_cnt = self.store([df_], 'tab_collection_data')
                print(f"{_} / {n}, {f}, insert_cnt: {insert_row_cnt}")
                bar()


if __name__ == "__main__":
    ds = DataStore(engine)
    ds.run()
