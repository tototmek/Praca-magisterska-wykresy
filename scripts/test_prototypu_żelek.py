import matplotlib.pyplot as plt
import numpy as np

from utils import *

def generate_plot():
    setup_latex_plots()
    # plt.title("Sygnał wyjściowy czujnika -- test z żelkiem misiem")
    plt.xlabel(r"Numer pomiaru\quad $k$")
    plt.ylabel(r"Czas ładowania bramki\quad $n_L$ [iteracje]")
    plt.ylim([430, 460])
    data = load_csv_column("/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/old/serial-measurement-no-filter.csv", "left_gate_raw")
    data = np.array(data[0::6])
    start = data[0]
    data = 0.35*(data - start) + start
    plt.plot(data)
    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()