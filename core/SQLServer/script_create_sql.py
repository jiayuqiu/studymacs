import pandas as pd
import numpy as np
import json


df = pd.read_csv(r"F:\Virtual Servers\shares\基于单车整理后数据_7.16-7.31\基于单车整理后数据_7.16-7.31\SDCE_冀B3S670_LZFH25V45MD018222\SDCE_LZFH25V45MD018222_20230725193200_20230725235959_48.46.csv")
desc_pid_dict = {}
for c in df.columns:
    if "-" in c:
        desc, pid = c.split("-")
    else:
        desc = c
        pid = c

    desc_pid_dict[desc] = pid
print(desc_pid_dict)

# save description and pid map to a json file.
with open(r"C:\Users\qiu\IdeaProjects\studymacs\core\utils\columns_map.json", "w") as fp:
    json.dump(desc_pid_dict, fp, indent=4, ensure_ascii=False)

# create table sql
sql = f"""
CREATE TABLE MacsDB.tab_collection_data (
"""

for col, t_ in zip(df.dtypes.index, df.dtypes.values):
    print(f"{col}: {t_}", t_, type(t_))
    if "-" in col:
        desc, pid = col.split("-")
    else:
        desc = col
        pid = col

    if isinstance(t_, np.dtypes.Float64DType):
        print(t_)
        sql += f"{pid} FLOAT NULL , \n"
    else:
        print("not float64!!!")
        sql += f"{pid} FLOAT NULL, \n"
sql += ")"
print(sql)

print(df.head())
print(df.dtypes)
print(1)
