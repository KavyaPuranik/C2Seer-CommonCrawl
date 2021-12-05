import os
import time
for i in range(1,12):
	print (f"Indexing {i}\n\n\n")
	os.system(f"curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/commoncrawlindex/_bulk' --data-binary @kavyaoutputfile{i}.txt")
	time.sleep(1)
