from random import uniform
import time

def wait_between(a, b):
    rand = uniform(a, b)
    time.sleep(rand)