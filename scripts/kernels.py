import pandas as pd
import matplotlib.pyplot as plt
from filtr_brak import moving_average, moving_median
from utils import *

def generate_plot():
    channel_idx = 0
    RAW_DATA_FILE = '/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/processed-data/raw-time-adjusted.csv'
    channel_name = f'delta{channel_idx}'
    df = pd.read_csv(RAW_DATA_FILE)
    mask = np.ones(len(df), dtype=bool)
    signal = df.loc[mask, channel_name].to_numpy(dtype=float)

    signal = moving_average(signal, 50)
    median = moving_median(signal, 1050)
    signal = signal-median

    KERNEL_START = 3103
    KERNEL_LENGTH = 600
    kernel_end = KERNEL_START + KERNEL_LENGTH
    kernel = signal[KERNEL_START:kernel_end]

    synthetic_kernel = np.zeros(141)
    sin = np.sin(np.linspace(0, 2*np.pi, 101))
    # fun = np.power(sin, 2) * np.sign(sin) * -1.33
    fun = sin * -1.33
    synthetic_kernel[20:121] = fun
    # print("{"+",".join(synthetic_kernel.astype(str))+"};")

    setup_latex_plots()

    plt.figure(figsize=(0.8*TEXT_WIDTH, 0.3*TEXT_WIDTH))
    plt.plot(-kernel, c="#b0b0b0", lw=1)
    plt.plot(-synthetic_kernel, c="black", lw=0.75)
    plt.xlabel(r'$m$')
    plt.ylabel(r'$w(m)$')
    plt.legend(['(a)', '(b)'], frameon=False)


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()