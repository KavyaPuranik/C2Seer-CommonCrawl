from datetime import datetime
from elasticsearch import Elasticsearch
import json,sys
import glob,os
from tqdm import tqdm
indexname = sys.argv[1]
indextype = sys.argv[2]
es = Elasticsearch()

'''
doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

'''
print ("Fetch the list of JSON files in the directory")
jsonList = glob.glob("kavyadata/*.txt")
print  (jsonList)
print()
#jsonList = jsonList[0:10]
i = 1
for jsonfile in tqdm(jsonList):
        filegen = "kavyaoutputfile" + str(i) + ".txt"
        os.system(f'node index1.js -f {jsonfile} --index {indexname} --type {indextype} -z {filegen} -o outp_kavya')
        i += 1
