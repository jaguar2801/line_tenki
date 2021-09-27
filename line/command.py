import subprocess
from subprocess import PIPE
import schedule
import time

def job():
    subprocess.run(["python", "line_send.py"])

schedule.every().day.at("08:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
