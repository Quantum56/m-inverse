#!/usr/bin/env python

import re
import numpy as np
from fractions import Fraction

nx = 0

def main():
    print('Matrix inverse calculator (c) Quantum56 \n\n')
    print('Please input the matrix dimension (2-4):')
    try:
        nx = int(input("Please enter a number: "))
    except ValueError:
        print("Error ln 15")
    xa = getMatrix(nx)
    inva = getMatrixInverse(xa.tolist())
    print('\n')
    for ab in range(len(inva)):
        print(inva[ab])
    inv = np.array(list(inva))
    print('Attempt fractions? (y/n)')
    yn = str(input())
    print('\n')
    if('y' in yn or 'yes' in yn):
        i = 0
        j = 0
        li = emptyArr(nx)
        for i in range(nx):
            for j in range(nx):
                li[i][j] = str(Fraction(inv[i, j]).limit_denominator())
    for a in range(len(li)):
        print(li[a])

def getMatrix(n):
    try:
        if(n==2):
            print("Enter row 1 separated by spaces (e.g. 1 2):")
            r1 = str(input()).split()
            print("Enter row 2:")
            r2 = str(input()).split()
            r1 = [float(i) for i in r1]
            r2 = [float(i) for i in r2]
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
            r3 = [float(i) for i in r3]
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
    except ValueError:
        pass
    return x

def emptyArr(na):
    li = []
    ia = 0
    for l in range(na):
        li.append([])
    for la in range(na):
        for ls in range(na):
            li[ia].append(na)
        ia+=1
    return li

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transposeMatrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


if(__name__=="__main__"):
    main()