import numpy as np
import matplotlib.pyplot as plt

P = 1000
E = 5
T = 10**6

x = [E for i in range(P)]

for t in range(T):
    i, j = np.random.choice(P, 2)
    if x[i] > 0:
        x[i] -= 1
        x[j] += 1

m = int(max(x))
X_axis = [i for i in range(m + 1)]
Y_axis = []
X_log = []
Y_log = []
for i in range(m + 1):
    ct = x.count(i)
    Y_axis.append(ct)
    if ct > 1:
        X_log.append(i)
        Y_log.append(np.log(ct))

fig = plt.figure()
sp1 = fig.add_subplot(1, 2, 1)
sp2 = fig.add_subplot(1, 2, 2)

sp1.scatter(X_axis, Y_axis, color="Orange")
sp1.set_title('Energy Distribution')
sp1.set_xlabel('Amount of Energy')
sp1.set_ylabel('Number of Particles')

m, b = np.polyfit(X_log, Y_log, 1)
fit = []
for i in X_log:
    fit.append(m * i + b)
sp2.plot(X_log, Y_log, "yo", X_log, fit, "--k")
sp2.set_title('Logarithmic Energy Distribution')
sp2.set_xlabel('Amount of Energy')
sp2.set_ylabel('ln(Number of Particles)')

plt.show()
