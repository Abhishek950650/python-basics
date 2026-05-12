# src/config.py — project ka config loader
from dotenv import load_dotenv
from pathlib import Path
import os

# .env file load karo
load_dotenv()

class Config:

    API_KEY     = os.environ.get('API_KEY', 'abc123')
    BATCH_SIZE     = int(os.environ.get('BATCH_SIZE', '1000'))
    
    @classmethod
    def validate(cls):
        """Zaruri config check karo startup pe"""
        required = ['API_KEY', 'BATCH_SIZE']
        missing  = [key for key in required 
                   if not os.environ.get(key)]
        
        if missing:
            raise ValueError(f"Missing config: {missing}")
        
        print("✅ Config valid!")


# Use karo
config = Config()
Config.validate()

print(config.API_KEY)     # localhost
print(config.BATCH_SIZE)   # /home/abhishek/sales_pipeline/data/input