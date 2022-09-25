import numpy as np
from sympy import Matrix
from fractions import Fraction

LimitDeno = 1000

def nequals (a, b):
    return abs(a - b) > 0.000001

def output (a, End):
    if a < 0:
        print('-', end = '')
        a = abs(a)
    c = Fraction(a).limit_denominator(LimitDeno)
    if c.denominator == 1:
        print(c.numerator, end = End)
    else:
        print('\\frac{{{0}}}{{{1}}}'.format(c.numerator, c.denominator), end = End)

def uniPrint(A, I):
    n = np.size(A, 0)
    m = np.size(A, 1)

    for i in range(n):
        for j in range(m):
            print(A[i][j], end = " ")
        
        print(" | ", end = " ")

        for j in range(n):
            print(I[i][j], end = " ")
        
        print("")

def formatPrint(A):
    n = np.size(A, 0)
    m = np.size(A, 1)

    print('\left[\\begin{array}{', end = "")
    for i in range(m): print('c', end = "")
    print('}')

    for i in range(n):
        for j in range(m - 1):
            output(A[i][j], " & ")

        output(A[i][m - 1], " ");
        
        if i != n - 1:
            print('\\\\')
        else:
            print('')

    print("\end{array}\\right]")

def uniFormatPrint(A, I):
# \left[\begin{array}{cccccc}
# 0 & 1 & 2 & 1 & 0 & 0 \\
# 1 & 0 & 3 & 0 & 1 & 0 \\
# 4 & -3 & 8 & 0 & 0 & 1
# \end{array}\right]
    n = np.size(A, 0)
    m = np.size(A, 1)

    print('\left[\\begin{array}{', end = "")
    for i in range(n + m): print('c', end = "")
    print('}')

    for i in range(n):
        for j in range(m):
            output(A[i][j], " & ")

        for j in range(n - 1):
            output(I[i][j], " & ")
        
        output(I[i][n - 1], " ")

        if i != n - 1:
            print("\\\\")
    
    print("\end{array}\\right]")

def MatInv(a, trace = 0):
    n = np.size(a, 0)
    m = np.size(a, 1)
    A = a.copy()
    I = np.eye(n)

    if trace == 2:
        uniFormatPrint(A, I)

    for i in range(n):
        if A[i][i] == 0.0:
            print('Divide by zero detected!')
            return -1
        
        for j in range(n):
            if i != j:
                ratio = A[j][i] / A[i][i]

                for k in range(m):
                    A[j][k] = A[j][k] - ratio * A[i][k]

                for k in range(n):
                    I[j][k] = I[j][k] - ratio * I[i][k]
                
                # print('num1={}, num2={}'.format(num1, num2))
                if trace == 1:
                    print('[{0}]-={1}*{2}'.format(j + 1, ratio, i + 1))
                    uniPrint(A, I)

                if trace == 2:
                    # \stackrel{\text{echelon form}}\longrightarrow
                    print('\stackrel{{[{0}] = [{0}] + ('.format(j + 1))
                    output(-ratio, "")
                    print(')\\times[{0}]}}\longrightarrow'.format(i + 1))
                    uniFormatPrint(A, I)

    for i in range(n):
        divisor = A[i][i]
        for j in range(m):
            A[i][j] = A[i][j] / divisor
        
        for j in range(n):
            I[i][j] = I[i][j] / divisor
            
        if trace == 1 and nequals(divisor, 1):
            print('[{}]/={}'.format(i + 1, divisor))

        if trace == 2 and nequals(divisor, 1):
            print('\stackrel{{[{0}] = [{0}] / ('.format(i + 1))
            output(divisor, ')}\longrightarrow')
        
    if trace == 2:
        uniFormatPrint(A, I)
    return I

def MatProduct(A, B):
    p = np.size(A, 0)
    q = np.size(A, 1)
    r = np.size(B, 1)

    C = np.empty((p, r), dtype=float)
    for i in range(p):
        for j in range(r):
            sum = 0
            for k in range(q):
                sum = sum + A[i][k] * B[k][j]
            C[i][j] = sum
    return C

def MatRREF(a, trace = 0):
    if trace == 2:
        formatPrint(a)

    A = Matrix(a)
    A = np.array(A.rref()[0].tolist(), dtype = float)
    
    if trace == 2:
        print("\stackrel{\\text{reduced echelon form}}\longrightarrow")
        formatPrint(A)

    return A

def MatTrans(a):
    n = np.size(a, 0)
    m = np.size(a, 1)

    C = np.empty((m, n), dtype=float)
    for i in range(m):
        for j in range(n):
            C[i][j] = a[j][i]

    return C

Mat1 = np.array([[1.0, 2.0, 3.0], [2.0, 2.0, 1.0], [4.0, -1.0, -2.0]])
MatInv(Mat1, 2)