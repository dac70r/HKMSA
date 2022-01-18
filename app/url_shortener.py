#import function from db.py to here
from loguru import logger
import traceback
import os
import pymysql
from dotenv import load_dotenv

class URL_Shortnener:

    def __init__(self):#constructor
        pass

    def __del__(self):#destructor
        pass

    def insert_value(self,shortened_url:str,original_url:str):
        query = f"INSERT INTO url(shortened_url,original_url) VALUES(%s,%s)"
        args = [shortened_url,original_url]
        #bad_query = f"INSERT INTO url(shortened_url,original_url) VALUES({shortened_url},{original_url}})" sql injection
        rows = self.execute(query,args) # add self. -> something to do with oop

    def execute(self,query:str,args:list=[]) -> int:
        '''
        Execute a sql query 
        '''
        logger.info(f'execute() running...............')
        try:
            logger.info('Runnig test connection....') #more information on what is going on                
            con = pymysql.connect(host=os.getenv('HOST'), #inside is string
            user=os.getenv('USER'),password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE'))

            with con.cursor() as cur:
                rows = cur.execute(query,args=args)
                con.commit() #must commit otherwise all will be for nothing
 
        except Exception as e:
            logger.error(e)
            logger.error(traceback.format.exc())
            con.rollback()

        finally:
            return rows

if __name__ == '__main__':
    load_dotenv()
    urls = URL_Shortnener()      #created object urls
    urls.insert_value('1234567','www.google.com')
