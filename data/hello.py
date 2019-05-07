from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")
data = sc.textFile("/tmp/data/access_log.txt", 2)     # each worker loads a piece of the data file

# conn = MySQLdb.connect(host='db', port=3306, user='www', passwd='$3cureUS', db='cs4501')

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
count = pages.reduceByKey(lambda x,y: int(x)+int(y))        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for page_id, count in output:
    print ("page_id %s count %d" % (page_id, count))
print ("Popular items done")

sc.stop()
