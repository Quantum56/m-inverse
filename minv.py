import re
import numpy as np
from fractions import Fraction

def main():
    print('Matrix inverse calculator (c) Quantum56 \n\n')
    print('Please input the matrix dimension (2-4):')
    try:
        n = int(input("Please enter a number: "))
    except ValueError:
        print("Error ln 11")
    if(n==2):
        print("Enter row 1 separated by spaces (e.g. 1 2):")
        r1 = str(input()).split()
        print("Enter row 2:")
        r2 = str(input()).split()
        print(r2)
        r1 = [float(i) for i in r1]
        r2 = [float(i) for i in r2]
        print(r2)
        x = np.array([r1, r2], dtype='float')
    elif(n == 3):
        print("Enter row 1 separated by spaces (e.g. 1 2 3):")
        r1 = str(input()).split()
        print("Enter row 2:")
        r2 = str(input()).split()
        print("Enter row 3:")
        r3 = str(input()).split()
        r1 = [float(i) for i in r1]
        r2 = [float(i) for i in r2]
        r3 = [float(i) for i in r2]
        x = np.array([r1, r2, r3], dtype='float')
    elif(n == 4):
        print("Enter row 1 separated by spaces (e.g. 1 2 3 4):")
        r1 = str(input()).split()
        print("Enter row 2:")
        r2 = str(input()).split()
        print("Enter row 3:")
        r3 = str(input()).split()
        print("Enter row 4:")
        r4 = str(input()).split()
        r1 = [float(i) for i in r1]
        r2 = [float(i) for i in r2]
        r3 = [float(i) for i in r3]
        r4 = [float(i) for i in r4]
        x = np.array([r1, r2, r3, r4], dtype='float')
    inv = np.linalg.inv(x)
    print(inv)
    print('Attempt fractions? (y/n)')
    yn = str(input())
    if('y' in yn or 'yes' in yn):
        i = 0
        j = 0
        li = []
        ia = 0
        li = []
        for l in range(n):
            li.append([])
        for la in range(n):
            for ls in range(n):
                li[ia].append(n)
            ia+=1
        for i in range(n):
            for j in range(n):
                print(inv[i, j], end=' ')
                li[i][j] = str(Fraction(inv[i, j]).limit_denominator())
                print(Fraction(inv[i, j]))
    print(li)

if(__name__=="__main__"):
    main()