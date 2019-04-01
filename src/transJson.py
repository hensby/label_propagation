import json
import csv
import pandas as pd

with open("../output/LPResult.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
    print(type(load_dict))


# column_node1 = pd.Series(load_dict.keys(), name='node_1')
# column_node2 = pd.Series(load_dict.values(),name='node_2')
res = pd.DataFrame.from_dict(load_dict,orient='index')
print(res)
write_csv = "../output/LPResult.csv"

res.to_csv(write_csv)
