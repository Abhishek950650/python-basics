import logging # loggin ko import 

logging.basicConfig(
    level=logging.INFO, # info ke liye
    format='%(asctime)s-%(levelname)s-%(message)s', #format ke liye
    handlers=[
        logging.FileHandler('data/pipeline.log'), # pipeline file me save
        logging.StreamHandler() # console me bhi dikhao
    ]
)

logger = logging.getLogger(__name__) # har file ka ek apna logger

#logger use kro

logger.debug('Debug details - sirf developement me dikhega')
logger.info('Pipeline started')
logger.warning('null values found 5 rows')
logger.error('file not found sales.csv')
logger.critical('database connection lost')

