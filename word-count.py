from __future__ import print_function
from operator import add
from pyspark.sql import SparkSession

import sys

if __name__ == "__main__":
  #  if len(sys.argv) != 2:
  #      print("Usage: wordcount <file>", file=sys.stderr)
  #      sys.exit(-1)

    stringToCount = "/home/sbenavidez/work/pruebaContador.txt"

    spark = SparkSession\
        .builder\
        .appName("Word Counter test environment")\
        .getOrCreate()

    lines = spark.read.text(stringToCount).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()