

# The Dirac delta3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return np.cos(x)
def d(x):
    return (n/(np.pi))*(1/(1+n**2*(x-2*np.pi)**2))*f(x)
n=int(input("Enter the value of n: "))
a=2*np.pi-50
b=2*np.pi+50
x=np.arange(a,b,0.1)
R=[]
for i in range(10):
    R.append(quad(lambda x:d(x),a,b)[0])
    i+=1

print(R)
print("function: ",f(2*np.pi))
plt.plot(x,d(x))
plt.xlabel("x-value")
plt.ylabel("Delta-value")
plt.grid(True)
plt.show()
