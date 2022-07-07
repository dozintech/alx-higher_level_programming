#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime


for i in range(100):
    sleep(random.random())
    sys.stdout.write(
        "{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            datetime.datetime.now(),
            '/projects/260',
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        ))
    sys.stdout.flush()
