import schedule
import time


#functions jo schedule karni hai

def get_weather_data():
    print('weather data fetch ho rha hai...')
    # pass

def generate_daily_report():
    print('daily report generate ho rha hai ...')
    # pass

def cleanup_old_files():
    print('files cleanup ho rha hai ...')
    # pass

def process_file(filename: str):
    print(f'processing : {filename}')



#schdule define karo
schedule.every(3).seconds.do(get_weather_data)
schedule.every(6).seconds.do(generate_daily_report)
# schedule.every(1).minutes.do(generate_daily_report)
# schedule.every().day.at('11:05').do(cleanup_old_files)
# schedule.every().day.do(process_file,filename='sales.csv')
print('scheduler started')

while True:
    schedule.run_pending()
    time.sleep(1)

# # Time based
# schedule.every(10).seconds.do(job)           # har 10 seconds
# schedule.every(5).minutes.do(job)            # har 5 minutes
# schedule.every(2).hours.do(job)              # har 2 ghante
# schedule.every().day.at("14:30").do(job)     # roz 2:30 PM
# schedule.every().hour.at(":15").do(job)      # har ghante ke :15 pe

# # Day based
# schedule.every().monday.do(job)              # har Monday
# schedule.every().wednesday.at("08:00").do(job)

# Job cancel karo
# job = schedule.every().day.do(process_file, filename="sales.csv")
# schedule.cancel_job(job)   # cancel karo