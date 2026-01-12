import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple

from utils import *

def generate_plot():
    setup_latex_plots()
    data = np.load("src/error2.npz")

    # Extract the arrays using the keys defined above
    time = data['time']
    detrended = data['detrended']
    up_threshold = data['up_threshold']
    bottom_threshold = data['bottom_threshold']
    signal_thresholded = data['signal_thresholded']
    fsm_enter_ts = data['fsm_enter_ts']
    fsm_leave_ts = data['fsm_leave_ts']
    enter_times = data['enter_ts']
    leave_times = data['leave_ts']
    data.close()

    fig, (ax0) = plt.subplots(1, 1, figsize=(0.8 * TEXT_WIDTH, 0.32*TEXT_WIDTH), sharex=True)


    enter_times = (enter_times-time[0])*100
    leave_times = (leave_times-time[0])*100
    fsm_enter_ts = (fsm_enter_ts-time[0])*100
    fsm_leave_ts = (fsm_leave_ts-time[0])*100
    fsm_leave_ts = np.append(fsm_leave_ts, 2699)

    pinheight_max = max(detrended) * 1.3
    pinheight_min = min(detrended) * 1.3

    for ts in list(enter_times) + list(leave_times):
        ax0.axvline(x=ts, color='gray', ls=':', lw=0.5)
    ax0.axhline(y=0, color='gray', ls='--', lw=0.5)


    ax0.vlines(enter_times, 0, pinheight_max, colors='green', linewidth=1.0)
    s1 = ax0.scatter(enter_times, [pinheight_max] * len(enter_times), color='white', marker='o', s=50, zorder=5, edgecolors="green")
    ax0.vlines(leave_times, pinheight_min, 0, colors='red', linewidth=1.0)
    s2 = ax0.scatter(leave_times, [pinheight_min] * len(leave_times), color='white', marker='o', s=50, zorder=5, edgecolors="red")


    ax0.vlines(fsm_enter_ts, 0, pinheight_max, colors='green', linewidth=1.0)
    sz1 = ax0.scatter(fsm_enter_ts, [pinheight_max] * len(fsm_enter_ts), color='green', marker='o', s=10, zorder=6)
    ax0.vlines(fsm_leave_ts, pinheight_min, 0, colors='red', linewidth=1.0)
    sz2 = ax0.scatter(fsm_leave_ts, [pinheight_min] * len(fsm_leave_ts), color='red', marker='o', s=10, zorder=6)

    p, = ax0.plot(detrended, c="black", lw=0.75, label='$y(k)$')

    ax0.set_ylabel(r'$y(k)$')
    ax0.set_xlabel(r'$k$')

    ax0.legend([p, (s1, s2), (sz1, sz2)], [r'$y(k)$', "Anotacja", "Detekcja"], 
           handler_map={tuple: HandlerTuple(ndivide=None)},
           loc='upper right')
    
    ax0.text(1038, -3.4, r"\small Brak detekcji")


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()