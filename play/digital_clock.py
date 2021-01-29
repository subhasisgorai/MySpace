from __future__ import print_function
import time
import sys

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result, end="\r")
    sys.stdout.flush()
    time.sleep(1)
