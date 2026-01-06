import matplotlib.pyplot as plt
import numpy as np

from utils import *

def generate_plot():
    setup_latex_plots()
    plt.figure(figsize=(TEXT_WIDTH, 0.4*TEXT_WIDTH))
    # plt.title("Sygnał wyjściowy czujnika -- test z żelkiem misiem")
    # plt.ylim([430, 460])
    time = load_csv_column("/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/v2/measurement-dead-bee.csv", "time")
    data = load_csv_column("/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/v2/measurement-dead-bee.csv", "delta")
    plt.ylabel(f'$x(t)$')
    plt.xlabel(r'$t [s]$')
    plt.plot(time[60800:150000], data[60800:150000], c="black", lw="0.5")
    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()