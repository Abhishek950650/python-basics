def decorator(func): #orignal function argument aata hai (func)

    def warapper(): # wrapper <- nayi layer ke liye
        print('Starting Work ...')
        func()
        print('Done Work !!!')
        
    return warapper

@decorator
def process_data():
    print('Data is Processing')

################################################

#Real Use - har pipeline kitna time le rha h - track karo

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'time taking by function : {end-start:.2f} seconds')
    
    return wrapper

@timer
def load_data():
    print('loading 2 millions row')
    time.sleep(2)

@timer
def process_data():
    print('process data')
    time.sleep(3)

# load_data()
# loading 2 millions row
# time taking by function : 2.00 seconds
# process_data()
# process data
# time taking by function : 3.00 seconds

#################################################

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'time take to execute this function : {end-start:.2f} sec')
        return result
    return wrapper

@timer
def load_file(file_path: str):
    print(f'loading file path : {file_path}')
    return 'done'

@timer
def connect_db(host:str, port: int, db: str):
    print(f'connecting to {host}:{port}/{db}')
    return 'connected'


# load_file('data/sales_data.csv')

# connect_db('localhost', 4200, 'orders_db')


########################################################

# Tumhe ye banana hai:
# - Database connect karne ki koshish kare
# - 3 baar try kare
# - Har attempt ke beech 5 second wait kare

def retry(max_attempt: int, delay: int):
    
    def decorator(func):

        def wrapper(*args, **awargs):

            for attempt in range(1, max_attempt+1):
                try:
                    return func(*args, **awargs)
                except Exception as e:
                    print(f'attempt of connection {attempt}/{max_attempt} :{e}')

                    if attempt == max_attempt:
                        raise

                    time.sleep(delay)

        return wrapper
    
    return decorator


@retry(max_attempt=5, delay=3)
def conncet_db(host:str, port: int, db: str):
    print(f'database connection : {host}:{port}/{db}')
    raise ConnectionError('Connection Failed')


# conncet_db(host='localhost', port = 4100, db = 'elogbook')

##################################################################

def logger(func):

    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} start hua')
        func(*args, **kwargs)
        print(f'Function {func.__name__} khatam hua')
        
    return wrapper


@logger
def tesing_without_args():
    print('testing function is running')

tesing_without_args()
    
@logger
def tesing_with_args(name: str, address: str):
    print(f'testing function is running with args : {name} and {address}')

tesing_with_args(name='Abhishek', address='Noida')