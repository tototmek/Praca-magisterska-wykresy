import matplotlib.pyplot as plt

from utils import *

def generate_plot():
    setup_latex_plots()
    plt.figure(figsize=(TEXT_WIDTH, 0.6*TEXT_WIDTH))
    plt.title("Przebieg wyjścia czujnika")
    plt.xlabel(r"Numer pomiaru $k$")
    plt.ylabel(r"Czas ładowania bramki $n_L$ [iteracje]")
    data = load_csv_column("/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/old/measurement.csv", "left_gate_raw")
    data = data[0::6]
    plt.plot(data)
    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()