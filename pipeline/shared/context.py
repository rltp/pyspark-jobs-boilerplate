import logging
from pyspark.sql import SQLContext
from pipeline.utils import filepath


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JobContext(object):

    def __init__(self, sc, environment):
        self.sqlContext = SQLContext(sc)
        self.session = self.sqlContext.sparkSession
        self.environment = environment

    def log(self, level, message):
        types = {
            "DEBUG" : 10,
            "INFO" : 20,
            "WARNING" : 30,
            "ERROR" : 40,
            "CRITICAL": 50
        }
        try:
            logger.log(types[level], message)
        except:
            logger.warning("Level not defined")
            logger.info(message)

    def save_db(self, dbtable, dataframe):
        dataframe.write.format("jdbc") \
            .mode("overwrite") \
            .options(dbtable=dbtable, **self.environment["sqlOptions"]) \
            .save()

    def load_db(self, dbtable):
        return self.session.read.format("jdbc").options(
            driver = "org.postgresql.Driver",
            sslfactory = "org.postgresql.ssl.NonValidatingFactory",
            dbtable = dbtable,
            **self.environment["sqlOptions"]
        ).load()

    def load_static_file(self, objectfile, format, schema):
        self.log('INFO', (filepath('shared/data/%s' % objectfile)))
        return (self.session
            .read.format(format)
            .schema(schema)
            .option("header", "true")
            .option("inferschema", "false")
            .load(filepath('shared/data/%s' % objectfile))
        )

    def load_file(self, filepath, format, schema):
        return (self.session
            .read.format(format)
            .schema(schema)
            .option("header", "true")
            .option("inferschema", "false")
            .load(filepath)
        )
    
    def save_file(self, filepath, format, dataframe):
        dataframe.write.format(format).save(filepath)

