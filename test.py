import requests
import urllib3
import time
# 3 baar retry kare
# 429 aane pe Retry-After header dekhe aur wait kare
# 500 pe 5 second wait karke retry kare
# Baaki errors pe turant raise kare

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RateLimitError:
    
    def __init__(self, retry_after: int):
        self.retry_after = retry_after

class ServerError:
    
    def __init__(self):
        pass

def retry(max_limit: int, time_delay: int):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for attempt in range(1, max_limit + 1):

                try:
                    response = func(*args, **kwargs)
                    return response

                except RateLimitError as e:
                    print(f'retry after {e.retry_after}')
                    time.sleep(e.retry_after)
                
                except ServerError:
                    print(f'Server error {attempt}/{max_limit}... waiting 5s')
                    if attempt == max_limit:
                        raise
                    time.sleep(time_delay)
                
                except Exception as e:

                    print(f'Unhandlled error is {e}')
                    raise

        return wrapper
    return decorator
    
@retry(max_limit=3, time_delay=5)
def api_fetcher(base_url: str):
    print(f'fetching data from {base_url}')

    response = requests.get(base_url,  verify=False)

    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 429:
        retry_after = int(response.headers.get('Retry-After', 60))
        raise RateLimitError(retry_after)
    elif response.status_code == 500:
        raise ServerError('Internal Server Error')
    else :
        response.raise_for_status()


api_fetcher('https://jsonplaceholder.typicode.com/posts/1')
                    
