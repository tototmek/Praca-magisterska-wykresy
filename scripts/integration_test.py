import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple

from utils import *
from filtr_brak import moving_average, moving_median, data_range

def generate_plot():
    setup_latex_plots()
    data = np.load("src/integration-test.npz")
    bees = data['arr_0']
    data.close()

    time = np.linspace(0, len(bees[0])/60, len(bees[0]))

    fig, axes = plt.subplots(4, 2, figsize=(TEXT_WIDTH, 0.6*TEXT_WIDTH), sharex=True)

    axes = axes.flatten("F")

    for i, ax in enumerate(axes):
        ax.plot(time, bees[i], lw=0.75, c='k')
        ax.set_ylabel(f'$bee_{i}$')
        ax.set_ylim((-0.5, 1.5))

    axes[3].set_xlabel(r'$t [s]$')
    axes[7].set_xlabel(r'$t [s]$')

    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()