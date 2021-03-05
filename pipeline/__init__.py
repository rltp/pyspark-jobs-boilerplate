import os
import time
import importlib
import threading

from pipeline.utils import filepath, listdir
from pipeline.shared.context import logger
from pyspark import SparkContext, SparkConf

threads = []

def createJobsThread(sc, environment):
    global threads

    for job_name in listdir('jobs'):
        try:
            logger.info("Job '%s' preparation" % job_name)
            job_module = importlib.import_module('pipeline.jobs.%s' % job_name)
            
            thread = threading.Thread(
                target=job_module.run,
                name=job_name,
                args=(sc, environment)
            )
            thread.daemon = True
            threads += [thread]

        except Exception as e:
            logger.error(e)


def startJobsThread():
    global threads

    for job in threads:
        try:
            start = time.time()
            job.start()
            job.join()
            end = time.time()
            logger.info("Execution of '%s' job took %s seconds" %
                        (job.name, end - start))
        except Exception as e:
            logger.error(e)


def main(name, conf, environment):

    sc = SparkContext(appName=name, conf=conf)

    createJobsThread(sc, environment)

    startJobsThread()
