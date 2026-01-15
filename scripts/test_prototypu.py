import matplotlib.pyplot as plt

from utils import *

def generate_plot():
    setup_latex_plots()
    plt.figure(figsize=(TEXT_WIDTH, 0.4*TEXT_WIDTH))
    # plt.title(r"Sygnał wyjściowy czujnika -- test z wilgotną gąbką")
    plt.xlabel(r"Numer pomiaru\quad $k$")
    plt.ylabel(r"Czas ładowania bramki\quad $n_L$ [iteracje]")
    plt.ylim([430, 460])
    data = load_csv_column("/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/old/measurement.csv", "left_gate_raw")
    data = data[0::6]
    plt.plot(data, c="k", lw=0.75)
    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()