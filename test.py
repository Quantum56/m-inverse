import os.path
from ctypes import *
from random import random
from math import sqrt
import multiprocessing
from joblib import Parallel, delayed
import time

def main():
    nums = []
    print("Pi Calculator using Monte-Carlo Method (C) Zack Bartley")
    i = int(input("Input number of iterations: "))
    j = int(input("Input number of times iterated: "))
    jobs = []
    for x in range(j):
        p = multiprocessing.Process(target=monteCarlo, args=(i,))
        jobs.append(p)
        p.start()
    p.join()
    fa = open("numslist.txt", "a+")
    ia = 1
    while os.path.isfile(str(ia) + ".txt"):
        f1 = open(str(ia) + ".txt")
        y1 = f1.readline()
        fa.write(y1)
        ia += 1
        f1.close()
    fa.close()
    fb = open("numslist.txt", "r")
    for x in fb:
        nums.append(float(x))
    print(average(nums))
    fb.close()
    deleteFunc()

def average(n):
    return sum(n) / len(n)

def deleteFunc():
    dir_name = os.getcwd()
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".txt"):
            os.remove(os.path.join(dir_name, item))

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
    boll = False
    a = 1
    while not boll:
        if not os.path.isfile(str(a) + ".txt"):
            f = open((str(a) + ".txt"), "w")
            boll = True
        else:
            a += 1
    f.write("{}\n".format(str(4*ratio)))
    f.close()

    return

if __name__ == '__main__':
    main()