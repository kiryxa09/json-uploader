import schedule
import time
import subprocess

def execute_script():
    subprocess.Popen(["python", "nopatents-update.py"])

schedule.every().monday.at("15:00").do(execute_script)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)