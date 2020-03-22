import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from time import gmtime, strftime

def main():
    # Real data from mos.ru
    days            = np.array([0, 2, 6, 8, 11, 12, 13, 14, 17, 18, 19,  20,  21,  22])
    infected_total  = np.array([0, 1, 6, 9, 15, 19, 24, 33, 56, 86, 98, 131, 137, 191])
    infected_new    = np.array([0, 1, 5, 4,  6,  4,  5,  9, 23, 30, 12,  33,   6,  54])
    recovered_total = np.array([0, 0, 1, 1,  1,  1,  1,  1,  1,  1,  5,   5,   8,   8])

    fig, ax = plt.subplots()
    plt.grid(True)

    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.xaxis.set_ticks(days)
    ax.yaxis.set_ticks(infected_total)

    plt.plot(days, infected_total,  'r.-')
    plt.plot(days, recovered_total, 'g.-')
    plt.bar(days, infected_new, width=0.25)

    plt.xlabel('$Days$')
    plt.ylabel('$People$')
    plt.title('Moscow COVID-19 cases, '+strftime("%Y-%m-%d", gmtime()))
    plt.legend((
        'Infected total',
        'Recovered total',
        'Infected new',
        ))
    plt.show()


if __name__ == '__main__':
    main()
