import numpy as np
from matplotlib import pyplot as plt

x1 = np.linspace(0, 5, num=200)
x2 = np.linspace(0, 6, num=200)
x3 = np.linspace(0, 7, num=200)
x4 = np.linspace(0, 8, num=200)



def sint(n):
  m = n/2

  assert n == 2*m, "n must be an even integer"

  coeff = [1 for i in range(int(m+1))]
  sign = 1
  fact = 1

  for i in range(2, int(m+1)):
    sign *= -1
    d = (2 * i) - 1
    fact *= (d-1)*d
    coeff[i] = sign/(fact*d)
  
  return np.array(coeff)


def poly_even(x, coeff, n):
  m = n/2

  assert n == 2*m, "n must be an even integer"

  xsq = x*x
  ones = np.array([1 for i in x])
  val = coeff[int(m)]*ones
  
  for i in range(int(m), 0, -1):
    temp = (xsq*val)
    val = temp[:] + coeff[i]

  return val

max_deg = 20

cf = sint(max_deg)

deg = [4, 8, 12, 16]
assert max(deg) < max_deg, "some value of degree is greater than max degree"

p1 = []
p2 = []
p3 = []
p4 = []

for i in range(4):
  p1.append(poly_even(x1, cf, deg[i]))
  p2.append(poly_even(x2, cf, deg[i]))
  p3.append(poly_even(x3, cf, deg[i]))
  p4.append(poly_even(x4, cf, deg[i]))
    
fig ,ax = plt.subplots(4)

# following code is used to display the graph using matplotlib

# fix aspect ratios
ax[0].grid(True, which='both')
ax[1].grid(True, which='both')
ax[2].grid(True, which='both')
ax[3].grid(True, which='both')

# plot the taylor polynomials for each graphs axis. ax[i] are axes of each graph
ax[0].plot(x1, p1[0], 'k--', label='P4(x)')
ax[0].plot(x1, p1[1], 'r--', label='P8(x)')
ax[0].plot(x1, p1[2], 'g--', label='P12(x)')
ax[0].plot(x1, p1[3], 'b--', label='P16(x)')

ax[1].plot(x2, p2[0], 'k--', label='P1(x)')
ax[1].plot(x2, p2[1], 'r--', label='P2(x)')
ax[1].plot(x2, p2[2], 'g--', label='P3(x)')
ax[1].plot(x2, p2[3], 'b--', label='P4(x)')

ax[2].plot(x3, p3[0], 'k--', label='P1(x)')
ax[2].plot(x3, p3[1], 'r--', label='P2(x)')
ax[2].plot(x3, p3[2], 'g--', label='P3(x)')
ax[2].plot(x3, p3[3], 'b--', label='P4(x)')

ax[3].plot(x4, p4[0], 'k--', label='P1(x)')
ax[3].plot(x4, p4[1], 'r--', label='P2(x)')
ax[3].plot(x4, p4[2], 'g--', label='P3(x)')
ax[3].plot(x4, p4[3], 'b--', label='P4(x)')

# y min and y max values displayed
ax[0].set_ylim(ymin=0, ymax=1.25)
ax[1].set_ylim(ymin=0, ymax=1.25)
ax[2].set_ylim(ymin=0, ymax=1.25)
ax[3].set_ylim(ymin=0, ymax=1.25)


# legend displays label values on the first graph's legend, which is the same for all graphs. thie anchor is to have it float outside of the graph
ax[0].legend(bbox_to_anchor=(1,1), loc="upper left")

#fix overlay of axes
plt.tight_layout()

#plt.savefig("1b_sint_intervals.png")
plt.show()