import schedule
import time

#this is a definition we must use to get reminders as shown below.
def Time_Reminder():
    print("Task executed at", time.strftime("%Y-%m-%d %H:%M:%S"))

# Schedule a task to run every day at a specific time (e.g., 14:30).
schedule.every().day.at("14:30").do(Time_Reminder)

# Schedule a task to run every hour.
schedule.every().hour.do(Time_Reminder)

# Schedule a task to run every 5 minutes.
schedule.every(5).minutes.do(Time_Reminder)

# Main loop to execute scheduled tasks.
while True:
    schedule.run_pending()
    time.sleep(1)
