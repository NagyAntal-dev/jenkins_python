#!/usr/bin/env python

import time
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--time",type=int, default=1, help="Time to sleep")
    
    args = parser.parse_args()
    
    for i in range(10):
        print(i+1)
        time.sleep(args.time)