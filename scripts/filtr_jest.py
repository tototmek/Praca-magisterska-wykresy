import matplotlib.pyplot as plt
import numpy as np


from utils import *
from filtr_brak import moving_average, moving_median, data_range_small

def generate_plot():
    setup_latex_plots()
    DATA_PATH = "/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/2025-07-26/2025-07-26_11-04-07.csv"

    filter_window = 50

    data = load_csv_column(DATA_PATH, f"delta0").astype(np.float64)
    data_raw = data[data_range_small[0]:data_range_small[1]]
    data = moving_average(data_raw, filter_window)

    plt.figure(figsize=(TEXT_WIDTH, 0.3*TEXT_WIDTH))
    plt.plot(data, c="black", lw=0.75, label="N=50")
    plt.ylabel(r'$x_\mathrm{f}(k)$')
    # plt.ylim((min(data)-0.3, max(data)+0.3))
    # plt.legend(frameon=False)
    plt.xlabel(r'$k$')


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()