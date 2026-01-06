import matplotlib.pyplot as plt
import numpy as np

from utils import *


def generate_plot():
    setup_latex_plots()
    DATA_PATH = "/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/2025-07-26/2025-07-26_11-04-07.csv"
    filter_window_size = 50

    range = (1000, 4000)

    time = load_csv_column(DATA_PATH, "time").astype(np.float64)[range[0]:range[1]]
    time -= time[0]
    time /= 600
    

    data = load_csv_column(DATA_PATH, f"delta0").astype(np.float64)
    data_raw = data[range[0]:range[1]]
    data = np.convolve(data, np.ones(filter_window_size)/filter_window_size, mode="same")[range[0]:range[1]]

    plt.figure(figsize=(TEXT_WIDTH, 0.4*TEXT_WIDTH))
    plt.plot(time, data_raw, c="lightgrey", lw=0.5, label="Dane surowe")
    plt.plot(time, data, c="black", lw=0.75, label="Dane filtrowane")
    plt.ylabel(f'$x_0(t)$')
    plt.ylim((min(data)-0.3, max(data)+0.3))
    plt.legend(frameon=False)
    plt.xlabel(r'$t [s]$')


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()