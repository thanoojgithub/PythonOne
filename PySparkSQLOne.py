import pyspark.sql as sparksql

if __name__ == '__main__':
    print(sparksql.SparkSession)
    spark = sparksql.SparkSession.builder\
        .master("spark://thanoojubuntu-Inspiron-3521:7077")\
        .config("spark.sql.hive.metastore.version", "2.3.0")\
        .config("spark.sql.hive.metastore.jars", "/home/hduser/softwares/apache-hive-2.3.3-bin/lib/*")\
        .enableHiveSupport().getOrCreate()
    print(spark.version)
    srcDf = spark.sql("CREATE TABLE IF NOT EXISTS mydb.src (key INT, value STRING)")
    spark.sql("LOAD DATA LOCAL INPATH '/usr/local/spark-2.4.6-bin-hadoop2.7/examples/src/main/resources/kv1.txt' INTO "
              "TABLE mydb.src")
    spark.sql("SELECT * FROM mydb.src").show()
    spark.sql("SELECT COUNT(*) FROM mydb.src").show()
