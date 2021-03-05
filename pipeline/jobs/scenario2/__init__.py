from pipeline.shared.context import JobContext

from pyspark.sql.types import *
import pyspark.sql.functions as psf
from pyspark.ml.feature import HashingTF, IDF, Normalizer


def run(sc, environment):
    context = JobContext(sc, environment)

    struct = StructType([
        StructField("user_id", LongType(), True),
        StructField("book_id", LongType(), True),
        StructField("score", IntegerType(), True)
    ])

    context.log("INFO", "Loading FILE ratings data...")

    ratings_file = context.load_file('ratings.csv', 'csv', struct)
    context.log("INFO", "Loading DB ratings data...")
    ratings_db = context.load_db('public."Ratings"').select('user_id', 'book_id', 'score')
    ratings = ratings_file.union(ratings_db)

    ratings.show()

    context.log("INFO", "Saving ratings data...")

    context.save_db('public."Ratings"', ratings)
