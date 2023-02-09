import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row 
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from sharepoint import download_file_sharepoint
import pandas as pd

# set file name
file_name = '<file_name>'

# set the folder name
folder_name = '<folder_name>'

#set file type
file_type = ''
for i in file_name[::-1]:
    if i  == '.':
        break
    file_type += i

file_type = file_type[::-1]

#set file location
file_loc = "file:///config/workspace/"+file_name


download_file_sharepoint(folder_name,file_name)


spark = SparkSession.builder \
	.master("local").appName("hive_pyspark").enableHiveSupport().getOrCreate()

print(file_type)
print(file_loc)

if file_type=='csv':
    datafile=spark.read.csv(file_loc,header=True)

elif file_type == 'xlsx' or file_type == '.xls':
    datafile = pd.read_excel(file_loc, engine='openpyxl')
    datafile = spark.createDataFrame(datafile)

else:
    print("Incorrect File Format")
    exit() 
    
#Typecasting
datafile = datafile.withColumn("id", datafile["id"].cast(IntegerType()))
datafile.show(5)
query_to_create_table =  """create table if not exists saascsd(
            id int,
            name string
            )
            row format delimited 
            fields terminated by ',';
            """
spark.sql(query_to_create_table)
df= spark.sql("describe new_sharepoint_table")
df.show()
datafile.write.insertInto('default.new_sharepoint_table', overwrite=False)
df1=spark.sql("select * from new_sharepoint_table")
df1.show()
