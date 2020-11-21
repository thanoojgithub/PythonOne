import pyspark.sql as sparksql
from pyspark.sql import Row, SparkSession
from pyspark.sql.types import StructField, StringType, StructType


def sparkwithhiveone():
    print(sparksql.SparkSession)
    print(sparkwithhive.version)
    try:
        # sparkwithhive.sql("CREATE TABLE IF NOT EXISTS mydb.src (key INT, value STRING)") sparkwithhive.sql("LOAD
        # DATA LOCAL INPATH '/usr/local/spark-2.4.6-bin-hadoop2.7/examples/src/main/resources/kv1.txt' INTO TABLE
        # mydb.src")
        sparkwithhive.sql("SELECT * FROM mydb.src").show()
        sparkwithhive.sql("SELECT COUNT(*) FROM mydb.src").show()
    except Exception as e:
        print("Unexpected error:", e)
        raise
    finally:
        print("finally block")


def schema_inference_example(sparkobj):
    sc = sparkobj.sparkContext
    # Load a text file and convert each line to a Row.
    # HDFS DFS
    lines = sc.textFile("people.txt")
    parts = lines.map(lambda l: l.split(","))
    people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))
    # Infer the schema, and register the DataFrame as a table.
    schemapeople = spark.createDataFrame(people)
    schemapeople.createOrReplaceTempView("people")
    spark.sql("SELECT * FROM people").show()
    spark.sql("SELECT count(*) FROM people").show()
    # SQL can be run over DataFrames that have been registered as a table.
    teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")
    # The results of SQL queries are Dataframe objects.
    # rdd returns the content as an :class:`pyspark.RDD` of :class:`Row`.
    teennames = teenagers.rdd.map(lambda p: "Name: " + p.name).collect()
    for name in teennames:
        print(name)


def programmatic_schema_example(sparkobj):
    sc = sparkobj.sparkContext
    # Load a text file and convert each line to a Row.
    lines = sc.textFile("people.txt")
    parts = lines.map(lambda l: l.split(","))
    # Each line is converted to a tuple.
    people = parts.map(lambda p: (p[0], p[1].strip()))
    # The schema is encoded in a string.
    schemastring = "name age"
    fields = [StructField(field_name, StringType(), True) for field_name in schemastring.split()]
    schema = StructType(fields)
    print(fields)
    print(schema)
    # Apply the schema to the RDD.
    schemapeople = sparkobj.createDataFrame(people, schema)
    # Creates a temporary view using the DataFrame
    schemapeople.createOrReplaceTempView("people")
    # SQL can be run over DataFrames that have been registered as a table.
    results = sparkobj.sql("SELECT name FROM people")
    results.show()


if __name__ == '__main__':
    spark: SparkSession = sparksql.SparkSession.builder \
        .master("spark://thanoojubuntu-Inspiron-3521:7077") \
        .getOrCreate()

    sparkwithhive = sparksql.SparkSession.builder \
        .master("spark://thanoojubuntu-Inspiron-3521:7077") \
        .config("spark.sql.hive.metastore.version", "2.3.0") \
        .config("spark.sql.hive.metastore.jars", "/home/hduser/softwares/apache-hive-2.3.3-bin/lib/*") \
        .enableHiveSupport().getOrCreate()

    # sparkwithhiveone(sparkwithhive)
    # schema_inference_example(spark)
    programmatic_schema_example(spark)
    sparkwithhive.stop()
    spark.stop()
