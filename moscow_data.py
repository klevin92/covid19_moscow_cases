import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

def main():
    # Real data from mos.ru
    days            = np.array([0, 2, 6, 8, 11, 12, 13, 14, 17])
    infected_total  = np.array([0, 1, 6, 9, 15, 19, 24, 33, 53])
    infected_new    = np.array([0, 1, 5, 4, 6,  4,  5,  9,  20])
    recovered_total = np.array([0, 0, 1, 1, 1,  1,  1,  1,  1])

    # Math function for scale
    line_grow = days
    quad_grow = np.power(days,2)
    cube_grow = np.power(days,3)
    exp_grow  = np.exp(days)

    fig, ax = plt.subplots()
    plt.grid(True)

    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.xaxis.set_ticks(days)

    plt.bar(days+0.25*1, infected_total, width=0.25)
    plt.bar(days+0.25*2, infected_new, width=0.25)
    plt.bar(days+0.25*3, recovered_total, width=0.25)
    # plt.bar(days+0.25*4, line_grow, width=0.25)

    # plt.plot(days, infected_total,  'r.-')
    # plt.plot(days, infected_new,    '+')
    plt.plot(days, line_grow, 'k--')
    # plt.plot(days, recovered_total, 'g.-')
    # plt.plot(days, quad_grow, '.-')
    # plt.plot(x, cube_grow)
    # plt.plot(x, exp_grow)
    
    plt.xlabel('$Days$')
    plt.ylabel('$People$')
    plt.title('Moscow COVID-19 cases')
    plt.legend((
        'line grow',
        'Infected total',
        'Infected new',
        'Recovered total',
        'quad grow'
        ))
    plt.show()

if __name__ == '__main__':
    main()
