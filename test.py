import webbrowser
import os
from ctypes import *
from random import random
from math import sqrt
import multiprocessing
from joblib import Parallel, delayed
import time

nums = []

def main():
    i = int(input("Input number of iterations: "))
    j = int(input("Input number of times iterated: "))
    jobs = []
    for x in range(j):
        p = multiprocessing.Process(target=monteCarlo, args=(i,))
        jobs.append(p)
        p.start()
    for job in jobs:
        job.join()
    fa = open("numslist.txt", "r")
    for x in fa:
        nums.append(float(x))
    print(average(nums))
    os.remove("numslist.txt")
    
def average(n):
    return sum(n) / len(n)

def monteCarlo(ia):
    inside = 0
    outside = 0

    for a in range(ia):
        x = random()
        y = random()
        z = sqrt((x)**2+(y)**2)
        if(z < 1):
            inside += 1
        else:
            outside += 1

    ratio = (inside / (outside + inside))
    print(4*ratio)
    f = open("numslist.txt", "a")
    f.write("{}\n".format(str(4*ratio)))
    f.close()

    return

if __name__ == '__main__':
    main()