import matplotlib.pyplot as plt
import numpy as np

from utils import *
from filtr_brak import moving_average, moving_median, data_range

def generate_plot():
    setup_latex_plots()
    DATA_PATH = "/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/2025-07-26/2025-07-26_11-04-07.csv"

    filter_window = 50
    median_window = 1200

    data = load_csv_column(DATA_PATH, f"delta0").astype(np.float64)
    data_raw = data[data_range[0]:data_range[1]]
    data = moving_average(data_raw, filter_window)
    median = moving_median(data, median_window)
    detrended = data - median

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize = (TEXT_WIDTH, 0.75*TEXT_WIDTH))
    ax1.plot(data, c="black", lw=0.75, label=r"$x_\mathrm{f}(k)$ -- \textit{sygnał oryginalny}")
    ax1.plot(median, c="red", lw=0.85, label=r"$x_\mathrm{m}(k)$ -- \textit{mediana z okna M}")
    ax1.set_ylabel(r'$x(k)$')
    ax1.legend()
    ax2.axhline(0, color='grey', lw=0.75, ls='--')
    ax2.plot(detrended, c="black", lw=0.75, label=r'$y(k) = x_\mathrm{f}(k) - x_\mathrm{m}(k)$')
    ax2.set_ylabel(r'$y(k)$')
    ax2.legend()
    ax2.set_xlabel(r'$k$')


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()