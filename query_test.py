import pandas as pd
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from datetime import date, timedelta, datetime
import time

'''
First of all, a Spark session needs to be initialized. 
With the help of SparkSession, DataFrame can be created and registered as tables. 
Moreover, SQL tables be executed, tables can be cached, and parquet/json/csv/avro data formatted files can be read.
'''

sc = SparkSession.builder.appName("PysparkExample")\
.config ("spark.sql.shuffle.partitions", "50")\
.config("spark.driver.maxResultSize","5g")\
.config ("spark.sql.execution.arrow.enabled", "true")\
.getOrCreate()

loading_start = time.time()
dataframe_csv = sc.read.option("header", True).csv('sample_HFT.csv')
loading_end = time.time()

print("Loading time is %s" % (loading_end - loading_start))

query_start = time.time()
dataframe_csv.select("StockSymbol").show(10)
query_end = time.time()

print("Query time is %s" % (query_end - query_start))