# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.collections import LineCollection


def grid(ax):
    segments,colors,linewidths = [], [], []
    for x in ax.xaxis.get_minorticklocs():
        segments.append([(x,ymin), (x,ymax)])
        colors.append("0.75")
        linewidths.append(0.50)
    for x in ax.xaxis.get_majorticklocs():
        segments.append([(x,ymin), (x,ymax)])
        colors.append("0.50")
        linewidths.append(0.75)
    for y in ax.yaxis.get_minorticklocs():
        segments.append([(xmin,y), (xmax,y)])
        colors.append("0.75")
        linewidths.append(0.50)
    for y in ax.yaxis.get_majorticklocs():
        segments.append([(xmin,y), (xmax,y)])
        colors.append("0.50")
        linewidths.append(0.75)

    collection = LineCollection(segments, zorder=-10,
                                colors=colors, linewidths=linewidths)
    ax.add_collection(collection)


fig = plt.figure(figsize=(8,8))
xmin, xmax = 0,10000
ymin, ymax = 0,10000

T = np.linspace(0,2*np.pi,1000)
X = (xmax+xmin)/2 + 4999.9*np.cos(T)
Y = (ymax+ymin)/2 + 4999.9*np.sin(T)

# -----------------------------------------------------------------------------
ax = plt.subplot(2,2,1)
ax.ticklabel_format(axis="both", style="sci")
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.plot(X, Y, color="black", linewidth=1.0)
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_xticklabels(["0","2.10³","4.10³","6.10³","8.10³","10⁴"])
ax.set_yticklabels(["0","2.10³","4.10³","6.10³","8.10³","10⁴"])
grid(ax)
ax.set_title("X linear, Y linear", size="medium")

# -----------------------------------------------------------------------------
ax = plt.subplot(2,2,2)
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.plot(X, Y, color="black", linewidth=1.0)
xmin, ymin = 0.1, 0.0
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_xscale("log")
ax.set_yticklabels(["0","2.10³","4.10³","6.10³","8.10³","10⁴"])
grid(ax)


# -----------------------------------------------------------------------------
ax = plt.subplot(2,2,3)
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.plot(X, Y, color="black", linewidth=1.0)
xmin, ymin = 0.0, 0.1
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_yscale("log")
ax.set_xticklabels(["0","2.10³","4.10³","6.10³","8.10³","10⁴"])
grid(ax)
ax.set_title("X linear, Y logarithmic", size="medium")

# -----------------------------------------------------------------------------
ax = plt.subplot(2,2,4)
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.plot(X, Y, color="black", linewidth=1.0)
xmin, ymin = 0.1, 0.1
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_xscale("log")
ax.set_yscale("log")
grid(ax)
ax.set_title("X logarithmic, Y logarithmic", size="medium")

plt.savefig("scales.pdf")
plt.show()
