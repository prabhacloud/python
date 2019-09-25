import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sparkContext = SparkContext()
glueContext = GlueContext(sparkContext)
sparkSession = glueContext.spark_session


source_df = sparkSession.read.format("jdbc").option("url", "jdbc:shopify:RTK=XXXXXXX;AppId=XXXXXX;Password=XXXXXX;ShopUrl=https://XXXXXX.myshopify.com;").option("dbtable","Customers").option("driver","cdata.jdbc.shopify.ShopifyDriver").load()
glueJob = Job(glueContext)
glueJob.init(args['JOB_NAME'], args)

dynamic_dframe = DynamicFrame.fromDF(source_df, glueContext, "dynamic_df")

retDatasink4 = glueContext.write_dynamic_frame.from_options(frame = dynamic_dframe, connection_type = "s3", connection_options = {"path": "s3://shopify-data"}, format = "csv", transformation_ctx = "datasink4")

glueJob.commit()