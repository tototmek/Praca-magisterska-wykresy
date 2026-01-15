import matplotlib.pyplot as plt
import numpy as np

from utils import *


def generate_plot():
    setup_latex_plots()

    DATA_PATH = "/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/weryfikacja-zlozenia/measurement-2025-07-08_17-33-47.csv"
    filter_window_size = 50

    time = load_csv_column(DATA_PATH, "time").astype(np.float64)
    time -= time[0]
    time /= 600
    data = [[] for _ in range(8)]
    # mapping = [7, 6, 5, 4, 0, 3, 2, 1]
    mapping = [3, 2, 1, 0, 4, 5, 6, 7]
    
    fig, axes = plt.subplots(4, 1, sharex=True, figsize = (TEXT_WIDTH, 6))

    for i in range(4):
        idx = mapping[i+4]
        left_gate_raw = load_csv_column(DATA_PATH, f"ch{idx}_left_gate_raw")
        right_gate_raw = load_csv_column(DATA_PATH, f"ch{idx}_right_gate_raw")
        data[idx] = left_gate_raw - right_gate_raw
        data[idx] = np.convolve(data[idx], np.ones(filter_window_size)/filter_window_size, mode="same")
        axes[i].plot(time[70:-50], data[idx][70:-50], label=f"Ch{i+4}", c="black", lw=0.5)
        axes[i].set_ylabel(f'$x_{i+4}(t)$')
    
    plt.xlabel(r'$t [s]$')

    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()