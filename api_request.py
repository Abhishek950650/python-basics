import requests
import urllib3
import logging
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('https://jsonplaceholder.typicode.com/posts/1', verify=False)

# print(response.json())
# print(response.status_code)
# print(response.headers)
# print(response.text)

# Status codes
# 2xx = Success
# 200 → OK
# 201 → Created
# 204 → No Content

# 3xx = Redirect
# 301 → Moved Permanently

# 4xx = Client Error (tumhari galti)
# 400 → Bad Request
# 401 → Unauthorized (login chahiye)
# 403 → Forbidden (permission nahi)
# 404 → Not Found
# 429 → Too Many Requests (rate limit)

# 5xx = Server Error (server ki galti)
# 500 → Internal Server Error
# 503 → Service Unavailable

# Check karo
if response.status_code == 200:
    data = response.json()
    print('--------------')
    print(f'response successfully {data}')
elif response.status_code == 404:
    print("Resource nahi mila!")
elif response.status_code == 429:
    print("Rate limit hit! Wait karo...")

# Shortcut — 4xx/5xx pe automatically exception
response.raise_for_status()   # 400+ pe HTTPError raise karta hai

#------ Parameters, Headers, Authentication
import requests

# Query Parameters — URL mein ?key=value
response = requests.get(
    'https://api.example.com/orders',
    params={
        'city'     : 'Delhi',
        'min_amount': 500,
        'page'     : 1,
        'limit'    : 100
    }
    # URL banta hai:
    # https://api.example.com/orders?city=Delhi&min_amount=500&page=1&limit=100
)

# Headers — API key, content type
response = requests.get(
    'https://api.example.com/data',
    headers={
        'Authorization': 'Bearer your_api_key_here',
        'Content-Type' : 'application/json',
        'Accept'       : 'application/json'
    }
)

# Basic Authentication
response = requests.get(
    'https://api.example.com/secure',
    auth=('username', 'password')
)

# API Key as parameter
response = requests.get(
    'https://api.example.com/data',
    params={'api_key': 'your_key_here'}
)

#----------------POST Request — Data Bhejana
import requests
import json

# POST — JSON data bhejo
payload = {
    'order_id': 'ORD001',
    'customer': 'Rahul',
    'amount'  : 700,
    'city'    : 'Delhi'
}

response = requests.post(
    'https://api.example.com/orders',
    json    = payload,    # ← automatically JSON serialize + Content-Type set
    headers = {'Authorization': 'Bearer token123'}
)

print(response.status_code)  # 201 Created
print(response.json())       # {'id': 'ORD001', 'status': 'created'}

# Form data bhejana (json nahi)
response = requests.post(
    'https://api.example.com/upload',
    data = {'name': 'Rahul', 'city': 'Delhi'}  # form data
)


#-----------------Timeout & Error Handling — Production Must!
import requests
from requests.exceptions import (
    Timeout,
    ConnectionError,
    HTTPError,
    RequestException
)

def fetch_data(url: str) -> dict:
    try:
        response = requests.get(
            url,
            timeout = (5, 30),  # (connect timeout, read timeout) seconds
            headers = {'Authorization': 'Bearer token123'}
        )

        # 4xx/5xx pe exception
        response.raise_for_status()

        return response.json()

    except Timeout:
        print("❌ Request timeout ho gaya!")
        raise

    except ConnectionError:
        print("❌ Server se connect nahi ho pa raha!")
        raise

    except HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code}")
        raise

    except RequestException as e:
        print(f"❌ Request failed: {e}")
        raise

#-------Session — Multiple Requests Efficient Banana

import requests

# Bina Session — har request naya connection banata hai (slow!)
for i in range(100):
    requests.get('https://api.example.com/data')  # 100 baar connect/disconnect

# Session ke saath — ek connection, 100 requests (fast!)
with requests.Session() as session:
    # Common headers ek baar set karo
    session.headers.update({
        'Authorization': 'Bearer token123',
        'Content-Type' : 'application/json'
    })

    # Ab har request mein headers automatically jayenge
    for page in range(1, 11):
        response = session.get(
            'https://api.example.com/orders',
            params={'page': page, 'limit': 100}
        )
        data = response.json()
        print(f"Page {page}: {len(data)} records")

#------------------Pagination — Large Data Fetch Karna

logger = logging.getLogger(__name__)


def fetch_all_pages(base_url: str, api_key: str) -> pd.DataFrame:
    
    print(f'get data from {base_url}')

    page = 1
    all_records = []
    with requests.Session() as session:
        session.headers.update(
            {'Authorization' : f'Bearer {api_key}'}
        )

        while True:
            logger.info(f'fetching page {page}...')

            response = session.get(
                base_url,
                params= {'page':page, 'limit':100},
                timeout=(5,20)
            )

            response.raise_for_status()

            data = response.json()

            #data khatam ?

            records = data.get('records', [])

            if not records:
                logger.info('sab page fetch ho gya')
                break
                
            all_records.extend(records)
            logger.info(f'Page {page}: {len(records)} records fetched')

            #next page hai ?
            if not data.get('has_next_page', False):
                break
                
            page += 1

    df = pd.DataFrame(all_records)
    logger.info(f'total records : {len(df)}')
    return df


