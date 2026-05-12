import time
import requests
from functools import wraps

def retry(max_attempts: int = 3, delay: int = 2):
    """
    Decorator — kisi bhi function pe lagao, automatically retry karega
    Real use: API calls, DB connections
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                
                except Exception as e:
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    
                    if attempt == max_attempts:
                        raise  # sabhi attempts fail — ab error uthao
                    
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
        
        return wrapper
    return decorator


# Use karo — sirf @retry lagao
@retry(max_attempts=3, delay=2)
def fetch_api_data(url: str):
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # 4xx/5xx pe exception uthata hai
    return response.json()


data = fetch_api_data("https://api.example.com/orders")