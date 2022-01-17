#import package
import pymysql 
from loguru import logger
import traceback

#python function
#try, catch and 
def test_connection():
    x = 0
    try:                #what we wanna execute, hrllo
        pass
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format.exc())
    finally:
        return 


          

