#%%

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("shivam").getOrCreate()

#%%

data = [
    ("A",10,"pat"),
    ("B",20,"cat"),
    ("C",30,"dat"),
    ("D",40,"eat"),
]


schemma =['NAME','AGE','HOBBY']
df =spark.DataFrame(data,schemma)
# %%
# data manipulation

