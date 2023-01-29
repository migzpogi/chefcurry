import time
from datetime import datetime
import sys


def hello():
    return "hello"


def run_clock():
    while True:
        now = datetime.now()
        sys.stdout.write("\r")
        sys.stdout.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        sys.stdout.flush()
        time.sleep(1)
