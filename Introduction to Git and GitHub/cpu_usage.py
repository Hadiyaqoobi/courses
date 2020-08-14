#!/usr/bin/env python3

#This script uses the psutil module to check the percentage of the CPU that's currently in use.

import psutil


def check_cpu_usage(percent):
    usage = psutil.cpu_percnet()
    usage = psutil.cpu_percnet(1)
    print("DBUG: usage: {}".format(usage))
    
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
    
else:
    print("Everything is ok")
          
          