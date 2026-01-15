import matplotlib.pyplot as plt
import numpy as np


from utils import *

def generate_plot():
    setup_latex_plots()
    DATA_PATH = "/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/2025-09-20/2025-09-20_12-12-52.csv"

    data = []

    data = [load_csv_column(DATA_PATH, f"delta{i}").astype(np.float64) for i in range(8)]
    time = load_csv_column(DATA_PATH, f"time")
    time = (time - time[0]) / 1000

    for i in range(8):
        data[i] = data[i][::1000]
    
    time = time[::1000]

    summed = np.sum(np.array(data), axis=0)

    plt.figure(figsize=(TEXT_WIDTH, 1/1.618*TEXT_WIDTH))
    for i in range(8):
        plt.plot(time, data[i], lw=0.6, label=f"$bee_{i}(t)$")
    plt.ylabel(f'$bee_i(t)$')
    plt.plot(time, summed, lw=1, c="k", label=f"Łącznie")
    # plt.ylim((min(data)-0.3, max(data)+0.3))
    leg = plt.legend(frameon=False, ncol=3)
    plt.xlabel(r'$t[s]$')

    for line in leg.get_lines():
        line.set_linewidth(1.5)


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()