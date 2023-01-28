import time
from datetime import datetime
import sys


def hello():
    return "hello"


def run_clock():
    while True:
        now = datetime.now()
        # print(now.strftime("%Y-%m-%d %H:%M:%S"), end="", flush=True)
        # print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("asd")
        print("\r", end="", flush=True)
        time.sleep(1)
        # sys.stdout.flush()
        # print('\r')
        # time.sleep(1)

    # while True:
    #     print(strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
    #     print("\r", end="", flush=True)
    #     time.sleep(1)

run_clock()