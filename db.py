#import package
import pymysql 
from loguru import logger
import traceback
from dotenv import load_dotenv
import os

#python function
#try, catch and 
def test_connection():
    #below try is what we actually want to execute 
    try:                
        con = pymysql.connect(host=os.getenv('HOST'), #inside is string
        user=os.getenv('USER'),password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'))

        with con.cursor() as cur:
            cur.execute('SELECT VERSION()')
            version = cur.fetchone()
            print(f'Database version: {version[0]}')

    except Exception as e:
        logger.error(e)
        logger.error(traceback.format.exc())

    finally:
        con.close()     #manually close the database


#Write the main function in python 
if __name__ == '__main__':
    load_dotenv()
    test_connection()



          

