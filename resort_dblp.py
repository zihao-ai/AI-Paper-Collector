import json
import csv
import pandas as pd

with open('conf/dblp_conf.json','r') as f:
    json_data = json.load(f)

newlist = sorted(json_data, key=lambda d: d['name']) 
df=pd.json_normalize(newlist)
df.to_csv('conf/dblp_conf.csv', index=False, encoding='utf-8')