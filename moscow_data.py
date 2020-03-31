import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from time import gmtime, strftime


def get_data(file_obj):
    row_0 = np.genfromtxt(file_obj, delimiter=',', usecols=(0))
    row_1 = np.genfromtxt(file_obj, delimiter=',', usecols=(1))
    row_2 = np.genfromtxt(file_obj, delimiter=',', usecols=(2))
    row_3 = np.genfromtxt(file_obj, delimiter=',', usecols=(3))
    return row_0, row_1, row_2, row_3


def main():
    # Get data from file
    data_file = "data.csv"
    days, inf_new, inf_t, rec_t = get_data(data_file)
    # Create approximation
    add_trend = input("Would you like to add trend on the plot? [y/n]\n")
    if add_trend == 'y':
        trend = pow(np.exp(days), 1/4)

    # Visualisation
    fig, ax = plt.subplots()
    plt.grid(True)

    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.xaxis.set_ticks(days)

    plt.plot(days, inf_t, 'r.-')
    plt.plot(days, rec_t, 'm.-')
    plt.bar(days, inf_new, width=0.45)
    if add_trend == 'y':
        plt.plot(days, trend, 'b--')

    plt.xlabel('$Days$')
    plt.ylabel('$People$')
    plt.title('Moscow COVID-19 cases, '+strftime("%Y-%m-%d", gmtime()))
    plt.legend((
        'Infected total',
        'Recovered total',
        'Infected new'
        'Trend',
    ))
    plt.savefig("moscow_covid_cases.png")


if __name__ == '__main__':
    main()
