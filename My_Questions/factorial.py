'''
    Two approaches to calculating factorials.
'''
import math
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def factorial_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return n*factorial_recursion(n-1)

def factorial_stirling(n):
    return (n**n)*math.exp(-n)*math.sqrt(2*math.pi*n)*(1+1/(12*n))

def main():
    x_range = [i for i in range(1,100)]
    r = []
    r_time = []
    s = []
    s_time = []
    for x in x_range:
        start = timer()
        r.append(factorial_recursion(x))
        end = timer()
        r_time.append(end-start)
        start = timer()
        s.append(factorial_stirling(x))
        end = timer()
        s_time.append(end-start)
    plt.figure(1)
    plt.subplot(211)
    plt.title("Factorials")
    plt.plot(x_range,r,x_range,s)
    plt.subplot(212)
    plt.title("Time")
    plt.plot(x_range,r_time,x_range,s_time)
    plt.show()

main()