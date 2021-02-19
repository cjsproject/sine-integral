import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from math import cos, exp, factorial

### you can simply run this code by 
### clicking run at the top for cost
### same code as main.py

"""
Although I took some methods from
the sint(x) program, I rewrote most
of this in a more pythonic way.

this program creates data for cost(x)
and its nth degree Taylor Polynomials 
Pn(x) with degrees in the array deg_1.
"""

x = np.linspace(-1, 1, num=200)
# a value close to 0; f(0) not defined
a = x[int(200/2)]
#degrees
deg_1 = [2, 4, 6, 8]

# integral of ( 1-cos(t) )/(t^2)
# t = some value of the domain
def integrand(t):
  return (1-cos(t))/(t**2)

# f(x) = 1/x* integral from 0->x of 
# integrand's domain value. 
# uses very neat integration function
# from the scipy library.
def f(t):
  integr = integrate.quad(integrand, 0, t)
  return (1/t)*integr[0]
  
# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = exp(-5)
  if degree == 0: 
    return f(v)
  elif degree > 1:
    return dydx((f(v+h) - f(v))/(h), degree-1)
  
  return (f(v+h) - f(v))/(h)

def poly(v, deg):
  return pow(v-a,deg)*dydx(a, deg)/factorial(deg)

# nth_tayl() and nth_tayl2() are 
# two different functions that do
# the same thing. I wanted to 
# make sure my calcualtions were right
def nth_tayl(n):
  if n >= 0:
    summation = np.zeros((n+1, len(x)))
    print(summation)
    for i in range(n+1):
      for j in range(len(x)):
        summation[i][j] = (poly(x[j],i))
  return [sum(col) for col in zip(*summation)]


# Finds nth taylor polynomial
def nth_tayl2(n):
  if n >= 0:
    summation = np.zeros(len(x))
    for i in range(n+1):
      for j in range(len(x)):
        summation[j] += (dydx(a, i)*pow((x[j]-a), i))/factorial(i)
  return summation

# array of domain values for Pn(x)
p = []

#similar to the main matlab code
for n in deg_1:
  p.append(nth_tayl2(n))

fx = [f(i) for i in x]

fig, ax = plt.subplots()

ax.plot(x, fx, 'k', label='f(x)')
# has the same behaviour as y=f'(a)
ax.plot(x, p[0], 'r--', label='P2(x)')
ax.plot(x, p[1], 'g--', label='P4(x)')
ax.plot(x, p[2], 'b--', label='P6(x)')
ax.plot(x, p[3], 'y--', label='P8(x)')

# take note of the very small range of y
# this allows us to see the curvature 
# more obviously. also helps check the
# polynomial outputs
ax.set_ylim(ymin=0.485, ymax=0.505)

ax.legend()
#plt.savefig("4_cost.png")

plt.show()