# -*- coding: utf-8 -*-
"""
Created on Sat May 30 03:00:43 2020

@author: ishan.m.jain
"""

import requests
import random
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import threading
import logging

f = open("usernames3.csv", "r")
data = f.readlines()

logging.basicConfig(level=logging.INFO,
                        datefmt="%H:%M:%S")

active_threads = []

def check(un):
    time.sleep(random.random())
    url = "https://www.instagram.com/"+str(un[:3])
    x = requests.get(url, verify = False)
    if x.status_code == 200:
        logging.info("skip - " + un[:3]+ " - "+ str(data.index(un)) + " - " + str(x.status_code))
    else:
        logging.info("available - " + un[:3] + " - "+ str(data.index(un)) + f" - {x.status_code}")
        f2 = open("available.txt", "a")
        f2.write(un)
        f2.close()
    if int(data.index(un))%20 == 0:
        time.sleep(15)

for un in data:
    x = threading.Thread(target=check, args=(un,), daemon=True)
    x.start()
    logging.info(f"Trying {un[:3]}") 
    active_threads.append(x)
    time.sleep(1.25)
