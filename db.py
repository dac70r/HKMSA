#import package
import pymysql 
from loguru import logger
import traceback
from dotenv import load_dotenv
import os

#why we use logger instead of print?
#because it has colours and it allows us to track our code better
#logger has 4 components: logger.debug(),logger.warning(),logger.info(),logger.error()
#inside gua hu you put string, essentially the message that you want to output

#python function
#try, catch and finally 

def test_connection():
    #below try is what we actually want to execute 
    try:
        logger.info('Runnig test connection....') #more information on what is going on                
        con = pymysql.connect(host=os.getenv('HOST'), #inside is string
        user=os.getenv('USER'),password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'))

        with con.cursor() as cur:
            cur.execute('SELECT VERSION()')
            version = cur.fetchone()
            print(f'Database version: {version[0]}')
            #logger.error('Database version: {version[0]}')
            #logger.warning('Database version: {version[0]}')
            #logger.info('Database version: {version[0]}')   #used inside functions
            #logger.debug('Database version: {version[0]}')


    except Exception as e:
        logger.error(e)
        logger.error(traceback.format.exc())

    finally:
        con.close()     #manually close the database

def execute(query:str) -> int:
    logger.info(f'execute() running...............')
    try:
        logger.info('Runnig test connection....') #more information on what is going on                
        con = pymysql.connect(host=os.getenv('HOST'), #inside is string
        user=os.getenv('USER'),password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'))

        with con.cursor() as cur:
            rows = cur.execute(query)
            con.commit() #must commit otherwise all will be for nothing
 
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format.exc())
        con.rollback()

    finally:
        return rows


#Write the main function in python 
if __name__ == '__main__':
    load_dotenv()
    test_connection()
    query = f''' 

    CREATE TABLE url(

    --id (should be integer)
    id int AUTO_INCREMENT UNIQUE,--auto increments your insert 

    --hash
    shortened_url varchar(7) UNIQUE,

    --original url 
    original_url varchar(1000) NOT NULL, -- not null meaning bu hui shi kong de 

    PRIMARY KEY(id,shortened_url)
    

);
    
    
    '''
    execute(query)


          

